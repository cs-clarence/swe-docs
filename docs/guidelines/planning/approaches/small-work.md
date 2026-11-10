# Small work

## Scope

A quick fix or small feature: one component, contained effects, easy to undo, behavior already understood. Not for work that touches a contract, persistent data, or a second component.

## Guidelines

### Confirm the problem before changing anything

Reproduce the defect or restate the need in one sentence. A fix for a misunderstood problem is the most common small-work mistake.

### Plan in a sentence

State the goal and the intended change in a sentence or two, in your head or in the description. A longer plan costs more than the change.

### Make one change with one purpose

Do only the fix or the feature. Note other problems you see instead of fixing them in the same change.

### Check it with something that would fail without it

Run or add a check that fails before the change and passes after. Without that, you do not know the change does anything.

### Move up a kind when it grows

If the change reaches a contract, data, or a second component, or takes much longer than expected, stop and treat it as a [medium work](medium-work.md). If it also meets a [trigger to ask](../../core/when-to-ask.md#stop-and-ask-when-the-work-is-bigger-or-different-than-agreed), stop and ask.

## Exceptions

A trivial change, such as a typo or a comment, needs no check beyond reading it.
