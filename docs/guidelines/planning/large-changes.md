# Large changes

## Scope

Work too big for one safe step, such as migrations, replacements, and wide renames. Work that fits one safe step needs no plan beyond [plan a change](plan-a-change.md).

## Guidelines

### Split into steps that each leave the system working

Cut along what can be released, not along file counts. Every step then ships, and any step can be the last ([break down work](break-down-work.md)).

### Build the new path beside the old

Add the new implementation next to the old, switch over, then remove the old. Replacing in place has no safe midpoint.

### Keep old and new in agreement

While both exist, compare their results on tests or real inputs so differences show before the switch.

### Make the end state visible

State what done means and what is left, including removal of the old path. Migrations that stall halfway leave two systems to maintain.

### Remove the old path

Delete the old code and data when the switch is complete.

### Agree the plan before the first step

Record the plan and the reasons for High-risk work ([decision records](../core/decision-records.md)) so the steps stay consistent over time ([plan a change](plan-a-change.md), [break down work](break-down-work.md)).

### Keep every step reversible or safe to stop

Each step is undoable, or leaves a safe state if work halts.

## Exceptions

A small codebase or private component may change in one step. State why that is safe.
