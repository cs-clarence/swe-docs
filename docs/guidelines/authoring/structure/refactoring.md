# Refactoring

## Scope

Changing structure without changing observable behavior. Excludes behavior changes ([approach](../approach.md#preserve-behavior-in-refactors)).

## Guidelines

### Pin behavior before restructuring

Make sure tests cover the behavior you will preserve, and add characterization tests where they are missing. Without them, you cannot show behavior is unchanged.

### Change in small, verifiable steps

Keep each step small enough to verify on its own, and verify after each one. A failure then points to one step.

### Keep structure and behavior changes apart

Do not mix a refactor with a behavior change in the same step. If both are needed, do the refactor first. A mixed change cannot be reviewed for either.

### Refactor for a stated purpose

Name what the change makes easier: an upcoming change, a defect class, or a readability problem. Restructuring with no purpose adds risk and no value.

### Stop when the purpose is met

Do not continue into unrelated cleanup. Note further candidates instead ([separate unrelated work](../approach.md#separate-unrelated-work)).

### Update every caller and reference

Move or rename completely: callers, docs, and configuration. A half-finished move leaves two ways to do one thing.

## Examples

Renaming a function: update all callers and references in the same change, with no behavior edits. A bug found on the way gets its own change.

## Exceptions

An urgent fix may change structure and behavior together when separating them is impractical; say so and verify both.
