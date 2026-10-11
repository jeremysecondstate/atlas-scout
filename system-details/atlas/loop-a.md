# Atlas Loop A and its scheduled tasks

**Observed October 10, 2026, 19:54–20:02 PDT (`America/Los_Angeles`).** This is Atlas's chapter. It describes read-only source, native configuration and saved runtime evidence; Scout maintains its own observations. Native IDs, absolute machine paths, full task definitions and receipt references remain in the dated private Atlas chapter. Evidence labels below identify the source and observation time behind the claims.

Loop A is the Loops system's data acquisition and feature-building process. On Atlas, it currently runs as the first numerical stage of the **datastore catch-up responsibility**, followed by stock-target archive maintenance. **Atlas Datastore Catch-up is active at 21:05 Pacific; the older Loops Overnight Gameplan task is paused.** The Windows dispatcher and Codex supervisors share the dated workflow state. A scheduler wake, a launched process, a successful Loop A core generation and a completed catch-up responsibility are four different facts. [N1, N2, W1, R1]

## Evidence levels and ownership

| Level | What was checked | What it establishes |
| --- | --- | --- |
| Checked-in design | Ducketz HEAD `90704d21801f60426493bd6cc650a7fac38d4f61`; clean core orchestrator, cycle, readiness and provider CLI source | The committed core behavior described below. It does not establish which bytes an already running process loaded. [S1–S4] |
| Local working source | Modified `ml/overnight_runtime.py` and `datafetching/runtime_lock.py`; untracked `ml/nightly_workflow.py`, `ml/nightly_dispatch.py`, watchdog and newer runbooks | The newer implementation present in this checkout. It is not all contained in that HEAD. Existing writers' files were inspected and preserved. [W1] |
| Installed coordination | Pinned release `7bd3da6cd674d78a6aafa01e1d4ecf3fbe66384a`, manifest verified, all 29 installed files verified; local profile identifies Atlas, source-publication authority and `github_only` notification policy | Coordination identity and publication procedure, not an application release or production-health certificate. [C1] |
| Installed local configuration | Atlas workflow binding selects archive history, XNAS stock-target history, five responsibility owners, bounded automatic recovery and a separate stronger model reviewer | The saved settings used by the current dispatcher. Local preparation's peer-communication flag is false; the separate exchange has its own state. [W2] |
| Scheduler registration | Fifteen saved Codex definitions, corroborated by native database readback; three Ducketz Windows registrations and their task info/XML | Current status, timing and entry points. Status ACTIVE/Ready does not mean a particular action date completed. [N1, N2] |
| Observed runtime | October 9 source-session / October 12 action-date preparation, core cycle, logs and receipts; 24 recorded output files match their saved hashes | That saved attempt completed locally. Its aggregate source fingerprint differs from the current working source, despite the same Git HEAD. Success must not be attributed to all today's modified files. [R1] |

This change owns only this Atlas chapter and the Atlas link in the shared index. The existing Ducketz Loop A report, Atlas scheduled-task history and Scout files remain unchanged. No application, scheduler, provider, broker, training or worker operation was performed for verification.

## Purpose and stage order

The production stage entry point is **`python -m datafetching.orchestrate --once`**, constructed by `ml.overnight_runtime`. **`datafetching.main` is a component CLI** for a symbol's provider fetches; it does not run the complete supervisor, calculations, cycle publication and OPRA tail. Current Atlas launches all five provider lanes and explicitly selects inline CME/options compatibility work and daily OPRA history. Those explicit flags override the orchestrator CLI's external/off defaults. The saved successful command corroborates the current launcher configuration. [S1, W1, R1]

```mermaid
flowchart TD
    A[Resolve Atlas watchlist and acquire ownership] --> B[Mark core generation WRITING]
    B --> C[Databento bars first]
    C -. eligible exact one-minute bars .-> Q[Readiness for Pricing and Options]
    C --> D[FMP, current FRED, Schwab and SEC]
    D --> E[Fundamentals, technicals and cross-domain signals]
    E --> F[Core COMPLETE or FAILED]
    F --> G[Configured OPRA history and catalog refresh]
    G --> H[Loop A bounded stage ends]
    H --> I[Stock-target history completes datastore catch-up]
    I --> J[Stats, model review, predictions, local Gameplan, display and handoff]
```

The dotted readiness branch is separate from full-cycle success. In Atlas's bounded `--once` call, the Databento one-minute callback attempts readiness. The retained recurring mode instead starts an independent readiness thread inside the Loop A supervisor, so a long feature/provider cycle does not hold up exact-bar acquisition. That recurring thread is a source capability, not evidence of an active recurring Atlas deployment. [S1, S3, R1]

1. **Choose scope and serialize work.** Explicit symbols or watchlist arguments select scope; otherwise a process watchlist override precedes the local watchlist and shared fallback. The supervisor lock prevents a second Loop A owner; the A/B datastore OS lock protects the full generation while Loop A writes and Loop B reads. A WRITING record identifies the generation. [S1, S2]
2. **Fetch and normalize provider inputs.** Databento runs first, then the remaining configured lanes. Batched watchlist requests and per-symbol outputs are used where supported; the shared FRED series fetch runs once. Stored timestamps permit overlapping continuation, not a complete historical rebuild each night. Native bars take precedence over overlapping derived bars while derived-only gaps survive. [S1, S4]
3. **Publish eligible bar readiness.** Readiness requires exact completed one-minute bars for every selected symbol and an eligible XNYS regular-session quarter-hour target. Outside that window, the decision is monitor-only with no target; no artificial readiness is published. Missing exact bars can trigger deadline-bounded recovery; inconsistent authoritative evidence fails integrity checks. Failure of this branch does not itself increment the heavyweight cycle's failure count. [S1, S3]
4. **Build calculated products.** Per symbol: fundamentals when FMP is configured, then technicals, then cross-domain signals. Failed provider/calculation stages contribute to the core failure count. Schwab quote-only errors have a special nonblocking rule, but Atlas's explicit inline-options mode does not qualify for that blanket exception. [S1, S4, R1]
5. **Publish the core boundary.** Zero blocking failures yields COMPLETE; otherwise FAILED. Only COMPLETE advances the last-successful-generation pointer. Loop B takes the shared lock and requires the *current* cycle to be COMPLETE; an older successful pointer cannot silently replace a failed current generation. [S2]
6. **Finish the configured history tail.** The OPRA subprocess and catalog audit run after the core terminal record. Their failure makes the bounded Loop A command fail even if the earlier core record says COMPLETE. The separate XNAS stock-target history stage then completes the broader datastore catch-up responsibility. [S1, S5, W1, R1]

## Inputs, outputs and consumers

Atlas's current local watchlist contains eleven equities. The exact membership remains in the private chapter and local profile; the saved successful attempt agrees with that local file. The four-symbol Hyperliquid profile belongs to a separate stack. Explicit process overrides remain possible, so a file alone is insufficient proof of a future process's selection. [C1, S4, R1]

| Input | What Loop A produces or preserves | Consumer and boundary |
| --- | --- | --- |
| Databento equity bars; the saved run reports operational EQUS.MINI | Normalized per-symbol market data, derived bars and exact-bar readiness | Loop B consumes full completed feature generations. Pricing and Options consume exact decision-time bars/readiness separately. Operational and cold archive datasets are not blindly timestamp-merged when identities differ. [S2–S4, R1] |
| FMP statements, ratios and corporate context | Normalized provider data and calculated fundamentals | Loop B and later Gameplan feature materialization; availability/publication clocks matter for historical use. [S1, S4] |
| Current FRED GDP, CPI, unemployment and federal-funds series | Current normalized observations | Current causal rate/monitoring inputs; this does not supply historical ALFRED-vintage authority. Pricing enforces its own causal evidence rules. [S4, S6] |
| Configured Databento CME futures context, enabled inline once for the first symbol | Raw/normalized bars and quotes, eligible nonsaturated event history and calculated cross-asset features; configured schemas can include depth (`mbp-10`) | Feature context under the CME writer lock. This bounded acquisition does not launch the independent recurring CME supervisor. [S4] |
| Schwab quotes and explicitly enabled inline options work | Quote/liquidity plus per-symbol chain snapshots, contracts/features and immutable snapshot receipts under the Options writer lock; persisted errors | Later stock/options contexts. This inline path does not invoke the independent Options supervisor or its Pricing barrier, perform Pricing inference, authorize orders or replace a trader's current broker checks. [S1, S4] |
| SEC filings and associated metadata | Filing/event inputs and derived cross-domain signals | Directional and later Gameplan feature families, subject to their own availability clocks. [S1, S4] |
| Databento OPRA history: `ohlcv-1h`, `cbbo-1m`, `definition` | History manifests, normalized data, verified cursors and refreshed catalog health | Later strategy-profit training and options research; acquisition is separate from Pricing inference, prospective option-chain capture and orders. [S5] |
| Core cycle and exact-bar publication records | Two distinct evidence boundaries | Loop B: current COMPLETE plus finish-time availability cutoff. Pricing: all-symbol exact readiness within its causal window. Options: target readiness and latest successful core finish as regime cutoff. [S2, S3, S6] |

Later Atlas workflow stages consume these products in dependency order: **datastore catch-up → Gameplan Stats → model review → training/predictions → local Gameplan → display verification → local handoff**. The configured stock-only flow omits legacy option strategy-training/generation stages; maintaining OPRA history does not imply those models ran. The stronger review step uses `gpt-6-astra` / high, separately from the Luna/low scheduled supervisors. Display and trader consumers use frozen plans rather than rerunning Loop A. [W1, W2, N1]

### OPRA history details

The saved Atlas command enables daily maintenance with a UTC-hour threshold of zero, a 20,000,000,000-byte estimated download cap, USD 1 estimated cost cap and 30-day maximum catch-up window. It requests incremental scopes and a verified live-replay fallback for the exact completed session. Missing valid cursors remain bootstrap-required; replay fallback is not permission for an initial bootstrap. History failure/capacity blockage and catalog failure remain visible to the wrapper. [S5, R1]

The orchestrator's daily attempt gate uses **UTC date/hour and in-process memory**, not a durable global daily receipt. 00:00 UTC is 17:00 PDT or 16:00 PST. Atlas's 21:05 *Pacific* scheduling comes from the workflow and native definitions. Do not interpret the internal gate as a DST-aware 17:00 Pacific schedule or as proof that a restarted process cannot attempt again. [S1, W1, N1, N2]

## Tasks and deterministic dispatchers on Atlas

All times below are Pacific (`America/Los_Angeles`, PDT on this observation date). Saved Codex recurrence rules do not embed a time-zone identifier; Pacific intent is established by the prompts/workflow and the native next-run epoch readback. Windows reports `Pacific Standard Time`, the DST-aware Windows zone. The daily Windows trigger uses local wall time; its repeating trigger is every five elapsed minutes. These settings were read, not changed. [N1, N2]

| Task or dispatcher | Observed status and recurrence | Model / effort | Entry point and exact Loop A relationship |
| --- | --- | --- | --- |
| Atlas Datastore Catch-up | **ACTIVE**, daily 21:05 | `gpt-6-luna` / low | `ml.nightly_workflow --launch --responsibility datastore --catch-up`; eligible work reaches `ml.overnight_runtime` → `datafetching.orchestrate --once`, then stock-target history. Current scheduled owner, retaining an older preparation identity. |
| Windows nightly responsibility dispatcher | **Enabled / Ready**; daily 21:05, every five minutes, and logon | None | `tools.nightly_watchdog` → `ml.nightly_workflow --dispatch` using the local binding. May launch one eligible responsibility; idle/complete/healthy work is retained. Last readback: October 10 19:53:25, result 0, missed runs 0. This result describes the dispatcher invocation, not a new Loop A run. |
| `ml.nightly_dispatch` | Installed local source; no separate native schedule | None | Selects the next unfinished dependency owner and intended session; uses the 21:05 source-session kickoff and 04:00 action-date deadline. It does not itself replace numerical execution. |
| `ml.overnight_runtime` | Invoked by eligible workflow segments; no separate current native schedule found | None | Constructs the bounded `loop_a_close_fetch` command and native stage report; datastore segment stops after configured stock-target history. |
| Atlas Gameplan Stats | **ACTIVE**, daily 03:00 | `gpt-6-luna` / low | Stats responsibility in `ml.nightly_workflow`; consumes completed catch-up and mature outcomes. Also owns the dated 03:00 readiness-risk alert. An eligible dispatch must preserve prerequisites. |
| Atlas Model Review Training and Predictions | **ACTIVE**, daily 03:00 | `gpt-6-luna` / low | Model responsibility in `ml.nightly_workflow`; consumes frozen Stats and completed data, supervises review and downstream training/predictions. Substantive reviewer model is separately configured. |
| Atlas Local Gameplan | **ACTIVE**, daily 03:00 | `gpt-6-luna` / low | Gameplan responsibility in `ml.nightly_workflow`; consumes accepted predictions and frozen inputs. Does not independently fetch another Loop A generation. |
| Atlas Ducketz Display and Readiness | **ACTIVE**, daily 03:35 | `gpt-6-luna` / low | Display responsibility and `ml.nightly_readiness`/`tools.nightly_notifications`; verifies saved results and owns the dated missed-confirmation alert. |
| Atlas Joint Gameplan Handoff | **ACTIVE**, Mon–Fri 21:00–23:40 every 20 minutes | `gpt-6-astra` / ultra | One `ml.nightly_workflow --dispatch` may recover a missed watchdog wake; then `tools.nightly_exchange` and handoff/verification helpers consume the completed research package. Handoff supervision, not the primary fetch owner. |
| Atlas Joint Gameplan Handoff After Midnight | **ACTIVE**, Tue–Sat 00:00, 00:20, 00:40 | `gpt-6-astra` / ultra | Same responsibility and continuity as preceding evening; no duplicate full pipeline. |
| Atlas Priority Source Reconciliation | **ACTIVE**, Mon–Fri 21:00–23:40 every 20 minutes | `gpt-6-astra` / ultra | Reviewed source intake, `ml.nightly_stage_repair` for preparation and `ml.nightly_exchange_repair` for post-preparation failures; ordinary review once per operating evening. Can help repair a failed dependency, not a second Loop A owner. |
| Atlas Priority Source Reconciliation After Midnight | **ACTIVE**, Tue–Sat 00:00, 00:20, 00:40 | `gpt-6-astra` / ultra | Continues the prior evening's source responsibility and deduplicates its review. |
| Atlas Trader Representative | **ACTIVE**, Mon–Fri 03:55, then 04:05 and hourly through 17:05 | `gpt-6-sol` / ultra | Readiness/accepted-plan downstream supervision. Its saved prompt has guarded launcher conditions; this documentation did not verify their installation or exercise trader control. It does not supply Loop A completion evidence. |
| Loops Overnight Gameplan | **PAUSED**; retains daily 21:05 | `gpt-6-astra` / ultra | Legacy monolithic `ml.overnight_runtime --once --scheduled` supervision. Its old prompt and timing are historical, not the active datastore owner. |
| Loops Gameplan Weekly Review | **PAUSED**; retains Saturday 09:00 | `gpt-5.6-luna` / medium | Reviews saved Gameplan history and downstream outcomes; not an ingestion launcher. |
| Finish Atlas and Scout overnight recovery | **PAUSED**; retains five-minute heartbeat | Inherits chat settings; no saved standalone model/effort | Temporary existing-chat recovery continuation. Separate from routine Loop A and separate from a data-fetch completion monitor. |
| Historical Windows stock-session registration | **Disabled**; saved Mon–Fri 03:55 trigger | None | `start_stock_session.ps1`, a downstream consumer launcher. Last run September 15, result 1, 18 missed runs. A future “next run” value does not override Disabled. |

Table evidence: Codex rows [N1], Windows rows [N2], module rows [W1]; observed at approximately 19:57 PDT. The five daily checkpoints are supervision opportunities, not barriers preventing an earlier eligible successor dispatch. The completed attempt below advanced through Stats/model/Gameplan before their next daily wake. A paused definition supplies no ordinary scheduled launches. Friday evening's active handoff/source window includes Saturday 00:00–00:40. [N1, W1, R1]

Two paused Hyperliquid schedules belong to the separate crypto stack; the enabled Windows completed-chat cleanup only archives eligible chats. They do not start or prove Loop A work. No current Atlas definition was found for the former Loops Operations Watch, standalone OPRA supervisor or a separate **data-fetch completion follow-up** in the fifteen saved TOMLs and fifteen native automation rows. Older cross-PC material described some monitors on Scout. Their current Atlas IDs, state and recurrence are therefore **not established**, and none have been copied here. [N1, N2, H1]

## What actually ran

The latest inspected preparation uses source session **October 9** and action date **October 12**. All times below are PDT; original UTC clocks and exact references are in the private evidence. [R1]

| Evidence boundary | Saved result | Interpretation |
| --- | --- | --- |
| Datastore responsibility started | October 9 21:05:03 | Real worker-stage evidence, beyond a scheduled wake. |
| Core Loop A generation | October 9 21:05:04–21:31:35; COMPLETE, zero failures | Core data/calculated products completed; OPRA was still downstream. |
| OPRA history tail | 33 requested scopes, 33 completed, zero failed/capacity-blocked/bootstrap-required/deferred; catalog refresh and exit 0 | Actual configured history work completed in this attempt; fallback was available but no live-replay scopes were used. |
| Bounded Loop A stage finished | October 9 22:42:12; COMPLETE | Includes the OPRA/catalog tail, unlike the earlier core pointer. |
| Stock-target history / datastore responsibility finished | October 9 22:44:26; COMPLETE | Full catch-up prerequisite satisfied. |
| Remaining local preparation | Stats 22:48:38; model review 22:53:40; training/predictions 23:44:59; local Gameplan October 10 00:04:15; local handoff 00:08:31 | All seven responsibility steps recorded COMPLETE. The frozen preparation terminal label is `LOCAL_COMPLETE_PEER_SETUP_PENDING`, reflecting its local-only configuration. |
| Separate later exchange state | October 10 03:25:58 saved status reports COMPLETE / HANDOFF_VERIFIED_LOCAL, joint/peer/UI readiness true | Do not misread the earlier local-only preparation label as today's proof of missing peer setup. Exchange flags were read; no new synthesis, financial audit or trader run was performed. [R2] |
| Latest inspected watchdog invocation | October 10 19:53:26, `dispatch=false`; retain completed session and original receipts | A healthy no-op. It did not perform another Loop A fetch. |

The stage report, two catch-up logs and all 24 workflow output bindings passed read-only hash checks. This verifies retained byte bindings, not every historical market-data row or a future run. Current source differs from the source identity recorded by this completed workflow. [R1]

The latest saved bar-readiness pointer is much older: **September 3 13:00 PDT target**, published 13:02:16, for a six-symbol scope. Its pointer-to-receipt hash matches. The October 9 overnight log explicitly reports `MONITOR_ONLY`, `MARKET_CLOSED_IDLE`, target `NONE`; it was not expected to issue fresh intraday readiness. The old pointer is not current eleven-symbol Pricing/Options readiness, and no active Pricing/Options process or current end-to-end intraday health was established. [R1, S3]

## Failure and recovery boundaries

- Provider errors are recorded where possible; blocking failures prevent core COMPLETE. Calculation failures also count. Handled interruptions attempt FAILED publication; a hard kill can leave WRITING. OS-lock release on process exit is different from deleting a persistent marker. [S1, S2, S4]
- Exact-bar recovery is deadline-bounded (configured 420 seconds, 10-second polling); corrupt authority is not repaired by a blind refetch. Pricing separately rejects missing/late readiness. Heavy Databento transient retries default to **no finite attempt limit** with four-second delay unless a caller sets one; calling the outer stage “bounded” does not make every inner retry finite. [S3, S4, S6]
- Current local supervisor-lock code uses a maintenance gate, complete owner-record publication and PID/birth/token evidence; uncertain ownership fails closed. This is locally modified source, and was not asserted to be loaded by a running process. The A/B datastore lock also has no built-in wait timeout. [S2, W1]
- The workflow checks session eligibility, a single owner/lease, prerequisite receipts and frozen source/configuration. Automatic transient retries are capped at three attempts per audited retry epoch; source/dependency failures require repair or restoration, and a reviewed repair can establish a new epoch. Recovery resumes the unfinished stage while retaining successful outputs. Missed-night recovery preserves the original 04:00 deadline and records a separate bounded expiry; it is not permission to rewrite clocks or replay terminal sessions. [W1, W2]
- Diagnose the relevant boundary: old readiness, core failure, OPRA failure, stock-history failure, model failure and missing combined handoff are different conditions. Scheduler result 0 or a model task's “last run” cannot substitute for the corresponding receipt. No recovery was initiated during this inspection. [R1, R2, N1, N2]

## Preserved history and discrepancies

The earlier Ducketz report is retained unchanged. Its September 8 “current deployment” heading and August 19 six-symbol recurring evidence are dated observations, not proof of today's installation. Current Atlas native readback and saved split-workflow execution establish the datastore owner described here. The older `current_start_command` also retains a six-symbol, monolithic 17:05 weekday example; it conflicts with the present eleven-symbol 21:05 responsibility binding. [H1, N1, W2, R1]

Other distinctions: recurring readiness now has its own thread; core COMPLETE precedes OPRA; OPRA includes explicit replay fallback and uses a UTC process-local gate; generic heavy transient retries are not uniformly bounded; the current local supervisor-lock implementation differs from the historical O_EXCL description. The orchestrator defaults and the explicit overnight inline flags are different configuration levels. [S1–S5, W1]

The existing [Atlas scheduled-task chapter](scheduled-tasks.md) preserves both its approximately noon snapshot and 12:58 revision. This evening's native readback agrees with the later active evening windows, not the earlier paused handoff/source table. This chapter neither overwrites those observations nor assigns Atlas state to Scout. [N1, H1]

## Evidence index and remaining unknowns

All source observations are October 10, 19:54–20:02 PDT. Native snapshots are 19:57 PDT; runtime snapshots begin 19:56:49 PDT. Portable source references below identify exact modules/functions; private evidence preserves byte hashes, absolute paths, IDs and receipt locations. Links pinned to Ducketz HEAD describe committed code only.

- **C1 — Coordination:** verified pinned release contract/bootstrap/common-main/GitHub-only/peer-adoption guidance; active pointer and Atlas local profile read first. Exact manifest and local ownership inventory retained privately.
- **S1 — Core orchestration:** [orchestrate.py](https://github.com/jeremysecondstate/ducketz/blob/90704d21801f60426493bd6cc650a7fac38d4f61/datafetching/orchestrate.py), lines 60–215 (CLI), 234–335 (cycle), 358–430 (OPRA), 433–773 (providers/calculations); [main.py](https://github.com/jeremysecondstate/ducketz/blob/90704d21801f60426493bd6cc650a7fac38d4f61/datafetching/main.py), lines 29–129 and 218–363 (component CLI/provider results).
- **S2 — Core publication/consumer barrier:** [loop_a_cycle.py](https://github.com/jeremysecondstate/ducketz/blob/90704d21801f60426493bd6cc650a7fac38d4f61/datafetching/loop_a_cycle.py), lines 75–133, 199–296; `ml/prediction_runtime.py:340–362`; local modified `datafetching/runtime_lock.py:71–202` is separately classified in W1.
- **S3 — Readiness:** [bar_readiness.py](https://github.com/jeremysecondstate/ducketz/blob/90704d21801f60426493bd6cc650a7fac38d4f61/datafetching/bar_readiness.py), lines 93–398 and 457–582; `datafetching/readiness_lane.py:75–195,295–329`; `datafetching/decision_time.py:152–220`.
- **S4 — Provider/input semantics:** `datafetching/symbol_universe.py:13–29`; local watchlist readback; `datafetching/databento_fetch.py:402–407,551–610,926–947,1223–1481`; `datafetching/schwab_fetch.py:283–424`; `options/snapshot.py:615–734`; `datafetching/fred_fetch.py:64–94`; `app/services/databento_retry.py:19–49,89–105`; `ml/rolling_materialization.py:300,463`.
- **S5 — OPRA:** `datafetching/options_history.py:50–52,147–180`; `datafetching/databento_opra_history.py:63,2231–2487`; `datafetching/opra_replay_fallback.py:135–137,187`; orchestrator OPRA command in S1.
- **S6 — Other consumers:** `ml/option_pricing_runtime.py:1217–1246`, `ml/option_pricing/causal.py`; `datafetching/options_runtime.py:359–432`. These are code contracts, not claims that their workers are active.
- **W1 — Local working implementation:** modified `ml/overnight_runtime.py:30–54,412–451,530` and `datafetching/runtime_lock.py`; untracked `ml/nightly_workflow.py` (`_run_native:220–295`, responsibility launch/dispatch), `ml/nightly_dispatch.py:18–48,60–175`, `ml/nightly_stage_repair.py:777` (retry epoch), `tools/nightly_watchdog.py`, `tools/register_nightly_watchdog.ps1`, `docs/development/nightly-operations.md`, `docs/development/nightly-workflow.md`. Private source snapshots distinguish these from HEAD.
- **W2 — Installed binding:** Atlas local workflow configuration and selected coordination-profile fields, matched to the saved run's configuration/symbol binding.
- **N1 — Codex native readback:** fifteen saved automation definitions and read-only native automation database inventory, plus retained run metadata. No datastore automation-run row was retained in that queried history; worker receipts supply its actual completion evidence.
- **N2 — Windows native readback:** `Get-ScheduledTask`, `Get-ScheduledTaskInfo`, exported XML and `Get-TimeZone`; all three Ducketz registrations inspected.
- **R1 — Runtime readback:** selected local preparation state, native catch-up stage report/receipt and log hashes, core current/last-complete records, readiness pointer/receipt, watchdog result, and 24 output-hash checks.
- **R2 — Separate handoff readback:** selected exchange status flags for the same action date and accepted-result receipt binding; private financial contents were not published.
- **H1 — History:** unchanged `docs/loops-system-analysis/loops/loop-a.md`, `docs/datafetch-ml/current_start_command`, older coordination task matrix and the existing Atlas scheduled-task chapter. Historical deployment statements were compared with N1/N2/R1, not adopted as current proof.

Unknowns remain: future wake/run completion; the exact application bytes loaded by any currently running worker; live provider availability/entitlements; current intraday Pricing/Options health; absent historical completion-follow-up registration; and end-to-end trader readiness/execution. The completed workflow's saved hashes and separate handoff flags do not resolve these. This is documentation and read-only verification, with no operating changes.
