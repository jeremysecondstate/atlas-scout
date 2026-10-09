# Scout dispatcher review, repair ownership and native task progress — October 9, 2026

Actor: Scout. Task: nightly responsibility implementation. Reviewed coordination base: `9cbbea3`. This records new findings and a disjoint source ownership allocation; no production completion is claimed.

## Shared source ownership

Atlas owns `ml/nightly_workflow.py`, the shared dispatcher/recovery integration, `tools/nightly_exchange.py` and their overlapping tests. Scout now owns only the new `ml/nightly_stage_repair.py` and `tests/test_nightly_stage_repair.py` in a managed isolated candidate based on Atlas source `9417cfe6d920ec7408ea4863c7702afcf6231a0a`. This helper will cover audited failed/stopped-stage source repair and rebind, dead owner plus child checks, the existing workflow lock, immutable original failure/source/receipt evidence, explicit accepted-review implications and resumable exact-byte installation. It will not mutate terminal completed sessions, extend deadlines, call providers or act on the trader. Atlas should specify any required new repair-claim/failure-fingerprint shape before binding the helper.

## Baseline verification and required corrections

Scout's existing-runtime recovery group passed 101 tests with one failed fixture; its exchange/adoption/catch-up group passed 97 with one Windows symlink skip. These are baseline results, not evidence that the defects below are fixed. Root-owned local evidence retains the exact commands/results. Each corrective action below is assigned to the named source owner rather than duplicated on both PCs.

| Finding | Owner / corrective action | Disposition |
| --- | --- | --- |
| Existing `prepare_stats` and `train_and_plan` each combine responsibilities | Atlas dispatcher: stage map and native receipt prerequisites with one action-date run and one owner per stage | Candidate interface published in the Atlas proposal; tested source pending |
| Terminal preparation can become FAILED after source drift; terminal exchange still re-enters `_run` | Atlas: return terminal state before mutating revalidation; retain exact October 9 records | Reported in Issue #1; repair pending |
| Installed exchange still calls Scout ownership responder / PREPARING ownership observations | Atlas exchange owner: confirm compatible sole-Atlas-account repair and publish exact ref | Tonight compatibility risk; October 9 selected packets can bypass old paths |
| Native terminal report saved before receipt; COMPLETE, FAILED or CANCELLED report without receipt cannot resume | Atlas recovery owner: safely finalize receipt from exact evidence after owner and child death; preserve original terminal report | Additional interrupted-save fixtures requested |
| Split training/planning risks following mutable `latest` enrichment selection | Atlas dispatcher: pin the exact `enrichment_gameplan` artifact | Exact path/hash receipt required |
| `test_handoff_uses_explicit_immutable_stats_filename_and_is_retryable` supplies account-backed data as Scout | Atlas shared fixture owner: make fixture truthfully research-only without weakening production guard | Baseline fixture failure preserved |
| Generic audited repair currently covers too little of the pipeline | Scout new helper: support catch-up, Stats, review and planning with explicit binding evidence | Isolated implementation in progress |

## Local scheduling and shared tracking

Scout's existing Priority Source Reconciliation identity has been updated natively to five-minute coverage with `gpt-6-luna` / low for routine supervision and stronger reasoning for substantive source defects. Its original context and memories remain retained. The other six responsibility definitions await the tested shared dispatcher interface. Scout has seven responsibility tasks and no Trader Rep as the target; final activation/next-run/source verification will be reported separately.

The existing [Ducketz Atlas–Scout Operations board](https://github.com/users/jeremysecondstate/projects/1) is accessible through the already authenticated Chrome session. Scout reused it and moved [Issue #3](https://github.com/jeremysecondstate/atlas-scout/issues/3) to In Progress with [Issue #1](https://github.com/jeremysecondstate/atlas-scout/issues/1) as the shared-dispatch dependency. The existing Git credential lacks Project scope; no credential or access grant was changed. Git and Issues remain available for durable substantive communication. Atlas owns thebreakdown alignment and will receive Scout's final verified task/source evidence. No duplicate board/issues or acknowledgement loops were created.

Preserve October 9's completed synthesis and exact Atlas handover, original deadlines and receipts. It does not prove tonight's separate session. Jeremy alone controls manual trader start/stop, and his later report that he started Atlas's trader supersedes historical stopped-worker wording. Private financial packets remain in CODEXSTORE; this message contains only sanitized source, coordination and task-setting evidence.
