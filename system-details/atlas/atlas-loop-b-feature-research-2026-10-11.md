# Atlas Loop B custom feature research — October 11, 2026

**Private local research. Do not publish this report, tables, sample selections, predictions or fitted state.** Completed at 18:21 PDT on October 11 (01:21 UTC October 12). Actor Atlas, machine pc-original; timezone America/Los_Angeles.

**No candidate demonstrated improvement under the predeclared rule.** All 105 planned fits succeeded across seven daily/weekly routes and three temporal folds. Of 28 evaluated candidate comparisons, 24 were rejected for this research cohort and four were inconclusive. None was retained. Both intraday routes are inconclusive without fitting because their labels begin after the frozen common protected boundary. These are findings about an explicitly delayed research baseline, not a reproduction or performance assessment of production.

## Reference, ownership and publication

Atlas's own accepted generation remains `20261010T055341.769790Z`; its manifest SHA-256 is `7cd518505519dda1045ffd5c150b12bb449786493b4561e12d29c467bffe96fe`. The accepted pointer, publication receipt, output bytes and nine identified model manifests were frozen locally. No fitted production model was deserialized. All recorded training/calibration/assessment counts, maximum training decisions, assessment endpoints and saved BACKTEST assessment identities reconcile using metadata only. **Directory name/version does not cryptographically pin a historical model manifest; reconstructed membership is not an original saved fit-ID receipt.** This experiment creates new exact membership receipts instead.

Atlas's configured equities are AAPL, AMZN, GOOG, MU, NVDA, SNDK, COST, CROX, PATH, TWST and IONQ. The experiment excludes NVDA before reading outcomes: its native raw-scale history includes a documented 2024 split, while the local action receipt is retrospective. The other ten symbols remain; SNDK has shorter history. No peer cohort, count or result supplied Atlas evidence.

The pinned coordination manifest and all 29 files verified. Application base `90704d21801f60426493bd6cc650a7fac38d4f61` had 210 dirty/untracked paths owned elsewhere. All research source work occurred in managed isolation. Scout PR #64 candidate `6b14d260e4c778c6f5c1146755907a0c82408faa` supplied the reusable implementation and tests. Atlas made five narrowly scoped research-source/test/documentation refinements. The installed exact-byte queue and fresh isolated candidate checks each passed **35 tests**, with **one Windows symlink-privilege skip**. That skip is not claimed as a pass.

Reviewed source SHA `92d7fb55367c882a87b28a147abc8cfb893eb58d` is published in [draft PR #65](https://github.com/jeremysecondstate/ducketz/pull/65), with verified remote SHA. Completion-Record `20261012T011445Z-688ae07049f849c585129f29e48a9e1c`; the immutable sanitized notice was delivered through Git. [Atlas–Scout issue #17](https://github.com/jeremysecondstate/atlas-scout/issues/17) supplies source/provenance review context only. No private evidence was exported. Main integration, production registration, model promotion, task changes and runtime deployment were not performed.

## Causality finding and research cohort

All 9,290 retained native daily rows exactly match aggregation of the native hourly rows over the full UTC date; only 2,594 also match the aggregate before 16:00 New York time. The [provider OHLCV specification](https://databento.com/docs/schemas-and-data-formats/ohlcv) defines native daily intervals by UTC date. Such a bar cannot be available at regular-session close plus five minutes. This review corrected the **research** semantic contract to UTC-day end plus five minutes. Production source/timing was left unchanged.

Saved daily sample features use that day's daily bar at an exchange-close decision, and saved target metadata describes regular-session endpoints while its numerical labels use native daily open/close. A direct contemporary-baseline experiment would therefore make an unsupported causal claim. Instead, the design frozen **before outcome access** uses the entire saved admitted baseline vector from the exact preceding exchange session, with candidate measurements from that same donor bar. Every donor's UTC-day end plus five minutes precedes the original recipient decision; no stale fallback is allowed. The donor ID and exact source date are retained. All baseline columns and transforms remain the accepted contract, but their input age is deliberately increased for this new research cohort.

Numerical outcomes, the 0.001 round-trip cost convention and saved target-definition strings remain unchanged. Original declared clocks are preserved alongside conservative physical UTC-date target bounds: start at the first target date's 00:00 UTC; end at 00:00 after the last target date; label availability five minutes later. Purging uses these wider bounds. This does **not** establish that the saved labels represent the intended regular-session forecast; it makes the comparison explicit for the saved numerical target.

The earliest protected calibration period among all nine routes gives a permanent common physical boundary of **2025-08-12 00:00 UTC**. Both target end and label availability must be strictly earlier. Calibration, assessment, sealed lockbox and prospective LIVE reservations remain excluded. Published nonmember IDs, lockbox metadata and this boundary are frozen. The moving latest pointer cannot expand eligibility. No sealed outcome table was opened or scored.

The original nine-horizon training reconstruction has 79,118 rows. After common protection, physical-clock checks and exact preceding-session donors, 38,355 metadata-eligible rows remain; excluding NVDA leaves **34,564 rows**. Missing initial donors were removed before labels were read. The only outcome read projected `target_cost_adjusted_positive` for those final exact recipient IDs. Donor reads projected only contracted features. Native minute-label coverage begins in May 2026, so neither 1h nor 4h has labels before this boundary. The route named 4h specifies 180 eligible target minutes with four checkpoint starts; the name was not interpreted as four ordinary hours.

## Fixed candidate definitions

Let `q=(high-low)/close` and `r_i=log(close_i/close_(i-1))`. All measurements are dimensionless and invariant to uniform positive price scaling across symbols; that property does not correct split jumps. Semantic version: `native-ohlcv-research-v2`.

| Family / measurement | Formula and hypothesis | Lookback / missingness |
| --- | --- | --- |
| Activity: slot range surprise | `log(q / median(previous comparable q))`; unusual range beyond ordinary time-slot seasonality | Previous 20 scheduled sessions, at least 10 native comparable bars; missing without support or positive ratio |
| Path: downside variation share | `sum(min(r,0)^2)/sum(r^2)`; asymmetry of realized movement | 10 returns / 11 consecutive eligible native bars; missing for zero variation |
| Path: movement concentration | `sum(abs(r)^2)/sum(abs(r))^2`; shocks versus distributed movement | Same window; defined range 0.1–1; missing when total movement is zero |
| Interaction: return × persistence | `sum(r)*abs(mean(sign(r)))`; signed movement conditioned on persistent signs | Same window; keeps direction and unsigned persistence explicit |

Existing market-regime/breakout features already represent momentum, volatility, position, compression and same-slot volume participation. A second session-volume ratio would mostly duplicate the current contract and was omitted. The chosen range seasonal comparison, downside share, movement concentration and explicit persistence product are distinct, while their shared price inputs and momentum overlap are acknowledged. No calendar/target-window predictor, minute-only feature, extra window, hyperparameter search or post-result family was added.

Native provenance requires retained raw `aggregation_method=native`, schema and raw-scale metadata plus exact timestamp/OHLCV equality. All 100,647 native hourly and 9,290 daily source rows were verified; 3,874 derived/carried hourly rows were identified and excluded. Unknown, derived, carried, incomplete, invalid-price/nonfinite/negative-volume bars do not contribute. Native zero-volume bars are not automatically called carried. No filling or synthetic observations occur.

Hourly bars become available at interval end plus five minutes; activity matches New York clock slot, session composition and regular-session duration. Hourly paths use consecutive full regular hours, skipping scheduled closures but breaking on missing native bars. Native daily availability is next UTC midnight plus five minutes. Daily activity matches scheduled regular-session duration, UTC opening time and prior-calendar-date session presence, so DST and possible prior-session tails are separated. Daily paths use eleven consecutive exchange-session-date native UTC aggregates, including between-session moves; weekend/holiday date labels are not substituted. Short sessions, Mondays/post-holidays and DST transitions can lack ten comparable activity bars. The calendar package is pinned at exchange-calendars 4.13.2. Five minutes is a modeled processing delay, not empirically proved historical delivery latency.

## Frozen model comparison

[Preanalysis design](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/preanalysis-design.json) SHA-256 `673666436bfc0798ac619ce600edc2b54bcff733f8f9b5bdd92b2b4bc6da44c7` was written before outcome access. [Prepared specification](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/experiments/prepared-v1/specification.json) SHA-256 `06a0ff4cb1295995502c2306b4d41f22e7e73c4d742b251cd7f6827618512fa2` freezes exact cohorts, exclusions, donors, source/input hashes, all transforms and folds. [Pre-fit review](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/prefit-review.json) independently checked group membership and purge clocks before fitting. No design revision or retry followed results.

Each route compares baseline alone, baseline + activity, baseline + path, baseline + interaction, and one all-family candidate. Fresh C=1 logistic regression uses the same eligible rows, targets, chronological folds, max_iter=1000 and seed 20261011. No fitted calibration is used. Each fold independently learns availability admission (20% minimum finite values), constant/exact-duplicate removal, semantic caps, medians, 0.25/99.75-percentile clipping and scaling from training only. Missing candidate values never select validation rows. No missing indicators are used in any variant.

Three expanding folds follow an initial half-history training region. The earliest training folds have 264–270 distinct target dates; validation folds have 85–90 each. Shared target starts remain grouped across symbols/decisions. Training outcome ends and label availability strictly precede the earliest validation decision. Validation groups crossing the next validation period are purged too. Both purge ID sets and hashes are saved. Training and scoring give each target start equal total weight, then equal symbols and equal decisions within symbol.

Primary metric is mean target-cluster log loss. Acceptance requires all three folds, at least 40 OOS dates, absolute improvement ≥0.005, at least two improving folds, improvement in a strict majority of symbols, no Brier deterioration, and a negative corrected one-sided bootstrap upper bound. The paired moving-block bootstrap uses five observed target dates, 10,000 draws and Bonferroni familywise 0.05/36, conservatively retaining the unfit intraday comparisons in the trial budget. Any passing result would mean further research only.

## Coverage is separate from contribution

The following is descriptive coverage over the frozen cohort, before preprocessing; column admission was relearned inside each training fold. Baseline rows with every contracted column finite are zero because entire auxiliary columns are empty. Every candidate row has at least one finite measurement, and all three path/interaction measurements are finite. Candidate columns are neither constant nor exact duplicates of another declared column. High finite coverage did not produce predictive improvement.

| Route | Baseline cols | Baseline finite cells | Empty cols | Constant cols | Activity finite | Path finite | Interaction finite | All 4 finite rows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1d | 139 | 55.02% | 61 | 2 | 69.69% | 100% | 100% | 3451/4952 |
| 1w | 132 | 58.05% | 54 | 2 | 69.69% | 100% | 100% | 3451/4952 |
| 1w-d1 | 132 | 58.05% | 54 | 2 | 69.69% | 100% | 100% | 3451/4952 |
| 1w-d2 | 132 | 58.05% | 54 | 2 | 69.63% | 100% | 100% | 3441/4942 |
| 1w-d3 | 132 | 58.05% | 54 | 2 | 69.57% | 100% | 100% | 3431/4932 |
| 1w-d4 | 132 | 58.05% | 54 | 2 | 69.71% | 100% | 100% | 3431/4922 |
| 1w-d5 | 132 | 58.05% | 54 | 2 | 69.65% | 100% | 100% | 3421/4912 |

The daily baseline has 61 entirely empty columns; weekly routes have 54. These include life/fund/options/SEC/CME/energy families and the daily quote field as listed in [column diagnostics](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/report-tables/columns-empty-constant-redundant.csv). `fdir__component_coverage` and `fdir__metric_coverage` are constant over this cohort. Exact redundant baseline columns are separately listed there; empty-column duplicates are not evidence of observed redundancy. No candidate was empty or constant.

Daily-route coverage by symbol is shown below. The other routes and **every observed month** are in [per-symbol coverage](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/report-tables/coverage-by-symbol.csv) and [per-month coverage](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/report-tables/coverage-by-month.csv); [coverage totals](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/report-tables/coverage-summary.csv) retain exact finite cell/row counts.

| Symbol | Rows | Activity | Downside share | Concentration | Interaction |
| --- | --- | --- | --- | --- | --- |
| AAPL | 543 | 69.61% | 100.00% | 100.00% | 100.00% |
| AMZN | 543 | 69.61% | 100.00% | 100.00% | 100.00% |
| COST | 543 | 69.61% | 100.00% | 100.00% | 100.00% |
| CROX | 543 | 69.61% | 100.00% | 100.00% | 100.00% |
| GOOG | 543 | 69.61% | 100.00% | 100.00% | 100.00% |
| IONQ | 543 | 69.61% | 100.00% | 100.00% | 100.00% |
| MU | 543 | 69.61% | 100.00% | 100.00% | 100.00% |
| PATH | 543 | 69.61% | 100.00% | 100.00% | 100.00% |
| SNDK | 65 | 75.38% | 100.00% | 100.00% | 100.00% |
| TWST | 543 | 69.61% | 100.00% | 100.00% | 100.00% |

## Out-of-sample results and dispositions

Baseline probabilities are uncalibrated research probabilities. ECE uses ten fixed bins with target-balanced weights; no production calibration/assessment data was consulted.

| Route | Eligible rows | OOS rows | OOS target dates | Baseline log loss | Baseline Brier | Baseline ECE |
| --- | --- | --- | --- | --- | --- | --- |
| 1d | 4952 | 2495 | 270 | 0.715807 | 0.260606 | 0.078219 |
| 1w | 4952 | 2468 | 267 | 0.770995 | 0.281229 | 0.142648 |
| 1w-d1 | 4952 | 2495 | 270 | 0.714300 | 0.260007 | 0.089198 |
| 1w-d2 | 4942 | 2467 | 267 | 0.717175 | 0.261328 | 0.081584 |
| 1w-d3 | 4932 | 2448 | 265 | 0.720390 | 0.262696 | 0.084695 |
| 1w-d4 | 4922 | 2420 | 262 | 0.725099 | 0.264769 | 0.097733 |
| 1w-d5 | 4912 | 2401 | 260 | 0.710250 | 0.258064 | 0.067785 |

Candidate-minus-baseline log-loss changes follow; **negative is better**. These seven horizons reuse market history and are not seven independent replications.

| Route | Activity Δ | Path Δ | Interaction Δ | Combined Δ |
| --- | --- | --- | --- | --- |
| 1d | +0.000596 | +0.009645 | +0.000093 | +0.010191 |
| 1w | +0.000442 | +0.013612 | +0.000105 | +0.014425 |
| 1w-d1 | +0.000581 | +0.010086 | +0.000073 | +0.010757 |
| 1w-d2 | -0.000388 | +0.004256 | -0.000032 | +0.003820 |
| 1w-d3 | +0.000473 | +0.003134 | +0.000904 | +0.004161 |
| 1w-d4 | -0.000428 | +0.003037 | +0.001158 | +0.003615 |
| 1w-d5 | -0.000119 | +0.001035 | +0.000747 | +0.001742 |

| Route | Activity | Path | Interaction | Combined |
| --- | --- | --- | --- | --- |
| 1d | reject | reject | reject | reject |
| 1w | reject | reject | reject | reject |
| 1w-d1 | reject | reject | reject | reject |
| 1w-d2 | inconclusive | reject | inconclusive | reject |
| 1w-d3 | reject | reject | reject | reject |
| 1w-d4 | inconclusive | reject | reject | reject |
| 1w-d5 | inconclusive | reject | reject | reject |

1h and 4h: **inconclusive for every family and the combined candidate; zero fits**. Their absent eligible pre-protection labels are a data constraint, not evidence of poor predictive contribution.

Activity improves slightly for 1w-d2, 1w-d4 and 1w-d5, by only 0.000388, 0.000428 and 0.000119 log-loss units. Interaction improves 1w-d2 by about 0.000032. All are below the predeclared 0.005 requirement and have corrected upper bounds above zero. They remain inconclusive, not retained. Path and combined candidates worsen log loss on every tested route and are rejected for this design. Rejection is a disposition for this bounded cohort/configuration, not proof that every future formulation must fail.

Detailed adjusted bootstrap bounds, Brier changes, calibration and stability are below. Bounds are the alpha/36 and 1-alpha/36 bootstrap quantiles, not a claim of independent observations or exact finite-sample coverage.

| Route | Variant | Log-loss Δ | Adjusted bootstrap bounds | Brier Δ | Candidate ECE | Improving folds | Improving symbols |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1d | activity | +0.000596 | [-0.000737, +0.001867] | +0.000270 | 0.082092 | 0/3 | 2/10 |
| 1d | path | +0.009645 | [+0.002351, +0.017219] | +0.004231 | 0.097649 | 0/3 | 0/10 |
| 1d | interaction | +0.000093 | [-0.000133, +0.000303] | +0.000045 | 0.077690 | 1/3 | 4/10 |
| 1d | all | +0.010191 | [+0.002637, +0.018170] | +0.004473 | 0.096262 | 0/3 | 0/10 |
| 1w | activity | +0.000442 | [-0.001543, +0.002784] | +0.000139 | 0.146237 | 0/3 | 5/10 |
| 1w | path | +0.013612 | [+0.001963, +0.025803] | +0.004396 | 0.149178 | 1/3 | 0/10 |
| 1w | interaction | +0.000105 | [-0.000600, +0.000790] | +0.000043 | 0.143910 | 1/3 | 5/10 |
| 1w | all | +0.014425 | [+0.002477, +0.026831] | +0.004646 | 0.151924 | 1/3 | 0/10 |
| 1w-d1 | activity | +0.000581 | [-0.000600, +0.001715] | +0.000263 | 0.089244 | 1/3 | 0/10 |
| 1w-d1 | path | +0.010086 | [+0.002221, +0.017903] | +0.004476 | 0.102832 | 0/3 | 1/10 |
| 1w-d1 | interaction | +0.000073 | [-0.000320, +0.000432] | +0.000032 | 0.088881 | 1/3 | 4/10 |
| 1w-d1 | all | +0.010757 | [+0.002696, +0.019161] | +0.004777 | 0.105155 | 0/3 | 0/10 |
| 1w-d2 | activity | -0.000388 | [-0.003265, +0.002070] | -0.000183 | 0.082977 | 2/3 | 6/10 |
| 1w-d2 | path | +0.004256 | [-0.000733, +0.009242] | +0.001862 | 0.093585 | 0/3 | 1/10 |
| 1w-d2 | interaction | -0.000032 | [-0.000460, +0.000356] | -0.000006 | 0.083304 | 2/3 | 4/10 |
| 1w-d2 | all | +0.003820 | [-0.001913, +0.009405] | +0.001657 | 0.093218 | 1/3 | 2/10 |
| 1w-d3 | activity | +0.000473 | [-0.001144, +0.002451] | +0.000214 | 0.090455 | 1/3 | 3/10 |
| 1w-d3 | path | +0.003134 | [+0.000134, +0.006208] | +0.001357 | 0.091313 | 0/3 | 1/10 |
| 1w-d3 | interaction | +0.000904 | [-0.000239, +0.002387] | +0.000410 | 0.086629 | 1/3 | 2/10 |
| 1w-d3 | all | +0.004161 | [+0.000262, +0.008702] | +0.001813 | 0.094442 | 0/3 | 2/10 |
| 1w-d4 | activity | -0.000428 | [-0.002139, +0.001367] | -0.000225 | 0.092569 | 2/3 | 6/10 |
| 1w-d4 | path | +0.003037 | [-0.000357, +0.006870] | +0.001312 | 0.100642 | 1/3 | 0/10 |
| 1w-d4 | interaction | +0.001158 | [-0.000142, +0.002790] | +0.000506 | 0.099892 | 2/3 | 3/10 |
| 1w-d4 | all | +0.003615 | [-0.000513, +0.008702] | +0.001517 | 0.103753 | 1/3 | 2/10 |
| 1w-d5 | activity | -0.000119 | [-0.001753, +0.001344] | -0.000058 | 0.067118 | 1/3 | 6/10 |
| 1w-d5 | path | +0.001035 | [-0.001566, +0.003976] | +0.000477 | 0.071565 | 1/3 | 2/10 |
| 1w-d5 | interaction | +0.000747 | [-0.000403, +0.002159] | +0.000342 | 0.066560 | 2/3 | 3/10 |
| 1w-d5 | all | +0.001742 | [-0.001693, +0.005590] | +0.000782 | 0.067997 | 1/3 | 4/10 |

[Per-fold, per-symbol and per-month metrics](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/report-tables/metrics-by-fold-symbol-month.csv) preserve every slice. Full reliability-bin counts, mean probabilities and observed frequencies are in each route's `results.json`; raw private OOS predictions and numerical model/preprocessor state are beside them. No favorable slice was used to revise the design. All 105 started/finished attempt records report success; there were no failed fits or parameter changes. An [independent saved-evidence review](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/results-review/independent-results-review.json) reproduced all 35 aggregate and 105 fold log-loss/Brier results within 2.22e-16, reconciled every matched model attempt, verified 122 unique pinned paths, and confirmed the frozen protection and donor identities without fitting again. [Saved-state forward verification](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/results-review/saved-state-forward-verification.json) reproduced all probabilities exactly for the last-fold combined model on each of seven routes without reading outcomes or refitting; [independent coverage review](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/results-review/independent-coverage-review.json) also matched.

## Limits and requirements before any production proposal

The baseline deliberately delays the full existing vector by one exchange session. Results cannot be transferred to the original contemporaneous production baseline, whose native-daily timing requires a separate audit/repair. The numerical target is preserved, but its declared regular-session interpretation is not established by the native UTC OHLC endpoints. Source snapshots were retrieved later; raw/native equality and modeled causal timestamp rules do not prove original delivery vintages or actual historical latency. Lagging repairs the identified daily-bar timing defect but does not independently establish every auxiliary component's historical revision vintage. Model manifests were frozen as observed, not cryptographically pinned by the old run manifest.

NVDA exclusion reduces representativeness. Missing corporate-action artifacts for some other symbols do not prove no historical action occurred. Candidates use unadjusted native market scale, not retrospectively fitted adjustments. The shorter SNDK history appears only late and is not an independent market regime. Repeated decisions, correlated symbols, overlapping weekly targets and dependence longer than the five-day bootstrap blocks limit uncertainty interpretation. The multiplicity-adjusted extreme quantiles depend on about 14 of 10,000 draws in each tail, adding Monte Carlo uncertainty. None of this converts a tiny favorable mean into reliable improvement. This study does not establish that its research baseline itself has deployable skill.

Any separately authorized production proposal would first need corrected and independently verified source/target interval semantics, a reviewed corporate-action and point-in-time availability policy, genuinely untouched prospective validation with fixed exclusions, an appropriate independent calibration segment, and evidence exceeding the predeclared effect/stability threshold. Only then could semantic registry admission, operational compatibility checks and an explicit promotion/deployment decision be considered. This experiment supplies no promotion recommendation.

## Reproduction and evidence map

Use the existing Python environment recorded in [environment.json](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/experiments/prepared-v1/environment.json): Python 3.13, numpy 2.5.1, pandas 3.0.3, scikit-learn 1.9.0, pyarrow 24.0.0 and exchange-calendars 4.13.2. [Driver](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/run_atlas_experiment.py) separates preparation from fitting and intentionally refuses to overwrite an existing experiment. To reproduce elsewhere, preserve these bytes/configuration/pins and choose a separately reviewed **new private destination**; do not delete or overwrite this evidence. Numeric models include coefficients and complete train-fitted preprocessing, so prediction verification needs no legacy model deserialization.

- [Atlas source/run provenance](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/provenance/atlas-provenance.json), [original membership metadata](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/provenance/reference-membership-metadata.parquet), and [causal donor reconciliation](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/provenance/causal-daily-reconciliation-v2.json).
- [Input provenance and raw comparisons](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/input-review/input-provenance.json), [corporate/interval evidence](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/input-review/corporate-action-and-interval-evidence.json), and [verified native bar adapter](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/input-review/verified_bar_adapter.py).
- [Prepared full specification](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/experiments/prepared-v1/specification.json), [exact donor map](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/experiments/prepared-v1/membership-with-donors.parquet), and [protected/excluded IDs](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/experiments/prepared-v1/protected-exclusions.json).
- [All-horizon results](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/experiments/bounded-run-v1/all-horizon-results.json), [run completion and stability](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/experiments/bounded-run-v1/run-completed.json), and [comparison table](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/report-tables/comparisons.csv).
- [Source publication receipt](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/source-publication-receipt.json), [isolated verification](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/source-isolated-verification.json), and [sanitized Git notice delivery](C:/dev/ducketz/scratch/loop-b-custom-features-atlas-20261011/source-notice-delivery.json).

Only dedicated private experiment files, the linked private chapter addendum, shared research source/tests/documentation in isolated worktrees, and required coordination receipts were written. No providers/brokers were called for data; no trading, scheduler change, restart, canonical DATASTORE write, model promotion or prediction publication occurred.
