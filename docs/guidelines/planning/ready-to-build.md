# Ready to build

## Scope

How to decide that a plan or design document is ready to build from. Meant for new systems and large features. Smaller work needs no gate beyond the checks in [plan a change](plan-a-change.md). Ready means safe to start, not finished: the plan still changes as facts appear ([update the plan when facts change](plan-a-change.md#update-the-plan-when-facts-change)). Applies to plans, and to [design docs](design-docs.md) where one exists.

## Guidelines

### Test whether someone else could start without asking

Check that a person who did not write the document could begin the first step without asking you anything. Every question they would have to ask marks a gap to close first.

### Make the goal, scope, and finish line checkable

State the outcome, what is excluded, and a check that shows the work is done ([state the goal and what done means](plan-a-change.md#state-the-goal-and-what-done-means)). For a new system or large feature, that check is a worked example of the hard parts ([define an example the finished work must handle](plan-a-change.md#define-an-example-the-finished-work-must-handle)). If you cannot tell when the work is finished, you cannot tell when it has drifted.

### Leave no open question that blocks the first step

Open questions may remain where the answer will not change what is built next, and each needs an owner. Check or name a way to check each assumption ([list assumptions and open questions](plan-a-change.md#list-assumptions-and-open-questions)). A blocking question found midway costs the work already done.

### Deal with the riskiest part first

Have the riskiest part tested, or make it the first step ([tackle the riskiest part first](plan-a-change.md#tackle-the-riskiest-part-first)). A plan that postpones its biggest unknown is not ready.

### Give every step a check and an undo

Each step has a stated check and a way back, or a reason it has none ([plan verification and undo](plan-a-change.md#plan-verification-and-undo)). The first step is concrete enough to start now.

### Decide the costly choices before starting

Make and record decisions that are costly to reverse ([compare options before choosing](plan-a-change.md#compare-options-before-choosing), [decision records](../core/decision-records.md)). Do not leave them "to decide while implementing", because by then work depends on them.

### Specify interfaces well enough to build compatible parts

For a design doc, give the interfaces and data shapes in enough detail that two people would build parts that fit ([cover the design, not the steps](design-docs.md#cover-the-design-not-the-steps)). Vague interfaces turn into disagreements after both sides exist.

### Match the gate to the size and risk

Apply all the tests to a new system or large feature. For medium work, the first three are enough, and small work needs no gate. A smaller change at High risk still gets the review its tier asks for ([get the plan reviewed before building](plan-a-change.md#get-the-plan-reviewed-before-building), [settle the design before building on it](design-docs.md#settle-the-design-before-building-on-it)). Gate effort scales with the size of the work and its [risk tier](../core/risk-tiers.md).

### Close the gap or ask when the gate fails

When a test fails, revise the document, or stop and ask if the answer is not yours to give ([when to ask](../core/when-to-ask.md#stop-and-ask-when-the-work-is-bigger-or-different-than-agreed)). Do not start in the hope of resolving it later.

## Exceptions

For an urgent fix, start with the gaps you can close fastest, say which remain, and close them as the work proceeds. For exploratory work, where the aim is to learn what the plan should be, a ready plan is the result and not the start.
