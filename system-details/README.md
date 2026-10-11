# Codex–Ducketz system details

This folder is the shared reference library for Jeremy, Atlas, and Scout. It describes how Codex, scheduled tasks, Ducketz, and the two PCs work together.

Each PC maintains its own observed configuration under its named folder. Keep the observation date and time zone visible, distinguish intended behavior from installed state, and identify the evidence behind each claim. A shared document is a reference; it does not change either PC's configuration or establish successful runtime operation.

## Current references

| Topic | Scout | Atlas |
| --- | --- | --- |
| Ducketz scheduled tasks | [Scout scheduled tasks](scout/scheduled-tasks.md) — October 10, 2026 snapshot | [Atlas scheduled tasks](atlas/scheduled-tasks.md) — October 10, 2026 snapshot |

## Folder convention

- `scout/`: Scout's observed system configuration and responsibilities.
- `atlas/`: Atlas's observed system configuration and responsibilities. See the [Atlas Loop A chapter](atlas/loop-a.md) — October 10, 2026 observation.
- Shared explanations and comparison documents can live directly in `system-details/` and link to the relevant PC-specific evidence.

Use stable, descriptive Markdown filenames so links survive later updates. Retain dated distinctions when configurations change. Compare logical purpose, schedules, model settings, prerequisites, ownership, and actual outcomes instead of assuming that the two PCs are identical.

Keep credentials, account state, private financial packets, raw data, databases, fitted models, full native task definitions, machine bindings, task memory, and receipts in their existing private locations. Publish a reviewed description or sanitized evidence summary here. See the [coordination operating rules](../coordination/README.md) for ownership and publication boundaries.
