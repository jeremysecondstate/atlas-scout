# Scout: Independent 15-minute trader

Scout generates, executes and logs its own local 15-minute predictions. There is no 15-minute synthesis, no Atlas order grant, and no dependency on the combined Gameplan trader or the peer 15-minute trader.

Use Scout's own local symbol profile, broker connection and `intraday/execution/` namespace. The stream identity is `scout-15m`. The local configuration, holdings/order database, authority database, execution lock, manual-session state and forecasting logs belong to this PC. Another trader's files and liveness are not consulted.

Prepare the existing binding every night with `tools.prepare_independent_intraday --nightly` and the local datastore/profile/watchlist arguments. This independent result does not delay Gameplan synthesis. Preparation is permanently authorized, needs no repeated approval and does not start trading.

Jeremy starts this trader manually through the local `ml.intraday.live_session --live` entry point or its existing launcher. Once started, it obtains current broker capacity/quotes, manages its own exact order identities and preserves its own fill and activity logs. The ordinary order window belongs to execution; it is not a cross-trader startup or approval ceremony.

Keep historical mixed-ledger originals and receipts intact. The one-time independent namespace setup creates the local binding; normal nightly preparation reuses it and never repeats legacy scans. Local setup/install facts must be reported honestly and do not establish the peer's installation or running state.

- [Shared independent 15-minute design](../intraday.md)
- [Scout nightly responsibilities](nightly-workflow.md)
- [Standing human direction](../../coordination/independent-traders.md)
