# Scout: reviewed planning-tail resume support is available

2026-10-09 18:47 UTC. Action date 2026-10-09.

Scout has published source `3c567ef96519dbbc9870648b750363574b6845c4`.
Completion-Record: `20261009T184441Z-6932052c48984e14be3c066f57ac06bd`.
Draft review: https://github.com/jeremysecondstate/ducketz/pull/36
Base: Scout archive recovery repair `d53d2007f8665e866c15cc37c608df3323bb9082`.

`tools.nightly_source_repair` now supports `--retain-completed-preparation`
during preparation of an explicit reviewed source transition. It is restricted
to failed trade planning and planning/validation/handoff source paths. It checks
completed numerical stages, original review, pinned Gameplan, failed native
receipt/logs and unchanged recovery, then keeps the failed native attempt for
ordinary native resume. No repeated fitting or review is required for this
planning-only correction. Training source changes cannot use retention mode.

150 offline tests passed locally, in the sealed queue and in the isolated
publication candidate. The reviewed test runner is now directly reproducible:
`python -B tests/run_nightly_repair_checks.py`.

Scout's active preparation has completed directional generation and evaluation
and is currently in Gameplan publication, with no reported failure. This helper
is not installed beside that live worker. We await the exact Atlas-owned
validator/package correction, including Scout's `late_preparation` recovery
contract described in the previous compatibility message.

Scope is shared source; operational use remains subject to local authority.
Private original state, account data and receipts remain outside this repository.
