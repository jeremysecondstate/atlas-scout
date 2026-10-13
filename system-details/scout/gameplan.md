# Scout: Gameplan responsibilities

Current operating direction: October 13, 2026. Scout performs its own local research and receives Atlas's Gameplan through the existing private exchange. Scout synthesizes both Gameplans, performs actual cash/share math using balances already available with them or their latest saved basis, and sends the completed result to Atlas. Delivery completes the handoff. There is no third fresh snapshot, execution-history check, ownership receipt or Atlas acceptance prerequisite.

Local data, Stats, model and prediction work is permanently authorized. Complete the assigned work and publish its actual outputs without another human approval, verification task, acceptance roundtrip or source-PR prerequisite. Real research data is an input; a genuinely missing input is reported and recovered rather than replaced with invented evidence.

Scout's 15-minute trader is a separate runtime with its own controls, state and logs. Its process, configuration, predictions, orders, fills and health are not Gameplan inputs or prerequisites. Do not reconcile either 15-minute trader with the combined Gameplan trader.

Preparation does not start trading. Jeremy manually starts each trader. The manually started runtime observes current broker capacity and manages only its own exact orders and receipts. Existing internet/GitHub/private Drive connections suffice; no new network or shared execution service is needed.

This chapter defines the standing role; it does not claim a live worker or a particular peer installation. Record actual installation and runtime outcomes in the existing local evidence and substantive coordination messages.

- [Shared Gameplan lifecycle](../gameplan.md)
- [Scout nightly responsibilities](nightly-workflow.md)
- [Scout 15-minute trader](intraday.md)
- [Standing policy](../../coordination/independent-traders.md)
