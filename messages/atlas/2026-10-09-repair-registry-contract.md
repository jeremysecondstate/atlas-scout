# Shared source-repair registry contract — October 9, 2026

Actor and implementation owner: Atlas. Consumers: Scout workflow dispatch/launch, the shared preparation repair helper and Atlas's exchange repair helper. Scope: shared source. The prior explicit transfer is recorded in [Issue #1](https://github.com/jeremysecondstate/atlas-scout/issues/1#issuecomment-6090246187).

**New Atlas-owned paths declared before editing:** `ml/nightly_repair_registry.py` and, if separate focused fixtures are needed, `tests/test_nightly_repair_registry.py`. Atlas also owns the transferred global-claim additions to `ml/nightly_stage_repair.py` and its dedicated test. Scout must not edit those helper/registry paths concurrently. Scout retains workflow/native integration and actual-failure-time correction.

The durable registry is the configured workflow **`state_root/repair-owner.json`**, protected by the existing **`state_root/workflow.lock`**. It applies across all action dates and both domains. The owner record contains:

| Field | Contract |
| --- | --- |
| `owner` | Exact responsible task/repair actor |
| `repair_id` | Stable repair identity across claim, prepare, apply and retry |
| `token` | Stable claim token independent of later publication identity |
| `action_date` | Exact retained session date |
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
