# Large changes

## Scope

Work too big for one safe step, such as migrations, replacements, and wide renames. Splitting into steps that each leave the system working is in [break down work](break-down-work.md), and the plan is in [plan a change](plan-a-change.md). Work that fits one safe step needs no plan beyond that.

## Guidelines

### Build the new path beside the old

Add the new implementation next to the old, switch over, then remove the old. Replacing in place has no safe midpoint.

### Keep old and new in agreement

While both exist, compare their results on tests or real inputs so differences show before the switch.

### Make the end state visible

State what done means and what is left, including removal of the old path. Migrations that stall halfway leave two systems to maintain.

### Remove the old path

Delete the old code and data when the switch is complete.

## Exceptions

A small codebase or private component may change in one step. State why that is safe.
