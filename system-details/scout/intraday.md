# Scout: Independent 15-minute trader

Scout generates, executes and logs its own local 15-minute predictions. There is no 15-minute synthesis, no Atlas order grant, and no dependency on the combined Gameplan trader or the peer 15-minute trader.

Use Scout's own local symbol profile, existing broker connection and `intraday/scout` books, journal and `execution.lock`. The stream identity is `scout-15m` and execution mode is `scout-local-broker-account`. The broker supplies the stable account fingerprint at manual startup; no Gameplan account configuration is needed. Forecasts, manual-session state and order/fill logs stay local. Another trader's files and liveness are not consulted.

Preparation is permanently authorized, needs no repeated approval and does not start trading. `python -B -m ml.intraday.scout_prestart` is the installed optional offline diagnostic; it never becomes a nightly or manual-start prerequisite. Scout preparation remains independent of Gameplan synthesis.

Jeremy starts this trader manually through the local `ml.intraday.live_session --live --scout-admission broker-local` entry point or its existing launcher. Once started, it obtains current broker capacity/quotes, manages its own exact order identities and preserves its own fill and activity logs. The ordinary order window belongs to execution; it is not a cross-trader startup or approval ceremony.

Keep historical mixed-ledger originals and receipts intact. Scout binds its own books to the existing broker identity at manual start; normal preparation never performs cross-trader migration or legacy scans. Local setup/install facts must be reported honestly and do not establish the peer's installation or running state.

- [Shared independent 15-minute design](../intraday.md)
- [Scout nightly responsibilities](nightly-workflow.md)
- [Standing human direction](../../coordination/independent-traders.md)
