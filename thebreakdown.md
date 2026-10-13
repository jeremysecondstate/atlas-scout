# Ducketz system breakdown

Current operating direction: October 13, 2026. Atlas is the original PC; Scout is the other PC. The permanent architecture consists of one combined Gameplan and three independently controlled traders.

## What each system does

| System | Atlas | Scout |
| --- | --- | --- |
| Local research | Prepares its established local symbols through data, Stats, model and prediction work. | Prepares its established local symbols through the same shared research framework. |
| Combined Gameplan | Receives both Gameplan contributions, synthesizes them and publishes the combined result. | Publishes its own Gameplan contribution for Atlas to combine. |
| Gameplan trading | Manually started combined Gameplan trader manages the established combined symbol universe and horizons. | Does not provide an execution-history or approval prerequisite for Atlas Gameplan. |
| Local 15-minute trading | Independently predicts, trades and logs the `atlas-15m` stream. | Independently predicts, trades and logs the `scout-15m` stream. |

The only cross-PC trading-plan synthesis is Atlas–Scout Gameplan research. There is no 15-minute synthesis and no cross-trader reconciliation, compatibility verification, peer order grant or shared trading ledger. Gameplan does not depend on either 15-minute trader, and neither 15-minute trader depends on Gameplan or the other trader.

## Nightly work is already authorized

The existing schedules perform each PC's data, Stats, model, prediction and Gameplan work. Each PC publishes its Gameplan contribution through the existing private exchange. Atlas combines and publishes the actual contributions without an additional approval, reciprocal acceptance or verification stage. Each PC separately prepares its own 15-minute trader using its own saved local binding.

A task finishes its assigned work and reports the real result. Actual missing inputs or failures are recovered under the same standing authority while completed work and real timestamps are preserved. Do not invent data, backdate outcomes or create duplicate healthy workers. A missing input is a concrete operational problem, not a reason to ask for a new permission ceremony.

The nightly result is ready for Jeremy's manual start. Preparation never starts trading. Each manually started trader observes current broker capacity and manages its own exact orders, fills, control and activity log. Scheduled tasks do not start/restart traders or place/cancel orders to prove readiness.

## State and communications

The combined Gameplan trader has its own Gameplan ledger and controls. Each PC's 15-minute trader has its own `intraday/execution/` binding and databases plus its own forecasting/manual-session records. Old mixed-ledger originals and receipts remain intact; they are historical evidence and are not a nightly dependency.

Existing internet connectivity, authenticated GitHub and private Drive/CODEXSTORE are sufficient. Routine sanitized communication uses `atlas-scout` GitHub. Ducketz shared-source/request queues retain their existing Git transport. Private nightly Gameplan packets remain in the authorized CODEXSTORE exchange. No VPN, LAN connection, private gateway, shared broker service or distributed execution authority is needed.

## Research, Stats and other systems

Data/feature acquisition, model generation and evaluation remain their established local numerical responsibilities. Stats evaluates actual saved forecasts/plans and observed outcomes; a forecast or planning quantity is not a broker fill. The shared source is common across PCs, while documented local symbols and operating bindings remain local.

Loop C review and Hyperliquid research/paper responsibilities remain separate from this equities Gameplan/15-minute architecture. This revision does not activate a paused legacy task, change a model strategy or authorize unrelated real-money trading.

## Source and private-data rules

Source development keeps explicit ownership, a reviewed base, exact-byte review, relevant offline checks, immutable completion records and the established publication process. Reviewed peer adoption is already authorized locally without repeated human permission. These engineering responsibilities do not become nightly preparation or trader approval gates.

Publish only sanitized coordination and authorized source. Credentials, account data, raw market data, fitted models, databases, private bindings and task memory stay in their existing local/private boundaries. Preserve all historical messages and receipts. Record source publication, installation, prepared state and running state as separate facts.

## Current references and history

- [Permanent operating policy](coordination/independent-traders.md)
- [Coordination and source publication](coordination/README.md)
- [Gameplan lifecycle](system-details/gameplan.md)
- [Nightly workflow](system-details/nightly-workflow.md)
- [Independent 15-minute traders](system-details/intraday.md)
- [Atlas tasks](system-details/atlas/scheduled-tasks.md) and [Scout tasks](system-details/scout/scheduled-tasks.md)
- [System details index](system-details/README.md)
- [Historical observations and prior operating descriptions](system-details/history.md)

The prior October 7–11 breakdown, recovery narrative and task inventories are retained at their immutable Git revision in the history index. They describe earlier implementations and do not override the October 13 operating direction.
