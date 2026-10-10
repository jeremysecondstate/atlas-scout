"""Synthetic-only reproduction; no application config or runtime operations."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
candidate = Path(sys.argv[1]).resolve()
result_path = Path(sys.argv[2]).resolve()
assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=candidate, text=True).strip() == "92a094027d97e5bdb8d868a87eff056310a5e354"
os.chdir(candidate)
sys.path.insert(0, str(candidate))
import pytest
from tests import test_nightly_exchange_repair as base
from tests import test_nightly_coordination_transition as t

assert Path(t.repair.__file__).resolve() == candidate / "ml/nightly_exchange_repair.py"
started = datetime.now(timezone.utc).isoformat()
with tempfile.TemporaryDirectory(prefix="scout-readonly-transition-review-") as directory:
    monkeypatch = pytest.MonkeyPatch()
    try:
        root = Path(directory)
        e = base.env.__wrapped__(root, monkeypatch)
        e = t.administrative.__wrapped__(e, root, monkeypatch)
        e = t.add_scout_handoff(e)
        e, old_repair, old_exchange, consumers = t.scout_installed_consumers.__wrapped__(e, monkeypatch)
        before = t.repair._inventory(e["repo"])
        protected = {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in e["original_bytes"]}
        transition = t.transition(e)
        verified = old_repair.verify_transition(e["config"], e["state"], t.repair._read(e["original_binding"]))
        assert verified == {"verified": True, "repairs": 1}
        try:
            old_exchange._check_ownership_binding(e["config"], t.DAY)
        except ValueError as error:
            message = str(error)
            assert message == "Ownership source or operating bindings changed"
        else:
            raise AssertionError("Exact installed ownership comparison unexpectedly accepted administrative drift")
        after = t.repair._inventory(e["repo"])
        protected_after = {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in e["original_bytes"]}
        assert before == after and protected == protected_after
        result = {
            "synthetic_only": True,
            "candidate": "92a094027d97e5bdb8d868a87eff056310a5e354",
            "old_consumer_blob_commit": "37bed6b7b0e0d4c1790b98aa5ea38a23e485795c",
            "started_at_utc": started,
            "completed_at_utc": datetime.now(timezone.utc).isoformat(),
            "transition_status": transition["status"],
            "old_verify_transition": verified,
            "old_ownership_check_error": message,
            "consumer_raw_sha256": consumers,
            "fixture_source_sha256_before": before,
            "fixture_source_sha256_after": after,
            "fixture_protected_sha256_before": protected,
            "fixture_protected_sha256_after": protected_after,
            "result": "reproduced; initial proof verification is compatible, old ownership binding check still rejects",
        }
        result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({k: result[k] for k in ("synthetic_only", "started_at_utc", "completed_at_utc", "old_verify_transition", "old_ownership_check_error", "result")}, sort_keys=True))
    finally:
        monkeypatch.undo()
