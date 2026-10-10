# Atlas trader incident — installed repair and verified disposition

**Verified complete at October 10, 2026, 00:40:53 UTC / October 9, 17:40:53 Pacific.** Atlas installed the exact reviewed repair and verified fresh imports, local readiness and protected history. No new live production trade run was started and no test orders were submitted. Jeremy retains manual trader start/stop. This disposition supersedes the earlier OPEN/publication-pending checkpoints in [the preserved investigation](2026-10-09-trader-submit-cancel-investigation.md).

## Failure, cause and correction

The original production evidence showed repeated broker rejections under changing catch-up prediction identities. A subsequent bounded read-only diagnostic for the actual incident established an opposite-side, same-equity, same-limit-price broker conflict. The original log had omitted that descriptive reason; its bytes remain unchanged and the later diagnostic remains separate evidence. No accepted duplicate executions or successful cancellations were inferred from UI submission labels.

The installed normal worker now preserves rejected-intention retry identity and defers conflicting orders using current account-wide open orders plus earlier submissions within the same batch. It does not cancel, replace or silently net orders to bypass the conflict. Original order, fill, symbol, horizon, account and allocation identities remain intact; missing records are not interpreted as zero holdings.

The manually invoked launcher now handles Ctrl-C/window-close for its own exact worker scope, including an exact adopted process pair, and refuses control of partial or wrong-birth attachments. The focused readiness parser accepts the installed runtime lock's birth-aware field while preserving readiness authority and existing account-first-use behavior. This source correction does not grant any scheduled responsibility authority to start, stop or restart the trader or change orders.

The [published operating runbook](https://github.com/jeremysecondstate/ducketz/blob/37bed6b7b0e0d4c1790b98aa5ea38a23e485795c/docs/development/trader-rejection-recovery.md) and [draft PR #49](https://github.com/jeremysecondstate/ducketz/pull/49) describe the exact changed behavior and validation.

## Separate publication, installation and verification

| Evidence stage | Verified fact |
| --- | --- |
| Published source | `37bed6b7b0e0d4c1790b98aa5ea38a23e485795c`, Completion-Record `20261010T001404Z-3123109b890f4a11a7c28d1baf883396`, Atlas branch of the same identity; all 28 published blobs and remote SHA verified. |
| Reviewed closure | Sixteen repair files plus twelve already-published prerequisite files. Existing reviewed Atlas account/readiness prerequisites are retained explicitly; Scout's separate common-main work and unrelated Hyperliquid source are preserved. |
| Frozen queue checks | 558 passing offline cases on exact captured bytes. |
| Separate isolated courier checks | 558 passing offline cases on the exact publication closure. |
| Actual Atlas composition | 558 passing offline cases on the exact sixteen-file repair overlay over Atlas's existing source, with zero import violations or source/test/active drift. |
| Guarded installer | 49 passing private fault/concurrency/identity checks; the earlier 45-check checkpoint remains historical. |
| Actual installation | `atlas-trader-incident-20261009-v2`, phase INSTALLED, completed at **00:39:38 UTC**. The retained v1 manifest was never applied. |
| Actual post-install readback | Fresh imports of five changed modules, local readiness and full protected-history verification passed at **00:40:53 UTC**. |
| Preserved state | All 74 protected files, eight trees and 428 unowned source files unchanged, including original accepted receipts/history. The sole additive Monday PENDING record was independently reviewed and separately preserved; it is not a completed or dispatched preparation. |
| Worker / execution boundary | Original worker naturally ended at the normal 17:00 Pacific close, `FINISHED_WITH_ERRORS`; process ABSENT at final readback. No agent stop/restart, control change or order action. |

The private manifest SHA-256 is `881c6e381bcae064234ea0a35a43c2cc5014bb60bb5ca3a9199858ce5432fd19`; journal `7c3fe21fc47a5a2a95a54dacd2c58d616ea74c26c052daf410043048a700b6fa`; final readback `87fd9e56ea04c78edd8c7bf978f3ce0e5e8a38d3b5db60ea6d001ac7f626233e`. The local readback file is `scratch/nightly-operations/trader-cancellation-incident/atlas-trader-incident-20261009-v2-readback.json`. Raw financial evidence, full history and local controls remain private.

All eight Atlas task memories were supplemented at **00:41:13 UTC** with the dated installed repair and manual-control boundary; every prior byte was retained. Native definitions remain ACTIVE. Atlas's final native files are `scratch/nightly-operations/native-task-readback-final.json` and `windows-task-readback-final.json`; actual 00:09 UTC readback showed all eight ACTIVE, enabled watchdog, and a natural 17:08:25 Pacific exit-zero wake correctly selecting Monday `WAITING_KICKOFF`, Friday 21:05 due time and Monday's original 04:00 deadline, with no dispatch. The earlier task table's next-wake values remain explicitly dated observations.

## Current conclusion

[Canonical Issue #4](https://github.com/jeremysecondstate/atlas-scout/issues/4) is **fixed, installed and offline/runtime-readback verified**. The original 209-check audit, production failure, manual-stop report, still-live observation, natural exit, candidate checks and installation checkpoints remain retained. The later repair is not presented as proof of a new successful production trading session.

The October 9 exact Scout handover and local setup are retained. Monday's handover is not yet present, as expected before tonight's separate **Friday, October 9 at 21:05 Pacific** launch for **Monday, October 12**. A final read-only binding audit confirmed that Monday has only an inert exchange PENDING status: no preparation run, binding, packet or executable transition exists. First launch will bind the newly installed source under the normal workflow lock; no frozen source or cutoff was rewritten. [The verified nightly arrangement](2026-10-09-final-nightly-readiness-verified.md) remains configured on both PCs. Future execution depends on the PC/application, usage, authentication, data and private exchange availability, and the normal trader only runs when Jeremy chooses to start it. No additional agent start/stop permission is needed to finish this installed-source verification because no such action is being taken.
