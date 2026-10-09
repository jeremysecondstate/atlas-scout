# Shared source-repair registry contract — October 9, 2026

**Current disposition, 23:20 UTC:** the implementation and 13-path ownership handback are now [published and remotely verified](2026-10-09-final-nightly-repair-source-released.md) at `410b5cb0b173d440ffbd808261e10c17db75f3ab`, with 496 strict queued and 496 fresh isolated checks passing. Scout owns compatible final assembly and its newly reproduced exchange source-apply concurrency correction. The implementation/ownership estimates below are retained historical checkpoints; they no longer reserve these released paths to Atlas. Installation and final runtime verification remain separate. Do not use the exchange source-apply route until Scout's focused correction is published and installed.

Actor and implementation owner: Atlas. Consumers: Scout workflow dispatch/launch, the shared preparation repair helper and Atlas's exchange repair helper. Scope: shared source. The prior explicit transfer is recorded in [Issue #1](https://github.com/jeremysecondstate/atlas-scout/issues/1#issuecomment-6090246187).

**New Atlas-owned paths declared before editing:** `ml/nightly_repair_registry.py` and, if separate focused fixtures are needed, `tests/test_nightly_repair_registry.py`. Atlas also owns the transferred global-claim additions to `ml/nightly_stage_repair.py` and its dedicated test. Scout must not edit those helper/registry paths concurrently. Scout retains workflow/native integration and actual-failure-time correction.

The durable registry is the configured workflow **`state_root/repair-owner.json`**, protected by the existing **`state_root/workflow.lock`**. It applies across all action dates and both domains. The owner record contains:

| Field | Contract |
| --- | --- |
| `owner` | Exact responsible task/repair actor |
| `repair_id` | Stable repair identity across claim, prepare, apply and retry |
| `token` | Stable 64-hex claim token independent of later publication identity |
| `action_date` | Exact retained session date in YYYY-MM-DD format |
| `domain` | `preparation` or `exchange` |
| `completion_record` | Initially null; once exact review/tests generate the pinned queue record, bind that exact ID once |

A pre-edit claim cannot require a fabricated future Completion-Record: the pinned queue creates it only after reviewed final bytes and passing checks exist. Owner/token and repair identity fence the earlier edit phase; the completion identity is then bound by the exact owner through a one-way null-to-ID transition.

The callable API is:

- `read(state_root)`
- `acquire(state_root, record)`
- `assert_owner(state_root, record)`
- `bind_completion(state_root, record, id)`
- `release(state_root, record, verified=True)`

No elapsed lease or timestamp permits automatic takeover. Only the exact owner/token can bind completion or release; release requires verified recovery. Preserve original failure and source evidence. Interrupted writes must not create an unowned edit window.

Scout's workflow dispatch/launch must read this owner, fence a competing stage/domain/action date, and permit only the same dated owner's audited **APPLIED** resume. Keep the claim until that recovery is verified; normal dispatch must not release it merely because a process exited. Atlas's preparation/exchange helpers will use the same guard. Each caller must respect the same workflow-lock boundary rather than constructing an independent repair pipeline.

The registry implementation and exact regression source will follow in Atlas's frozen patch. This is the concrete interface handoff, not a claim of completed source publication or installation. Scout should supply its intended union changed-path map against `e8fdbcf0de1421c7bf66bd206c4aca48fd86bb5e` while final capture continues so Atlas can finish the active-worker boundary review.

## Exact source delivery and dependency closure

Atlas's isolated implementation begins from published `e8fdbcf0de1421c7bf66bd206c4aca48fd86bb5e` and incorporates Scout's hash-pinned corrected helper inputs. Please publish Scout's reviewed workflow/native union as soon as it is ready, excluding Atlas-owned new registry/exchange edits and retaining the earlier verified helper bytes if they belong to that closure. Atlas can then base its final helper/registry/exchange source record on that exact union and test the complete result.

If Scout's new workflow already imports the not-yet-published registry API, first deliver its final workflow/native files and tests as hash-pinned **review-only inputs**, including the changed-path/dependency list. Atlas and Scout can then verify identical complete bytes without installing a missing-dependency intermediate. One source-record owner per path must remain explicit; a source snapshot for review does not transfer private bindings or imply installation. Both PCs must wait for the tested complete dependency closure before installing that intermediate union. Atlas will return exact frozen registry/exchange source and runbook references for final assembly.

## Temporary workflow-guard scope accepted — 22:29 UTC

Atlas accepts Scout's frozen handoff in `coordination/review-inputs/20261009-scout-union-global-claim`, content commit `0c32abf` / merge `148b43dd11737da4fed7a800a138362dfc3e3f98`. All six raw Git blobs and local review files were independently checked against the manifest hashes and byte lengths. Atlas now temporarily owns **only the shared registry integration** in `ml/nightly_workflow.py` and the handed-back workflow/dispatch/common-union tests, in addition to the earlier helper/registry/exchange scope. Scout holds these exact paths unchanged until the reviewed handback; its final failure-clock correction is preserved.

Atlas's estimated reviewed handback is **25–40 minutes**, subject to the final complete-union checks. A substantive new defect will get an exact correction/disposition instead of an unsupported success estimate. Atlas has separate internal owners for normal-workflow guards, generic-helper integration, and registry/exchange repair in one isolated candidate; no active application source is being overwritten.

The immediate remaining source dependency is the **full changed-path map against `e8fdbcf` and the remaining corrected Scout union blobs**. The current Atlas candidate has the published Atlas base plus only the six frozen review files, so it cannot yet claim to test Scout's complete dependency closure. Please deliver those review inputs now, retaining one owner per path, or the complete ready immutable union source if it can be published with all required dependencies. Intermediate files missing the registry or research/recovery closure are not installation-ready.

## Atlas guard implementation checkpoint

Atlas's normal-workflow/direct-launch/dispatch gates and verified-release integration now pass **103 focused workflow/dispatch/common-union checks in 18.58 seconds** in the isolated candidate. Covered cases include a real audited APPLIED repair resume, competing action dates/domains, preserved terminal completion, interruption after saved success but before owner release, and refusal when repaired source bytes change.

The narrow legacy repair guard and public prepare/apply competition fixtures pass **18 recovery checks in 5.44 seconds**. This implementation scope is exactly `ml/nightly_workflow.py`, `tests/test_nightly_workflow.py`, `tests/test_nightly_dispatch.py`, `tests/test_nightly_common_union.py`, `tools/nightly_source_repair.py` and `tests/test_nightly_recovery.py`. Other Atlas agents retain the already declared registry/exchange and generic-helper paths, with no overlapping writers.

These are intermediate bytes while the helper continuation integration and Scout's offline SDK dependency correction proceed. They are not final full-union, installed-source or runtime verification. The previously stated 25–40 minute reviewed handback window still applies; exact final source/checks and limitations will be reported at handback.

## Frozen registry read/release semantics for both installers

`read(state_root)` returns **None only when `state_root/repair-owner.json` is absent**. A present valid file returns its six-field owner record unchanged. A symlink, malformed JSON, incomplete/extra fields, invalid token/date format or domain is rejected with `ValueError`, the JSON parse exception or a file-I/O exception as applicable. No malformed or unreadable owner is interpreted as absence.

`release(state_root, record, verified=True)` requires the exact current record and verified recovery, then unlinks the owner file. File absence is the released representation; there is no terminal/archived owner marker. The domain helper first persists an immutable verified-resolution receipt. Original immutable claim, prepared spec, audit, resolution and history evidence remain in their existing retained records.

An installer holding the same `workflow.lock` **must refuse before its first write whenever `read` returns any non-None owner or raises on malformed/unreadable ownership**. It must never delete, clear or take over the global owner. This rule applies whether old or new application source is currently installed. Atlas's protected installer will use the same boundary. The registry release is performed only by the exact repair owner after verified recovery, not by general source installation.

The registry owner pointer is durably published without overwriting an existing owner; binding and any audited continuation replace it atomically. A continuation archives the previous/replacement owner, evidence and root ancestry before replacement, with no unowned gap. Installers may inspect the exact persisted schema without importing a not-yet-installed module, but malformed or unknown representations must fail closed.

## Current reviewed-handback estimate and documentation scope

The reviewed Atlas handback estimate is now **23:10–23:25 UTC on October 9**, subject to the whole-union strict checks. Exchange final checks are underway; no active source installation has occurred. Atlas's final scope explicitly includes `docs/development/nightly-operations.md` alongside the relevant exchange runbook update. The handback will list exact paths, frozen source/reference, check results and any real remaining condition. Earlier timing estimates remain historical checkpoints rather than a completion claim.

## Final-review resume defect under correction

Atlas's independent review reproduced one additional release failure: a successfully resumed native stage advances the mutable `overnight-latest/run.json` pointer, but the generic repair resolver incorrectly treated that old pointer as immutable original evidence. Training could succeed and then fail to release its repair owner. Atlas's generic-helper owner is implementing the focused correction and regression. Original native receipts remain immutable; only the latest-run pointer's legitimate advancement is distinguished from retained evidence. No completed session or original receipt is rewritten.

The complete Atlas candidate offline suite, approximately 1,000 fixtures, is running alongside this correction. A running suite is not a passing result; final changed bytes will receive renewed checks before handback. The previously recorded exact source/input and ownership boundaries remain in force.
