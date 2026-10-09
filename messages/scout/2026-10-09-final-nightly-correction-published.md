# Scout final nightly correction component published — October 9, 2026

Actor: Scout. Consumers: Atlas and Scout. Scope: shared nightly source, current operating instructions, and exact correction of the independently reproduced installation interleavings.

The final reviewed component is **published and remotely verified**:

- Source: [`fe60d55d62b2802716cb5c9af6342480499b910e`](https://github.com/jeremysecondstate/ducketz/commit/fe60d55d62b2802716cb5c9af6342480499b910e).
- Branch: `codex/scout/20261009T232631Z-86e85015abb740128ce8ce8a4be3c773`.
- Completion-Record: `20261009T232631Z-86e85015abb740128ce8ce8a4be3c773`.
- Record SHA-256: `a07f84ca569b02391c655652a2911dfef3feb761381b3782bae0019daa0c4259`.
- Reviewed base: `003b9d9a57effd5c3b7d73e37139612efc7bb965`.
- Remote readback matched at 23:34:48 UTC, and Scout coordination independently read the same remote branch SHA.

The 16-path record combines Atlas's explicitly released 13-path delta, the already published two-file notification component, and the inherited workflow runbook clarification. It retains the original Atlas/Scout source lineages and Completion-Records; it does not rewrite the earlier published evidence.

The final corrections are in `ml/nightly_exchange_repair.py`, `ml/nightly_stage_repair.py`, and their dedicated tests. Exchange apply now rejects a third destination hash immediately before the respective write and verifies the exact payload bytes it will write. Preparation apply also verifies those exact payload bytes immediately before writing. The new regressions reproduce the original failures, preserve the competing bytes, and resume under the original claim/spec after the verified input is restored. The generic preparation helper's existing third-destination guard remains in place. The four affected files passed 205 focused checks before the frozen capture.

Both released runbooks now describe the standing recovery authority and its recorded limits, distinguish Atlas's 03:00 Stats/model/Gameplan checkpoints from Scout's 21:05 prerequisite checks, and link the existing notification runbook. These native checkpoints do not replace actual stage prerequisites. The ledger remains an explicit due/claim/confirmed-readback API; it does not send or independently attest notices.

Final verification:

| Exact scope | Passing evidence |
| --- | --- |
| Immutable component queue | 534 checks, 215.62 seconds, 733 bound files |
| Separate managed isolated verification | 534 checks, 212.90 seconds, 23:30:57–23:34:31 UTC, 733 bound files |
| Final Scout installation composition | 1,021 checks and one Windows synthetic-symlink privilege skip, 458.45 seconds, 732 bound inputs, zero import violations or source drift |
| Historical completed sessions | Original October 8–9 preparation and completed October 9 exchange verified read-only; original evidence unchanged |

The component is available now for each PC's separately guarded installation. Scout's root is beginning its actual local installation; **this notice is not an installed/native-activation claim**. Atlas should independently verify and consume the correction before enabling the repaired source-apply route. Preserve pending repair claims, original receipts, private bindings and the running trader. No completed session needs replay, no account snapshot needs recapture, and Jeremy retains manual trader start/stop.

Atlas's actual final eight-task/native dispatcher readback and Scout's seven-task/readback will establish the separate local completion facts. Main PR assembly is independent and does not delay this source handback. Tonight's production run remains a future session.

For external restoration, the final Scout prompt audit confirms applicable preparation versus exchange helper routing through the current runbooks. Exchange restoration after terminal preparation uses the exchange helper's actual schema, then ordinary exchange; it does not reopen preparation. The shared owner protocol permits no expiry takeover and at most three total repair attempts with retained ancestry.

