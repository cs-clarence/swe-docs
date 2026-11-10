# Large work

## Scope

Work across many components or involving many collaborators, or hard to undo, or lasting weeks: migrations, replacements, and large features. Mechanics for migrations and replacements are in [large changes](../large-changes.md).

## Guidelines

### Write the plan and record the decisions first

Record the goal, the end state, the approach, the options rejected, and the risks before the first step ([plan a change](../plan-a-change.md), [decision records](../../core/decision-records.md)). Large work drifts without a stated destination.

### Define an example that exercises the hard parts

Write a worked example that covers the system's complexity and make working against it the goal ([define an example the finished work must handle](../plan-a-change.md#define-an-example-the-finished-work-must-handle)). Without one, each part can pass its own tests while the whole misses the point.

### Test the riskiest assumption first

Run a prototype or a thin slice ([tackle the riskiest part first](../plan-a-change.md#tackle-the-riskiest-part-first)) through the part most likely to break the plan, and let the result change the plan. Finding the flaw after building around it is the costliest outcome.

### Deliver in thin end-to-end slices

Cut by outcome, so each slice works and can ship ([break down work](../break-down-work.md)). Layer-by-layer work delivers nothing until the end.

### Release in stages that can be reversed

Ship behind a switch or to a subset, and keep the old path until the new one is proven ([large changes](../large-changes.md)). Each stage needs a way back.

### Agree ownership and interfaces up front

Name who owns each part, even if one person owns all of them, and agree the contracts between them before parallel work starts. Parallel work on unsettled contracts has to be redone.

## Exceptions

A large change in an area that no one else uses may reduce coordination steps. State why.
