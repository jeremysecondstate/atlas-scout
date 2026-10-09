# Nightly readiness notification runbook

Owner: the local GAMEPLAN SYNTHESIS / HANDOVER and DUCKETZ DISPLAY responsibilities, using their existing wakes and private workflow bindings. This runbook covers the shared dated notification ledger. Scout's source is [`b9ffaecaa5c54572e9d28ea79004f85d1b357b41`](https://github.com/jeremysecondstate/ducketz/commit/b9ffaecaa5c54572e9d28ea79004f85d1b357b41), Completion-Record `20261009T230401Z-53c9a2c6d5094aad9c7a2daec197beeb`. Exactly `tools/nightly_notifications.py` and its dedicated test were added. The strict queue and separate isolated run each passed 35 checks. Publication, each PC's installation, native prompt integration and actual notice delivery are separate facts.

The event thresholds are **03:00 America/Los_Angeles for `readiness-risk`** and **03:35 for `missed-confirmation`**, on the exact action date selected by the application's exchange calendar. The existing five-minute synthesis/handover wake reconciles missed or interrupted work; display uses the same event identities. No additional model-polling task is needed. An early or weekend wake does not move the threshold or invent a trading session.

Use the task's existing local Python/runtime/config bindings and repository module path. Uppercase arguments below are local placeholders; keep their actual files, tokens, native IDs and evidence private. Do not copy the peer PC's configuration.

1. Obtain fresh intended-session local/joint/UI readiness and exact peer-acceptance evidence through the existing read-only checks. Write a normalized private readiness JSON with these fields:

   | Field | Required value |
   | --- | --- |
   | `action_date` | Exact intended calendar action date |
   | `observed_at` | Actual zoned time of the readiness observation |
   | `confirmed` | JSON boolean derived from fresh verified readiness and exact acceptance |
   | `evidence` | Nonempty reference to retained actual evidence |

   The observation may be no more than ten minutes old; future timestamps are rejected. An old completed session does not confirm a new intended session. A missing result must not be represented as confirmed.

   ```text
   python -B -m tools.nightly_notifications --config WORKFLOW_CONFIG --inspect --readiness READINESS_JSON
   ```

   The result includes the selected action date, observation time and dated events. Each event has a stable `event_id` and threshold kind.

2. Claim an eligible due event with the same fresh readiness record, the existing local automation identity and the actual current native thread ID:

   ```text
   python -B -m tools.nightly_notifications --config WORKFLOW_CONFIG --claim readiness-risk --readiness READINESS_JSON --owner AUTOMATION_ID --thread-id CURRENT_NATIVE_THREAD_ID
   ```

   Use `missed-confirmation` for the 03:35 event. Native `CODEX_THREAD_ID` and read-only `automation_runs` mapping identify the actual run; retain the exact binding as local evidence. Emit only when **both `claimed` and `eligible` are true**. A competing thread receives the existing `PENDING_NATIVE_CONFIRMATION` claim and has no permission to emit another notice. Ownership never expires into an automatic takeover.

3. Publish the meaningful notice as the ordinary visible native final, including its stable `event_id` and the concrete failure/owner/next action. Do not archive an actionable notice. Save the original event/token/owner/thread binding privately. **Do not confirm delivery during this turn before the final exists.** For unchanged or non-actionable wakes, use the native archive tool as required by the local task prompt and preserve the saved task identity/memory.

4. On the **next existing five-minute wake**, inspect the original claimed thread through native `read_thread`, the matching read-only native automation outcome and inbox disposition. `thread.status=notLoaded` is not completion evidence. Inspect the actual turn status/completed time and the event-bearing final. Unknown, nonterminal or truncated evidence keeps the event pending.

   Retain the actual readback, then build a private proof JSON:

   | Field | Required value |
   | --- | --- |
   | `source` | Literal `native_thread_readback` |
   | `event_id` | Original claimed event ID |
   | `owner`, `thread_id` | Original claimed owner and native thread |
   | `run_status` | Verified `completed`, `failed` or `interrupted` |
   | `completed_at`, `observed_at` | Actual zoned terminal/readback times |
   | `notice_visible` | JSON boolean supported by the actual event-bearing final/inbox outcome |
   | `readback_reference` | Nonempty reference to retained actual native evidence |

   Never infer delivery from command completion, prepared text, a claim record, an empty thread summary or an assumed timeout. A reference must identify real saved evidence; the proof must not be manufactured to clear a pending event.

5. Confirm the observed outcome against the original token:

   ```text
   python -B -m tools.nightly_notifications --config WORKFLOW_CONFIG --confirm --event-id EVENT_ID --token ORIGINAL_TOKEN --proof PROOF_JSON
   ```

   Verified visible delivery records `DELIVERED`. Positively verified terminal non-delivery records `CONFIRMED_UNDELIVERED`, allowing a fresh claim with the **same stable event identity**. Original claims and outcomes remain immutable. Unknown outcome stays pending until actual evidence resolves it; another owner cannot simply expire or steal it.

The module is a pure ledger and explicit confirmation API. It sends no notice and does not independently query or attest native delivery: the caller must supply the actual native proof described above. Offline tests covered early/missed wakes, weekends, Christmas, duplicate owners, interrupted saves and delivery reconciliation. No real actionable notice was emitted merely to test the implementation. The actual production delivery must be verified from its later native outcome.

Keep task IDs, complete readback, private paths and tokens local. Publish only a sanitized substantive failure/correction/verified-disposition summary through the existing coordination issue when needed. Preserve the completed October 9 session and all financial receipts; notifications do not launch preparation, capture an account, change trader controls or alter orders.
