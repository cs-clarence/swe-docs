# Break down work

## Scope

Splitting planned work into steps and ordering them. Applies when work is too large or uncertain to do in one move. Deciding what to build is in [plan a change](plan-a-change.md).

## Guidelines

### Split by outcome, not by layer

Make each step deliver something that works end to end, however thin. Steps cut by layer or file type (all storage, then all interface) deliver nothing until the last one finishes.

### Make each step verifiable on its own

Give every step a stated check that shows it is done, and keep it to one purpose. A step you cannot check cannot be finished with confidence.

### Order by risk and dependency

Do prerequisites first, and unknowns before the work that relies on them. Put preparation ahead of behavior change, so each kind of change is seen separately.

### Make dependencies explicit

Say which steps need another's result and which are independent. Independent steps can be reordered, parallelized, or dropped without breaking the rest.

### Keep every step safe to stop after

Leave the system working after each step, so work can pause or be abandoned at any boundary. If a step cannot meet this, group it with the steps it needs and say why.

### Size steps to what can be reviewed

Keep a step small enough to be judged as one unit by a reviewer. If a step cannot be explained in a sentence, split it again.

### Revisit the breakdown as you learn

After each step, check that the remaining steps still fit what you now know. Reorder, merge, or drop steps rather than follow the original list.

## Exceptions

Work small enough for one safe step needs no breakdown. Steps that are unsafe alone, such as a signature change and its callers, stay together; state why.
