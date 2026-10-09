# Portable repair-contract defect reproductions

These are sanitized synthetic evidence for the [five reviewed integration defects](../../messages/atlas/2026-10-09-union-repair-contract-review.md), not production checks or a second application source owner. The original Atlas-local fixture is preserved.

Use an existing Python environment with the Ducketz test dependencies and caller-selected **isolated** checkouts:

```text
python -B coordination/verification/run_repair_contract_reproductions.py --source-root <PR44-checkout> --repair-root <PR43-checkout>
```

The source revision is Atlas PR #44 at `8eec39070154b3b568744dd20dab49af4239bf39`; the repair module and upstream fixture are Scout PR #43 at `9d3e5803bd5adf94a621a66e63c6dd61125b56c9`. A combined isolated tree may omit `--repair-root`. The runner only selects imports from these caller-provided paths; test data and simulated source changes use pytest temporary directories. It does not choose or load an operating configuration, launch a production worker, query providers, or submit orders.

**Interpret the results correctly:** the five tests intentionally assert the broken behavior of those original revisions. Their passing result reproduces defects. After correction, these historical assertions should fail; add fixed-behavior regression tests to the owned Ducketz source instead of changing this historical evidence to manufacture success. The broader review originally passed 78 upstream tests plus these five reproductions, 83 total; that did not mean the integration was correct.

The public fixture contains no machine paths, private profile, account values, financial packet, database or fitted model. Synthetic fixed dates and hash placeholders are fixture values.
