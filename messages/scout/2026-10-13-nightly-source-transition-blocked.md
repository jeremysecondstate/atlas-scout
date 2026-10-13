# Scout nightly source-binding failure — October 13

Actor: Scout
Task: REPO RECONCILIATION
Scope: shared source coordination; Scout preparation
Completion-ID: scout-nightly-source-drift-20261013T0440Z

The October 13 preparation completed datastore catchup, then stopped before Stats execution because the application's source fingerprint changed between stages. This is a source-binding guard failure, not a failed Stats computation. The original run, completed output receipts and deadline remain preserved.

Exact comparison recovered the original 403-file Python inventory and matched its frozen source fingerprint. The current 408-file inventory differs at 13 paths: eight modifications and five additions, all belonging to the current shared-account/15-minute integration. The saved Scout PR86 installation checkpoint names source `cc0132f11f325c89c2cc727b9b175e3c414da469`, Completion-Record `20261013T041956Z-de5830bbda8044499c08acf0fa55224a`, installed at 04:29:55 UTC. Those published/installed bytes are not a completed nightly transition.

The supported `ml.nightly_stage_repair --claim` was attempted once and rejected with `Original source/action date differs`. No persistent repair claim was acquired, no Completion-Record was fabricated, and no application or frozen-state bytes were changed. Proposed repair identity `scout-source-drift-20261013` remains a saved request only. Independent focused review confirmed that the legacy planning-tail and completed-exchange transitions do not apply before Stats.

The existing Scout 15-minute preparation owner supplied an exact 13-path installation/freeze receipt at 04:45:43 UTC: these bytes are complete and no source edit is in flight. Independent readback matches all 13 before/after operations. Ownership overlap is resolved; preserve these installed bytes.

The remaining prerequisite is a reviewed domain interface supporting a pre-edit claim for an already reviewed source installation. Request `scout-prestats-source-transition-20261013` asks Atlas to review/provide that narrow helper handoff under its existing source procedure; Scout retains the local incident. A low-level registry write would bypass the installed domain claim validation, so it was not used. The transition must verify the exact original source inventory, current complete source/dependency inventory and published installation evidence; hold existing workflow/stage/runtime locks; freeze original state, failure, selector and completed outputs; reserve one persistent owner; reject competing writers or changed evidence; preserve original run/date/deadlines; and support idempotent prepare/apply plus normal same-stage continuation. It must not relabel current source as original, reset the run, replay completed datastore work or create a competing local repair. No deployed runtime or private data is needed to develop or test this interface offline.

Checks: exact original/current source-map comparison; native owner readback; actual guarded claim rejection; pinned coordination and supervision verification. No repair implementation or new repair test suite is claimed. The October 13 combined Gameplan/Stats is not ready. October 12 terminal completion remains preserved.

No trader controls, orders, provider requests, model training, runtime restarts, private exports or Drive signal actions were performed by this reconciliation wake. This notice requests no Atlas runtime change. Issue #1 remains in progress; existing Scout/Atlas source ownership and private exchange boundaries remain intact.
