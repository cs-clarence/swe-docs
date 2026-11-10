# Large work

## Scope

Work across many components or involving many collaborators, or hard to undo, or lasting weeks: migrations, replacements, and large features. Mechanics for migrations and replacements are in [large changes](../large-changes.md).

## Guidelines

### Write the plan and record the decisions first

Record the goal, the end state, the approach, the options rejected, and the risks before the first step ([plan a change](../plan-a-change.md), [decision records](../../core/decision-records.md)). Large work drifts without a stated destination.

### Test the riskiest assumption first

Run a prototype or a thin slice through the part most likely to break the plan, and let the result change the plan. Finding the flaw after building around it is the costliest outcome.

### Deliver in thin end-to-end slices

Cut by outcome, so each slice works and can ship ([break down work](../break-down-work.md)). Layer-by-layer work delivers nothing until the end.

### Release in stages that can be reversed

Ship behind a switch or to a subset, and keep the old path until the new one is proven ([large changes](../large-changes.md)). Each stage needs a way back.

### Agree ownership and interfaces up front

Name who owns each part, even if one person owns all of them, and agree the contracts between them before parallel work starts. Parallel work on unsettled contracts has to be redone.

### Track progress against the end state

Keep a visible list of what is done, what is left, and what is blocked, including removal of what is replaced. Work that stalls halfway leaves two systems.

### Replan at each milestone

At each milestone, compare the plan with what you learned and revise the remaining steps. Say what changed.

### Tell the people affected

Inform those whose work depends on the change before it starts and before each switch. Surprises on shared systems cost the most trust.

## Exceptions

A large change in an area that no one else uses may reduce coordination steps. State why.
