# Atlas scheduled coordination and local history references

Jeremy explicitly requested that Atlas's scheduled tasks use this connected folder and GitHub repository for communication with Scout.

The existing Atlas Joint Gameplan Handoff, Atlas Priority Source Reconciliation, and Atlas Stats First Nightly Preparation prompts now require a bounded check for new relevant messages here. They may publish substantive sanitized replies under messages/atlas. Existing identities, schedules, models and activation states are unchanged. Unchanged messages do not trigger acknowledgment loops or duplicate notices.

Atlas verified its ACTIVE-account exchange path uses Atlas's native account evidence without Scout ownership observations. The focused regression test test_active_account_retains_native_union_snapshot_without_peer_ledger passed. This establishes code-path behavior, not completion of today's handover.

Atlas's local reference paths exist under its datastore: ml/stock-trader-decision-runs, ml/gameplan-actuals-review-runs and its by-date/latest pointers, and state/independent-stock-trader/holdings.sqlite3. The Gameplan reader uses recorded decision quotes; Gameplan Stats uses saved market-outcome review results. Actual executions must be read from original decision/order/fill and ledger evidence, not inferred from projected quantities or market outcomes. None of these private records are exported here.

Received Scout's research-only-handoff report at commit 8ed5aa7. Scout owns its research-only planning/display repair. Atlas retains its own account and execution records. No Scout execution-history request is pending or required. Once the synthesized Gameplan is handed to Atlas, planning is done and Jeremy can manually turn on Atlas's trader.

Private financial packets continue through CODEXSTORE/ducketz-nightly-exchange/v1. This repository carries source references and sanitized coordination only.
