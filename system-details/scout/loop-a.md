# Scout Loop A and scheduled tasks

**Observed October 10, 2026, 19:35–19:41 PDT** (`America/Los_Angeles`). This chapter describes Scout's saved configuration and read-only run evidence. Atlas maintains its own chapter and native schedule. A scheduled wake, a launched worker, a complete datastore cycle, and a complete overnight stage are distinct events.

## Evidence used

| Label | Evidence and observation time | What it establishes |
| --- | --- | --- |
| **Checked-in source** | Ducketz source at Scout HEAD `9c5b502`, read October 10, 19:35–19:37 PDT. The Loop A orchestrator, cycle/readiness modules, component CLI, guardian, and September report were clean. | Source behavior at that commit, not present-day task registration. |
| **Local working source** | Modified `ml/overnight_runtime.py` and `datafetching/runtime_lock.py`; locally untracked `ml/nightly_workflow.py`, `ml/nightly_dispatch.py`, and `tools/nightly_watchdog.py`, read October 10, 19:35–19:37 PDT. | The available split-workflow implementation. Its use is corroborated separately by saved configuration and a dated run. |
| **Installed configuration** | Scout's local profile, watchlist, and private nightly-workflow configuration, read October 10, 19:35–19:38 PDT. | This PC is Scout, with eleven local symbols and distinct nightly responsibility owners. The specific symbols and bindings stay private. |
| **Native registration** | Saved Codex automation definitions and Windows Task Scheduler action/trigger readback, October 10, 19:35–19:38 PDT. | Current active/paused state, recurrence, model/effort, and deterministic dispatcher registration. |
| **Run outcome** | Scout cycle, overnight stage, OPRA log, workflow, watchdog, and process readback, October 10, 19:35–19:39 PDT. | A completed October 9 Pacific source-session run and a later idle watchdog wake. Exact receipt identities remain private. |

The verified pinned coordination release identifies this PC as Scout. Its contract separates shared Ducketz behavior from local symbols, task IDs, and operating bindings; Atlas retains live execution ownership. The Ducketz working tree contained substantial other writers' work at observation time, so local modified and untracked source is described as **local working source** throughout. [Scout pinned release/profile verification and Git status, October 10, 19:35–19:37 PDT]

## Purpose and stage order

Loop A provides canonical equity/provider data and calculated features for later loops. Its scheduled Scout path is a bounded datastore catch-up responsibility. The first stage invokes the multi-symbol `datafetching.orchestrate` entry point once; it does not invoke `datafetching.main` as a production loop. `datafetching.main` is a single-symbol provider/normalization component CLI. [Checked-in `datafetching/orchestrate.py:60-103,234-305`; `datafetching/main.py:29-33,104-129`; local working `ml/nightly_workflow.py:220-284` and `ml/overnight_runtime.py:411-445`, read October 10, 19:35–19:37 PDT]

```text
Scout local watchlist + prior canonical data + eligible source session
    -> datastore catch-up responsibility / deterministic dispatcher
    -> one-shot Loop A orchestrator
    -> owner and shared A/B locks -> WRITING cycle
    -> Databento equity bars -> exact-bar readiness attempt
    -> FMP, current FRED, Schwab, SEC -> fundamental/technical/signal features
    -> COMPLETE or FAILED cycle -> bounded OPRA history and catalog audit
    -> stock target history -> datastore catch-up receipt
    -> Stats -> model review and Loop B -> Gameplan and joint handoff
```

Databento operational `EQUS.MINI` bars run first. The separate cold `XNAS.ITCH` archive is provenance and does not silently replace the live operational dataset. Other provider lanes are FMP fundamentals/metadata, current FRED observations, Schwab, and SEC. FRED's current rate context may be used prospectively; it is not historical ALFRED-vintage authority. Per-symbol calculations follow provider capture. The installed bounded command requests all five providers plus inline CME/Options compatibility work, daily OPRA maintenance, and a missing-bar recovery bound. [Checked-in `datafetching/orchestrate.py:458-479,607-760`; `datafetching/databento_fetch.py`; local working `ml/overnight_runtime.py:411-445`, read October 10, 19:35–19:37 PDT]

The one-shot overnight path attempts exact-bar readiness after its Databento one-minute callback. The retained continuous orchestrator instead starts a separate readiness lane before waiting for the shared datastore lock. Readiness can therefore precede the full provider/calculation cycle. The scheduled one-shot command's explicit inline Options mode makes Schwab failures blocking; the continuous default quote-only mode has a different best-effort rule. OPRA's configured due threshold is expressed in **UTC**, so a fixed Pacific-hour interpretation would be inaccurate across daylight-saving changes. [Checked-in `datafetching/orchestrate.py:234-248,286,358-369,469,492-603,649-660,765-773`; `datafetching/readiness_lane.py:37-98,212-328`; local working `ml/overnight_runtime.py:426-444`, read October 10, 19:35–19:37 PDT]

## Inputs, outputs, and downstream use

| Product or control boundary | Meaning | Direct consumer |
| --- | --- | --- |
| Local watchlist and prior canonical provider data | Eleven Scout symbols select the batch scope; same-dataset prior rows support incremental overlap/upsert. | Loop A's provider and calculation stages. |
| Exact-bar readiness | An eligible all-symbol target, exact one-minute close, and checksum-verified readiness receipt. No eligible target means no new readiness publication. | Active Pricing's underlying close; Options Capture's decision clock. |
| Current cycle and last-complete cycle | Current generation is `WRITING`, `COMPLETE`, or `FAILED`; last-complete advances only on zero blocking failures. | Directional Loop B requires the **current** `COMPLETE` cycle under the shared lock and uses its finish time as the causal cutoff. Options can use the last complete regime cutoff. |
| Normalized bars, quotes, fundamentals, filings, macro context, and calculated features | Canonical provider and feature data with source/availability clocks. | Loop B feature construction; Pricing's causal current rate where eligible; Strategy's stock context; later Gameplan stages through predictions. |
| Bounded OPRA history | `ohlcv-1h`, `cbbo-1m`, and `definition` history maintained with valid cursors, provider preflight, and catalog audit. | Strategy-profit training and later Strategy/Gameplan scoring. |
| Datastore catch-up stage result | Loop A's stage result plus subsequent stock target history. | Stats responsibility, then model review/Loop B and Gameplan through the split workflow. |

[Checked-in `datafetching/loop_a_cycle.py:15-18,75-133,198-234`; `datafetching/bar_readiness.py:93-189`; `ml/prediction_runtime.py:340-363`; `ml/option_pricing_runtime.py:1217-1245`; `datafetching/options_runtime.py:359-375,428-449`; `datafetching/options_history.py:49-94,147-180`; local working `ml/nightly_dispatch.py:16-49`, `ml/overnight_runtime.py:30-54,529-532`, read October 10, 19:35–19:37 PDT]

The orchestrator's owner lock prevents a second Loop A owner; its OS-held datastore-cycle lock also gates Loop B. A failed or still-writing current cycle does not become a fresh complete input. Readiness can fail independently, leaving Pricing to its own deadline. OPRA work happens **after** the core cycle closes: a `COMPLETE` cycle record alone does not prove the whole overnight Loop A stage passed. A one-shot OPRA failure can still fail that stage; the stage report and OPRA result must be checked separately. Interrupted workflow dispatch reuses action-date claims and completed receipts under the recorded deadlines. [Checked-in `datafetching/orchestrate.py:234-335`; `datafetching/loop_a_cycle.py:75-133,198-234`; `datafetching/bar_readiness.py:93-189`; local working `ml/overnight_runtime.py:572-714`, `ml/nightly_workflow.py:1104-1144`; October 10, 19:35–19:37 PDT]

## How Scout's scheduled tasks relate to Loop A

All times below are Pacific wall time, following PST/PDT. The Codex model/effort entries are saved native settings. Windows dispatch is deterministic and has no model. A task's **active** status means it can receive a wake; it says nothing by itself about stage success. [Scout Codex saved definitions and Windows registration readback, October 10, 19:35–19:38 PDT]

| Task or dispatcher | Observed state and recurrence | Model / effort | Entry point | Exact relationship |
| --- | --- | --- | --- | --- |
| **Scout DATASTORE CATCH-UP** | **Active**; daily 21:05 and 04:05 fallback | `gpt-6-luna` / low | `ml.nightly_workflow --check`, then `--launch --responsibility datastore --catch-up` | Native Loop A responsibility owner. Launches eligible datastore catch-up; the fallback does not reset the original deadline. |
| **Scout nightly Windows dispatcher** | **Ready**; separate daily 21:05, every-five-minute, and logon triggers | Deterministic | Private PowerShell launcher → `tools.nightly_watchdog` → `ml.nightly_workflow --dispatch` | Selects the next eligible responsibility under shared claims and locks. A successful dispatcher wake is not a completed Loop A run. |
| **Scout GAMEPLAN STATS** | **Active**; daily 21:05 | `gpt-6-luna` / low | `ml.nightly_workflow --launch --responsibility stats --catch-up` | Directly waits on completed datastore catch-up; the watchdog can dispatch it after that receipt. |
| **Scout MODEL REVIEW, TRAINING & PREDICTING** | **Active**; daily 21:05 | `gpt-6-luna` / low for supervision; internal reviewer configured `gpt-6-astra` / high | `ml.nightly_workflow --launch --responsibility model --catch-up` | Downstream of Stats; includes Loop B, without starting another Loop A. |
| **Scout GAMEPLAN** | **Active**; daily 21:05 | `gpt-6-luna` / low | `ml.nightly_workflow --launch --responsibility gameplan --catch-up` | Downstream plan responsibility after accepted predictions. |
| **Scout DUCKETZ DISPLAY** | **Active**; daily 03:00 and 03:35 | `gpt-6-luna` / low | `ml.nightly_workflow --launch --responsibility display --catch-up`; notification helper | Verifies downstream display/handoff and owns dated readiness-risk or missed-confirmation alerts; does not run Loop A. |
| **Scout GAMEPLAN SYNTHESIS** | **Active**; Mon–Fri every 20 minutes 21:00–23:40, with Tue–Sat 00:00, 00:20, 00:40 companion | `gpt-6-astra` / ultra | Codex synthesis prompt and private exchange helper | One logical downstream synthesis owner, consuming completed research packages. |
| **Scout REPO RECONCILIATION** | **Active**; same evening and after-midnight windows | `gpt-6-astra` / ultra | Codex source-reconciliation prompt | Coordinates bounded failure/source repair for the owning responsibility; not a second Loop A owner. |
| **Loops Overnight Gameplan** | **Paused**; retained daily 21:05 definition | `gpt-6-astra` / ultra | Legacy `ml.overnight_runtime --once --scheduled` prompt | Historical monolithic owner; its saved time is not an additional active launch. |
| **Loops Gameplan Weekly Review** | **Paused**; Saturday 09:00 | `gpt-5.6-luna` / medium | Codex weekly-review prompt | Retrospective downstream review. |

No standalone OPRA Codex automation or separate Loop A Windows task action was present in the current saved inventory. The older data-fetch completion follow-up was a distinct bootstrap/progress monitor; no current saved definition was found, so its present registration status is **unknown**, rather than inferred from a historical adoption record. An unrelated scheduled-chat cleanup Windows task does not consume Loop A. The checked-in continuous eight-process launcher and guardian remain diagnosis/compatibility paths; no matching continuous orchestrator or guardian process/service was observed at 19:37–19:38 PDT. [Codex TOML inventory; all Windows task-action query; process/service readback, October 10, 19:35–19:38 PDT; checked-in `docs/loops-system-analysis/LOOP_INVENTORY.md:68-85`, `docs/datafetch-ml/start_all_loops.ps1:275-359`, `ml/system_guardian.py:118-195`]

## What actually completed

The latest saved **core Loop A cycle** checked at 19:35–19:38 PDT belonged to the **October 9 Pacific source session**. It covered Scout's eleven symbols and all five provider lanes, ended `COMPLETE` with zero blocking failures at October 9, 21:16:47 PDT. The separate one-shot overnight Loop A stage exited successfully at 21:43:28 PDT after OPRA maintenance reported **33 of 33 scopes complete, none failed or deferred**. Datastore catch-up then finished after stock target history at 21:46:05 PDT. The local workflow bound this source session to the next action date, October 12. These are observed saved outcomes for that dated run, not evidence of a new Saturday October 10 market-session cycle. [Scout core cycle, overnight stage report/receipt, OPRA log and workflow-state readback, October 10, 19:35–19:39 PDT; exact private references retained locally]

The Windows dispatcher reported a successful wake on October 10 at 19:33:23 PDT, but the watchdog's saved decision was **no dispatch** because it retained the completed session. No matching orchestrator or overnight Python worker was visible at 19:38 PDT. A successful watchdog wake must not be counted as another Loop A completion. [Windows task last-result, watchdog and process readback, October 10, 19:33–19:38 PDT]

## Dated history and unknowns

The checked-in [Ducketz Loop A report](https://github.com/jeremysecondstate/ducketz/blob/9c5b50281169f05032bb0d6d943f761447e70cab/docs/loops-system-analysis/loops/loop-a.md) describes Loop A as a **September 8** daily 21:05 stage of the then-current overnight runtime and records an **August 19** live worker/readiness observation for six symbols. That report is preserved as historical evidence. Scout's October 10 native readback instead shows a split active DATASTORE CATCH-UP owner, a registered watchdog dispatcher, a paused legacy overnight task, and an eleven-symbol completed October 9 source-session run. The report's generic readiness and quote-only Schwab descriptions also have the source-mode distinctions described above. [Dated report `:3-18,165-190`; Scout native and run readback, October 10, 19:35–19:39 PDT]

Future wake execution, future provider/OPRA availability, the next eligible exact-bar readiness, and the current status of an absent historical data-fetch follow-up remain **unknown**. No production workflow was started for this documentation. Source publication, peer installation, and runtime deployment are separate facts. [Read-only inspection scope and native inventory, October 10, 19:35–19:41 PDT]
