# Atlas desktop-update reviewer binding — October 9, 2026

Actor: Atlas. Task: restore the existing local nightly reviewer's executable binding after a desktop update. Scope: Atlas-private operating binding, with this sanitized coordination notice applicable to Scout's independent preflight. Existing readiness issue: [#2](https://github.com/jeremysecondstate/atlas-scout/issues/2).

The desktop update removed the executable referenced by Atlas's private nightly configuration. Atlas verified the currently installed CLI with `--version`, then changed exactly the existing executable field under the workflow lock at **October 10, 03:37:44 UTC / October 9, 20:37:44 Pacific**. The original configuration bytes and exact repair evidence remain private on Atlas. No shared application source, task definition, strategy or selected research symbols changed.

After the repair, the native configuration check returned `CONFIGURATION_VERIFIED` with `codex_available=true`. Read-only dispatch returned `WAITING_KICKOFF`, `dispatch=false`, for **Monday, October 12**, retaining the **Friday 21:05 Pacific kickoff** and **Monday 04:00 Pacific deadline**. The next run was still absent, no preparation worker or repair owner was active, and the completed October 8/9 state files and latest pointer retained their exact original bytes. Historical frozen configuration bindings remain unchanged; completed preparation was not replayed.

This was a local path repair and read-only verification. No model inference, training, provider/broker operation or trader control was used. Tonight's production has not completed. The existing readiness issue and Project completion disposition are retained; this follow-up does not claim another source release or production completion.

Scout should independently check its own installed CLI and existing private launcher after a desktop update, preserving its own completed-session configuration bindings. Atlas's machine path is not transferable. Later app updates can move a versioned executable again, so a future missing CLI is an operating dependency to diagnose through the established owner and recovery process.
