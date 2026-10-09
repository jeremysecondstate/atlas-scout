# Atlas execution investigation after manual stop — October 9, 2026

Owner: Atlas execution-diagnosis agent. Scope: the normal Atlas trader's repeated submit/cancel report. Scout has no execution role and no ownership of this investigation.

Canonical work record: **[Issue #4](https://github.com/jeremysecondstate/atlas-scout/issues/4), explicitly selected by the Atlas parent**. Concurrent attempts by both coordination agents to defer to the other's record briefly left inconsistent status references. Atlas coordination now owns all Issue #4/#5 metadata changes until this is reconciled; Scout should leave their identity/state unchanged and add only substantive evidence. Issue #5 remains a closed duplicate. Both original reports and Issue #4's completed offline-audit history are retained. One Atlas owner performs diagnosis and correction.

Jeremy reports repeated submission/cancellation behavior and a manual stop. **Subsequent actual runtime readback at 23:47:14 UTC found the original worker still alive**, with a fresh 16:47:11 Pacific heartbeat and saved decisions after the reported stop. Do not describe the worker as STOPPED on the strength of the manual-stop report. Atlas informed Jeremy of this discrepancy and requested his explicit decision about stopping the remaining worker under the manual-control boundary. The private screenshot and raw process/order evidence remain local.

Atlas's saved-evidence diagnosis found repeated broker `REJECTED` attempts bypassing the intended retry-identity protection. The exact provider rejection reason was not persisted. Atlas owns the focused isolated correction and relevant offline regression; no broker call is being made to fill that missing field. The repeated UI status alone does not establish duplicate accepted broker executions or successful cancellations.

Atlas is inspecting the saved private order state, logs, worker/control status and original identities to identify the cause. Preserve the initial report and relevant local evidence. Do not publish order identities, quantities, account information, raw screenshots, financial packets or databases here. The investigation uses saved evidence and offline fixtures; no broker calls, test orders, cancellation requests or trader restart are authorized as infrastructure verification. Jeremy retains manual start/stop control.

Corrective action: reproduce the observed behavior from sanitized offline fixtures, identify and claim any exact source paths before editing, implement a focused correction if it is a source defect, and verify existing-order, partial-fill, net-quantity, restart and duplicate-submission behavior relevant to the cause. Publish the exact reviewed source and install only through the supported audited boundary. Do not assume a successful earlier offline audit proves this newly reported production behavior is correct.

Disposition: **OPEN — Atlas owns the isolated retry-identity correction and verification, with actual worker status tracked separately from the user's stop report.** The original [209-check offline audit](https://github.com/jeremysecondstate/atlas-scout/issues/4#issuecomment-6089611127) remains verified historical evidence; it does not resolve this production incident. The completed October 9 preparation and exact Scout handover remain preserved. Final nightly installation/readback is separate work; Scout should continue its seven-task readiness verification and must not add a Trader Rep or execution-history exchange. No task independently restarts or stops the worker or changes orders.

## Explicit isolated source ownership

Atlas's coordinator owns the focused candidate based on exact published `fe60d55d62b2802716cb5c9af6342480499b910e`; its private ownership record was captured before editing. Shared-file scope is:

- Modify `ml/stock_trader/catchup.py`, `ml/stock_trader/independent_runtime.py`, `ml/stock_trader/horizon_ledger.py`, `ml/stock_trader/horizon_broker.py` and `tests/test_stock_horizon_broker.py`.
- Add `tests/test_catchup_rejection_guard.py` and the focused `docs/development/trader-rejection-recovery.md`.
- Reserve `tests/test_gameplan_catchup.py` for a relevant fixture if needed; it remains unchanged at this checkpoint.

Scout must not edit these paths concurrently. Atlas's parent owns exact final review/queue/publication; a separate Atlas recovery-audit agent owns disjoint launcher investigation. Any additional path claim must be declared before overlapping work. The saved evidence identifies identical payload retries under changing catch-up prediction identities and confirmed rejection, while the provider's original descriptive reason is unavailable. Candidate work is not an installed correction or verified recovery; the running/stopped execution boundary is assessed separately before any deployment.
