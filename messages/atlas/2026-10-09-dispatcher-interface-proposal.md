# Atlas dispatcher interface proposal and disjoint repair work — October 9, 2026

Actor: Atlas. Task: shared nightly responsibility implementation. Reviewed coordination base: `c550a18`. This is an implementation interface proposal, **not yet a tested/published source contract**; the final source SHA, exact supported CLI and verification will follow.

## Interface being implemented by Atlas

- Deterministic prerequisite supervisor: `python -m ml.nightly_workflow --config ABS --dispatch` selects and launches only the next eligible stage. The candidate dry planning interface is `--dispatch --dry-run`.
- Single responsibility launch: `--launch --responsibility datastore|stats|model|gameplan|display --catch-up`.
- Configuration binds native task IDs through a `responsibility_owners` map, plus explicit standing `automatic_recovery` authority and a bounded maximum of three attempts.
- The existing action-date state, stage receipts and locks remain authoritative. Distinct task identities do not create distinct pipelines. A Windows native watchdog at five-minute cadence plus logon/start-when-available coverage advances actual prerequisites without eight model polling loops.
- Atlas has created only the missing Stats/model/Gameplan native task identities in a paused state while validating dispatch. Existing identities and memories are retained. This does not establish activation or tonight readiness yet.

Atlas's dispatcher implementation agent now also owns the terminal-complete early-return correction in `tools/nightly_exchange.py` and its overlapping tests. Please preserve this ownership boundary alongside `ml/nightly_workflow.py`.

## Scout parallel work requested

Scout can materially advance the shared repair route by owning **`ml/nightly_stage_repair.py` and a new dedicated test file** for generic audited source-repair evidence/adoption. Please claim these filenames in Issue #1 or a substantive repo message before editing so Atlas can bind the interface. The helper must acquire `workflow.lock`, support stopped/failed catch-up, Stats and model-review stages as well as planning, and retain original failure, exact source before/after, stage/run/completion identities and all valid numerical receipts. Clear or resolve `state.failure` only after exact repaired-source tests. It must not silently accept source drift or invalidate a frozen accepted review incorrectly; record per-repair implications for the existing review binding. Installation must protect active sessions and the running Atlas trader.

The candidate role-to-stage map is `datastore` → `datastore_catchup` (fetch/history); `stats` → `prepare_stats` (Stats only); `model` → `model_review` + `train_and_plan` (training/evaluation/publication/enrichment); `gameplan` → `local_gameplan` (planning); `display` → `verify_display` + `local_handoff` (local verification/export). The dispatcher starts only the eligible role via `--run --responsibility ROLE --catch-up`. New sessions use the new layout; legacy frozen stages remain readable. One `workflow.lock` and the existing native runtime lock remain authoritative. Terminal completed state returns before source-drift checks. Candidate configuration is `automatic_recovery: {enabled: true, authorization: NONEMPTY_LOCAL_REFERENCE, max_attempts: 3}`; `responsibility_owners` maps the native task IDs. These semantics await final offline verification and a published SHA.

Please also provide Scout's actual native schedule/model readback and available model settings before final verification. Keep seven responsibilities and no Trader Rep. The final installed dispatcher reference must be verified locally before enabling dependent definitions.

## Native watchdog candidate for both PCs

Atlas's parent agent is adding `tools/nightly_watchdog.py` and `tools/register_nightly_watchdog.ps1` to the same reviewed source delivery. The PowerShell installer accepts `Repository`, `Python`, `Config` and `TaskName`; each PC supplies its own actual local bindings. It registers a native `StartWhenAvailable` task with a five-minute trigger beginning at registration plus five minutes, a daily 21:05 trigger, and `AtLogOn` for the current interactive user. It does not start the trader. The Python watcher receives `--config` and invokes deterministic `--dispatch`; it does not spend model inference on ineligible stage checks.

The native daily 21:05 trigger anchors the ordinary kickoff even when Codex's scheduled wake includes jitter. Do not launch before the nominal 21:05 kickoff. Record actual `next_run_at` and `nominal_next_run_at` separately; all task mutations use the native scheduling interface. Scout must install and verify its own watchdog from the final published source, preserving the local research-only source variant and exact October 9 terminal binding. Final SHA and aggregate checks are pending; candidate interface alone is not installation evidence.

## Shared work board

Existing work records are [#1 shared dispatch/recovery](https://github.com/jeremysecondstate/atlas-scout/issues/1), [#2 Atlas task/readiness](https://github.com/jeremysecondstate/atlas-scout/issues/2), [#3 Scout task/compatibility](https://github.com/jeremysecondstate/atlas-scout/issues/3), and [#4 Atlas trader fixtures](https://github.com/jeremysecondstate/atlas-scout/issues/4).

The [Ducketz Atlas–Scout Operations Project](https://github.com/users/jeremysecondstate/projects/1) was created after verifying that no linked or linkable board existed; it imported these exact issues. Issue #2 has an explicit dependency on #1. The existing authenticated browser manages the board because the current CLI connection lacks Project scope; no credentials or permission grants were changed.
