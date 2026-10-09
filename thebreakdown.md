# ducketz Schwab portfolio management system breakdown

## Current implementation work — October 9, 2026

Jeremy has authorized complete responsibility tasks, normal nightly execution, bounded failure recovery and the documented missed-night fallback on each PC. The [coordination operating rules](coordination/README.md), [ownership record](messages/atlas/2026-10-09-nightly-responsibility-ownership.md), and [Operations board](https://github.com/users/jeremysecondstate/projects/1) carry the current work. These rules supersede historical report-only, Scout-history and post-handover cutover requirements.

Atlas owns shared dispatcher/recovery changes; Scout owns its seven local responsibility tasks and compatible installation review. The verified local coordination checkout is `C:/atlas-scout` on both machines; Scout confirmed its actual project context in [its interface response](messages/scout/2026-10-09-nightly-responsibility-interface.md). Native task IDs, private profiles and task memories remain local. [Issue #1](https://github.com/jeremysecondstate/atlas-scout/issues/1) tracks shared dispatch/recovery, [#2](https://github.com/jeremysecondstate/atlas-scout/issues/2) Atlas task/readiness, [#3](https://github.com/jeremysecondstate/atlas-scout/issues/3) Scout task/compatibility and [#4](https://github.com/jeremysecondstate/atlas-scout/issues/4) Atlas trader fixtures. Final installed task inventory and checks will be recorded after native readback; the [candidate interface](messages/atlas/2026-10-09-dispatcher-interface-proposal.md) is not yet a verified installed release.

The ordinary kickoff remains **21:05 America/Los_Angeles**. Actual prerequisite receipts advance one authoritative action-date pipeline through catch-up → Stats → model review/training/predictions → local Gameplan → Scout synthesis/Atlas handover → combined display. Distinct task identities do not launch competing full pipelines. Repo reconciliation remains independent and Hyperliquid receives priority intake. Healthy running work stays running; completed outputs and terminal sessions are reused. The existing 03:00 and 03:35 notifications remain; neither is a startup prohibition.

Jeremy subsequently reported manually starting Atlas's active trader. Earlier stopped-worker statements below and in dated messages remain historical evidence, not standing instructions to stop or restart it. The tasks inspect status without disturbing the worker. The October 9 13:23 handover is complete; tonight's separate intended trading session must be selected from the configured exchange calendar and verified separately.

## Late-start fallback route — added October 9, 2026

**Status: verified end to end for the October 9 recovery at 13:23 Pacific.** Scout returned the synthesized Gameplan and combined Stats, Atlas adopted the exact result and receipt (`HANDOFF_VERIFIED_LOCAL`), and the read-only manual-start check returned `EXECUTION_SETUP_READY` with `manual_start_ready=true` and no blockers. The ordinary 9:05pm Pacific nightly workflow remains the primary route. This fallback handles a genuinely missed nightly launch, such as after an outage or unavailable usage. A failed or interrupted run resumes its existing dated work instead of starting another run. This preparation fallback is separate from the trader's overdue-order catch-up described later.

**Current operating rule:** both PCs prepare their research; Scout synthesizes the combined Gameplan and hands it back to Atlas. Once that synthesized Gameplan is handed over and loaded on Atlas, planning is done and Jeremy can manually turn on Atlas's trader. Scout does not trade and is not expected to supply execution or ownership history. Atlas alone executes all symbols and horizons. There is no additional human approval, Scout-history export, migration or cutover ceremony after handover. This rule supersedes conflicting October 7 rollout requirements retained below as history. Normal account/order reconciliation belongs to Atlas's manually started worker.

### Recovery sequence

1. **Identify the exact intended trading date.** Read that date's saved preparation state and worker log. A previous date's completion does not satisfy tonight's work. `NOT_STARTED` means the intended date has no run; distinguish that from a running, failed or completed run.
2. **Select the appropriate continuation.** If the night's operations genuinely never started, use an explicitly dated missed-night recovery with a fixed, recorded recovery cutoff. If the matching run already exists, retain its identity and resume its failed or interrupted stage. Never duplicate a running or completed matching run.
3. **Finish the normal preparation stages.** Data catch-up → Gameplan Stats → model review → training/predictions → local Gameplan and planning-price preparation. Preserve valid completed stages, original forecasts, Stats and accepted review. A reviewed source repair records its before/after binding and original failure evidence; it does not silently relabel old results as newly produced.
4. **Use the explicit late-publication path.** Carry the intended date and recovery deadline into publishing and trade planning. Keep the original morning deadline as provenance and record actual creation/publication times. Separate the time an artifact was created from the cutoff for market information used in its predictions; do not backdate artifacts or include future inputs.
5. **Complete the same Scout-to-Atlas handover.** Scout combines both research packages using Atlas's account-wide capital evidence, then returns the synthesized Gameplan and associated Stats. Delivery/loading of the exact returned result completes handover. No Scout execution ledger is required. Jeremy may then manually start Atlas's trader; preparation never starts it automatically.

Atlas's implemented recovery interface is `ml.nightly_workflow --launch --recover-action-date YYYY-MM-DD --recovery-deadline ZONED_TIMESTAMP`, with its existing private `--config`. An existing failed run uses `--launch --resume-action-date YYYY-MM-DD` instead. The current missed-night interface accepts the current trading date after 04:00 Pacific, with a future cutoff no more than seven hours away and no later than 17:00 Pacific. Retries retain the chosen cutoff. These describe the implemented interface, not an instruction to launch or extend an expired run. Scout uses its locally reviewed recovery-spec interface; neither PC copies the other's private bindings.

### Verified completion and retry behavior — 13:23 Pacific

The actual recovered preparation, private packet exchange, Scout synthesis and Atlas adoption completed end to end. Atlas's Gameplan and Stats readers verified the returned publications for the intended action date. This establishes the late-start preparation and handover route; Jeremy controls the separate manual trader start.

If a reviewed repair finishes after a recovery cutoff, the implemented planning-tail interface is `--resume-action-date YYYY-MM-DD --planning-tail-exception ABSOLUTE_RECORD` with the existing private config. It retains the original run, original morning deadline, original recovery cutoff and all completed numerical results. A separately authorized continuation has its own fixed expiration and cannot be silently replaced or extended. It is limited to the already published planning tail. Source repairs preserve the original exception through recorded before/after source evidence. Normal retries reuse completed stages, including after a worker exits between writing a native receipt and saving outer workflow status.

Local preparation verifies its exact saved local Gameplan and reviewed Stats before exporting them; it no longer depends on a combined Gameplan that Scout has not synthesized yet. The ordinary application display still selects the accepted combined publication. Once the exchange is terminal `COMPLETE/HANDOFF_VERIFIED_LOCAL`, inspect and retain its original receipt; later checks do not rerun preparation, account capture or handover.

| Final repair | Verified evidence |
| --- | --- |
| Fixed continuation, conservative planning reservations and sole Atlas account snapshot | [PR #40](https://github.com/jeremysecondstate/ducketz/pull/40); 365 frozen-source and 365 isolated checks, plus 255 installed-variant checks. |
| Interrupted-save recovery without duplicate native planning | [PR #41](https://github.com/jeremysecondstate/ducketz/pull/41); 143 frozen-source and 143 isolated checks; included in the final installed repair. |
| Exact local display before synthesis and audited source repair | [PR #42](https://github.com/jeremysecondstate/ducketz/pull/42), source `9417cfe6d920ec7408ea4863c7702afcf6231a0a`, Completion-Record `20261009T201155Z-99d27767d26343e498196d42518ef343`; 292 checks passed independently in frozen source, isolated candidate and installed Atlas source. |
| Actual final handover | Scout synthesized both retained research packages against Atlas's one account snapshot. Atlas verified and adopted the exact Gameplan, Stats and receipt; both local/joint readiness and manual-start readiness passed. |

The existing Atlas preparation, handoff and priority tasks retain their identities and schedules. Their saved instructions and memories retain the sole-executor rule, the completed recovery, its original records and terminal-session behavior. No Scout execution-history prerequisite follows the handover. Earlier checkpoints below remain historical evidence and are superseded by this verified completion.

### What October 9 established

| Part | Verified status |
| --- | --- |
| Date-pinned recovery and continuation | Implemented; Atlas's real recovery retained its original run and completed stages across repairs. |
| Late publication and trade-planning deadline | Implemented and installed on Atlas; [PR #34](https://github.com/jeremysecondstate/ducketz/pull/34) carries the fixed recovery deadline through planning; 217 targeted tests passed. |
| Late forecast and joint-package timestamps | Implemented and installed on Atlas; [PR #35](https://github.com/jeremysecondstate/ducketz/pull/35) separates actual publication time from input availability; 304 tests passed with one Windows symlink skip. Scout's compatible adoption is tracked separately. |
| Atlas account scope | [PR #38](https://github.com/jeremysecondstate/ducketz/pull/38) uses Atlas's full bound execution universe rather than its eleven research symbols; 204 tests passed. |
| Historical failure, now resolved | At the 11:58am Pacific checkpoint, Atlas's planning snapshot stopped on `PENDING_LEDGER_RESERVATIONS_REQUIRE_RECONCILIATION`, reported as `OWNERSHIP_SNAPSHOT_UNAVAILABLE`. This Atlas planning-path failure was resolved before the 13:23 handover; it did not require Scout history or a new approval ceremony. |
| Earlier recovery checkpoint, now superseded | Recovery was incomplete at the 12:04pm Pacific checkpoint. The original deadline was 04:00 and the fixed recovery cutoff was noon; both remained intact. The separately frozen continuation and final end-to-end verification are recorded above. |

The existing preparation, synthesis/handoff and source-reconciliation tasks retain their schedules and identities. Atlas's tasks check the connected `atlas-scout` folder/GitHub repository for substantive coordination. Private financial packets remain in `CODEXSTORE/ducketz-nightly-exchange/v1`. Atlas's existing Ducketz decision logs, Gameplan review artifacts and native holdings ledger provide local history references; projected Gameplan quantities and market-outcome Stats must not be mistaken for actual fills.
### Scout recovery interface and verified checkpoint

**Current operating rule, confirmed directly by Jeremy:** Scout prepares the Gameplan and Gameplan Stats for Scout's 11 symbols; Atlas does the same for Atlas's 11. Scout synthesizes both Gameplans against one fresh Atlas account-wide view of cash, holdings and order reservations, then hands the synthesized Gameplan back to Atlas. Atlas is the sole executor for all 22 symbols. Delivery and loading of that exact synthesized Gameplan completes planning. Jeremy manually starts Atlas's trader. No further planning approval or Scout ownership-history gate follows handover.

Scout does not execute trades. Its local research preparation must not require a Scout broker/account snapshot, execution ledger, ownership response, order/fill history or migration. Preserve the existing application logs and saved prediction outcomes underlying Gameplan Stats and Gameplan; use those for historical evaluation. Do not infer zero holdings from missing Scout execution records. Actual account and order reconciliation belongs to Atlas.

**Historical wording below is superseded where it requires Scout execution history, the Scout ownership responder, or an additional cutover approval after handover.** The October 7 status table records what was believed and installed then; it is not evidence that the corrected workflow has completed a production handover.

#### Scout missed-night / late-start preparation route

This route covers a missed kickoff, exhausted usage, power outage, interruption or an otherwise late start. It is distinct from the existing trader's catch-up of overdue trade intentions after Jeremy manually starts trading.

1. At the ordinary 21:05 Pacific kickoff, run preparation for the intended session. A daytime completion or an older `latest.json` must never be interpreted as completion of the upcoming nightly session.
2. The existing Scout preparation task also has a 04:05 Pacific fallback. Read `ml.nightly_workflow --config scratch/nightly-workflow/config.json --status --catch-up` for the intended action date, including its exact active native report, log, owner liveness and completed receipts. A healthy live owner keeps running; do not launch a duplicate.
3. If that intended session is missing or an eligible failed worker has exited, run `ml.nightly_workflow --config scratch/nightly-workflow/config.json --check`, then one authorized `--launch --catch-up --recovery-reason "Operator-authorized missed nightly preparation"`. Use the existing task and locks. Diagnose deterministic failures before retrying; do not repeatedly relaunch unchanged failures.
4. Catch-up selects the newest completed exchange session and its next action date. Before the normal deadline it retains the normal deadline. After it, the first request creates one immutable recovery record with the real request time, original 04:00 Pacific deadline and a fixed expiry capped at seven hours after the request or 17:00 Pacific on the action date, whichever is earlier. Retries retain that expiry and all usable completed work.
5. Preserve real acquisition/publication timestamps. Training inputs retain the original information cutoff. A plan produced late is explicitly identified as late; publication after 04:00 is not by itself future market information or proof that the wrong session was selected.
6. Resume from the eligible failed stage. If a reviewed source correction is required, preserve the original failure and establish an explicit new source binding before resuming. A planning-only repair can retain completed Stats, review, generation, evaluation, forecasts and enrichment instead of training them again.
7. Continue the same private exchange and Scout synthesis once both exact preparation packages are ready. Use Atlas's account state for the combined budget. Deliver/load the synthesized result on Atlas; planning is then complete. Legacy LOG remains paused and trader startup remains manual.

#### Scout implementation checkpoint — October 9, 2026, 19:05 UTC / 12:05 Pacific

The fallback is **partly exercised in production, not yet verified end to end**. The October 9 action-date recovery selected October 8 as its completed source session. The saved request was 14:49:40 UTC / 07:49:40 Pacific; its unchanged expiry is 21:49:40 UTC / 14:49:40 Pacific. Stats and model review completed; generation, evaluation and publication completed, including 264 forecasts at 18:50:18 UTC; enrichment completed at 18:51:36 UTC. The final local planning stage failed at 18:51:49 UTC on a validator that treated late publication as future information. A synthesized handover has not yet been established by this checkpoint.

| Component | Evidence and actual state |
| --- | --- |
| Missed-launch selection, fixed recovery evidence and native-stage propagation | Implemented and used in today's recovery; published source `197dea8e461a35118d4c03272f2913ef73191893`. |
| Archive acquisition time versus original information cutoff | [PR #33](https://github.com/jeremysecondstate/ducketz/pull/33), source `d53d2007f8665e866c15cc37c608df3323bb9082`, Completion-Record `20261009T182830Z-bafca648331d458bab9a029c5849fd43`. Installed on Scout; recovery then reached forecast publication and enrichment. 143 offline checks passed for the reviewed source and isolated candidate. |
| Retain completed numerical work during a planning-only source repair | [PR #36](https://github.com/jeremysecondstate/ducketz/pull/36), source `3c567ef96519dbbc9870648b750363574b6845c4`, Completion-Record `20261009T184441Z-6932052c48984e14be3c066f57ac06bd`. Published and tested (150 passed); not yet installed at this checkpoint. |
| Accept truthful late publication under the existing recovery record | [PR #37](https://github.com/jeremysecondstate/ducketz/pull/37), source `6be0d1ef71201133c351a7ed0825b95456c8a9e5`, Completion-Record `20261009T185159Z-65356abaaccc448197ff44f058c30871`. Published and tested (410 passed, one Windows symlink privilege skip); a read-only check accepted all 264 saved forecasts unchanged. Not yet installed at this checkpoint. |
| Remove Scout's erroneous local account/ownership dependency | Correction in progress; targeted research-role and workflow tests passed (42). This is not yet a published, installed or production-complete change. |
| Scheduled instructions | Scout's five existing preparation, readiness, synthesis, priority and paused legacy tasks now contain the corrected roles and completion rule. Schedules and activation states were preserved, including 21:05 / 04:05 preparation and paused LOG. Atlas separately reported updating its preparation, handoff and priority tasks. |

Later checkpoints must distinguish publication, local installation, completed preparation and actual synthesized handover. Keep exact private evidence, account values and packets out of this repository.

**Scout update at 19:17 UTC / 12:17 Pacific:** [PR #39](https://github.com/jeremysecondstate/ducketz/pull/39), source `5c90a2345e67e22a0814be0877a16d6d320898f0`, Completion-Record `20261009T191236Z-2c5e29837aa343cfa9126d82360094e6`, is published. The exact Scout-compatible research-only planner/UI changes, PR #37 validator and planning-tail retention were installed through a recorded source transition. Shared source and isolated verification each passed 431 checks with one Windows symlink skip; the final Scout-specific changed-path/UI audit passed 119 checks with one unrelated preexisting account-UI field test deselected. The existing recovery resumed only failed planning at 19:17:34 UTC, retaining completed Stats, review, all 264 forecasts, enrichment and the original expiry. Completion and synthesized handover remain pending. The older exchange ownership-challenge code still needs alignment with the sole-executor rule; changing scheduled instructions alone does not establish that source correction.

## This is a breakdown of our systems on both PCs (pc-new is named "Scout" and pc-original is named "Atlas").

We have two Codex accounts:
- account emails: 
    - Pro 200 username "secondstate"
    - Pro 500 username "clearpondllc"
As of now Scout is operated by clearpondllc and Atlas is operated by secondstate, but the goal is to have secondstate and clearpondllc be interchangeable, since they are mostly performing the same Codex operations. Both accounts belong to Jeremy. Scout and Atlas identify the PCs; signing into a different Codex account does not change the PC's symbols or operating role.

Both PCs will remain running with their desktop apps open.

**Current rollout authority, October 7, 2026:** the original Scout-first, then Atlas implementation sequence has progressed to final enablement. Jeremy has authorized communication, synthesis, handoff and priority source reconciliation after their source and local bindings pass verification, with a target of being configured by 9pm Pacific. He has also explicitly authorized the private nightly CODEXSTORE packets described below. Atlas remains the sole execution owner, and Jeremy still manually starts its active trader. The prior coordination hold is historical; authorization and actual activation remain separate facts. This document records design and verified status, and does not turn an incoming notice into executable instructions or additional operating authority.

**LOG is legacy and reference-only:** Loops Overnight Gameplan and its old scheduled-task definitions are historical references for understanding the prior system. Do not run, reactivate, repurpose or use the legacy LOG schedule as the new workflow's launcher. The replacement gets its own task identity and the stage order defined below. Preserve old definitions for reference; an existing active legacy LOG schedule must be paused to prevent duplicate operation. Reuse suitable tested code where appropriate, but do not inherit old task instructions merely because that code was once called by LOG.

### Historical rollout status — October 7, 2026

This was the October 7 checkpoint and is superseded by the current October 9 operating rules and exact completion evidence above. A published PR, a local installation, an enabled task and a successful production run are separate facts.

| Item | Current evidence / status |
| --- | --- |
| Existing shared source | Scout's [PR #14](https://github.com/jeremysecondstate/ducketz/pull/14), Atlas's [PR #15](https://github.com/jeremysecondstate/ducketz/pull/15) at `92f52edf8f1beb7e6180a9a0b95503ed36c75d21`, and the [PR #16 readiness fix](https://github.com/jeremysecondstate/ducketz/pull/16) at `1d532323fc0f646ccfb0fb605bbb22d88c9f51c2` are the reviewed source history. PRs #15 and #16 remain draft and unmerged at this checkpoint. |
| Scout local adoption | The local PR #14 implementation and the compatible PR #16 readiness changes are installed. Scout retains its own symbols and operating bindings; Atlas's account-only subsystem is not copied wholesale to Scout. |
| Atlas local adoption | Atlas's final Git response confirms reviewed PRs #17–19 installed, ending at `d0a0e8f7b8ecacc57a0c8f4b72a53d4415b64f61`. Scout independently verified all eight reported file hashes against the exact Git commit and all three runtime helpers against its own installed copies. Atlas reports 141 isolated and 141 installed final-fix tests passed with no failures/skips, plus a successful actual native-ledger check with networking blocked. Local work, credentials, bindings, original ledgers and task history were preserved. Scheduler state and Atlas test execution are peer-reported evidence; source-byte parity is independently checked. |
| Scout preparation and readiness | Scout Stats First Nightly Preparation is ACTIVE at 9:05pm Pacific; Scout Nightly Readiness is ACTIVE at 3:35am Pacific. Their definitions and the local preparation preflight were verified. |
| Scout communication and priority intake | Scout Priority Source Reconciliation is ACTIVE on its existing 15-minute cadence, with Hyperliquid first. Source installation must preserve an in-progress or completed nightly session's frozen source. |
| New private exchange source | [Draft PR #17](https://github.com/jeremysecondstate/ducketz/pull/17), commit `df1ba4b06163f8ad20deff41903df8bc790deee0`, stacked on PR #16. Reviewed source and isolated candidate each passed 252 offline tests with zero failures or skips. Scout installed the four new runtime/doc/example files; its installed compatibility suite passed 205 tests with one Windows synthetic-symlink permission skip. |
| Private exchange bindings | Scout verified Atlas's immutable private bootstrap against the exact SHA-256 advertised through Git, including both ordered owner lists. Scout's private configuration is installed and `tools.nightly_exchange --check` passes. Account values and private configurations stay out of this document and Git. |
| Exchange activation | Both PCs' final setup is enabled: Scout verified at 8:58:57pm Pacific; Atlas reports enablement at 9:08:54pm. Scout synthesis and Atlas exchange/handoff run bounded five-minute dependency checks. Atlas's existing task now includes `--allow-snapshot-refresh` after both verified preparations, with the fresh ownership challenge protocol. Scout remains the sole synthesis owner against one account-wide budget. Actual combined-plan readiness still requires tonight's completed preparations, fresh account evidence and exact acceptance receipt. |
| Production outcome | Scout started at 9:05:08pm Pacific for October 8, then recorded a Schwab authentication failure. The first attempt was preserved with a controlled-stop receipt. After Jeremy supplied replacement local credentials, Scout installed them through the existing locked cache and resumed the same outer run at 9:40:33pm Pacific, retaining the original 4am deadline and continuation data. A read-only Schwab quote succeeded at 9:41:21pm, confirming authenticated market-data access. Current state is `RUNNING / prepare_stats`, data catch-up; full Stats, training, Gameplan and combined handoff completion remain pending. Atlas reported its preparation started independently. |
| Ownership planning follow-up | [Draft PR #18](https://github.com/jeremysecondstate/ducketz/pull/18), commit `7b079e8f3b84e2f294e0bfddfabccea891b19cf7`, supplies fresh sanitized observations from each eleven-symbol ledger and checks them against one fresh Atlas account read. Its reviewed source and isolated candidate each passed 179 offline tests. Both PCs adopted it together with the required PR #19 native-format correction and passed their local ownership checks. Setup adoption is complete; the first production exchange remains pending. |
| Native ledger format correction | [Draft PR #19](https://github.com/jeremysecondstate/ducketz/pull/19), commit `d0a0e8f7b8ecacc57a0c8f4b72a53d4415b64f61`, normalizes the native ledger's saved Decimal-string quantities without rounding or weakening numeric transport validation. Source and isolated candidate each passed 141 tests. Scout's actual installed exporter then passed with all eleven symbols and original DB/WAL/SHM unchanged; network, account calls, packet export and responder launch were blocked during this audit. This correction is required with PR #18. |
| Atlas additional schedules | Atlas's report lists weekly review ACTIVE Saturday 9am Pacific, legacy LOG PAUSED and both existing Hyperliquid operating tasks PAUSED. Hyperliquid source intake still receives priority through active source reconciliation. No operating-task activation was inferred from source synchronization. |
| Atlas execution cutover | Atlas reports account status `PREPARING`; `COMBINED_ACCOUNT_CUTOVER_NOT_ACTIVE` still blocks the combined trader even if Jeremy starts it manually. The ownership follow-up enables planning evidence without migrating native ledgers or activating execution. A separate Atlas-local reviewed cutover must fence producer execution, reconcile and install complete native ownership, and bind its verified receipt. The existing migration procedure requires both original native ledgers/archives; database transfer is outside today's sanitized-packet permission. Do not change a configuration pinned by an in-flight exchange. |

The final exchange source uses `tools.nightly_exchange`, the read-only producer ownership exporter and the Atlas-only read-only account snapshot adapter. Its publication, local installation and activation are tracked in the rows above; implementation in an isolated worktree alone does not establish any of them. Legacy LOG remains paused and is not reused.

Both Atlas and Scout have a local folder where symbol data is stored named "DATASTORE"
    - DATASTORE is where price data from Schwab, FMP, Databento, SEC, ALFRED, etc. are stored, on each PC, and each 11 symbols (see below).

Both Atlas and Scout have a local google drive folder where communications are executed named "CODEXSTORE"
    - this is a shared google drive folder where both Scout and Atlas and both secondstate and clearpondllc Codex accounts are synced too

Both Atlas and Scout manage my Schwab/thinkorswim portfolio.

---

### GAMEPLAN and GAMEPLAN STATS

- ducketz pycharm project is on both Scout and Atlas
 
    - both projects share the same canonical GitHub `main` in [jeremysecondstate/ducketz](https://github.com/jeremysecondstate/ducketz). Reviewed local source adoption and unmerged PRs must be recorded explicitly; being installed on one PC does not mean a change is merged into `main` or installed on the peer.
    - common Gameplan, UI, model and strategy behavior is shared. Each PC preserves its symbol overlay and existing operating role; staged source differences and Atlas-only account execution bindings must be recorded explicitly.
    - it fetches the most recently completed market session's data 
    - each ducketz project/PC/Codex manages 11 symbols
    - Scout:
        "DOCU",
        "DBX",
        "SDGR",
        "QBTS",
        "PYPL",
        "GLOB",
        "OUST",
        "ABCL",
        "MRNA",
        "RR",
        "PDYN"
- Atlas: 
        "AAPL",
        "AMZN",
        "SNDK",
        "MU",
        "NVDA",
        "GOOG",
        "COST",
        "CROX",
        "PATH",
        "IONQ",
        "TWST"

Original LOG background: communication previously began around 9pm with the scheduled 'Loops Overnight Gameplan' ("LOG") tasks. The split workflow below supersedes that design; these links are historical references, not a verified inventory of currently active tasks:
- [clearpondllc LOG](https://chatgpt.com/scheduled?automationId=scout-overnight-gameplan-observer&automationSource=local) and [secondstate LOG](https://chatgpt.com/scheduled?automationId=loops-hourly-operations&automationSource=local).

Scout and Atlas independently fetch the most recently finished session's data for their own 11 symbols and save it in DATASTORE. First, create Gameplan Stats by evaluating the previously saved predictions against the newest completed session's actual outcomes. Next, use those findings to review and adjust the models where justified, then train/evaluate the models and create predictions for each horizon. Finally, create the Gameplan for the next trading session. Monday night's improvement review should use Monday's completed stats, not deliberately wait one session; Tuesday night should use Tuesday's completed stats, and so on. Only outcomes that have actually matured can be scored.
Once Atlas and Scout finish their respective Gameplans and Gameplan Stats, the separate private exchange transfers each owner's exact completed packages. After both preparations match the next action date and newest completed Stats session, Atlas provides a fresh sanitized account-wide snapshot. Scout's code combines both plans against that one budget, including inventory, exposure, reservations and horizon ownership, and publishes the combined Gameplan, combined Stats sources and exact receipt. Atlas verifies and adopts that exact result, then returns an acceptance receipt; it does not independently reallocate Scout's plan. Once Atlas is ready, I manually turn on the 'active trader' in Atlas's ducketz project, using this command in the ducketz pycharm terminal: & "C:\dev\ducketz\Start-Gameplan-Trader.cmd". Atlas handles trades for all 22 symbols. 
- The rationale for Scout taking on the synthesis and Atlas taking on the trading for all 22 symbols is because Scout is currently using the clearpondllc Codex which is the Pro 500 account and Atlas is currently using the secondstate Codex which is the Pro 200. And the synthesis will likely take up Usage whereas the active trader doesn't really take up Usage.

### REPO RECONCILIATIONS

Atlas, Scout and Jeremy will make changes to the ducketz projects. Reviewed completed changes are published through the existing source procedures, and each PC reconciles the changes applicable to it. Review at the level of behavior, configuration fields and documented local overlays. Common engine, UI, model code and strategy defaults belong on both PCs even when they process different symbols. Preserve each PC's symbol selection and operating bindings. Do not discard an entire file or commit merely because it mentions symbols. Add or refine the shared/local distinctions as we discover them.

Repository reconciliation is a separate responsibility from producing the nightly Gameplan. Record which source revision produced each run. Preserve unfinished work and resolve actual overlapping edits; do not replace another writer's work to make the checkouts appear identical.

### WHAT IS UP WITH HYPERLIQUID STUFF?!

Hyperliquid operations are in development, and should match 1:1 without any barriers between ducketz projects. I'm currently working on this mostly on Atlas's PC, so any Hyperliquid stuff seen on Github is automatically reconciled. Also, I might work on Hyperliquid stuff on either secondstate or clearpond or Atlas/Scout PCs, so both accoutns and PCs and ducketz projects should be lined up with ANY and ALL Hyperliquid stuffs!

**Priority:** Hyperliquid development changes should receive automatic priority intake on both projects, ahead of routine reconciliation, rather than waiting for the nightly reconciliation time. Shared Hyperliquid code and defaults should stay aligned regardless of which PC/account produced them. Actual overlapping local edits still require resolution rather than being overwritten. Source adoption does not itself restart a running application or copy private credentials/account state. Jeremy has now authorized this final phase, and Scout's priority intake task is active as recorded above. Intake and review can continue while nightly work is running, but installation must wait when it would change source pinned by the current preparation or exchange session. Actual Atlas task state requires its own evidence.

### CODEX SCHEDULED TASKS ON BOTH 'CLEARPONDLLC' and 'SECONDSTATE' accounts

Use the legacy Loops Overnight Gameplan/'LOG' only as a reference for building a new workflow with smaller responsibilities, implemented on both PCs according to their operating roles. Create distinct replacement task identities rather than reusing LOG. Gameplan Stats is now a separate stage before model adjustment/training and Gameplan creation.

### Responsibility and model-use breakdown (updated October 9, 2026)

These responsibilities define the updated sequence below. Model effort depends on the work actually performed: routine command execution can be light, while diagnosing results and changing models requires stronger reasoning. The Scout implementation uses a lightweight native launcher and readiness task, with one stronger Codex CLI review after Stats completes. The initial local launcher/readiness selection is gpt-6-luna/low, and the bounded model review uses gpt-6-astra/high. Package exchange, capital allocation and receipt verification are deterministic code; stronger reasoning remains appropriate for reviewing exceptions or proposing a separately reviewed change.

| Responsibility | Owner | Suggested role for Codex |
| --- | --- | --- |
| DATASTORE CATCH-UP | Both PCs, their respective 11 symbols | Light routine supervision; deeper analysis for gaps or failures. |
| GAMEPLAN STATS | Both PCs, after data catch-up | Code scores previously saved predictions using the newest completed outcomes and existing UI metric definitions; Codex reviews completeness and anomalies. |
| MODEL REVIEW, TRAINING & PREDICTING | Both PCs, after Gameplan Stats | Stronger reasoning for reviewing the newest completed Gameplan Stats and making justified parameter, feature, calibration or architecture adjustments; lighter supervision of established training and prediction runs. |
| GAMEPLAN | Both PCs, after training and predictions | Create and review the next trading session's local plan from the accepted predictions. |
| GAMEPLAN SYNTHESIS | Scout synthesizes; Atlas delivers, validates and adopts | Scout code selects exact packages and calculates quantities against Atlas's one account-wide budget. Atlas adopts Scout's exact Gameplan, Stats and receipt; Atlas does not run numerical synthesis. |
| DUCKETZ DISPLAY | Both PCs | Verify exact local Gameplan/Stats before research export, then the accepted combined Gameplan/Stats after synthesis/handover. |
| REPO RECONCILIATION | Both PCs, independently of the nightly pipeline | Review shared changes at field/behavior level; resolve meaningful conflicts. Give Hyperliquid development priority intake. |
| TRADER REP | Atlas only | Check actual readiness/status and verify the existing worker reconciles overdue intentions when Jeremy starts it late, using current evidence, net quantities and duplicate protection. The task never submits orders or controls the trader. |

The order below supersedes the original hourly schedule and combined Gameplan/Stats stage. The 9:05pm kickoff remains the initial target. Later operating stages start when their prerequisites complete, rather than assuming completion from the clock. A local coordinator owns this sequence, saved stage receipts, locks and recovery. The native launcher does not wait inside a chat for numerical jobs to finish.

**Starting at 9:05pm PDT/PST**
**Light routine supervision; stronger reasoning for exceptions**
1. Fetch Catch-Up Data for DATASTORE symbols ("DATASTORE CATCH-UP"):
    - fetches/overlap data fetch getting DATASTORE up to speed with all the current data.

**After DATASTORE CATCH-UP completes**
**Code calculates metrics; Codex reviews completeness and anomalies**
2. Gameplan Stats ("GAMEPLAN STATS"):
    - score the previously saved forecasts against the newest completed session's actual outcomes, preserving the existing UI metric definitions and forecast probability targets.
    - publish the completed statistics before model improvement and training. Pending longer-horizon outcomes remain pending until they mature.

**After GAMEPLAN STATS completes**
**Stronger reasoning for model improvement; lighter routine run supervision**
3. Model Review, Train/Eval/Predict ("TRAINING & PREDICTING"):
    - use the newest completed Gameplan Stats to diagnose issues and make justified model adjustments, including parameters or architecture where appropriate.
    - with fresh/current/up-to-date DATASTORE data, models train/eval/print predictions.

**After TRAINING & PREDICTING completes**
**Middleweight review; stronger reasoning for exceptions**
4. Gameplan ("GAMEPLAN"):
    - create the next trading session's local Gameplan from the accepted predictions. Gameplan Stats was already completed before training.

**After both PCs' Gameplans and Gameplan Stats are complete**
**Bounded private exchange; code calculates quantities and verifies the shared budget**
5. Gameplan/Gameplan Stats Synthesis ("CODEXSTORE GAMEPLAN SYNTHESIS"):
    - Each PC exports its verified current-session Gameplan and Stats packages through `CODEXSTORE/ducketz-nightly-exchange/v1`. Missing or partly synced peer inputs remain pending.
    - After both preparations are present, Atlas supplies one fresh account-wide budget snapshot covering the bound 22-symbol execution universe, including current holdings, working orders and reservations. Preserve original account/symbol/horizon/allocation/order/fill identities and evidence; missing records do not establish zero holdings.
    - Scout performs synthesis from both frozen research packages against that single Atlas snapshot. Scout has no broker/account snapshot, execution-ledger, ownership-responder or migration prerequisite. The superseded ownership-challenge design remains in the October 7 Git history, not as a standing operating step.
    - Freeze the exact selected inputs and receipts. Recover partial publication/adoption through the same durable selection. A completed terminal session never captures another snapshot or replays handover.
    - Scout publishes the combined result and both owners' original package pairs. Atlas verifies the plan, Stats and its own original snapshot publication before adopting; it returns exact acceptance evidence. Jeremy still manually starts the trader.

**After the combined results are accepted**
**Light verification**
6. Ducketz UI/App Display ("DUCKETZ DISPLAY"):
    - Before export, verify the exact saved local research Gameplan and Stats. After synthesis or handover, verify the ordinary readers select the accepted combined Gameplan and Stats for the intended action date. Do not demand a combined publication before Scout has synthesized it.

**Separate workflow; 1:25am PDT/PST remains an initial routine-review target**
**Middleweight review; stronger reasoning for meaningful conflicts**
7. Ducketz Projects Reconciled ("REPO RECONCILIATION"):
    - via CODEXSTORE and/or GitHub, Atlas and Scout publish reviewed completed changes using the existing source procedures. They adopt common changes and preserve documented local fields and symbol overlays through granular review. Both projects need to be on the same page for seamless interchangeability. Hyperliquid development receives priority intake rather than waiting for this time.

**Starting at 3:55am PDT/PST**
**Light status review; deterministic catch-up calculations**
8. Trader Representative ("TRADER REP"):
    - Determine actual readiness and whether Jeremy has turned on Atlas's active trader. Verify that the normal worker catches up outstanding net intentions, accounting for offsetting buys/sells, starting inventory, actual fills and outstanding orders. A scheduled timestamp alone is not an expiry. Continue covering manual starts after the initial 03:55 check. The task never starts, stops or restarts the trader, changes its controls, or submits/cancels/replaces orders.

### Confirmed refinements and implementation notes

**Existing Gameplan Stats:** retain the current tab and its metric meanings. The UI already shows direction accuracy, probability error (Brier score), bullish/bearish accuracy, company scorecards and counts, outcome coverage, horizon filters and the thirteen hourly outcome windows. Cell details include saved probabilities, observed returns and observation times. These are saved prediction outcomes; pending/missing results are not scored as failures. Use the underlying saved results for model feedback rather than reading screen text or inventing another scorecard.

**Nightly model improvement:** use the newest completed Gameplan Stats. On Monday night, finish Monday's stats first, review/adjust the models, then train and create the next trading session's predictions and Gameplan. Jeremy confirmed the existing metrics should determine whether changes earn promotion. The stronger reviewer may propose up to two bounded candidates per horizon, including model parameters and neural layer architecture. Existing defaults and the latest compatible accepted reviewed specification remain baselines. Chronological selection and held-out assessment/promotion gates decide acceptance; equal or worse proposals do not displace the baseline, and failed promotion may retain a verified compatible champion. Record comparisons and retention/promotion evidence. Do not force a change merely because a review ran, and freeze the original predictions being scored. Broader feature-code or model-family redesign remains a separately reviewed source change.

**Implemented feedback ordering on Scout:** `ml/gameplan_actuals_review.py` now supports standalone completed-session Stats without waiting for the successor plan. The replacement coordinator invokes the existing numerical runtime with Stats-first ordering, stops after Stats, obtains the stronger review, then starts training with the exact reviewed proposal. The existing UI metrics and saved forecast targets feed the diagnostics. Legacy receipt/stage ordering remains readable for historical runs.

**Research versus execution:** each PC researches its own 11 symbols, while Atlas's active trader accepts the combined 22-symbol plan. Scout's new source separates the accepted execution universe from research selection, with explicit source/account/session/actor bindings. Scout can display the combined plan without gaining execution authority. Atlas's PR #15 account-control implementation and PR #16 readiness changes have now been reviewed; the current local adoption evidence is recorded in the dated status table above. Account cutover, execution bindings and manual trader startup remain separate from source adoption and exchange readiness.

**Portfolio synthesis:** one account-wide capital budget is a central purpose of synthesis. Combine both plans with existing holdings, working orders and reservations so the two symbol groups do not each allocate the same funds. Scout produces the combined plan; Atlas remains the live execution owner.

**Late-start catch-up:** Jeremy's example is a 4am AAPL buy of one share followed by a 5am sell of one or two shares, with the active trader started at 5:15am. The new source offsets opposing overdue quantities within each symbol and inventory-owning horizon. Buy one then sell one can cancel; buy one then sell two leaves a net sale of one when starting holdings support it. Plan-related fills and open orders reduce outstanding quantities, cancelled residuals can retry, and unrelated manual activity is not treated as a plan fill. A missed timestamp alone is not an expiry rule. This applies to accepted combined plans and verified complete local direction ledgers; separate horizon inventory ownership and the manual trader start remain in place.

**Handover completes planning:** exact Scout synthesis and Atlas adoption completed on October 9, and Jeremy later reported starting the trader manually. Do not add a Scout-history export, migration, cutover, duplicate broker preflight or additional approval ceremony. Existing account/order reconciliation belongs to Atlas's normal worker. The superseded October 7 first-start requirements remain in Git history as historical evidence.

**Transport and private data:** preserve the installed Git coordination history, pinned Drive signals, existing queues, identities and receipts for source and sanitized status notices. The nightly operating data uses a deliberately separate, explicitly authorized private synchronized folder at `CODEXSTORE/ducketz-nightly-exchange/v1`; it is not a replacement or fallback for the Git notice channel. Do not publish private exchange packets, configurations or account state to Git/GitHub.

Jeremy explicitly authorized this private packet to carry cash, equity, inventory and exposure for the agreed 22 symbols, working-order reservations, horizon ownership and the resulting combined plan, alongside the necessary original plan/Stats packages and completion evidence. Credentials, account numbers, raw broker responses, databases and fitted models are excluded. Exact receipt paths are provenance strings, never paths or instructions executed by the receiver.

Each wake is bounded. Packet selections bind the action date, completed Stats session, actor, account scope, exact owner lists, byte count and hashes. Preparation, joint and acceptance selections are immutable. Atlas may refresh an unconsumed snapshot before a joint result is selected; a frozen or partially adopted synthesis retains its original snapshot and completion identity. Atlas saves its own local capture proof before publishing, so an Atlas-named shared packet or receive cache cannot establish that Atlas captured it. A snapshot must be no more than 900 seconds old at first synthesis; a frozen attempt that expires before first adoption remains pending for explicit review. A prepared package is not peer receipt, and receipt verification does not activate trading. Actual source installation, configuration and schedule status are listed above.

### Historical October 7 replacement task inventory

The shared implementation/runbook is `docs/development/nightly-workflow.md` in ducketz, with a portable example configuration in `coordination/nightly-workflow.example.json`. Machine paths, native IDs, profiles and task memory remain local. The table below records the earlier rollout, not the final October 9 eight/seven-responsibility inventory. Its 15-minute Scout priority interval is historical; the current request requires five-minute priority coverage.

| New Scout task | Schedule / role | Rollout state |
| --- | --- | --- |
| Scout Stats First Nightly Preparation | 9:05pm Pacific; launch the dependency-driven local worker | ACTIVE on Scout; definition verified |
| Scout Nightly Readiness | 3:35am Pacific; verify actual saved results and report incomplete stages | ACTIVE on Scout; definition verified |
| Scout Joint Gameplan Synthesis | Every five minutes; bounded private exchange, prerequisite checks and exact synthesis | ACTIVE on Scout; final ownership-follow-up adoption and production readiness are recorded above |
| Scout Priority Source Reconciliation | Every 15 minutes; Hyperliquid first; routine review at the first wake after 1:25am | ACTIVE on Scout; preserve source pinned by the current nightly session |
| Loops Overnight Gameplan | Historical definition only | Paused; never reused as the launcher |

The preparation worker retains `LOCAL_COMPLETE_PEER_SETUP_PENDING` as its local completion state. The separate exchange consumes those exact frozen exports; the state alone does not establish joint readiness or peer adoption. Readiness verifies the original local preparation separately from the exact selected synthesis/handoff receipt, so combined UI publication does not invalidate the earlier local work. Scout's `JOINT_READY_LOCAL` and Atlas's `HANDOFF_VERIFIED_LOCAL` verify their respective combined UI artifacts. Exchange completion additionally requires Atlas's matching acceptance evidence. The existing Atlas execution binding and manual trader start remain separate, and offline fixture tests do not establish a successful production overnight run.

If there is no saved prior Gameplan for a session, preserve an explicit no-history Stats baseline with no invented accuracy or forecast rows. The review keeps current specifications and allows the first actual forecast to be prepared. Exports and combined Stats retain which producer has no saved history; this is not treated as a failed prediction.

**Historical Scout build handoff — October 7, 2026, before PR #15 review, PR #16 adoption and final-phase authorization.** The paragraph below is retained as the record of that earlier checkpoint; its hold and installation statements are superseded by the current status above.

**Scout build handoff, October 7, 2026:** reviewed shared source is published in [draft PR #14](https://github.com/jeremysecondstate/ducketz/pull/14), commit `0d9c81c973a01da9a7872c225d4363bd9fa8c002`. The final local and isolated regression suite passed 419 tests; the candidate combined with current main passed 634 tests. Each had one Windows synthetic-symlink privilege skip. Main has not been merged and Atlas has not been installed or contacted. Scout's configuration and the two active local schedules are verified; the production worker has not been launched as an implementation test. On Atlas, use the PR's common source and `docs/development/nightly-workflow.md` with Atlas's own pinned release, profile, symbols and account bindings, then confirm both local installations before enabling transport, reconciliation and synthesis.

---

The rationale for splitting the tasks up is to have control over which tasks use which models, because some tasks do not require such an intensive model.

The nightly operating stages 1-6 should follow completion dependencies: DATASTORE CATCH-UP -> GAMEPLAN STATS -> MODEL REVIEW / TRAINING & PREDICTING -> GAMEPLAN -> SYNTHESIS -> DISPLAY. Each PC can advance through its local stages independently; synthesis waits for the matching completed outputs from both. Avoid tasks waking early and repeatedly checking unfinished work. Repository reconciliation is independent, and Trader Rep must also handle Jeremy starting the active trader after its first scheduled check. Use America/Los_Angeles for the intended Pacific schedule and actual trading-session identities across weekends and holidays.

---

**Original kickoff notes, retained as history:** the final-phase authorization and current verified status above supersede the initial coordination hold described here.

**_I've cleared all chats, cleaned up most of the Codex Scheduled tasks, and reset PCs, so we can start with a clean slate._**  

**_I'm also going to do this separately on the other PC; I want to implement this on both Codex accounts/PCs and then once we finish this implementation, Atlas and Scout will cross-verify their Scheduled tasks and ducketz projects_**
