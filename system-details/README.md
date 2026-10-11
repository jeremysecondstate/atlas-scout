# Codex–Ducketz system details

This folder is the shared reference library for Jeremy, Atlas, and Scout. It describes how Codex, scheduled tasks, Ducketz, and the two PCs work together.

Each PC maintains its own observed configuration under its named folder. Keep the observation date and time zone visible, distinguish intended behavior from installed state, and identify the evidence behind each claim. A shared document is a reference; it does not change either PC's configuration or establish successful runtime operation.

## Current references

| Topic | Scout | Atlas |
| --- | --- | --- |
| Ducketz scheduled tasks | [Scout scheduled tasks](scout/scheduled-tasks.md) — October 10, 2026 snapshot | [Atlas scheduled tasks](atlas/scheduled-tasks.md) — October 11, 2026 readback, with October 10 history retained |
| Loop A | [Scout reviewed chapter](https://github.com/jeremysecondstate/atlas-scout/blob/31913a790057db85dd41f92bc6741ddc40d75dea/system-details/scout/loop-a.md) — PR #7 | [Atlas reviewed chapter](https://github.com/jeremysecondstate/atlas-scout/blob/bfa2ab9a002c114230ac297c49ae73768c215d40/system-details/atlas/loop-a.md) — PR #8 |
| Loop B | [Scout reviewed chapter](https://github.com/jeremysecondstate/atlas-scout/blob/d42deafb1504a2eca41de3d4ab59993eb509b1b7/system-details/scout/loop-b.md) — PR #10 | [Atlas reviewed chapter](https://github.com/jeremysecondstate/atlas-scout/blob/8487ccdbe873d7cd307e7e3c9f4e22419f8f08c0/system-details/atlas/loop-b.md) — PR #9 |
| Loop C | [Scout curated companion](https://github.com/jeremysecondstate/atlas-scout/blob/f648c1d9f6096b53f5c330bb045ecf85bec2a537/system-details/scout/loop-c.md) — PR #12 | [Atlas dated observations and separate stock execution](atlas/loop-c.md) — also retained in PR #11 |

The [shared Loop C design](https://github.com/jeremysecondstate/atlas-scout/blob/f648c1d9f6096b53f5c330bb045ecf85bec2a537/system-details/loop-c.md) and Scout provenance correction belong to [PR #12](https://github.com/jeremysecondstate/atlas-scout/pull/12). Its separate curation is preserved. The pending [Scout scheduling revision](https://github.com/jeremysecondstate/atlas-scout/blob/dc60ac43b959f1a880e243feb69abfa985f5be9c/system-details/scout/scheduled-tasks.md) belongs to PR #6. Immutable links identify prepared work while these PRs remain unmerged; they do not establish local installation.

## Stats, Gameplan and nightly references

**October 11, 2026 review:** the three shared chapters and Atlas companions are complete in this publication. Scout independently completed its three companions in [PR #13](https://github.com/jeremysecondstate/atlas-scout/pull/13); the links below select those exact reviewed bytes rather than the older main-branch placeholders. Each companion retains its own observation times and evidence limits. Completion of documentation is not proof of current operation or successful trading.

| Topic | Shared explanation (Atlas owner) | Scout evidence (Scout owner) | Atlas evidence (Atlas owner) |
| --- | --- | --- | --- |
| Stats and model feedback | [Shared Stats](stats-and-feedback.md) — reviewed | [Scout Stats](https://github.com/jeremysecondstate/atlas-scout/blob/8b1ef9d547adbaa8ece26de585ce0ef126c70215/system-details/scout/stats-and-feedback.md) — reviewed PR #13 | [Atlas Stats](atlas/stats-and-feedback.md) — verified local inspection |
| Gameplan lifecycle | [Shared Gameplan](gameplan.md) — reviewed | [Scout Gameplan](https://github.com/jeremysecondstate/atlas-scout/blob/8b1ef9d547adbaa8ece26de585ce0ef126c70215/system-details/scout/gameplan.md) — reviewed PR #13 | [Atlas Gameplan](atlas/gameplan.md) — verified local inspection |
| Nightly workflow and recovery | [Shared nightly workflow](nightly-workflow.md) — reviewed | [Scout nightly workflow](https://github.com/jeremysecondstate/atlas-scout/blob/8b1ef9d547adbaa8ece26de585ce0ef126c70215/system-details/scout/nightly-workflow.md) — reviewed PR #13 | [Atlas nightly workflow](atlas/nightly-workflow.md) — verified local inspection |

The [handoff prompt](documentation-handoff-prompt.md) records the original scope and ownership; future work must preserve completed chapters and dated history. Scout's [reviewed handoff](https://github.com/jeremysecondstate/atlas-scout/blob/8b1ef9d547adbaa8ece26de585ce0ef126c70215/messages/scout/2026-10-11-documentation-review.md) records its findings and pending integration boundaries.

Atlas's [dated Loop A history](atlas/atlas-loop-a-2026-10-10.md) now retains the complete portable historical chapter with private detail removed from this proposed edition. Scout's equivalent Loop B correction is in PR #13. Private originals are preserved locally; neither correction erases earlier public Git history or changes main before integration.

The [Atlas scheduling/source follow-up](atlas/nightly-workflow.md#october-11-follow-up-scheduling-versus-reader-verification) separates native timing revisions from an independently documented reader dependency transition. The [Scout follow-up prompt](scout-schedule-supervision-handoff-prompt.md) requests the same independent evidence review and documentation maintenance on Scout; it does not presume matching settings or authorize operating changes.

## Folder convention

- `scout/`: Scout's observed system configuration and responsibilities.
- `atlas/`: Atlas's observed system configuration and responsibilities.
- Shared explanations and comparison documents can live directly in `system-details/` and link to the relevant PC-specific evidence.

Use stable, descriptive Markdown filenames so links survive later updates. Retain dated distinctions when configurations change. Compare logical purpose, schedules, model settings, prerequisites, ownership, and actual outcomes instead of assuming that the two PCs are identical.

Keep credentials, account state, private financial packets, raw data, databases, fitted models, full native task definitions, machine bindings, task memory, and receipts in their existing private locations. Publish a reviewed description or sanitized evidence summary here. See the [coordination operating rules](../coordination/README.md) for ownership and publication boundaries.
