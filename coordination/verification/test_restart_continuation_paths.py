"""Focused reproductions of operational paths; no real workers are launched."""
import copy
from pathlib import Path

import pandas as pd
import pytest

from test_nightly_stage_repair import env, write
from ml import nightly_workflow as workflow, overnight_runtime as native
from ml.artifacts import file_checksum, utc_timestamp
from ml.preparation_deadline import RECOVERY_VERSION


def valid_tail(env, monkeypatch, *, scheduled=False):
    now = pd.Timestamp("2026-10-09T20:15Z")
    monkeypatch.setattr(native, "utc_timestamp", lambda value=None: utc_timestamp(value) if value is not None else now)
    state = copy.deepcopy(env["state"])
    state.pop("recovery", None)
    state.update(recovery_deadline_at="2026-10-09T19:00Z", current_step="train_and_plan")
    state["failure"].update(kind="TRANSIENT", step="train_and_plan", disposition="RESOLVED")
    state["steps"]["model_review"] = {"status": "COMPLETE", "output": {"files": {}}}
    source = env["root"] / "ml/nightly-gameplan-runs/original"
    write(source / "receipt.json", {"action_date": state["action_date"]})
    run = env["root"] / "ml/overnight-runs/original-failed-tail"
    report = {"schema_version": native.OVERNIGHT_RUNTIME_VERSION, "status": "FAILED",
        "deadline_at": state["recovery_deadline_at"], "preparation_scope": "STOCK_ONLY",
        "stock_only": True, "independent_stock_horizons": True, "stats_first": True,
        "review_action_date": state["source_session"], "failed_stage": "gameplan_trade_planning",
        "stage_order": ["gameplan_trade_planning"], "stages": [],
        "enrichment_gameplan": {"run_path": source.relative_to(env["root"]).as_posix(),
                                "receipt_sha256": file_checksum(source / "receipt.json")}}
    write(run / "stage-report.json", report)
    write(run / "receipt.json", {"schema_version": native.OVERNIGHT_RUNTIME_VERSION,
        "run_path": run.relative_to(env["root"]).as_posix(), "status": "FAILED", "logs": {},
        "stage_report_checksum_sha256": file_checksum(run / "stage-report.json"),
        "orders_placed": 0, "broker_orders_enabled": False})
    state["steps"]["train_and_plan"] = {"status": "FAILED", "native_run": str(run)}
    record = {"schema_version": RECOVERY_VERSION, "scope": "PINNED_STOCK_PLANNING_AND_ACTUALS_ONLY",
        "operator_authorized": True, "orders_authorized": False,
        "authorization_text": "Recorded local human continuation authority", "authorization_source": "fixture",
        "workflow_source_identity": state["source_identity"], "workflow_run_id": state["run_id"],
        "action_date": state["action_date"], "original_session_deadline_at": state["deadline_at"],
        "original_deadline_at": state["recovery_deadline_at"], "approved_at": "2026-10-09T20:00Z",
        "expires_at": "2026-10-09T23:00Z", "failed_native_run": run.relative_to(env["root"]).as_posix(),
        "failed_native_receipt_sha256": file_checksum(run / "receipt.json"),
        "gameplan_run": source.relative_to(env["root"]).as_posix(),
        "gameplan_receipt_sha256": file_checksum(source / "receipt.json")}
    path = env["root"] / "tail-continuation.json"
    write(path, record)
    state["planning_tail_continuation"] = {"path": str(path), "sha256": file_checksum(path)}
    env["config"]["automatic_recovery"] = {"enabled": True, "authorization": "Fixture human authority", "max_attempts": 3}
    if scheduled:
        from ml.nightly_dispatch import RECOVERY
        recovery = {"schema_version": RECOVERY, "actor": "Scout", "workflow_run_id": state["run_id"],
            "datastore": str(env["root"]), "action_date": state["action_date"],
            "source_session": state["source_session"], "original_deadline_at": state["deadline_at"],
            "approved_at": "2026-10-09T12:00Z", "expires_at": state["recovery_deadline_at"],
            "authorization": "Recorded human recovery authority", "orders_authorized": False}
        recovery_path = env["root"] / "scheduled-recovery.json"
        write(recovery_path, recovery)
        state["scheduled_recovery"] = {"path": str(recovery_path), "sha256": file_checksum(recovery_path)}
    write(env["state_path"], state)
    assert workflow._planning_tail_continuation(env["config"], state, None, now) == pd.Timestamp(record["expires_at"])
    return state, now


def test_valid_saved_planning_continuation_is_blocked_by_automatic_dispatch(env, monkeypatch):
    state, now = valid_tail(env, monkeypatch)
    decision = workflow.dispatch_status(env["config"], now=now)
    assert decision["status"] == "RECOVERY_EXPIRED" and decision["dispatch"] is False
    calls = []
    result = workflow.run_workflow(env["config"], resume_action_date=state["action_date"], now=now,
        identity=workflow.source_identity, supervise=False,
        execute_step=lambda config, current, step, save: calls.append(step) or {"files": {}})
    assert result["status"] == "LOCAL_COMPLETE_PEER_SETUP_PENDING"
    assert calls == ["train_and_plan", "verify_display", "local_handoff"]
    assert result["recovery_deadline_at"] == state["recovery_deadline_at"]


def test_expired_scheduled_recovery_blocks_even_valid_existing_tail_before_validation(env, monkeypatch):
    state, now = valid_tail(env, monkeypatch, scheduled=True)
    with pytest.raises(ValueError, match="Frozen nightly recovery is invalid or expired"):
        workflow.run_workflow(env["config"], catch_up=True, responsibility="model", now=now,
            identity=workflow.source_identity, supervise=False,
            execute_step=lambda *args: pytest.fail("Blocked before valid existing planning tail"))


def test_native_birth_aware_recovery_does_not_clear_pid_reused_runtime_lock(env, monkeypatch):
    from datafetching import runtime_lock
    now = pd.Timestamp("2026-10-09T18:00Z")
    monkeypatch.setattr(native, "utc_timestamp", lambda value=None: utc_timestamp(value) if value is not None else now)
    run = env["root"] / "ml/overnight-runs/interrupted-original"
    write(run / "stage-report.json", {"status": "RUNNING", "owner_pid": 424242, "owner_created_at": 100.0,
        "stage_order": ["gameplan_trade_planning"], "stages": [], "deadline_at": "2026-10-09T19:00Z"})
    # OS birth evidence proves the saved supervisor exited and its PID was reused.
    monkeypatch.setattr(native, "_process_created_at", lambda pid: 200.0)
    monkeypatch.setattr(runtime_lock, "_pid_is_running", lambda pid: pid == 424242)
    lock = env["root"] / ".ducketz-overnight-runtime.lock"
    lock.write_text("process=original-supervisor\npid=424242\nstarted_at=2026-10-08T21:05:00Z\ntoken=original\n")
    original_lock = lock.read_bytes()
    native.recover_interrupted_run(env["root"], run, "Verified original supervisor exited; PID was reused")
    assert workflow._json(run / "receipt.json")["status"] == "CANCELLED"
    state = copy.deepcopy(env["state"])
    state.update(recovery_deadline_at="2026-10-09T19:00Z", current_step="train_and_plan")
    state["steps"]["model_review"] = {"status": "COMPLETE", "output": {"files": {}}}
    state["steps"]["train_and_plan"] = {"status": "CANCELLED", "native_run": str(run)}
    write(env["state_path"], state)
    with pytest.raises(RuntimeError, match="Another Nightly workflow owns these artifacts"):
        workflow.run_workflow(env["config"], resume_action_date=state["action_date"], now=now,
            identity=workflow.source_identity, supervise=False,
            execute_step=lambda *args: pytest.fail("Runtime lock blocks before stage recovery"))
    assert lock.read_bytes() == original_lock
