"""Read-only source review reproductions: broken outcomes are intentionally asserted."""
import copy
from pathlib import Path

import pytest

from test_nightly_stage_repair import env, prepare, apply, write
from ml import nightly_stage_repair as repair
from ml import nightly_dispatch, nightly_workflow


def tail_state(env):
    state = env["state"]
    state["planning_tail_continuation"] = {"path": str(env["root"] / "original-tail.json"), "sha256": "b" * 64}
    state["recovery_deadline_at"] = state["effective_deadline_at"]
    write(env["state_path"], state)
    return state


def test_demonstrates_prepared_transient_repair_claim_does_not_stop_dispatch(env):
    state = env["state"]
    state["failure"].update(kind="TRANSIENT", step="model_review")
    state["steps"]["model_review"]["attempts"] = 1
    write(env["state_path"], state)
    env["config"]["automatic_recovery"] = {"enabled": True, "authorization": "Local human authority", "max_attempts": 3}
    prepare(env)
    claimed = repair.workflow._json(env["state_path"])
    assert claimed["repair_claim"]["token"] == env["request"]["repair_id"]
    decision = nightly_workflow.dispatch_status(env["config"], now="2026-10-09T18:30Z")
    assert decision["dispatch"] is True and decision["responsibility"] == "model"


def test_demonstrates_planning_tail_cannot_verify_helper_repair_audit(env):
    state = tail_state(env)
    original = copy.deepcopy(state["source_identity"])
    apply(env, prepare(env))
    saved = repair.workflow._json(env["state_path"])
    with pytest.raises(ValueError, match="Continuation source repair chain is not a reviewed transition"):
        nightly_workflow._verify_continuation_source_repair(saved, original, state["planning_tail_continuation"])


def test_demonstrates_same_source_restore_makes_later_repair_anchor_ambiguous(env):
    state = tail_state(env)
    original = copy.deepcopy(state["source_identity"])
    state["failure"]["kind"] = "EXTERNAL_DEPENDENCY"
    write(env["state_path"], state)
    (env["candidate"] / "ml/nightly_workflow.py").write_text("original workflow\n")
    checks = copy.deepcopy(env["request"]["checks"])
    checks[0]["source_files"] = repair._inventory(env["candidate"])
    apply(env, prepare(env, changes={}, risk="external_dependency", checks=checks))
    after_restore = repair.workflow._json(env["state_path"])
    assert after_restore["source_repairs"][0]["original_source_identity"] == original
    assert after_restore["source_repairs"][0]["reviewed_source_identity"] == original
    after_restore.update(status="FAILED", current_step="model_review")
    after_restore["failure"].update(kind="SOURCE_DEFECT", disposition="OPEN", fingerprint="second-fixture-failure")
    write(env["state_path"], after_restore)
    (env["candidate"] / "ml/nightly_workflow.py").write_text("fixed workflow\n")
    apply(env, prepare(env, repair_id="second-fixture-repair"))
    saved = repair.workflow._json(env["state_path"])
    with pytest.raises(ValueError, match="Frozen continuation source has no reviewed repair chain"):
        nightly_workflow._verify_continuation_source_repair(saved, original, state["planning_tail_continuation"])


def test_demonstrates_dispatcher_repair_path_missing_from_orchestration_scope(env):
    with pytest.raises(ValueError, match="Orchestration repairs cannot relabel"):
        repair._validate_scope(env["state"], {"ml/nightly_dispatch.py": "modify"}, "orchestration", None, "preserved")


def test_demonstrates_new_scheduled_recovery_record_not_bound_by_repair(env):
    state = env["state"]
    state["scheduled_recovery"] = state.pop("recovery")
    write(env["state_path"], state)
    spec = prepare(env)
    Path(state["scheduled_recovery"]["path"]).write_text("modified frozen recovery")
    assert apply(env, spec)["status"] == "SOURCE_REPAIR_APPLIED"
