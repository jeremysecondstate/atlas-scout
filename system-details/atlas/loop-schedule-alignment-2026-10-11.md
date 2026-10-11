# Atlas loop and scheduled-task alignment — October 11, 2026

Atlas's installed native schedules already match its latest authorized weekday and overnight windows. **Fresh full-definition readback at 12:46:17 PDT agrees with the native scheduler database for all 15 definitions: ten ACTIVE and five PAUSED.** A second readback at 13:10:28 PDT confirmed all fifteen definitions unchanged. No native update or replacement task was required. This dated audit aligns documentation and preserves historical observations; it does not establish a new production run.

The comparison inputs were [Scout's reconciliation at PR #15's exact published revision](https://github.com/jeremysecondstate/atlas-scout/blob/0c76367a79c1b6b224f01c55f63173f2dc7f789f/system-details/scout/loop-schedule-alignment-2026-10-11.md), its [current schedule chapter](https://github.com/jeremysecondstate/atlas-scout/blob/0c76367a79c1b6b224f01c55f63173f2dc7f789f/system-details/scout/scheduled-tasks.md), the [reviewed weekday handoff](https://github.com/jeremysecondstate/atlas-scout/blob/480e531e415518aa3d0f3e7c75788d0d547764dc/messages/atlas/2026-10-11-datastore-weekday-eligibility.md), and [Atlas's latest earlier schedule revision](https://github.com/jeremysecondstate/atlas-scout/blob/3db3ff4d6e750fd9329e14082a5cbce9a1f4c688/system-details/atlas/scheduled-tasks.md). Scout PR #15 is stacked on its PR #13; Atlas's current companion history comes from PR #14. Peer evidence supplied comparison questions, while Atlas's own installed configuration supplied the findings below.

## Verified schedules and discrepancies

All wall times mean **America/Los_Angeles**, following PST/PDT. These are nominal registrations, separate from assigned launch metadata and actual execution.

| Atlas responsibility | Verified nominal schedule | Model / effort |
| --- | --- | --- |
| Datastore Catch-up | ACTIVE; Monday–Friday 21:05 | Luna / low |
| Gameplan Stats | ACTIVE; Monday–Friday 03:00 | Luna / low |
| Model Review Training and Predictions | ACTIVE; Monday–Friday 03:00 | Luna / low; separate substantive reviewer Astra / high |
| Local Gameplan | ACTIVE; Monday–Friday 03:00 | Luna / low |
| Ducketz Display and Readiness | ACTIVE; Monday–Friday 03:35 | Luna / low |
| Joint Gameplan Handoff, including companion | ACTIVE; Monday–Friday 21:00–23:40 every 20 minutes; Tuesday–Saturday 00:00, 00:20, 00:40 | Astra / ultra on both definitions |
| Priority Source Reconciliation, including companion | ACTIVE; same evening and after-midnight windows | Astra / ultra on both definitions |
| Trader Representative | ACTIVE; Monday–Friday 03:55, then 04:05 hourly through 17:05 | Sol / ultra; unrelated operating settings retained |

The five paused definitions remain paused: Hyperliquid Operations Watch, Hyperliquid Paper Improvement, Loops Gameplan Weekly Review, Loops Overnight Gameplan, and the historical overnight-recovery chat follow-up. Their retained recurrences do not schedule active launches. The two companion pairs account for four active definitions and two logical supervision responsibilities.

| Older wording or comparison risk | Current Atlas finding and disposition |
| --- | --- |
| Daily preparation checkpoints or old weekend pause | Superseded by installed Monday–Friday checkpoints and ACTIVE custom night windows. Preserve earlier observations as history. |
| Scout's Stats/Model/Gameplan at 21:05, double Display checkpoint, and 04:05 Datastore fallback | These are Scout settings. Atlas retains 03:00 Stats/Model/Gameplan, 03:35 Display, and its sole 21:05 native Datastore checkpoint. |
| Five-minute synthesis/handoff or source-reconciliation model wakes | Native supervision uses twenty-minute custom windows. The separate Windows watchdog keeps its five-minute timer. |
| Ordinary reconciliation gated at 01:25 | Current native instruction is once per operating evening at the first eligible 21:00 wake, or a later eligible wake in the same window. The after-midnight companion retains that evening and does not repeat the cycle. |
| Cleanup is assumed to cover current night supervisors because its Windows registration is enabled | Installed cadence guard accepts only exact five-minute cron recurrence. Both allowlisted original supervisors now fail it; their after-midnight companions are not allowlisted. This audit documents the gap without broadening cleanup eligibility. |

Atlas Stats owns the dated **03:00 readiness-risk** notification; Atlas Display owns **03:35 missed-confirmation**. This differs from Scout's combined Display checkpoints. Existing original deadlines, notification ledgers, completion receipts and dependency gates remain authoritative. An early assigned wake does not change a nominal checkpoint or justify an early deadline alert.

## Nominal versus assigned next launch

This table records future scheduler metadata observed at 12:46:17 PDT on October 11. It is not observed execution or a promise of exact starts.

| Responsibility | Next nominal Pacific slot | Saved assigned Pacific launch |
| --- | --- | --- |
| Gameplan Stats | Monday, October 12, 03:00:00 | October 12, 03:00:09 |
| Model Review Training and Predictions | Monday, October 12, 03:00:00 | October 12, 03:02:15 |
| Local Gameplan | Monday, October 12, 03:00:00 | October 12, 02:55:34 |
| Ducketz Display and Readiness | Monday, October 12, 03:35:00 | October 12, 03:34:40 |
| Trader Representative | Monday, October 12, 03:55:00 | October 12, 03:55:00 |
| Both evening supervisors | Monday, October 12, 21:00:00 | October 12, 21:00:00 |
| Datastore Catch-up | Monday, October 12, 21:05:00 | October 12, 21:05:40 |
| Both after-midnight companions | Tuesday, October 13, 00:00:00 | October 13, 00:00:00 |

These October dates use PDT (UTC−07:00). Native recurrence strings omit `TZID`; Pacific interpretation is supported by the current prompts/configuration, host zone and native nominal epochs. Offline calendar checks covered the autumn transition and preserved the Monday 04:00 deadline at its correct PST offset. Future native scheduler behavior through a DST transition was not executed or observed.

## Executable responsibilities

Five local responsibility owners cover seven workflow steps, before the separate joint exchange:

```text
DATASTORE: datastore_catchup
  Loop A core -> configured OPRA/catalog tail -> separate stock-target history
STATS: prepare_stats
MODEL: model_review -> train_and_plan
  Loop B directional generation -> Gameplan evaluation/publication -> enrichment
GAMEPLAN: local_gameplan
DISPLAY: verify_display -> local_handoff
separate Scout numerical synthesis -> Atlas exact combined-result adoption
```

[Loop A](loop-a.md) core completion does not establish completion of the broader datastore/history responsibility. [Loop B](loop-b.md), invoked through `ml.prediction_runtime --once`, is one numerical stage inside the MODEL responsibility; Stats and substantive model review precede it, while independent Gameplan evaluation/publication and stock enrichment follow it. Planning, display, joint handoff/adoption, repository reconciliation and completed-chat cleanup have separate responsibilities. Atlas does not duplicate Scout's numerical synthesis. The [nightly workflow chapter](nightly-workflow.md) retains the detailed ownership and saved-outcome history.

Dependency dispatch can advance a successor before its nominal native checkpoint. A schedule or active task does not authorize overlapping workers, re-running a completed source/action session, bypassing accepted model review, or altering trader controls.

## Calendar, Windows tasks and cleanup

The application calendar selects the source session and next action session. Friday preparation normally targets Monday; holidays follow that calendar. Morning checkpoints use Monday–Friday. Each night supervision responsibility has nine evening slots and three after-midnight slots: Friday continues through Saturday 00:40, retaining Friday's operating identity. Sunday evening is excluded. No new supervisor launch is scheduled at or after 01:00; 00:40 is a final launch slot, not a forced stop for healthy already-owned work.

The 21:05 preparation kickoff and original action-date **04:00 deadline** remain separate from the 21:00 supervision window. Offline cases verified Friday/Saturday/Monday continuity, Monday pre-kickoff ineligibility, and autumn DST deadline conversion. Atlas has no added native 04:05 fallback; Scout's existing fallback does not move its original 04:00 deadline. Existing deterministic fallback/recovery semantics and terminal receipts were preserved.

| Windows registration | Read-only registration and outcome evidence |
| --- | --- |
| Ducketz Nightly Responsibility Dispatch | Enabled/Ready; daily 21:05, five-minute timer and logon; three-minute task limit; saved last result 0 at 12:43:25 PDT |
| Ducketz Completed Scheduled Chat Cleanup | Enabled/Ready; five-minute timer and logon; four-minute task limit; saved last result 0 at 12:43:29 PDT |
| Ducketz Independent Stock Session | Disabled; retained Monday–Friday 03:55 trigger; its next-run timestamp does not activate it |

No Windows registration was invoked or changed for verification. The dispatcher can inspect eligible existing work outside the native weekday schedule; weekday Codex settings do not disable all deterministic weekend activity. Original calendar, ownership, deadline and receipt gates still apply.

The installed cleanup helper retains an exact-five-minute cadence predicate and an allowlist containing only the two original handoff/source definitions. The offline predicate checks rejected both current twenty-minute originals and accepted a historical five-minute control. The two companions fail the separate allowlist boundary. Reading the saved 12:43:30 PDT cleanup outcome found zero considered, eligible or archived chats; that record does not establish why no candidate was considered. The independently inspected predicate establishes the present coverage gap. Repair would require separate review of the helper and its installation; this audit neither changes that policy nor archives chats.

## Validation and evidence limits

Atlas's pinned coordination manifest and all 29 declared files were verified, and its local profile establishes Atlas identity and GitHub-only routine coordination. Full saved native definitions and read-only database rows agree for all 15 tasks. Current native schedules already reflect the reviewed handoffs, so their identities, prompts, models, contexts, notifications, memory and private bindings were left unchanged.

Offline executable-boundary checks passed **13 tests, with 78 deselected**. Pure calendar and installed-cleanup-predicate checks passed **seven calendar cases and three predicate cases**. These checks exercised no provider/broker call, training, prediction generation, synthesis, application restart/deployment or trader operation. Exact definitions, bindings, hashes, original evidence and detailed receipts remain private.

This revision preserves the earlier Atlas PR #14 chapter history and Loop A privacy correction, links the immutable reviewed Loop A/B chapters, and adds current schedule/boundary explanations. Configured schedules, local installation, documentation publication and actual runtime completion are separate claims. The audit establishes the first two within its inspection scope; publication requires its own verified commit/PR, and no new runtime completion is asserted. Current loaded application modules, future launches and expanded cleanup coverage remain unverified.

Actor: Atlas. Producer: human-authorized-development. Task: loop-schedule-alignment. Scope: sanitized Atlas-local schedule/configuration findings and shared task-boundary documentation; Scout retains its own verified times and bindings. Reviewed documentation base: `3db3ff4d6e750fd9329e14082a5cbce9a1f4c688`. Completion-ID: `20261011T194859Z-atlas-loop-schedule-audit-ddac2770`.
