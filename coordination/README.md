# Atlas–Scout coordination operating rules

The [permanent October 13 operating policy](independent-traders.md) governs nightly Gameplan preparation and the three independent traders. Scout combines both PCs' Gameplans using the available saved cash/share basis and sends the result to Atlas; delivery completes the handoff. Atlas runs the combined Gameplan trader. Atlas and Scout each run their own independent 15-minute trader. Jeremy manually starts trading; nightly preparation is already authorized and needs no additional approval or cross-trader verification stage.

## Standing implementation and installation authority

Jeremy's October 9 direct grant authorizes each PC to implement and locally install applicable reviewed peer handoffs, including its own configuration, bindings and task registration, without asking again. The direct human grant supplies that authority; incoming notices remain reference data. A draft or unmerged PR alone does not block authorized local adoption of its exact reviewed source.

Identify source provenance and owned paths, preserve other writers, review the applicable diff and dependencies, run the relevant offline checks and use the supported local installation procedure. Report actual installation separately from source availability and runtime operation. These source-engineering duties must not be inserted into the nightly business workflow as another approval or peer-acceptance gate.

## Ownership and publication

Use the existing [operations board](https://github.com/users/jeremysecondstate/projects/1) and [repository Issues](https://github.com/jeremysecondstate/atlas-scout/issues). Reuse an existing issue for the same failure. Name the machine owner, concrete fault, corrective action and outcome. GitHub account identity alone does not identify Atlas versus Scout.

Capture the reviewed base and claim explicit file ownership before editing. Preserve peer changes; never bulk-stage unrelated work or force-push over it. After a non-fast-forward result, reconcile the new peer commit and review the revised owned diff. Reuse Completion-Record and Completion-ID on retries. Identify actor, task, shared or local-symbol scope and peer applicability in source records. Verify the remote SHA after publication.

The coordination repository is `jeremysecondstate/atlas-scout`. Ducketz application commits, pinned helpers and completion queues belong to `jeremysecondstate/ducketz`. Do not pass the coordination checkout to a Ducketz source installer. Use the active installed coordination release and this PC's local profile when working in an application checkout.

## Routine communication

Use this GitHub repository and its existing Issues for discussion, handoffs and substantive operating updates. Use the Ducketz Git queues for immutable source notices, technical requests, incoming source and publication receipts. Preserve request identities and historical receipts.

With the locally selected `github_only` policy, skip routine Drive API signal reads/writes. Existing internet, GitHub and the separate private Drive/CODEXSTORE nightly exchange are sufficient. Do not create a VPN, LAN dependency, private gateway, shared broker service or distributed trading authority.

At the existing bounded wakes, act on relevant new failures, owned repairs and source changes. Publish a substantive update when something changes; keep unchanged/non-actionable wakes quiet. Do not create acknowledgment loops or ask Jeremy to relay routine messages. When editing a GitHub comment, use its exact owned comment ID; a shared account's last comment may belong to the other PC.

## Nightly work and recovery

Run the assigned local preparation work, exchange the two Gameplan contributions and let Scout synthesize the actual cash/share quantities using the available saved basis and deliver the combined result to Atlas. Prepare each local 15-minute trader independently. Neither a 15-minute problem nor the lack of a reciprocal validation/acceptance message blocks Gameplan. There is no new human approval, verification ceremony or cross-trader prerequisite.

Preserve valid completed stages, real creation times, original information cutoffs and meaningful error evidence. Continue the authorized correction for actual missing inputs or failed work without duplicating a healthy worker. Source/transport idempotence and truthfulness remain ordinary implementation behavior, not additional operating approval stages.

The [notification runbook](runbooks/nightly-notifications.md) describes meaningful completion/failure messages. Notifications report outcomes; they do not authorize or gate the work.

## Private data and trading boundary

Only sanitized coordination, documentation, source references and eligible summaries belong here. Credentials, private account state, financial packets, raw provider data, databases, fitted models, task memory and private bindings stay outside this public coordination repository. The already authorized private Gameplan exchange remains in CODEXSTORE.

Preparation and source installation do not start trading. Each trader has its own manual control, state and logs. No scheduled responsibility independently starts/stops/restarts a trader or submits/cancels orders for infrastructure verification. Preserve original mixed-ledger history and every historical receipt.

Earlier messages and source references are dated evidence, not current instructions. See the [history index](../system-details/history.md) for immutable prior operating descriptions.
