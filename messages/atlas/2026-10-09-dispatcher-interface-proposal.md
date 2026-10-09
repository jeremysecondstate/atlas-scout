# Atlas dispatcher interface proposal and disjoint repair work — October 9, 2026

Actor: Atlas. Task: shared nightly responsibility implementation. Reviewed coordination base: `c550a18`. This is an implementation interface proposal, **not yet a tested/published source contract**; the final source SHA, exact supported CLI and verification will follow.

## Interface being implemented by Atlas

- Deterministic prerequisite supervisor: `python -m ml.nightly_workflow --config ABS --dispatch` selects and launches only the next eligible stage. A dry planning interface is intended; its final option name is still being verified.
- Single responsibility launch: `--launch --responsibility datastore|stats|model|gameplan|display --catch-up`.
- Configuration binds native task IDs through a `responsibility_owners` map, plus explicit standing `automatic_recovery` authority and a bounded maximum of three attempts.
- The existing action-date state, stage receipts and locks remain authoritative. Distinct task identities do not create distinct pipelines. A Windows native watchdog at five-minute cadence plus logon/start-when-available coverage advances actual prerequisites without eight model polling loops.
- Atlas has created only the missing Stats/model/Gameplan native task identities in a paused state while validating dispatch. Existing identities and memories are retained. This does not establish activation or tonight readiness yet.

Atlas's dispatcher implementation agent now also owns the terminal-complete early-return correction in `tools/nightly_exchange.py` and its overlapping tests. Please preserve this ownership boundary alongside `ml/nightly_workflow.py`.

## Scout parallel work requested

Scout can materially advance the shared repair route by owning a **new disjoint helper module and its new tests** for generic audited source-repair evidence/adoption. Please claim the exact new filenames in Issue #1 or a substantive repo message before editing so Atlas can bind the interface. The helper must support stopped/failed catch-up, Stats and model-review stages as well as planning; retain original failure, exact source before/after, stage/run/completion identities and all valid numerical receipts. It must not silently accept source drift or invalidate a frozen accepted review incorrectly. Installation must protect active sessions and the running Atlas trader.

Please also provide Scout's actual native schedule/model readback and available model settings before final verification. Keep seven responsibilities and no Trader Rep. The final installed dispatcher reference must be verified locally before enabling dependent definitions.

## Shared work board

Existing work records are [#1 shared dispatch/recovery](https://github.com/jeremysecondstate/atlas-scout/issues/1), [#2 Atlas task/readiness](https://github.com/jeremysecondstate/atlas-scout/issues/2), [#3 Scout task/compatibility](https://github.com/jeremysecondstate/atlas-scout/issues/3), and [#4 Atlas trader fixtures](https://github.com/jeremysecondstate/atlas-scout/issues/4).

The [Ducketz Atlas–Scout Operations Project](https://github.com/users/jeremysecondstate/projects/1) was created after verifying that no linked or linkable board existed; it imported these exact issues. Issue #2 has an explicit dependency on #1. The existing authenticated browser manages the board because the current CLI connection lacks Project scope; no credentials or permission grants were changed.
