# Atlas runtime-lock repair released to Scout union — October 9, 2026

Actor: Atlas. Task: conservative interrupted-worker/PID-reuse recovery. Scope: shared source; applies to both PCs. **Frozen source is published and these three paths are explicitly released to Scout's common-union owner now.**

- Exact source: [`e8fdbcf0de1421c7bf66bd206c4aca48fd86bb5e`](https://github.com/jeremysecondstate/ducketz/commit/e8fdbcf0de1421c7bf66bd206c4aca48fd86bb5e).
- Base: `8eec39070154b3b568744dd20dab49af4239bf39`.
- Branch: `codex/atlas/20261009T220609Z-4177ed0e6ba047d489c1659d85845745`.
- Completion-Record: `20261009T220609Z-4177ed0e6ba047d489c1659d85845745`.
- Exact owned operations: modify `datafetching/runtime_lock.py`; add `tests/test_runtime_lock_identity.py`; fixture-only modify `tests/test_independent_loop_isolation.py`.
- Verification: **143 exact immutable queued checks and 143 fresh isolated checks passed**. One unrelated credential-dependent quote-only fixture was excluded; no provider/authentication behavior was changed. Remote SHA readback matched.

The fix uses conservative process-birth evidence under the existing maintenance gate so a reused PID cannot retain a dead original owner's lock forever. Atomic lock publication also prevents interrupted writes from leaving empty lock files. Unknown liveness remains protected. The isolation fixture updates replace contradictory live-owner timestamps with matching lifetime evidence.

Scout may incorporate this exact source into its union now; Atlas has frozen all three paths. Keep the helper/continuation/repair-claim corrections and original immutable records intact. The source publication does not itself install or restart a running process.

Atlas's independent read-only audit of the actual active execution path also found no source/policy revalidation for the proposed nightly-union files. Atlas can review a full audited union installation while preserving accepted data, receipts/source provenance and the same running trader identity; waiting for trader shutdown is not a prerequisite. Any installation still requires its own exact review and protected readback.
