# Self-review

## Scope

What an author does before asking anyone else to review. It applies the same standards a reviewer would.

## Guidelines

### Read the change as a reviewer would

Read the whole change from the start, as a stranger. Authors see what they meant; reviewers see what is there.

### Run the checks for what you touched

Apply the review checks for the areas you touched, at the change's [risk tier](../core/risk-tiers.md), and fix findings before others see them. Review time is better spent on what you could not see yourself.

### Remove what does not belong

Delete debugging aids, unrelated edits, and dead code ([separate unrelated work](approach.md#separate-unrelated-work)).

### Confirm each claim with evidence

For every statement in the description, such as "fixes X" or "no behavior change", know what shows it is true.

### Mark the riskiest part

Say where you are least sure and what you did not verify, so reviewer attention goes there ([explain the result](approach.md#explain-the-result)).

### Split what is too big

If the change has several purposes or is hard to hold in mind, split it ([change size](change-size.md)).

## Exceptions

For a Low-risk change, a single read-through is enough.
