# Scout: Directional Loop B

**Observation date: October 10, 2026, Pacific time (`America/Los_Angeles`, PDT / UTC−07:00).** Source was inspected at approximately 20:55–20:58, saved task definitions at 20:55–20:56, and saved runtime evidence at 20:55–20:58. This is Scout's independently observed chapter. Exact symbols, native identifiers, machine paths, task definitions and receipt references are retained in Scout's dated private chapter.

Loop B turns completed, causally available data into calibrated directional forecasts and publishes a verifiable generation for other components to read. On Scout it runs once inside a larger, split nightly workflow. **Loop B, the model-review responsibility, and the complete training/predictions segment are different boundaries.** A scheduler wake, process launch, numerical stage completion, accepted publication and finished downstream workflow each require different evidence. [S1], [W1], [N], [R]

## Evidence and scope

| Layer | Observation and authority | Limits |
| --- | --- | --- |
| Checked-in design | Scout Ducketz HEAD was `9c5b50281169f05032bb0d6d943f761447e70cab`. The existing directional report, prediction runtime, rolling materialization, directional model pipeline and publication reader were clean. Source references below point to that commit where applicable. | Checked-in behavior does not establish today's task registration or a completed run. |
| Local working source | `ml/overnight_runtime.py`, `datafetching/runtime_lock.py`, `ml/nightly_gameplan.py` and several Gameplan readers were modified. The split workflow, dispatcher, model-feedback module and watchdog were locally untracked. | References marked **W** describe the inspected working bytes; they are not claims that those bytes are committed at HEAD. |
| Installed configuration | Verified coordination release `7bd3da6cd674d78a6aafa01e1d4ecf3fbe66384a`, its manifest and all 29 files; local profile, watchlist, nightly configuration and private launcher. | Establishes Scout, its eleven-equity research scope and publication authority. Atlas retains live execution ownership. Deployment authority is separate. |
| Scheduler registration | Current saved Codex definitions, read-only native scheduler metadata and Windows Task Scheduler action/trigger readback. | Active means eligible to wake; nominal recurrence is not a launch/completion guarantee. |
| Observed outcome | Existing stage logs/reports, model review, directional publication, downstream pointers and later supervision/exchange records; recorded hashes were checked without running the application. | The completed run has a different source digest from today's working source. Its success cannot validate later changes. |

[Scout Git, pinned-installation and profile readback, approximately 20:51–20:55 PDT; source inventory 20:55–20:58; native readback **N** and runtime audit **R** below.]

This chapter follows the evidence separation and private/shared convention of [Scout's Loop A chapter](https://github.com/jeremysecondstate/atlas-scout/blob/31913a790057db85dd41f92bc6741ddc40d75dea/system-details/scout/loop-a.md) and [revised scheduled-task chapter](https://github.com/jeremysecondstate/atlas-scout/blob/dc60ac43b959f1a880e243feb69abfa985f5be9c/system-details/scout/scheduled-tasks.md). Those earlier observations are format references, not evidence for this inventory. The original Ducketz report and every peer chapter remain unchanged.

## Purpose, boundaries and stage order

The executable directional owner is `python -m ml.prediction_runtime`. Within one attempt it takes the current Loop A completion gate, materializes rolling features and targets, fits or reuses one model for each horizon, calibrates probabilities, scores retrospective assessment and eligible prospective rows, reconciles matured prior predictions, builds monitoring/display tables, and promotes one immutable directional generation. It does not acquire provider data, capture option chains, fit contract fair values, select the final Strategy portfolio, or place orders. [S1], [S3], [S4]

```text
Loop A datastore catch-up + separately configured stock target history
  -> completed-session Stats -> bounded model review
  -> training/predictions responsibility:
       LOOP B: current-A gate -> features/targets -> fit/reuse + calibration
               -> BACKTEST / eligible LIVE -> evaluation -> B publication
       -> Gameplan evaluation -> Gameplan models/publication -> stock enrichment
  -> local Gameplan/trade planning -> display verification -> local handoff
  -> separate joint synthesis / acceptance / downstream execution controls
```

Scout's installed split workflow has seven steps: `datastore_catchup`, `prepare_stats`, `model_review`, `train_and_plan`, `local_gameplan`, `verify_display`, `local_handoff`. The model responsibility owns review and `train_and_plan`; Loop B is the first numerical stage within that latter segment. Its segment ends after `stock_enrichment_training`. Local trade planning is a subsequent responsibility. Current Scout configuration uses stock-only independent horizons and research-producer mode, so the separately implemented `strategy_profit_training` and `strategy_generation` stages are omitted from this path. [W1], [N], [R]

The actual scheduled chain is a Codex responsibility wake or the registered Windows launcher → `tools.nightly_watchdog` / `ml.nightly_workflow` → `ml.overnight_runtime` → **`ml.prediction_runtime --once`**. The constructed Loop B command selects the local watchlist, Databento, public horizons `1h 4h 1d 1w`, feature profile `loop-a-all-bsgp-active-v3`, logistic models, Platt calibration, one round-trip cost of `0.001`, and **`--require-all-routes`**. The saved completed run confirms these settings. A component CLI alone would not establish the production entry point. ([W1]: `overnight_runtime.py:446–470`; [N]; [R])

The retained prediction CLI can run every 30 minutes at `:06/:36`, and the continuous launcher/guardian can supervise it. That capability is historical/diagnostic in this observation, not Scout's registered nightly cadence. The current saved legacy overnight Codex task is paused, and no separate current Windows Loop B worker registration was found. ([S1]: `:28–32,258–336`; [N])

## Inputs, feature profiles and clocks

Scout selects its own eleven equities through the configured local watchlist. The local profile and watchlist agree; exact membership stays private. Loop B pools this scope by horizon. It reads operational provider and feature products already present in the datastore; upstream acquisition, historical catch-up and daily ALFRED/CME/Options/Pricing work have their own owners. ([S1]: `:476–493`; [S2]; [S4]; [N])

| Input | What Loop B uses and checks | Boundary |
| --- | --- | --- |
| Loop A cycle | Current generation must be `COMPLETE`, with completion time and no recorded blocking failures, under the shared datastore lock. | It does **not** use exact-bar readiness as its gate, or fall back to an older successful cycle. |
| Operational bars and technicals | One compatible adjusted consolidated dataset per required source timeframe, with native one-minute target marks; technical regime, breakout, shape and weekly context. | Missing/ambiguous structural data or inconsistent adjustment basis is an error. History is not fetched here. |
| Other Loop A families | Registered fundamental, lifecycle, signal, quote, energy and SEC features, selected by horizon and joined on their availability clocks. | Valid missing/stale optional observations can become audited nulls; malformed required structure does not become silent success. |
| Options Capture | Receipt-selected committed option-quality surfaces available by the input cutoff; narrowly supported legacy quality fallback when no committed snapshots exist. | This is an input to B, not a B-produced chain. Integrity/quality failure differs from ordinary unavailable evidence. |
| Active Pricing | Verified compact pricing features; coverage and freshness determine admission or a registered non-Pricing baseline. | Naming the BSGP profile does not prove Pricing features were admitted. |
| ALFRED macro | Verified point-in-time readiness and vintage joins for the daily/weekly v3 profile. | Current FRED context is not a substitute for ALFRED history. Readiness failure can abort publication. |
| CME | Causal cross-asset context, using derived or supported normalized evidence. | Missing permitted legacy context differs from partially present, invalid source evidence. |
| Prior Loop B generations | Receipt-proven prior LIVE forecasts and exactly compatible models. | Prior rows/models are not reusable solely because a directory or old pointer exists. |

([S2]: `:182–190,263–295,478–886,939–1034,1483–1646`; [S3]: `:376–501`; [S4]: `:664–711`; [S5])

The requested v3 profile maps `1h`/`4h` to active-v2 feature sets and daily/weekly routes to active-v3 sets. The public `1w` selection expands internally into the aggregate plus `1w-d1` through `1w-d5`. Only registered profiles are accepted; arbitrary feature-column substitution is not part of this runtime contract. Effective feature sets must be read from the manifest. ([S6]: `:387–445,466–480`)

There are several distinct clocks:

- **Input authority:** Loop A's finish time is passed as `input_available_at` and recorded as the causal cutoff. Committed Options and Pricing evidence are explicitly bounded by it.
- **Feature availability:** backward as-of joins use observation availability and horizon-specific freshness. A completed source bar normally requires an additional five-minute processing delay before a decision.
- **Label availability:** a target matures only after its price constituents are available and the target end plus processing delay has passed. Future outcomes cannot be used merely because a historical sample row exists.
- **Actual scoring/publication:** the real runtime clock must still meet the LIVE actionability contract. A receipt's promotion time is different from the sample decision time.

([S1]: `:348–363`; [S2]: `:176–178,648–723,939–1034`; [S6]: `:62`; [S7]: `:280–306`; [S3]: `:620–660,914`)

Freshness is family-specific. Examples from the actual loaders: intraday quotes five minutes; option quality two hours for intraday, one day daily, three days weekly; CME fifteen minutes intraday, one day daily, three days weekly. Pricing feature bounds are two hours/four hours/two days/eight days for `1h/4h/1d/1w`. Macro limits differ by series: 45 days for rates/CPI, 56 for unemployment, 120 for GDP. These are admission limits, not guarantees that current evidence exists. ([S2]: `:69–74`; [S8]: `:83–147`)

One limit deserves explicit wording: the materializer calls `read_verified_macro_evidence(root)` without its optional `available_not_after` parameter. Vintage feature joins remain causal, but the recorded Loop A cutoff alone does not prove that every external authority was frozen at that exact wall-clock instant. The shared A/B lock serializes Loop A writes; it is not a universal snapshot lock over all other producers. ([S2]: `:788–809`; [S9]: `:354–358`; [S5])

Historical boundaries also differ by product. Upstream Databento policy permits 100 calendar days of native minute history, 1,825 days hourly and 2,555 days daily; that policy is not a measured local coverage inventory. Loop B reads existing compatible operational data. The separate downstream independent Gameplan path explicitly combines XNAS archive and operational feature sources, checks overlap/quality and builds its own targets. Do not attribute all of that longer-history training to Loop B or substitute an archive with a different provider/dataset identity silently. ([S10]: `:13–18`; [S2]: `:1483–1646`; [W2]: `nightly_gameplan.py:242–319`)

## Targets, training, calibration and retention

Loop B's positive class means **simple target return minus the configured round-trip cost is strictly positive**. The production `0.001` is a single 0.1% cost deduction. Its calibrated probability is therefore not automatically the separate downstream raw-direction Gameplan probability. ([S7]: `:297–306`; [W1]: `overnight_runtime.py:467–468`; [W2])

| Route | Target and actionability meaning |
| --- | --- |
| `1h` | Next 60 calendar-selected eligible equity minutes; starts at a permitted segment opening/full local hour, with eligible later starts within two hours of information availability. Publish before target start. |
| `4h` | The route name is retained, but its current target is **180 eligible minutes** from the 07:30, 11:30, 15:30 or 19:30 Eastern checkpoint. Publish before target start. It is not a simple four-wall-clock-hour return. |
| `1d` | Next eligible regular-session open-to-close return. Publish before that session opens. |
| `1w`, `1w-d1…d5` | One frozen remaining-week aggregate plus a coherent contiguous set of remaining-session components. Aggregate deadline is the first component close; each component has its own close deadline. Calendar-inapplicable suffixes are distinguished from missing forecasts. |

([S6]: `:159–374`; [S11]: `:53–58`; [S3]: `:1780–1980,4005–4425`)

Intraday sources accept completed extended-hours bars within 04:00–20:00 Eastern. Actionable target minutes use 07:00–09:25 premarket, the regular session and 16:05–20:00 postmarket; early closes use the official core session. Holidays, closures and DST come from the exchange-calendar rules. Native minute opens/closes are used when present; a no-trade minute may use a strictly earlier close, never a future fill, and collection coverage through the target end is required. ([S11]: `:20–22,457–518,815–818`; [S6]: `:181–216`)

Within B, selected symbols are pooled into one model per internal horizon with `include_symbol=False`. Only complete targets train; target starts already used prospectively are excluded. Target clusters are split chronologically into training, calibration, assessment and a closed lockbox, with overlap purging. Minimum cluster allocations are 160/40/40/80 for `1h`, 128/32/32/64 for `4h`, and 252/63/63/126 for daily/weekly. Older eligible training clusters are retained beyond those minimums. ([S4]: `:76–90,167–374,409–416`; [S3]: `:486–501`)

A latest model is reused only when every compatibility field recorded for that route and its model bytes match. Those fields include feature/schema semantics, partitions, training-through boundary, input inventory and preprocessing/runtime metadata. Weekly and intraday routes also bind explicit target/cost specifications; the inspected daily configuration does not separately record that full target/cost contract. This limits the reuse guarantee and is not evidence of a bad saved run. Otherwise a new fit is needed, including both target classes. Calibration has its own partition; Platt/isotonic mappings are constrained to nondecreasing probability orientation. Single-class calibration can fall back to identity/none, and rejected calibration is recorded. Assessment reports raw/calibrated metrics and base-rate comparisons without feeding fitting. **B has no separate champion-superiority promotion gate in `fit_or_reuse_model`.** Directional publication acceptance is an integrity, completeness and timing decision, not proof of predictive superiority. ([S4]: `:432–552,566–819`)

The wider workflow's Codex model review is separate. It consumes the exact completed Stats evidence, records a named reviewer and bounded `KEEP_CURRENT` or candidate decisions, and binds training-policy hashes. It may not change features, targets, splits, seeds or promotion gates. The inspected overnight wrapper requires reviewed feedback before Stats-first training, but that proposal is passed to the later `ml.nightly_gameplan` stage; it is not an argument to Loop B's fixed logistic command. Downstream Gameplan builds independent stock groups, selects candidates, applies its own promotion gates and can retain a compatible champion. Stock enrichment is another stage. ([W1]: `overnight_runtime.py:399–405,446–470,510,608–610`; [W2]: `gameplan_model_feedback.py:26–42,99–139,223–300`; `nightly_gameplan.py:298–319,396–442`)

B retains immutable generations, exactly compatible model reuse, still-active ordinary LIVE forecasts and coherent frozen weekly bundles. Mature outcomes are reconciled without exposing the closed lockbox; lockbox targets are redacted from public sample/evaluation outputs. These meanings of retention differ from downstream champion retention. No fixed model/run garbage-collection period was established in the inspected B component. ([S3]: `:620–770,2461–2483,2715–3099`; [S4]; [W2])

## Locks, publication and failure handling

The executable singleton lock is `.duckets-ml-prediction-runtime.lock` (the spelling is part of the current code). The local modified runtime-lock helper verifies PID and process-birth identity, only reclaims positively stale ownership and fails closed on uncertain ownership. Every B cycle then holds Loop A's OS file lock for the entire computation/publication call. That OS lock releases on process exit; the persistent lock file is not itself a live-owner signal. ([S1]: `:258–259,348–364,534–539`; [W3]; [S5]: `:198–271`)

`require_complete_loop_a_cycle` reads the **current** cycle. Missing, `WRITING` or `FAILED` state aborts B even if `.ducketz-loop-a-complete.json` still describes an older success. The helper validates completion metadata but has no maximum-age or requested-symbol-superset check and does not checksum every source product. Thus a current, old `COMPLETE` record is not rejected there solely for age; source contracts and later actionability checks still matter. Exact-bar readiness used by Pricing/Options is a different control artifact and cannot replace this B gate. ([S5]: `:37–53,136–167`; [S1]: `:348–363`)

| B output | Meaning and acceptance boundary |
| --- | --- |
| Immutable `ml/runs/<generation>/samples.parquet` | Features, decision/availability clocks, target geometry; lockbox outcomes redacted. |
| `predictions.parquet` | BACKTEST and eligible LIVE rows with raw/calibrated probability, model/calibration identity and target/actionability clocks. |
| `evaluations.parquet`, `monitoring.parquet`, `intelligence.parquet` | Matured-outcome evidence, route/model/feature monitoring and consolidated display data. |
| `sequence-encoder-shadow.json` | A shadow assessment sidecar; does not alter B's probabilities or decision authority. |
| Model generations | Estimator, calibrator, compatibility metadata and assessment evidence; a fitted model can exist before B publication succeeds. |
| `manifest.json`, `publication.json`, `ml/latest/run.json` | Exact input/output inventory and configuration, verified publication receipt, then one atomically replaced current pointer. These together select authority. |
| Compatibility mirrors | `ml/latest/*.parquet` and `ml-intelligence/latest/rolling-predictions.parquet`; convenient readers' paths, not independent generation authority. |

([S3]: `:734–945,999–1157`; [S4]: `:525–552`; [S12]: `:12–15,189–245`; [S13]: `:222–256`)

The reader verifies the immutable run manifest and output hashes, the receipt's path/timestamp/manifest hash, and the pointer's exact manifest/receipt record. A prepared receipt alone does not establish that a run entered the authoritative publication chain. Promotion checks concurrent pointer changes and actual LIVE deadlines; failure leaves the previous authority, with attempted mirror rollback. An unchanged older pointer may still be valid historically while its forecasts have become operationally stale. ([S12]: `:66–245`; [S3]: `:999–1157,2834–2843`)

Current code first prunes fresh LIVE rows whose deadlines have expired, carries eligible receipt-proven prior rows, and then enforces the remaining deadlines and route requirements. Empty output or a required missing/error route fails the production attempt. The component's permissive default is overridden by Scout's `--require-all-routes`. Optional Pricing coverage/freshness failure can select the registered baseline; corrupted Pricing evidence or invalid macro readiness is a contract failure. A weekly suffix is N/A only when a coherent calendar-valid bundle proves it; absence/ambiguity cannot be labeled healthy. ([S2]; [S3]: `:620–732,4005–4425`; [W1])

There are two recovery layers. The recurring CLI permits at most one delayed retry for classified transient failures; explicit failed Loop A, integrity and deadline errors are not automatically retryable. Its immediate startup recovery uses absent or verified ≥35-minute-old authority, while corrupt authority fails closed. **`--once` returns after one attempt before that recurring retry logic.** The installed workflow provides separate same-stage retry/resume: checksum-valid completed segments are reused, interrupted segments retain their evidence, and failed segments resume under workflow/global claims, the overnight lock and original source/configuration bindings. ([S1]: `:303–334,391–461`; [W1]: `nightly_workflow.py:170–183,251–258,930–969`; [W4])

Workflow recovery is bounded: configured maximum three transient attempts, five-minute backoff, and an immutable original 04:00 Pacific action-date deadline. The missed-night mechanism only opens on the exact action session between 04:00 and 17:00, bounded to seven hours or 17:00, whichever is earlier. Source defects and unavailable dependencies require the retained repair owner rather than endless retries. Separately authorized continuation/repaired-source records preserve the original identity and deadline; a fallback wake does not reset them. These are source/configuration capabilities, not evidence that recovery was exercised during this review. ([W4]: `nightly_dispatch.py:31–36,52–96,135–184`; [W1]: `nightly_workflow.py:599–644,899–921`; [N])

## Downstream consumers and feedback

| Consumer | Actual relationship to Loop B |
| --- | --- |
| Strategy | Directly reads the verified B samples, LIVE probabilities, configured symbols and cutoff, then publishes a separate Strategy generation. Strategy training/scoring are omitted from Scout's current stock-only nightly segment. |
| Gameplan | Reads B's verified publication and features, then builds its own stock targets, models, evaluations and frozen forecasts. B success is a prerequisite, not accepted Gameplan completion. |
| Pricing | Supplies gated features to B. No direct B model/probability input to contract-price inference was found. There is optional later Strategy-outcome eligibility feedback whose lineage can include B; this is distinct from pricing inference. |
| Options Capture | Supplies committed quality surfaces to B. No direct B-to-capture artifact dependency was found in the inspected paths; shared timing is not proof of a dependency. |
| ALFRED | Uses B's sample decision grid for asynchronous historical-coverage planning. A registered decision-only bootstrap path also exists, so a full B fit is not the only possible initial grid authority. |
| Rolling Forecasts display | Defaults to a nightly Gameplan pointer when present; otherwise resolves B intelligence through the authoritative reader. A configured path override has priority. Source behavior does not prove a live UI render. |
| Trader paths | Legacy stock-trader inputs can directly read actionable verified B LIVE signals. Current independent Gameplan paths consume accepted/frozen plans through separate readers. Scout's observed role is research/synthesis; no B publication grants live execution or changes the human's trader controls. |

([S14]: `:85–135`; [W2]: `nightly_gameplan.py:206–237`; [S15]: `:920–950`; [S16]: `:823–855`; [S2]: `:150–156,646–709`; [S9]; [S17]: `:321–350`; [S18]: `:30–69`; [W5]; [N])

## Scout task-to-Loop-B relationship

These are **current local saved definitions**, not copied peer schedules. Pacific nominal times follow PST/PDT; date selection uses the XNYS source session and next action date. Saved native metadata can apply launch jitter, so a nominal 21:05 wake is not an assertion of an exact 21:05 start. The internal reviewer model is separate from its lightweight scheduled supervisor. ([N]; [W4])

| Task or deterministic dispatcher | Observed state and nominal Pacific recurrence | Model / effort | Entry point and exact role |
| --- | --- | --- | --- |
| Scout DATASTORE CATCH-UP | **Active**; daily 21:05 and 04:05 fallback | `gpt-6-luna` / low | `ml.nightly_workflow --check`, then `--launch --responsibility datastore --catch-up`; supplies Loop A/target-history prerequisites, does not itself run B. |
| Scout GAMEPLAN STATS | **Active**; daily 21:05 | `gpt-6-luna` / low | `--launch --responsibility stats --catch-up`; completed datastore → Stats evidence used by review. |
| Scout MODEL REVIEW, TRAINING & PREDICTING | **Active**; daily 21:05 | Supervisor `gpt-6-luna` / low; bounded internal reviewer `gpt-6-astra` / high, 1,800-second configured limit | `--launch --responsibility model --catch-up`; owns separate model review, then the numerical segment beginning with B and ending with stock enrichment. |
| Scout nightly Windows dispatcher | **Ready**, enabled; daily 21:05, every five minutes, and logon triggers | Deterministic; no model | Private PowerShell launcher → `tools.nightly_watchdog` → workflow dispatch. Chooses the next eligible owner; honors locks, claims and terminal receipts. A result of zero proves only that wake's process result. |
| Scout GAMEPLAN | **Active**; daily 21:05 | `gpt-6-luna` / low | `--launch --responsibility gameplan --catch-up`; separate local planning after the pinned accepted training publication. |
| Scout DUCKETZ DISPLAY | **Active**; daily 03:00 and 03:35 | `gpt-6-luna` / low | `ml.nightly_workflow --launch --responsibility display --catch-up` and `tools.nightly_notifications`; verifies downstream display/handoff and owns dated readiness-risk/missed-confirmation alerts. |
| Scout GAMEPLAN SYNTHESIS + after-midnight companion | **Active**; Mon–Fri 21:00–23:40 every 20 minutes; Tue–Sat 00:00, 00:20, 00:40 | `gpt-6-astra` / ultra | `tools.nightly_exchange` plus inspect-only pinned supervision helper. One logical downstream synthesis owner for completed research packages, with preserved claims/continuity and bounded repair delegation. Does not redefine B. |
| Scout REPO RECONCILIATION + after-midnight companion | **Active**; same evening and after-midnight windows | `gpt-6-astra` / ultra | Saved reconciliation procedure and pinned `nightly_supervision.py --inspect/--record` helper. Retained source/dependency repair and continuation owner; not a second numerical B writer. |
| Loops Overnight Gameplan | **Paused**; retained daily 21:05 definition | `gpt-6-astra` / ultra | Historical monolithic `ml.overnight_runtime --once --scheduled` owner. Its recurrence is not an additional active pipeline. |
| Loops Gameplan Weekly Review | **Paused**; Saturday 09:00 | `gpt-5.6-luna` / medium | `ml.gameplan_evaluation` and saved-reader verification; retrospective downstream review, not the `1w` B route or a B launcher. |

([N]: saved Codex TOMLs/native metadata and Windows action/trigger readback, 20:55–20:56 PDT; [W1]/[W4] for dispatcher-to-stage routing.)

The current inventory contains 13 Ducketz Codex definitions, all cron: nine active and four paused, including two paused Hyperliquid definitions outside B. No current temporary recovery heartbeat, standalone B automation or Loops operations-watch definition was present. The historical operations watch was a cron monitor; completion follow-ups were separate heartbeats. Mapped data-fetch completion/operations-watch IDs and earlier recovery follow-ups remain **historical or unregistered in this inventory**, not assumed active. The old data-fetch completion follow-up tracked separate bootstrap completion; it was not the recurring B owner. The Windows completed-chat cleanup task only maintains eligible chats and has no B numerical/acceptance role. [N]

## What the saved run establishes

The latest relevant saved source session is **Friday, October 9**, with **Monday, October 12** as action date. Reading a Saturday scheduler result as a new Saturday market-session run would be incorrect. All times in the following table are actual saved event times converted to PDT; observation was October 10, approximately 20:55–20:58. [R]

| Evidence level | Saved outcome | What was verified / what it does not prove |
| --- | --- | --- |
| Loop A prerequisite | October 9 core cycle finished 21:16:47; datastore segment finished 21:46:05 after history. | Current and last-complete records agree; B manifest cutoff equals that core finish time. Full datastore completion and core cycle remain separate. |
| Stats and model review | Stats completed about 21:48; reviewed output completed 21:53:38, before training. | All four reviewed groups said `KEEP_CURRENT`: diagnostics had zero saved forecasts/completed observations and null accuracy/Brier evidence. Bound review bytes were checked; this is not a fit or empirically demonstrated improvement. |
| Loop B computation and publication | Began about 21:53:39; promoted **22:02:13**. Log records nine trained horizon models, zero reused, 99 fresh LIVE rows. | Current pointer, receipt, manifest and all six declared B output hashes agree. Manifest records 7,117 BACKTEST + 99 fresh LIVE = 7,216 prediction rows, 33 actionable ordinary routes, no route errors. These were publication-time counts, not present-time actionability. |
| Effective feature admission | BSGP v3 was requested; every Pricing feature route was quarantined to its registered baseline. | Effective sets were `loop-a-all-v1` for intraday and `loop-a-all-v3` for daily/weekly. Successful B publication did not establish admitted Pricing surfaces. |
| Larger training/predictions segment | Finished **22:14:34**, after Gameplan evaluation, separate Gameplan publication and stock enrichment. | Native report/log hashes and downstream publication bindings were checked. Option Strategy stages were omitted. B's earlier completion was not segment completion. |
| Local planning/display/handoff | Planning segment finished 22:23:25; seven local workflow steps were complete by **22:28:28**. | Retained preparation state says `LOCAL_COMPLETE_PEER_SETUP_PENDING`; that earlier local terminal record alone does not establish joint acceptance. |
| Later downstream completion | October 10 **08:59:10** supervision record says `FINAL_VERIFIED`, with exchange `COMPLETE`, joint/peer/UI readiness true. | Separate saved exchange verification resolves the earlier peer-pending stage. Execution remains unauthorized by that result; no activation change or orders are recorded. This is saved acceptance evidence, not a new live display/trader test. |
| Later scheduler wake | October 10 20:53:23 Windows result 0; watchdog decision one second later was `dispatch=false`. | The watchdog retained the completed source/action-date pair. It did not run B again. |

([R]: direct stored-file/hash audit; [N]: Windows/watchdog readback. Exact run identities, paths and hashes remain private.)

The runtime audit passed **83 of 83 direct SHA-256 comparisons across 68 distinct retained files**, covering bound workflow outputs, native reports/logs, B publication/output files and compatibility copies, model-review evidence, selected downstream artifacts and saved display/exchange evidence. The 381 upstream input entries were inventoried but not rehashed; the nine B model bundles were not individually audited. No fitted model was loaded or executed. Retained exchange packet files were hashed without parsing or copying their contents; canonical packet digests and the complete semantic acceptance validator were not rerun. The local synthesis pointer's earlier `JOINT_READY_LOCAL` record and later exchange verification remain separate evidence layers. These checks establish retained byte integrity and recorded-reference agreement within that scope. [R]

**The completed run does not match current working source.** Both identify HEAD `9c5b502…`, but the recorded aggregate source digest begins `edd8831f6c9a…` and the inspected current digest begins `42fa58e6a243…`. The workflow algorithm hashes all 367 current Python files under `ml`, `datafetching` and `app`, including untracked files there; it excludes tools, tests, configuration and native bindings. Consequently even that identity is not a complete installed-environment attestation, and matching HEAD alone is insufficient. The private audit retains full digests and file hashes. ([W1]: `nightly_workflow.py:154–161`; [R])

## Preserved history, discrepancies and unknowns

The existing [Directional Loop B report], [H] has a September 4 one-shot-overnight header, older recurring `:06/:36` and standalone-monitor text, and August 19 live-worker/publication observations. Those observations are preserved as history. Older Scout saved overnight reports likewise show monolithic segments, later failed stages and resumed tails; a tail receipt marked `COMPLETE` cannot retroactively certify an entire original attempt. Current split native definitions and the correlated October 9/12 evidence above govern this Scout snapshot. ([H]; [R]; [N])

The older report's current-A gate and separate Strategy ownership still agree with source. Its permissive-route description needs the production `--require-all-routes` qualification; its blanket deadline-failure wording needs the expired-row pruning step; lock ownership is now birth-aware locally. The sequence shadow sidecar and decision-only macro bootstrap also need recognition. Downstream independent Gameplan review, raw-direction targets, candidate promotion and champion retention must stay outside B's scope. (sources S1–S13 and W1–W3 in the evidence register below)

The scheduled-task chapter's October 10 afternoon revision matches the current evening/after-midnight supervision window. Its preserved earlier morning pause/count is labeled history. Temporary recovery and separate completion follow-ups were not converted into permanent B owners for this report. ([N]; Scout scheduled-task history)

The local working nightly-operations runbook still describes five-minute synthesis/reconciliation and a 01:25 ordinary review. Current native definitions instead specify the twenty-minute evening window and first eligible 21:00 reconciliation. Older display-prompt references to five-minute synthesis do not establish extra overnight synthesis wakes. The Windows watchdog's five-minute cadence remains current. ([W4]: `docs/development/nightly-operations.md:26–38,151–165`; [N])

Still **unknown or not established here**: future wake/provider availability; a future run on the currently modified source; today's actionability or accuracy of every saved forecast; live UI rendering; loaded worker source; full current datastore coverage; every external feature authority's exact cutoff freeze; a fixed B artifact-deletion policy; and any absent native task outside the inspected saved inventory. No production workflow, provider/broker call, training, prediction generation, schedule change, restart, deployment or trade was performed for this chapter. Documentation publication, main integration, peer installation and runtime deployment remain separate facts.

## Source and native evidence register

**S references** below identify clean checked-in paths read at approximately 20:55–20:58 PDT on October 10. Line references throughout this chapter identify inspected code, not execution proof. **W** references identify local working bytes and were hashed privately. **N/R** are observed native/runtime evidence, not checked-in design.

- **S1:** `ml/prediction_runtime.py` — entry point, command options, locks, current-A gate and retry.
- **S2:** `ml/rolling_materialization.py` — data loading, causal feature families and source contracts.
- **S3:** `ml/runtime_pipeline.py` — route/model orchestration, LIVE retention, outputs and publication.
- **S4:** `ml/model_runtime.py` — target partitions, fit/reuse, calibration and assessment.
- **S5:** `datafetching/loop_a_cycle.py` — current versus last-complete state and shared OS lock.
- **S6/S7/S11:** horizon specifications, rolling samples and exchange-calendar target rules.
- **S8/S9/S10:** family freshness, ALFRED readiness and upstream history policy.
- **S12/S13:** current-publication verification and sequence shadow consumer.
- **S14–S18:** Strategy, Pricing feedback lineage, display and legacy trader consumers.
- **W1:** modified `ml/overnight_runtime.py:30–53,399–470,510,608–620`; untracked `ml/nightly_workflow.py:154–183,220–284,296–356,581–644,899–969` — split production chain and receipt/source guards.
- **W2:** modified `ml/nightly_gameplan.py:172–177,201–319,396–442`; untracked `ml/gameplan_model_feedback.py:26–42,99–139,223–300`; modified champion/Stats dependencies — separate review/training/promotion contracts.
- **W3:** modified `datafetching/runtime_lock.py:70–110,174–202` — birth-aware runtime ownership.
- **W4:** untracked `ml/nightly_dispatch.py:18–49,52–96,135–184`, `tools/nightly_watchdog.py`, and nightly runbooks — deterministic responsibility and recovery rules.
- **W5:** modified `ml/stock_trader/independent_runtime.py:233–255,322,400–433` and Gameplan readers — accepted-plan consumer path, not observed execution.
- **N:** Scout's current saved automation TOMLs and native metadata, Windows task actions/triggers/results, private launcher, local watchlist/profile and nightly configuration, read 20:55–20:56 PDT. Exact private hashes/readback retained locally.
- **R:** read-only audit at 20:55–20:58 PDT of the latest source-session/action-date state, stage receipts/logs, directional current pointer/manifest/publication, feedback evidence and later supervision/exchange summaries; 83 direct recorded-hash checks across 68 distinct files. Private audit contains the exact references and limitations.
- **H:** original dated directional report at Scout's checked-in HEAD, preserved without edits.

[S1]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/prediction_runtime.py
[S2]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/rolling_materialization.py
[S3]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/runtime_pipeline.py
[S4]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/model_runtime.py
[S5]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/datafetching/loop_a_cycle.py
[S6]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/horizons.py
[S7]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/rolling_samples.py
[S8]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/datasets/families.py
[S9]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/datafetching/fred_alfred_readiness.py
[S10]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/datafetching/databento_history_policy.py
[S11]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/calendars.py
[S12]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/current_publication.py
[S13]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/sequence_encoder/consumer.py
[S14]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/strategy_runtime.py
[S15]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/option_pricing_runtime.py
[S16]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/option_pricing/strategy_outcomes.py
[S17]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/app/ui/rolling_forecast_data.py
[S18]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/ml/stock_trader/inputs.py
[W1]: #source-and-native-evidence-register
[W2]: #source-and-native-evidence-register
[W3]: #source-and-native-evidence-register
[W4]: #source-and-native-evidence-register
[W5]: #source-and-native-evidence-register
[N]: #source-and-native-evidence-register
[R]: #source-and-native-evidence-register
[H]: https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/docs/loops-system-analysis/loops/directional-loop-b.md
