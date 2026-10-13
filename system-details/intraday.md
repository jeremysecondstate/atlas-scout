# Independent 15-minute traders

Atlas and Scout each generate, trade and log their own local 15-minute predictions. Neither consumes a combined 15-minute plan. There is no distributed grant, peer approval, Gameplan loaded-code proof, shared trading ledger or cross-trader reconciliation.

Atlas's documented implementation uses its own `intraday/execution` configuration and databases. Scout's installed broker-local executor uses its own `intraday/scout` books, journal and `execution.lock`, with account identity obtained directly from its existing broker at manual start. Each retains its own manual-session control and local forecasting logs. Existing mixed-ledger history remains preserved as historical evidence; it is not replayed into the independent epoch or read by normal preparation.

## Nightly preparation and manual start

Use each PC's existing installed local preparation entry point. Atlas documents `tools.prepare_independent_intraday --nightly`; Scout uses the broker-local executor and offers `ml.intraday.scout_prestart` as an optional offline diagnostic. Do not copy the other PC's implementation or add a diagnostic result as a startup prerequisite. Local preparation does not scan other traders, call brokers/providers, train, start a worker or enable trading. Its outcome cannot delay Gameplan synthesis.

The human explicitly starts `ml.intraday.live_session --live` through the existing local launcher and bindings. Without `--live`, the entry point only reports local preparation information. No repeated human approval is required for nightly preparation; manual start remains the only human action needed to begin trading.

After manual start, each trader checks current broker capacity and quotes, manages its own exact order identities, retains its own fills and writes its own logs. Another trader's activity is not a reason to request its ledger, compatibility proof or status. Current broker account availability remains the source of actual capacity.

Preserve each implementation's original history and local books. Scout needs no cross-trader migration or Gameplan configuration; it binds to its existing broker at the manual start. Do not run migration or old-ledger scans at nightly wakes.

- [Atlas 15-minute trader](atlas/intraday.md)
- [Scout 15-minute trader](scout/intraday.md)
- [Standing policy](../coordination/independent-traders.md)
