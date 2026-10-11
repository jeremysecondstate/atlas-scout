# Scout loop and scheduled-task alignment — October 11, 2026

Scout's five preparation and morning checkpoint definitions now use **Monday–Friday eligibility**, with their existing Pacific wall-clock times. Native updates and saved-definition verification completed on **October 11, 2026, at 12:33:20 PDT**. This adopts the [reviewed Atlas weekday handoff at immutable commit `480e531`](https://github.com/jeremysecondstate/atlas-scout/blob/480e531e415518aa3d0f3e7c75788d0d547764dc/messages/atlas/2026-10-11-datastore-weekday-eligibility.md). The earlier October 10 loop chapters and [scheduled-task inventory](scheduled-tasks.md) retain their dated observations; this revision supersedes their daily checkpoint eligibility.

The loop boundaries still agree with the inspected source. **Loop A's completed core cycle is an upstream prerequisite; the DATASTORE responsibility also includes separately configured stock-target history. Loop B is the directional numerical stage inside the larger training/predictions responsibility.** A scheduled wake, dispatched worker, completed loop, accepted publication and finished joint workflow remain separate facts.

The preparation workflow has **seven steps and five local responsibility owners**:

```text
DATASTORE: datastore_catchup
  -> STATS: prepare_stats
  -> MODEL: model_review -> train_and_plan
       Loop B directional generation
       -> Gameplan evaluation -> Gameplan publication -> stock enrichment
  -> GAMEPLAN: local_gameplan
  -> DISPLAY: verify_display -> local_handoff
  -> separate joint synthesis / Atlas acceptance
```

Loop B runs through `ml.prediction_runtime --once`; it is not the whole MODEL responsibility. Model review precedes it, while independent Gameplan training/publication and enrichment follow it. Local planning consumes the completed numerical segment. Synthesis and repository reconciliation are **two additional logical supervision responsibilities**, each represented by an evening definition and an after-midnight companion. The companions preserve their canonical owner, memory, claims and completion identities.

All times below use **America/Los_Angeles**, following PST/PDT. These are nominal registrations, not promises of exact starts or permission to bypass dependencies.

| Logical role | Current state and nominal Pacific eligibility | Model / effort | Relationship to the loops |
| --- | --- | --- | --- |
| Scout DATASTORE CATCH-UP | Active; Monday–Friday 21:05 and 04:05 fallback | `gpt-6-luna` / low | Loop A catch-up and separate target-history prerequisites |
| Scout GAMEPLAN STATS | Active; Monday–Friday 21:05 | `gpt-6-luna` / low | Completed-session Stats after datastore completion |
| Scout MODEL REVIEW, TRAINING & PREDICTING | Active; Monday–Friday 21:05 | Supervisor `gpt-6-luna` / low; internal reviewer `gpt-6-astra` / high, 1,800-second limit | Review plus numerical segment containing Loop B and downstream Gameplan/enrichment |
| Scout GAMEPLAN | Active; Monday–Friday 21:05 | `gpt-6-luna` / low | Local planning after accepted numerical output |
| Scout DUCKETZ DISPLAY | Active; Monday–Friday 03:00 and 03:35 | `gpt-6-luna` / low | Display/handoff verification; dated readiness-risk and missed-confirmation alerts |
| Scout GAMEPLAN SYNTHESIS, including after-midnight companion | Active; Monday–Friday 21:00–23:40 every 20 minutes; Tuesday–Saturday 00:00, 00:20, 00:40 | `gpt-6-astra` / ultra | Joint research synthesis and exact handoff to Atlas |
| Scout REPO RECONCILIATION, including after-midnight companion | Active; same evening and after-midnight windows | `gpt-6-astra` / ultra | Source/dependency repair and installation supervision; ordinary reconciliation once per operating evening at the first eligible 21:00 wake |
| Loops Overnight Gameplan | Paused; retained daily 21:05 definition | `gpt-6-astra` / ultra | Historical monolithic workflow; no additional active pipeline |
| Loops Gameplan Weekly Review | Paused; retained Saturday 09:00 definition | `gpt-5.6-luna` / medium | Retrospective evaluation; distinct from Loop B's weekly forecast routes |
| Hyperliquid Operations Watch | Paused; retained every-30-minute definition | `gpt-6-luna` / low | Separate simulated-crypto system |
| Hyperliquid Paper Improvement | Paused; retained hourly definition | `gpt-6.1-sol` / medium | Separate simulated-crypto system |
| Windows nightly dispatcher | Enabled; daily 21:05, separate five-minute timer, and logon | Deterministic | Dependency-driven dispatch of the next eligible responsibility |
| Windows completed scheduled-chat cleanup | Enabled; five-minute timer and logon | Deterministic | Chat maintenance; no loop computation, readiness or acceptance role; current eligibility limitation below |

This is **13 Ducketz Codex definitions: nine active and four paused**. The paired supervision definitions account for four of the nine active registrations. Windows tasks are separate from that count.

Friday evening prepares the next application action session, normally Monday. There is no Sunday-evening Codex preparation checkpoint. DISPLAY's morning eligibility is Monday–Friday, whereas the two after-midnight supervision companions use Tuesday–Saturday to continue the preceding operating evening. Each supervision responsibility has 12 nominal wakes per operating evening, with Friday continuing through Saturday 00:40. No new supervision launch is scheduled at or after 01:00; late off-window catch-up must defer production work, while healthy already-claimed work retains its owner and original cutoffs.

The original action-date deadline remains **04:00**. The **04:05 fallback does not move or reset it**. The application calendar still selects source session and action date; bounded recovery preserves recorded deadlines and evidence. The Windows dispatcher's daily/five-minute/logon triggers were intentionally retained. They can inspect existing workflow state outside Codex checkpoint times, so weekday Codex registration does not imply that all deterministic activity stops on weekends. Dependency, calendar, ownership and terminal-receipt gates still govern dispatch. DISPLAY verification may also occur as soon as planning finishes; its 03:00/03:35 wakes are notification checkpoints.

Saved next-launch readback at the verification timestamp distinguishes the nominal slot from the scheduler's currently assigned time. The assigned times below are future metadata, not observed executions.

| Role | Next nominal Pacific checkpoint | Saved assigned Pacific launch |
| --- | --- | --- |
| DUCKETZ DISPLAY | Monday, October 12, 03:00:00 PDT | October 12, 03:00:00 PDT |
| DATASTORE CATCH-UP | Monday, October 12, 04:05:00 PDT | October 12, 04:09:05 PDT |
| GAMEPLAN STATS | Monday, October 12, 21:05:00 PDT | October 12, 21:04:33 PDT |
| MODEL REVIEW, TRAINING & PREDICTING | Monday, October 12, 21:05:00 PDT | October 12, 21:06:01 PDT |
| GAMEPLAN | Monday, October 12, 21:05:00 PDT | October 12, 21:09:29 PDT |
| SYNTHESIS and RECONCILIATION evening definitions | Monday, October 12, 21:00:00 PDT | October 12, 21:00:00 PDT |
| Both after-midnight companions | Tuesday, October 13, 00:00:00 PDT | October 13, 00:00:00 PDT |

All five native updates succeeded. Exact before/after comparison found only recurrence, narrow eligibility/timing prompt prefixes, and update timestamps changed. Each original prompt remains an exact suffix. Status, models, effort, contexts, notification policies, task identities and memory were preserved; all other definition bytes were unchanged. Offline validation passed **1,820 recurrence instances and 10 night-window cases**, including both DST offsets and Friday-to-Saturday continuity. A second readback at 12:34:20 PDT confirmed the same definitions. Exact definitions, prompt hashes and verification evidence remain private.

Two discrepancies remain recorded rather than treated as current scheduling authority. The older nightly-operations runbook still describes five-minute synthesis/reconciliation and a 01:25 ordinary review, and the DISPLAY prompt retains older five-minute synthesis alert-coverage wording in its historical suffix. The new explicit DISPLAY timing prefix supersedes that premise and preserves its 03:00/03:35 alert ownership and ledger. Separately, the installed cleanup helper only admits an exact five-minute Codex recurrence; its allowlisted synthesis/reconciliation definitions now use the custom twenty-minute windows, so new chats from those definitions fail that cadence eligibility check. An enabled cleanup task or successful process exit does not establish that a chat was archived. The cleanup task was not changed by this correction.

This review verified source boundaries, saved registrations and offline recurrence behavior. It did not run provider calls, training, prediction generation, synthesis, application restarts, deployment or trading, and it does not revalidate the older runtime outcomes in the dated loop chapters. Scout's schedule adoption is complete; documentation publication, Atlas verification and runtime outcomes require their own evidence. A [ready-to-paste Atlas review prompt](atlas-loop-schedule-review-prompt.md) accompanies this report.

Actor: Scout. Producer: human-authorized-development. Task: loop/schedule alignment. Scope: shared sanitized description of Scout-local installation; Atlas keeps its independently verified bindings and checkpoint times. Completion-ID: `20261011T193224Z-scout-loop-schedules-287ebbc5`. The follow-up preserves the exact historical schedule chapter from [PR #13](https://github.com/jeremysecondstate/atlas-scout/pull/13), reviewed parent `56d7f19084576f14447b66e9934f41ad8b61b90a`. Private dated loop originals and full native evidence are not part of this publication.
