# Medium work

## Scope

Work across a few components or modules, or a fix that needs investigation, with some unknowns. Effects are contained and each step can be reviewed. Larger or harder to undo is a [large work](large-work.md).

## Guidelines

### Understand the affected area before choosing an approach

Read the callers, tests, and neighbors of what you will change, and confirm how it behaves today. A plan built on assumed behavior breaks on contact with the real code.

### Write a short plan first

Record the goal, the approach, the steps, the risks, and how each step is verified ([plan a change](../plan-a-change.md)). A paragraph or list in the description is enough.

### Settle the interfaces before the internals

Decide how the parts connect before building either side. Changing a contract after both sides exist costs the most.

### Break it into two to five reviewable steps

Order the steps by dependency and risk, with preparation first ([break down work](../break-down-work.md)). Each step should be judged as one unit.

### Verify each step as you go

Check each step before starting the next, so a fault is found where it was introduced. Testing only at the end makes the cause hard to find.

### Show an early step to a reviewer

Share the plan or the first step before finishing everything. Disagreement is cheapest to resolve early.

### Escalate when it grows

If the work reaches a contract, persistent data, or many components, or cannot be undone cheaply, treat it as a [large work](large-work.md).

## Exceptions

Medium work that is routine and well understood may use a plan of a few lines.
