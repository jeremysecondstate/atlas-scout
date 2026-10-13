# Gameplan lifecycle

Operating policy updated October 13, 2026. [The standing human direction](../coordination/independent-traders.md) defines a combined Atlas–Scout Gameplan and three independent traders.

## Research and synthesis

Atlas and Scout each perform their established local data, Stats, model and prediction work for their own research symbols. Their Gameplan contributions are the only cross-PC trading-plan inputs. Scout combines those Gameplans using balances already available with them or their latest saved basis, performs the actual cash/share calculations, and sends the combined Gameplan and associated views to Atlas. Delivery completes the handoff. Preserve the basis observation time without requesting a third fresh snapshot or waiting for Atlas acceptance.

The combined Gameplan covers the existing Gameplan symbol universe and horizons. Its forecasts, intended quantities, planning prices and Stats are planning records. Actual orders and fills appear only after Jeremy manually starts Atlas's combined Gameplan trader.

## Automatic publication

Nightly preparation, exchange and synthesis are permanently authorized. Publish the completed result directly; do not wait for another human approval, reciprocal acceptance, loaded-code attestation, extra verification task, source-PR state or a 15-minute readiness result.

Both real research contributions are calculation inputs. If either is genuinely unavailable, preserve completed work, identify the missing input and continue the existing authorized recovery. Do not fabricate a contribution or turn missing data into an approval request.

## Independent execution

Atlas's Gameplan trader uses only its own plan, control, orders, fills and ledger. It does not inspect either 15-minute trader's process, configuration, data, ledger, reservations or health. The 15-minute systems have no Gameplan synthesis role and no reciprocal execution dependency.

On a manual start, the Gameplan trader handles current broker capacity, its own exact orders and its own logging. Preparation does not activate it. Existing account connectivity is sufficient; no shared execution service or new network is needed.

## Evidence and history

Source review/tests and source-publication privacy rules remain separate engineering responsibilities. Describe prepared, published, installed and running outcomes accurately; this policy page is not a claim about either PC's current process state.

- [Atlas Gameplan](atlas/gameplan.md)
- [Scout Gameplan contribution](scout/gameplan.md)
- [Nightly workflow](nightly-workflow.md)
- [Independent 15-minute systems](intraday.md)
- [Historical records](history.md)
