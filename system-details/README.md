# Codex–Ducketz system details

This folder is the shared reference library for Jeremy, Atlas, and Scout. It describes how Codex, scheduled tasks, Ducketz, and the two PCs work together.

Each PC maintains its own observed configuration under its named folder. Keep the observation date and time zone visible, distinguish intended behavior from installed state, and identify the evidence behind each claim. A shared document is a reference; it does not change either PC's configuration or establish successful runtime operation.

## Current references

| Topic | Scout | Atlas |
| --- | --- | --- |
| Loop B | To be observed on Scout | [Atlas Loop B](atlas/loop-b.md) — October 10, 2026 observed chapter |
| Ducketz scheduled tasks | [Scout scheduled tasks](scout/scheduled-tasks.md) — October 10, 2026 snapshot | [Atlas scheduled tasks](atlas/scheduled-tasks.md) — October 10, 2026 snapshot |

## Planned documentation

The nine chapters below are **placeholders, not yet investigated or verified**. Their presence does not establish installed configuration or successful operation. Shared chapters explain common behavior; each PC's companion will provide independently verified local observations.

| Topic | Shared explanation (Atlas owner) | Scout evidence (Scout owner) | Atlas evidence (Atlas owner) |
| --- | --- | --- | --- |
| Stats and model feedback | [Shared Stats](stats-and-feedback.md) | [Scout Stats](scout/stats-and-feedback.md) | [Atlas Stats](atlas/stats-and-feedback.md) |
| Gameplan lifecycle | [Shared Gameplan](gameplan.md) | [Scout Gameplan](scout/gameplan.md) | [Atlas Gameplan](atlas/gameplan.md) |
| Nightly workflow and recovery | [Shared nightly workflow](nightly-workflow.md) | [Scout nightly workflow](scout/nightly-workflow.md) | [Atlas nightly workflow](atlas/nightly-workflow.md) |

Use the [documentation handoff prompt](documentation-handoff-prompt.md) to complete the existing files on each PC. Retain these paths and update each placeholder's status only after its evidence and review are complete. Loop C curation remains a separate task; preserve its compatible index changes.

## Folder convention

- `scout/`: Scout's observed system configuration and responsibilities.
- `atlas/`: Atlas's observed system configuration and responsibilities.
- Shared explanations and comparison documents can live directly in `system-details/` and link to the relevant PC-specific evidence.

Use stable, descriptive Markdown filenames so links survive later updates. Retain dated distinctions when configurations change. Compare logical purpose, schedules, model settings, prerequisites, ownership, and actual outcomes instead of assuming that the two PCs are identical.

Keep credentials, account state, private financial packets, raw data, databases, fitted models, full native task definitions, machine bindings, task memory, and receipts in their existing private locations. Publish a reviewed description or sanitized evidence summary here. See the [coordination operating rules](../coordination/README.md) for ownership and publication boundaries.
