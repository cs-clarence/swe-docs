# Approach

## Scope

Any change: feature, fix, or refactor. Activities, not a mandated sequence; skip what the [risk tier](../core/risk-tiers.md) makes unnecessary.

## Guidelines

### Check local rules first

Read the repository's instructions and [overrides](../core/precedence.md#overriding-rules) before changing anything. They outrank these guidelines.

### Understand before changing

Read the code, its callers, and its tests, and confirm current behavior before editing. Changes made on assumptions about existing behavior cause regressions.

### Define the scope

State what the change must achieve and what it will not touch ([plan a change](../planning/plan-a-change.md)). If the goal is ambiguous and a wrong guess is costly, ask; otherwise state the assumption and proceed.

### Make the smallest sufficient change

Change only what the goal requires. Fix the cause, not the symptom, unless a stopgap is explicit and temporary.

### Separate unrelated work

Do not mix refactors, formatting, or fixes for other problems into the change ([change size](../planning/change-size.md)). Mention them instead. Mixed changes are hard to review and hard to undo.

### Preserve behavior in refactors

A refactor must not change observable behavior. If behavior must change, treat it as a feature or fix and verify accordingly.

### Verify the result

Run the checks that exercise the change: tests, build, linter, or manual use, scaled to risk. For a fix, confirm the failure existed before and is gone after.

### Explain the result

Describe what changed, why, how it was verified, and what remains unverified or risky. Detail scales with the risk tier.

## Exceptions

Urgent fixes may compress these activities. Still state what was skipped and why, and follow up.
