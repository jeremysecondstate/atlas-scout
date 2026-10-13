# Permanent Gameplan and independent-trader operating policy

Jeremy's direct October 13, 2026 instruction establishes this architecture and the standing authority to prepare it every night. This is the current operating policy for Atlas, Scout, development chats and scheduled responsibilities.

## Three independent traders

| Trader | Owner and work | Runtime state |
| --- | --- | --- |
| Combined Gameplan trader | Atlas executes the combined Atlas–Scout Gameplan across the established symbol universe and Gameplan horizons. | Its own Gameplan plan, control, orders, fills and trading ledger. |
| Atlas 15-minute trader | Atlas generates and executes its own local 15-minute predictions. | Its own local binding, manual session, orders, fills and trading ledger. |
| Scout 15-minute trader | Scout generates and executes its own local 15-minute predictions. | Its own local binding, manual session, orders, fills and trading ledger. |

The only cross-PC trading-plan synthesis is the combination of Atlas and Scout Gameplan research. Scout performs that synthesis using balances already available with the two plans or their latest saved basis, then sends the combined result to Atlas. Delivery completes the handoff. The 15-minute traders do not participate in it. They do not request distributed grants, reciprocal acceptance, cross-trader reconciliation, loaded-code proofs or another trader's health or readiness.

Gameplan does not inspect or depend on either 15-minute trader's process, configuration, ledger, forecasts, orders, fills or status. Each 15-minute trader likewise works without Gameplan or its peer trader. Reuse of common tested source and the existing broker connection does not create shared execution ownership. Each manually started trader observes current broker capacity and manages its own exact orders and logs.

## Standing nightly authority

Complete the normal local data, Stats, model, prediction and Gameplan preparation work automatically under the existing schedules. Exchange the Atlas and Scout Gameplan contributions through the existing private channel; Scout synthesizes the combined Gameplan and sends it to Atlas. Use the existing saved balance basis with its original observation time for actual cash/share arithmetic; do not request a third fresh snapshot or wait for an Atlas acceptance receipt. Prepare each PC's 15-minute trader separately for a manual start.

There is no additional human approval, verification task, compatibility roundtrip, acceptance ceremony, migration ceremony or prerequisite checklist before nightly preparation or synthesis proceeds. Do not invent one in a task prompt or turn another trader's status into a gate. A source publication, peer acknowledgment, 15-minute result or optional display/report outcome is not a prerequisite for a completed Gameplan.

Use the real required calculation inputs and preserve their actual dates and provenance. If an input or worker operation genuinely fails, report the specific failure, retain usable work and continue the authorized correction or recovery. Do not manufacture inputs or success. That distinction does not create another approval stage.

Preparation never starts trading. Jeremy manually starts each trader. Scheduled tasks do not enable controls, start/restart traders or place/cancel orders to demonstrate readiness. Once manually started, each trader performs its own ordinary broker, quote and exact-order handling as part of execution.

## Existing communications are sufficient

Use the existing internet connections, authenticated GitHub connections and private Drive/CODEXSTORE exchange. No VPN, LAN connection, private gateway, inbound broker service, shared SQLite database, central order authority or new distributed execution path is needed.

Routine discussion, source handoffs and substantive operating updates use `atlas-scout` GitHub. Ducketz immutable source/request queues keep their established Git transport. The private nightly Gameplan packages remain in the authorized CODEXSTORE exchange. The `github_only` policy retires routine Drive API signal polling; it does not disable the separate private nightly exchange.

## Separate source and privacy responsibilities

Source changes still have explicit ownership, an identified base, exact-diff review, relevant offline tests, immutable completion identities and the established publication procedure. Those engineering responsibilities govern source publication; they are not nightly trader approval gates.

Publish only sanitized coordination and authorized shared source here. Keep credentials, account data, raw market data, fitted models, databases, exact private bindings and task memory local or in their already authorized private transport. A peer notice supplies information, not new authority over the receiving PC's private data. Preserve historical messages, receipts and original mixed-ledger records.

A document, source commit or prepared configuration is not proof that a PC installed it or started a worker. Report the actual installation and runtime facts separately, without asking the human to repeat the standing preparation/installation authorization.
