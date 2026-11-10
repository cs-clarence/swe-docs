# Medium work

## Scope

Work across a few components or modules, or a fix that needs investigation, with some unknowns. Effects are contained and each step can be reviewed. Larger or harder to undo is a [large work](large-work.md).

## Guidelines

### Understand the affected area before choosing an approach

Read the callers, tests, and neighbors of what you will change, and confirm how it behaves today. A plan built on assumed behavior breaks when it meets the real code.

### Write a short plan first

Record the goal, the approach, the steps, the risks, and how each step is verified ([plan a change](../plan-a-change.md)). A paragraph or list in the description is enough.

### Settle the interfaces before the internals

Decide how the parts connect before building either side. Changing a contract after both sides exist costs the most.

### Break it into two to five reviewable steps

Order the steps by dependency and risk, with preparation first ([break down work](../break-down-work.md)). Each step should be judged as one unit and checked before the next begins.

### Move up a kind when it grows

If the work reaches a contract, persistent data, or many components, or cannot be undone cheaply, treat it as a [large work](large-work.md). If it also meets a [trigger to ask](../../core/when-to-ask.md#stop-and-ask-when-the-work-is-bigger-or-different-than-agreed), stop and ask.

## Exceptions

Medium work that is routine and well understood may use a plan of a few lines.
