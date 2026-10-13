# Atlas: Nightly responsibilities

Current operating direction: October 13, 2026. Use Atlas's existing native schedules, installed Python/runtime paths, private datastore and local symbol profile. Do not copy Scout's bindings or invent a new schedule.

| Responsibility | Completed work |
| --- | --- |
| Local preparation | Finish the existing data, Stats, model, prediction and local Gameplan work for the intended action date. |
| Gameplan contribution | Publish Atlas's real research output to the existing private Gameplan exchange. |
| Combined Gameplan | Combine Atlas and Scout contributions locally and publish the combined Gameplan immediately when the inputs are available. |
| Local 15-minute preparation | Independently prepare Atlas's saved local 15-minute binding for a human manual start. Its outcome never gates Gameplan. |
| Notifications | Report meaningful completion, concrete faults and recovery without duplicate acknowledgments. |
| Source coordination | Carry out owned source handoffs/publication through the separate reviewed GitHub procedure. |

Every assigned preparation and recovery action above is already authorized. Do not insert a new approval, verification, compatibility or reciprocal-acceptance stage. Use actual calculation inputs and keep real source/action dates and creation times. Continue authorized repair of genuine missing-input or worker failures while preserving usable completed work and healthy workers.

Normal independent 15-minute preparation uses `python -B -m tools.prepare_independent_intraday --nightly` with Atlas's own datastore/profile/watchlist arguments. It uses the existing local binding and does not read Gameplan state, the peer's state or legacy ledgers. Do not run a migration each night.

Jeremy manually starts trading. Nightly responsibilities never start/restart traders, enable controls or place/cancel orders to test readiness. Existing internet, authenticated GitHub and private Drive/CODEXSTORE are sufficient; no VPN, LAN/private gateway or shared broker authority is needed.

See [shared nightly work](../nightly-workflow.md), [Atlas's task responsibilities](scheduled-tasks.md), [notifications](../../coordination/runbooks/nightly-notifications.md) and [historical inventories](../history.md). This page specifies current responsibilities without asserting a fresh native registration or process observation.
