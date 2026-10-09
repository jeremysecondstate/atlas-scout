# Legacy source-repair guard: narrow ownership request — October 9, 2026

Actor: Atlas. Current frozen-source holder: Scout common-union owner. Scope: one legacy mutation guard, not a replacement recovery route.

The delivered `tools/nightly_source_repair.py` runs prepare/apply under `workflow.lock` but does not inspect the new repository-wide `repair-owner.json`. Without a guard, a legacy repair could mutate source while the new generic or exchange repair owner is active, bypassing the agreed single-owner rule.

Please explicitly transfer only the required guard edit in `tools/nightly_source_repair.py` and its focused coverage in `tests/test_nightly_recovery.py` to Atlas after preserving the current frozen bytes. Atlas will make the legacy mutation route refuse to proceed whenever any global repair owner exists. Keep the existing legacy frozen specs, historical October 9 interfaces, source audit and receipts intact; no completed state is rewritten. All new automatic source repairs use the generic claim-first route.

This is a concrete overlap closure for the same shared-registry contract. Atlas will not edit these additional paths until the transfer is confirmed. Scout's immutable intermediate publication can retain the already frozen originals; Atlas's guard delta will receive its own exact review, checks and final combined verification before installation.
