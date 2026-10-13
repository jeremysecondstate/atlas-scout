# Independent 15-minute traders

Atlas and Scout each generate, trade and log their own local 15-minute predictions. Neither consumes a combined 15-minute plan. There is no distributed grant, peer approval, Gameplan loaded-code proof, shared trading ledger or cross-trader reconciliation.

Each PC uses its own `intraday/execution/config.json`, `intraday/execution/holdings.sqlite3` and `intraday/execution/authority.sqlite3`, with its own execution lock, manual-session control and local forecasting logs. Existing mixed-ledger history remains preserved as historical evidence; it is not replayed into the independent epoch or read by normal preparation.

## Nightly preparation and manual start

Use the installed `tools.prepare_independent_intraday --nightly` module with that PC's existing datastore, profile and watchlist arguments. It reuses the saved local 15-minute binding and reports `PREPARED_MANUAL_START_ONLY`. It does not scan legacy traders, call a broker/provider, train, start a worker or enable trading. Run it independently of Gameplan so its outcome cannot delay synthesis.

The human explicitly starts `ml.intraday.live_session --live` through the existing local launcher and bindings. Without `--live`, the entry point only reports local preparation information. No repeated human approval is required for nightly preparation; manual start remains the only human action needed to begin trading.

After manual start, each trader checks current broker capacity and quotes, manages its own exact order identities, retains its own fills and writes its own logs. Another trader's activity is not a reason to request its ledger, compatibility proof or status. Current broker account availability remains the source of actual capacity.

A one-time namespace setup is distinct from ordinary nightly preparation. It preserves original history and creates the local binding without starting trading. Do not repeatedly run migration or old-ledger scans at nightly wakes.

- [Atlas 15-minute trader](atlas/intraday.md)
- [Scout 15-minute trader](scout/intraday.md)
- [Standing policy](../coordination/independent-traders.md)
