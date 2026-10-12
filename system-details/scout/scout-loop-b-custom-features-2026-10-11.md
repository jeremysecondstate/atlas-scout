# Scout Loop B custom-feature research — October 11, 2026

**Private local report. No production adoption.** This is Scout's completed, bounded implementation and evaluation, using Scout's accepted generation and local data. It is a companion to the [historical Loop B chapter](C:/atlas-scout/system-details/scout/scout-loop-b-2026-10-10.md), whose earlier observations remain unchanged. Times are explicitly UTC unless described as Pacific; the work date is October 11 in America/Los_Angeles.

## Finding and disposition

None of the four predeclared candidate profiles passed the improvement rule on any evaluated horizon. The experiment completed **105 successful fits**: seven daily/weekly routes × three temporal folds × five matched models. Independent verification recomputed log loss, Brier score and calibration diagnostics, checked exact membership and all purges, and reverified frozen source/input hashes. There were no failed fits or post-result parameter/feature revisions.

The strongest favorable result was daily **range activity**, with log loss 0.697839 → 0.696930 (delta −0.000909) and Brier 0.251933 → 0.251495. The log-loss improvement is smaller than the predeclared 0.005 threshold. Its multiplicity-corrected upper bootstrap bound is +0.000839, so evidence does not establish an incremental gain. The path family and combined profile worsen mean log loss and Brier on all seven evaluated routes. High feature coverage did not translate into accepted predictive improvement.

| Candidate | Overall disposition for this fixed research profile | Evidence and interpretation |
| --- | --- | --- |
| Same-slot normalized range surprise | **Inconclusive** | Small favorable point estimates on six routes, unfavorable on d2; no route meets effect-size and corrected-uncertainty gates. Not retained as a demonstrated improvement. |
| Downside variation share | **Reject the tested path family** | Evaluated jointly with concentration; path loss worsened on every route. This does not isolate this scalar's individual effect. |
| Movement concentration | **Reject the tested path family** | Same joint ablation evidence; no unsupported attribution of harm to either individual scalar. |
| Signed return × persistence | **Inconclusive overall** | Modest favorable weekly/d3/d5 point estimates, unfavorable other routes; no accepted result. Per-route rejection/inconclusive labels appear below. |
| Combined four-feature profile | **Reject** | Worse log loss and Brier on every evaluated route. |
| Any hourly/4h profile | **Insufficient evidence** | No eligible intraday labels remain after the common protected-period exclusion. No intraday models fitted. |

“Reject” means do not advance this tested profile on this evidence; it is not proof of universal harm. There are 19 reject and nine inconclusive evaluated contrasts, zero retained contrasts. The two intraday routes add explicit no-fit conclusions. The two path scalars were deliberately grouped, keeping the search bounded; individual scalar ablations were not attempted.

## This PC, ownership and accepted evidence

The installed profile identifies **Scout / pc-new**, America/Los_Angeles, checkout `C:/dev/ducketz`, DATASTORE `C:/DATASTORE`, and local symbols DOCU, DBX, SDGR, QBTS, PYPL, GLOB, OUST, ABCL, MRNA, RR and PDYN. Reviewed source base: `9c5b50281169f05032bb0d6d943f761447e70cab`. The initial ownership receipt records 184 pre-existing changed/untracked file hashes. Only five new shared source/test/documentation paths were owned; all experimental data/model/evidence outputs are under the dedicated private directory.

The active coordination release is `7bd3da6cd674d78a6aafa01e1d4ecf3fbe66384a`, manifest SHA `e4d98044a79726ec44eb81b94997ac315af64cc500ef76d738ad0f34db471420`. All 29 pinned files matched. The stricter CLI check initially rejected three pre-existing bytecode cache files; they were preserved in `coordination-bytecode-quarantine/` with hashes, then CLI verification passed. No pinned file, scheduler binding or durable queue was replaced.

The current accepted pointer still selects **20261010T045339.610934Z**. Run-manifest SHA is `a761a4d8d75bb7691b288d7ad0d562852381b462e1c2a446940f88ed288199e6`; published samples SHA is `8f3ca4eefb98c687ddc3e9df5b118b6a0c39be34017486a824a4d0a9f98b0d2a`. The accepted target is saved `target_cost_adjusted_positive`: one exactly when target simple return minus the saved 0.001 one-time round-trip cost is strictly positive. Labels were reused, not redefined or reconstructed from minute prices. In particular, the saved route called `4h` is **180 eligible target minutes with four checkpoint starts**, not a generic four-hour elapsed return.

The current metadata audit independently reconciled all **108 recorded partition checks** and all **292,900** published identities/row positions against the previous reconstruction. Model name/version paths locate manifests but the accepted directional receipt does not cryptographically pin those model manifests. Reconciled membership remains **retrospective reconstruction, not an original saved training-ID receipt**. This run pins current bytes and exact IDs for a new research cohort and does not claim reproduction of an original fit.

## Protected periods and research design

The frozen shield is **2025-09-29 13:30 UTC (06:30 Pacific)**, the earliest calibration/assessment/lockbox target start across all nine production routes. Eligibility requires original reconstructed training membership and label availability strictly before this common shield. This excludes 251,451 published rows and admits 41,449 research row identities across seven related routes. Counts across horizons are not independent observations or additional history.

Scout's intraday minute-price labels begin in 2026. Although some are intraday production-training rows, they overlap daily/weekly protected outcomes. They were excluded before outcome reads. No 2026 native bars were returned for candidate calculation. Frozen original calibration, assessment, reserved/live and lockbox exclusions were not moved forward. Sealed rows are absent from the published samples file; no sealed artifact was opened, no removed outcomes reconstructed and no protected outcomes scored. Arrow filtering returned only exact approved IDs; physical column decoding inside a shared row group is not claimed to be row-level disk isolation.

The [predeclared design](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/predeclared-design.json) predates outcome inspection. The initial half of chronological target dates supplies training, followed by three expanding validation segments. All symbols and decisions with a shared target start remain together. Training target ends **and label availability** must strictly precede the earliest validation decision. Validation outcomes crossing the next fold's first decision are purged. Complete frozen fold IDs and purge receipts are in each horizon's specification.

Baseline, baseline+activity, baseline+path, baseline+interaction and baseline+all use the same rows/folds/targets and C=1 logistic family. No hyperparameter search, calibration fitting or additional indicator sweep occurred. Saved baseline semantic transformations are fitted using each fold's training rows; finite availability (20% minimum), constant/duplicate admission, median imputation, 0.25%/99.75% clipping and standard scaling are also training-only. Model fitting weights average decisions within symbol and then symbols within target start. Scoring follows the same hierarchy. Preprocessing statistics themselves use training rows rather than cluster weights.

This is a **matched research baseline**, not a claim to reproduce the production estimator: standard scaling replaces production RobustScaler, entirely empty/constant/duplicate or low-coverage columns are excluded by the research admission rule, and no missing-indicator expansion or production calibrator is fitted. These settings are held constant across variants. No legacy fitted object was deserialized.

The primary metric is target-cluster mean log loss. Acceptance requires an absolute reduction of at least 0.005; three successful folds; improvement in at least two folds and more than half the symbols; at least forty OOS dates; no Brier deterioration; and a corrected upper paired log-loss bound below zero. The uncertainty method resamples paired blocks of five consecutive observed target dates, 4,000 draws, fixed seed 20261011. Bonferroni uses 36 predeclared comparisons, retaining the full nine-route budget despite two no-fit routes. Log loss/Brier are proper probability scores; fixed ten-bin reliability/ECE is descriptive calibration evidence, not a fitted correction.

## Feature definitions and availability


The semantic version is `native-ohlcv-research-v1`. All four values are
dimensionless and apply to hourly or daily native bars. Daily measurements may
support daily and weekly target routes; the saved target definition determines
the experiment, not a horizon's display name.

| Family / column | Formula | Hypothesis and overlap |
| --- | --- | --- |
| activity: `rx_activity__slot_range_log_ratio` | `log(q / median(previous comparable q))`, where `q=(high-low)/close`; previous 20 scheduled sessions, at least 10 valid native comparators | Unusual range relative to the same session slot may distinguish ordinary seasonal movement from unusual activity. Existing breakout logic already normalizes volume by session slot, so another volume ratio is omitted. |
| path: `rx_path__downside_variation_share_10` | `sum(min(r,0)^2)/sum(r^2)`, for 10 close-to-close log returns | Measures downside concentration of realized variation, beyond overall volatility and signed momentum. |
| path: `rx_path__movement_concentration_10` | `sum(abs(r)^2)/sum(abs(r))^2`, for the same 10 returns | Distinguishes movement spread across bars from a small number of shocks; ranges from 0.1 to 1 when defined. |
| interaction: `rx_interaction__return_persistence_10` | `sum(r)*abs(mean(sign(r)))`, for the same 10 returns | A signed move with persistent return signs may behave differently from oscillating movement. Cumulative return overlaps existing momentum; unsigned persistence supplies the explicit interaction. |

These are underlying measurements, not a combined bullishness score. No
calendar/target-window context features are admitted in this initial design.
Target/future/label/outcome feature names remain prohibited by the harness.

## Source and availability contract

Call `calculate_research_ohlcv_features(bars, symbol=..., timeframe="1h"|"1d")`.
Inputs are `timestamp` (or `bar_timestamp`), OHLCV, and explicit boolean
`is_native`. Optional `bar_complete` also requires boolean evidence. Unknown,
derived, carried-price and incomplete bars never contribute. Provenance must
come from reviewed source metadata; absence of a derived flag does not prove a
bar native. The caller must review splits and other price adjustments before
calculation. Uniform price rebasing is invariant; an unadjusted split within a
window is not. Do not infer corporate actions using future price observations.

Hourly timestamps denote interval starts. A value becomes available one hour
after that timestamp plus five minutes. Daily timestamps are UTC-midnight
session-date labels, available at the official XNYS session close plus five
minutes. Supplied bar-end timestamps are checked against this policy. The
caller must join the exact source bar and require `available_at <= decision_at`;
there is no stale as-of carry. Inputs with invalid OHLC ordering, nonpositive
prices, nonfinite values or negative volume are ineligible. A native zero-volume
bar is not automatically classified as carried.

The pinned `exchange_calendars` package supplies XNYS holidays, early closes,
and DST. Hourly activity comparators match New York clock slot, session
composition (including the hour crossing the regular open), and regular-session
duration. Normal sessions support whole-hour slots from 04:00 through 19:00
Eastern. Short sessions conservatively use only hours wholly within the regular
session. Daily comparators match regular-session duration. Both use only earlier
sessions and never fall back to another slot or session type. Early-close
activity is usually missing because ten comparable short sessions do not occur
within the last twenty sessions.

Hourly path windows require eleven consecutive scheduled full regular hours
(normally starts 10:00 through 15:00 Eastern); daily paths require eleven
consecutive exchange sessions. Scheduled overnight/weekend/holiday closures are
skipped. A missing scheduled native bar breaks the window. Across-session
returns include the overnight move; there is no inference about movement inside
a bar. Extended-session hourly rows have no path measurement. No synthetic rows
or forward/backward price filling are used. Insufficient warm-up and zero
denominators yield missing values. The complete contract is returned by
`semantic_contract()`.


## Coverage, model comparisons and temporal stability

All three path/interaction measurements are finite on every research row. Range activity is approximately 98.94% finite. Each route has 63 missing activity values: 62 shortened-session rows without ten matching-duration comparators in the twenty-session window, plus one native zero-range PDYN bar on July 26, 2024. This is the declared denominator/warm-up policy, not a fill or stale join. None of the four candidate columns is constant, empty or an exact duplicate of another admitted measurement. Some baseline contract columns are entirely empty (61/139 daily, 54/132 weekly); this is reported separately and does not constitute candidate predictive value.

The displayed bootstrap endpoints each use tail probability 0.05/36. Acceptance uses the upper **one-sided** bound; the pair is not labelled a 95% simultaneous two-sided interval. With 4,000 draws only about six draws populate either extreme tail, so tail precision is limited. Dependence beyond five observed dates, common market exposure and overlapping weekly targets remain substantive limitations.

## Cohort and fold summary


| Horizon | Research rows | Target starts | OOS rows | OOS target starts | OOS dates | Folds | Successful fits |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1h | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4h | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1d | 5,937 | 578 | 3,179 | 289 | 289 | 3 | 15 |
| 1w | 5,937 | 578 | 3,146 | 286 | 286 | 3 | 15 |
| 1w-d1 | 5,937 | 578 | 3,179 | 289 | 289 | 3 | 15 |
| 1w-d2 | 5,926 | 577 | 3,157 | 287 | 287 | 3 | 15 |
| 1w-d3 | 5,915 | 576 | 3,124 | 284 | 284 | 3 | 15 |
| 1w-d4 | 5,904 | 575 | 3,102 | 282 | 282 | 3 | 15 |
| 1w-d5 | 5,893 | 574 | 3,069 | 279 | 279 | 3 | 15 |

## Matched out-of-sample comparisons

| Horizon | Variant | Log loss | Δ log loss | Brier | Δ Brier | Corrected Δ bounds | Better folds | Better symbols | ECE | Disposition |
| --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| 1d | baseline | 0.697839 | — | 0.251933 | — | — | — | — | 0.049081 | reference |
| 1d | activity | 0.696930 | -0.000909 | 0.251495 | -0.000438 | [-0.002354, +0.000839] | 2/3 | 7/11 | 0.046913 | inconclusive |
| 1d | path | 0.700054 | +0.002214 | 0.252958 | +0.001025 | [-0.000183, +0.004350] | 0/3 | 2/11 | 0.057628 | reject |
| 1d | interaction | 0.698077 | +0.000238 | 0.252014 | +0.000081 | [-0.001569, +0.001956] | 1/3 | 5/11 | 0.052639 | reject |
| 1d | all | 0.699593 | +0.001754 | 0.252678 | +0.000744 | [-0.001535, +0.004969] | 1/3 | 2/11 | 0.057800 | reject |
| 1w | baseline | 0.740695 | — | 0.269133 | — | — | — | — | 0.119510 | reference |
| 1w | activity | 0.740571 | -0.000124 | 0.269050 | -0.000083 | [-0.001687, +0.001424] | 1/3 | 6/11 | 0.125399 | inconclusive |
| 1w | path | 0.742390 | +0.001695 | 0.269956 | +0.000823 | [-0.001306, +0.004314] | 0/3 | 5/11 | 0.123856 | reject |
| 1w | interaction | 0.740028 | -0.000667 | 0.268706 | -0.000427 | [-0.004129, +0.002953] | 2/3 | 5/11 | 0.117726 | inconclusive |
| 1w | all | 0.741800 | +0.001105 | 0.269494 | +0.000361 | [-0.003518, +0.005890] | 1/3 | 3/11 | 0.124309 | reject |
| 1w-d1 | baseline | 0.696106 | — | 0.251112 | — | — | — | — | 0.042823 | reference |
| 1w-d1 | activity | 0.695547 | -0.000560 | 0.250845 | -0.000268 | [-0.001805, +0.000899] | 1/3 | 9/11 | 0.042482 | inconclusive |
| 1w-d1 | path | 0.698419 | +0.002313 | 0.252180 | +0.001067 | [-0.000041, +0.004430] | 0/3 | 2/11 | 0.050710 | reject |
| 1w-d1 | interaction | 0.696331 | +0.000224 | 0.251195 | +0.000083 | [-0.001376, +0.001793] | 1/3 | 5/11 | 0.043057 | reject |
| 1w-d1 | all | 0.698041 | +0.001935 | 0.251963 | +0.000850 | [-0.000985, +0.004971] | 1/3 | 1/11 | 0.053514 | reject |
| 1w-d2 | baseline | 0.699808 | — | 0.252588 | — | — | — | — | 0.054740 | reference |
| 1w-d2 | activity | 0.699927 | +0.000119 | 0.252633 | +0.000045 | [-0.000246, +0.000522] | 2/3 | 4/11 | 0.057726 | reject |
| 1w-d2 | path | 0.701634 | +0.001826 | 0.253407 | +0.000819 | [-0.000114, +0.003572] | 0/3 | 2/11 | 0.057518 | reject |
| 1w-d2 | interaction | 0.699995 | +0.000187 | 0.252657 | +0.000068 | [-0.000440, +0.000795] | 0/3 | 6/11 | 0.053852 | reject |
| 1w-d2 | all | 0.701987 | +0.002179 | 0.253527 | +0.000939 | [-0.000022, +0.004213] | 0/3 | 2/11 | 0.058937 | reject |
| 1w-d3 | baseline | 0.696928 | — | 0.251414 | — | — | — | — | 0.050770 | reference |
| 1w-d3 | activity | 0.696740 | -0.000188 | 0.251327 | -0.000088 | [-0.000963, +0.000658] | 3/3 | 8/11 | 0.047567 | inconclusive |
| 1w-d3 | path | 0.698219 | +0.001291 | 0.251997 | +0.000583 | [-0.000141, +0.002458] | 0/3 | 2/11 | 0.053414 | reject |
| 1w-d3 | interaction | 0.696311 | -0.000617 | 0.251017 | -0.000397 | [-0.003150, +0.001964] | 1/3 | 6/11 | 0.047659 | inconclusive |
| 1w-d3 | all | 0.697998 | +0.001070 | 0.251749 | +0.000335 | [-0.001837, +0.004131] | 1/3 | 4/11 | 0.055224 | reject |
| 1w-d4 | baseline | 0.697759 | — | 0.251714 | — | — | — | — | 0.059486 | reference |
| 1w-d4 | activity | 0.697694 | -0.000065 | 0.251690 | -0.000024 | [-0.000314, +0.000121] | 2/3 | 9/11 | 0.058573 | inconclusive |
| 1w-d4 | path | 0.699402 | +0.001644 | 0.252456 | +0.000741 | [-0.000344, +0.003437] | 0/3 | 1/11 | 0.061026 | reject |
| 1w-d4 | interaction | 0.697811 | +0.000052 | 0.251741 | +0.000026 | [-0.002181, +0.002676] | 1/3 | 5/11 | 0.056040 | reject |
| 1w-d4 | all | 0.699706 | +0.001947 | 0.252562 | +0.000848 | [-0.000916, +0.004914] | 0/3 | 3/11 | 0.062792 | reject |
| 1w-d5 | baseline | 0.698413 | — | 0.251714 | — | — | — | — | 0.060287 | reference |
| 1w-d5 | activity | 0.698378 | -0.000034 | 0.251713 | -0.000001 | [-0.000363, +0.000294] | 1/3 | 6/11 | 0.057465 | inconclusive |
| 1w-d5 | path | 0.699651 | +0.001238 | 0.252259 | +0.000545 | [-0.000233, +0.002944] | 1/3 | 4/11 | 0.062553 | reject |
| 1w-d5 | interaction | 0.697798 | -0.000614 | 0.251369 | -0.000345 | [-0.003420, +0.001702] | 2/3 | 6/11 | 0.053000 | inconclusive |
| 1w-d5 | all | 0.699344 | +0.000931 | 0.252014 | +0.000300 | [-0.001690, +0.003368] | 0/3 | 6/11 | 0.061308 | reject |

## Candidate coverage by horizon

Counts are finite / total research rows before learned preprocessing; they measure availability, not predictive contribution. All four measurements are dimensionless. Baseline empty columns are reported separately.

| Horizon | Range anomaly | Downside share | Movement concentration | Return × persistence | All four finite rows | Baseline empty / admitted contract |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1d | 5,874/5,937 | 5,937/5,937 | 5,937/5,937 | 5,937/5,937 | 5,874/5,937 | 61/139 |
| 1w | 5,874/5,937 | 5,937/5,937 | 5,937/5,937 | 5,937/5,937 | 5,874/5,937 | 54/132 |
| 1w-d1 | 5,874/5,937 | 5,937/5,937 | 5,937/5,937 | 5,937/5,937 | 5,874/5,937 | 54/132 |
| 1w-d2 | 5,863/5,926 | 5,926/5,926 | 5,926/5,926 | 5,926/5,926 | 5,863/5,926 | 54/132 |
| 1w-d3 | 5,852/5,915 | 5,915/5,915 | 5,915/5,915 | 5,915/5,915 | 5,852/5,915 | 54/132 |
| 1w-d4 | 5,841/5,904 | 5,904/5,904 | 5,904/5,904 | 5,904/5,904 | 5,841/5,904 | 54/132 |
| 1w-d5 | 5,830/5,893 | 5,893/5,893 | 5,893/5,893 | 5,893/5,893 | 5,830/5,893 | 54/132 |

## Frozen temporal folds

Training labels and target ends precede the earliest validation decision; whole shared target-start clusters stay together. Earlier validation outcome windows also end before the next fold's first decision.

| Horizon | Fold | Training rows | Training target starts | Validation rows | Validation target starts | First validation decision UTC | Last training label UTC |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| 1d | fold-1 | 2,747 | 288 | 1,067 | 97 | 2024-08-01T20:05:00+00:00 | 2024-07-31T20:05:00+00:00 |
| 1d | fold-2 | 3,814 | 385 | 1,056 | 96 | 2024-12-18T21:05:00+00:00 | 2024-12-17T21:05:00+00:00 |
| 1d | fold-3 | 4,870 | 481 | 1,056 | 96 | 2025-05-09T20:05:00+00:00 | 2025-05-08T20:05:00+00:00 |
| 1w | fold-1 | 2,714 | 285 | 1,034 | 94 | 2024-08-01T20:05:00+00:00 | 2024-07-26T20:05:00+00:00 |
| 1w | fold-2 | 3,792 | 383 | 1,056 | 96 | 2024-12-18T21:05:00+00:00 | 2024-12-13T21:05:00+00:00 |
| 1w | fold-3 | 4,826 | 477 | 1,056 | 96 | 2025-05-09T20:05:00+00:00 | 2025-05-02T20:05:00+00:00 |
| 1w-d1 | fold-1 | 2,747 | 288 | 1,067 | 97 | 2024-08-01T20:05:00+00:00 | 2024-07-31T20:05:00+00:00 |
| 1w-d1 | fold-2 | 3,814 | 385 | 1,056 | 96 | 2024-12-18T21:05:00+00:00 | 2024-12-17T21:05:00+00:00 |
| 1w-d1 | fold-3 | 4,870 | 481 | 1,056 | 96 | 2025-05-09T20:05:00+00:00 | 2025-05-08T20:05:00+00:00 |
| 1w-d2 | fold-1 | 2,725 | 286 | 1,056 | 96 | 2024-07-31T20:05:00+00:00 | 2024-07-30T20:05:00+00:00 |
| 1w-d2 | fold-2 | 3,792 | 383 | 1,045 | 95 | 2024-12-17T21:05:00+00:00 | 2024-12-16T21:05:00+00:00 |
| 1w-d2 | fold-3 | 4,848 | 479 | 1,056 | 96 | 2025-05-08T20:05:00+00:00 | 2025-05-07T20:05:00+00:00 |
| 1w-d3 | fold-1 | 2,714 | 285 | 1,034 | 94 | 2024-07-31T20:05:00+00:00 | 2024-07-30T20:05:00+00:00 |
| 1w-d3 | fold-2 | 3,770 | 381 | 1,034 | 94 | 2024-12-16T21:05:00+00:00 | 2024-12-13T21:05:00+00:00 |
| 1w-d3 | fold-3 | 4,826 | 477 | 1,056 | 96 | 2025-05-07T20:05:00+00:00 | 2025-05-06T20:05:00+00:00 |
| 1w-d4 | fold-1 | 2,692 | 283 | 1,023 | 93 | 2024-07-30T20:05:00+00:00 | 2024-07-29T20:05:00+00:00 |
| 1w-d4 | fold-2 | 3,748 | 379 | 1,023 | 93 | 2024-12-13T21:05:00+00:00 | 2024-12-12T21:05:00+00:00 |
| 1w-d4 | fold-3 | 4,804 | 475 | 1,056 | 96 | 2025-05-06T20:05:00+00:00 | 2025-05-05T20:05:00+00:00 |
| 1w-d5 | fold-1 | 2,681 | 282 | 1,012 | 92 | 2024-07-30T20:05:00+00:00 | 2024-07-29T20:05:00+00:00 |
| 1w-d5 | fold-2 | 3,737 | 378 | 1,012 | 92 | 2024-12-13T21:05:00+00:00 | 2024-12-12T21:05:00+00:00 |
| 1w-d5 | fold-3 | 4,793 | 474 | 1,045 | 95 | 2025-05-06T20:05:00+00:00 | 2025-05-05T20:05:00+00:00 |


## Per-symbol and per-period coverage

The [main private tables](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/result-review-tables.md) include all symbol/horizon coverage rows and calibration diagnostics. The [detailed appendix](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/result-detail-tables.md) provides monthly coverage, per-fold and per-symbol loss deltas, and constant/empty/redundant column names. Each horizon's `coverage.json` and `results.json` supply exact values and denominators. Those observations describe this frozen cohort; they did not control admission using validation data. For example, 1d has 578 rows for each of the nine longer-history symbols, 415 RR rows and 320 PDYN rows. Their corresponding activity counts are 572, 411 and 315. The shorter symbol histories were not padded or manufactured.

Per-horizon conclusions are explicit in the comparison table. Daily and d1 activity show small favorable estimates but fail acceptance; d2 rejects all additions; d3/d4/d5 activity remains inconclusive; weekly activity and persistence remain inconclusive. All seven path and combined contrasts are rejected for advancement. Shared targets and overlapping horizons mean these are related views of one market history, not seven independent replications. Weekly aggregate calibration is visibly weak (baseline ECE about 0.120); tiny incremental improvements cannot establish calibrated forecast utility.

## Validation, evidence limits and reproducibility

Synthetic tests: **31 passed, one Windows symlink-creation privilege skip** in the local checkout, immutable source candidate and current-main review candidate. Coverage includes future append/mutation prefix invariance, warm-up/zero denominators, sparse/unknown/derived/incomplete bars, exact availability, session changes, holiday/DST/early close, semantic quarantine, fold purging, train-only transformations, matched IDs, temporal uncertainty, immutable writes and input mutation detection. The skipped OS-specific test is not represented as passed.

Independent result verification confirms 105 successful attempts and 105 saved numeric model states; identical baseline/candidate OOS membership on every route; zero excluded or post-shield IDs; no cross-boundary outcome leakage; agreement of independently recomputed metrics within 1e-12; and all **32 input hashes and 14 source hashes** stable. OUST's in-history reverse split predates all admitted lookbacks; adjusted-versus-raw candidate equality was explicitly checked. Current split metadata lacks historical publication timestamps, so the invariance check is the relevant protection rather than a claim of point-in-time corporate-action authentication.

The frozen accepted baseline measurements inherit their original source/materialization limitations. Existing regime/breakout calculators select FULL/BOOTSTRAP using supplied history length around sixty rows; this task does not recertify their entire historical prefix behavior. New candidate calculations use fixed per-row windows and pass prefix tests. Saved model manifests and the former workflow source are not promoted to stronger historical provenance simply because current hashes are pinned. Research uncertainty is approximate, and a single local symbol group/calendar regime cannot prove broad generalization.

| Private artifact | Purpose |
| --- | --- |
| [Ownership](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/ownership.json) | Reviewed base, unrelated-writer inventory and exact owned scope. |
| [Cohort verification](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/cohort-verification.json) | 108 current reconciliation checks and common shield. |
| [Frozen metadata membership](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/frozen-membership-metadata.parquet) | Exact research/excluded identities without outcomes; SHA `05013096dbd75230713f60ec2de14517da84f52b422a4cd234122351f505a009`. |
| [Private adapter](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/run-private-experiment.py) | Reproducible bounded input selection, native feature computation and model evaluation. |
| [Pre-outcome freeze](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/frozen-run-v1/freeze-before-outcomes.json) | Design, target/source contracts, dependency/input hashes and package versions. |
| [All results](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/frozen-run-v1/all-results.json) | All variants and no-fit route conclusions; each subdirectory holds exact specifications, cohorts, predictions, attempts and model states. |
| [Independent result review](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/result-review.json) | Metric recomputation, membership/purge/model-count/hash checks. |
| [Detailed tables](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/result-review-tables.md) | Coverage by horizon/symbol/period, loss comparisons, uncertainty, fold and calibration diagnostics. |
| [Detail appendix](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/result-detail-tables.md) | Monthly coverage, per-fold and per-symbol deltas, and baseline empty/constant/redundant lists. |
| [Final stability](C:/dev/ducketz/scratch/loop-b-custom-features-20261011/frozen-run-v1/stability.json) | Source/input invariance and no production writes. |

To reproduce, use the saved source/input hashes, package versions and private adapter. Its `frozen-run-v1` output path deliberately refuses reuse; a new reviewed run must use a new private output identity while retaining the old receipts. Reproduction must verify frozen input hashes and eligibility, not reread a newer pointer or expand the cohort. Saved JSON model states contain semantic caps, retained columns, medians, clipping bounds, centering/scales, coefficients/intercept/classes and solver iterations. No canonical models, samples, technicals, latest pointers or prediction receipts were modified.

## Source completion and possible future adoption

Shared source completion record: `20261012T004655Z-7fa7bf8271a74de9a92620b5f640fcfc`. The installed queue captured exact bytes and real checks. The source courier published and remotely verified `e9c491976445aa7546d849e2b06bd6b22b484619`. A separate reviewed/tested candidate on main `4826eed87b2e283724e2a02f761e4561727a7248` is `6b14d260e4c778c6f5c1146755907a0c82408faa`, available as [draft PR 64](https://github.com/jeremysecondstate/ducketz/pull/64). Only two modules, two synthetic tests and portable documentation are shared. This report, all fitted models, raw/source data, sample selections and detailed experimental evidence stay local. Source availability does not establish Atlas installation, main integration or loaded runtime. No merge or runtime deployment occurred.

Before any separately authorized production adoption: independently validate historical feature and corporate-action provenance; obtain sufficient nonprotected intraday history if intraday use is intended; preregister a confirmatory design using genuinely untouched development evidence, with adequate temporal uncertainty and a separate chronological calibration segment; establish material stable incremental improvement against a suitable production-family baseline; review semantic registration, runtime availability, computational cost and monitoring; and explicitly authorize model promotion/deployment. This experiment supplies no positive adoption recommendation. Moving a lockbox boundary, pooling correlated rows or expanding an indicator search after these results would not resolve its evidence limits.
