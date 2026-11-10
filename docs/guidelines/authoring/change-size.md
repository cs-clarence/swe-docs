# Change size

## Scope

How big one change should be and how to split it. Applies when planning work and before asking for review.

## Guidelines

### Keep a change small enough to review

Limit a change to what a reviewer can hold in mind and judge as one unit, with one purpose describable in a sentence ([separate unrelated work](approach.md#separate-unrelated-work)). One bad part of a mixed change blocks the rest.

### Split by purpose, not by file type

Make each part stand alone: it works, passes its checks, and can be accepted or reverted on its own. A split into "all tests" and "all code" leaves neither reviewable.

### Put preparation first

Order parts as preparatory restructuring, then the behavior change, then cleanup ([keep structure and behavior changes apart](structure/refactoring.md#keep-structure-and-behavior-changes-apart)). Each kind of change is then seen in isolation.

### Keep together what only works together

Do not split parts that are unsafe or meaningless alone, such as a signature change and its callers. Say why they are together.

### Separate mechanical change from logic

Keep renames, formatting, and regenerated output apart from hand-written logic, and say how they were produced or checked ([generated and vendored code](generated-and-vendored-code.md)).

### Plan work too big for one change

Break it into steps that each leave the system working ([large changes](structure/large-changes.md)).

## Exceptions

Urgent fixes may be larger than ideal. State what was not separated.
