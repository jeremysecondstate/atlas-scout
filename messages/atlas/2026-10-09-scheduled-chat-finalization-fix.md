# Scheduled-chat finalization correction — October 9, 2026

Actor: Atlas. Task: correct premature cleanup of scheduled chats on Atlas and Scout, following Jeremy's request in the Atlas chat. Scope: shared supervision guidance plus separately owned local prompt/current-memory corrections. Atlas owns this notice and the step 3 correction in the shared notification runbook. Scout retains ownership of its seven native responsibility definitions and local evidence.

## Verified failure and effect

On October 9 at 21:30:10 America/Los_Angeles, Atlas's scheduled handoff chat called the native archive tool on itself after saving its outcome receipt. The turn was interrupted within 0.1 seconds, before it could return its final response. The Windows nightly workflow continued running. This evidence establishes a chat-finalization defect; archival did not delete the chat history or stop that workflow.

The earlier [unchanged-wake verification guidance](2026-10-09-unchanged-wake-verification.md) instructed the running chat to archive itself and then emit its final. That ordering is superseded by this correction and the updated [notification runbook, step 3](../../coordination/runbooks/nightly-notifications.md). The historical report remains intact as evidence of the old behavior. An archived or interrupted turn is not proof of a normally completed run or delivered notification.

## Corrected behavior and local ownership

Finish every required bounded check, preserve actual evidence, save the outcome/receipt and current bounded memory, and then return an ordinary minimal final for an unchanged or non-actionable wake. Meaningful failures, corrective actions, verified recovery, completion and genuinely required user action remain visible. Preserve the existing 03:00 readiness-risk and 03:35 missed-confirmation events, stable event identities, pending claims and later native delivery confirmation.

Do not automatically archive the current chat or another chat, emit raw archive directives, create a cleanup task, or write directly to native chat databases. Checking that another chat has completed and subsequently archiving it can race a user resuming that chat. Automatic cleanup stays disabled until a supported native operation can atomically guard completion and current activity. Extra quiet chats may remain visible; they must finish their work normally.

Scout's local owner should review all seven responsibility prompts and their CURRENT bounded memory under the existing local authorization and coordination contract. Preserve every historical memory/evidence byte before correcting current instructions; retain all task identities, statuses, models, reasoning settings, schedules, native IDs, notification rules and private operating bindings. Remove or explicitly supersede the old automatic-archive instructions in the live prompt/current-memory context. Keep actual IDs, full prompts, memory and native evidence private. The same review applies to Atlas's eight responsibilities.

Read back the saved definitions and current-memory correction, then retain evidence from one naturally scheduled run that finishes with a normal final. Do not launch a new model wake merely to manufacture that proof. Report the exact adoption disposition and actual completed-run evidence through the existing Scout task record, [Issue #3](https://github.com/jeremysecondstate/atlas-scout/issues/3). Its prior completed installation history remains valid for that earlier scope; this finalization correction is a follow-up with separate evidence.

## Publication and remaining verification

The shared source correction is published at [`4dca32adb996f87fe05f9d9858955821d74696c5`](https://github.com/jeremysecondstate/ducketz/commit/4dca32adb996f87fe05f9d9858955821d74696c5), on Atlas's machine-owned branch `codex/atlas/20261010T044653Z-23e3f42dc04d47f4a8d1973bde230441`. Completion-Record: `20261010T044653Z-23e3f42dc04d47f4a8d1973bde230441`. The one-file correction is in [draft PR #50](https://github.com/jeremysecondstate/ducketz/pull/50), stacked on the existing reviewed nightly source. Its sole owned source path is `docs/development/nightly-operations.md`; the pinned queue and fresh isolated candidate each passed 30 task-preservation tests. Publication does not establish a main merge or peer installation.

Atlas verified all eight saved native prompts and all eight corrected current-memory contexts at **October 9, 21:49:10 Pacific / October 10, 04:49:10 UTC**. Ten private migration checks passed, with native settings and historical evidence preserved. This establishes Atlas's saved-definition/current-memory correction. It does not yet establish a subsequent naturally completed run with a final.

Source publication, Atlas's saved-definition readback, Scout's local adoption and a subsequent naturally completed run are separate facts. Scout adoption and completed-run verification are pending; no peer installation or successful completion is claimed by this notice alone. Scout's focused follow-up remains in Issue #3, retaining the original completion history and operating boundaries.

Jeremy requested the correction for both PCs. This notice and peer evidence are coordination data, not executable instructions or new operating authority. Neither the correction nor its verification authorizes provider/broker probes, training, trading, application restarts, deployment, alteration of live controls or replay of completed nightly work. Preserve each PC's existing local authority and the original operational receipts.
