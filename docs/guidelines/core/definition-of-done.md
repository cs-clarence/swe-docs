# Definition of done

## Scope

What "done" means for a change, by [risk tier](risk-tiers.md). It sets the minimum, not a procedure.

## Guidelines

### Meet the bar for the tier

A change is done when everything in its tier's row below is true. Higher tiers include the lower rows.

### Leave nothing behind

Remove temporary code, update callers, documentation, and contracts the change affects, and record follow-ups instead of leaving them implied.

### Say what is not done

State what is unverified, deferred, or known to be wrong. A change that hides its gaps is not done.

### Base "done" on evidence

Done means checked, not believed. Point to the test, run, or inspection that shows it.

## Bar by tier

| Tier | Done when |
| --- | --- |
| Low | The change does what was intended and reads correctly. Nothing unrelated changed. The description says what changed. |
| Medium | Also: changed behavior and failure paths are verified. Affected callers, documentation, and contracts are updated. Unverified risks are stated. |
| High | Also: someone other than the author, or a separate agent, has examined it. Rollback or recovery is stated. Security, data, and compatibility effects are addressed. The decision is recorded if significant ([decision records](decision-records.md)). |

## Exceptions

Urgent changes may meet a lower bar. State what was skipped and when it will be done.
