# Plan a change

## Scope

Deciding what a change will do, how, and how it will be checked, before work starts. Applies to anyone planning, human or agent, alone or with collaborators. Order and size of steps are in [break down work](break-down-work.md).

## Guidelines

### Match the plan to the risk

Plan in proportion to the [risk tier](../core/risk-tiers.md): none for Low, a few sentences for Medium, a written plan for High ([choose the approach](approaches/choose-the-approach.md)). Planning that costs more than the change protects against is waste.

### State the goal and what done means

Say what must be true when the change is finished, and what is out of scope ([definition of done](../core/definition-of-done.md)). A plan without a finish line cannot be checked.

### List assumptions and open questions

Write down what you believe but have not confirmed, and what you do not know. Ask about the ones where a wrong guess is costly; mark the rest as assumptions and proceed.

### Find what the change touches

Name the components, callers, data, and users the change can affect before choosing an approach. Missed dependents become regressions.

### Compare options before choosing

For a decision that is costly to reverse, list at least two options with their costs, choose one, and give the reason ([decision records](../core/decision-records.md)). For a routine choice, pick the simplest option that meets the goal.

### Tackle the riskiest part first

Identify the part most likely to invalidate the plan, such as an unknown or an unproven assumption, and test it early with the smallest experiment that answers the question. Learning it late wastes the work built on it.

### Plan verification and undo

Say how each outcome will be verified and how the change will be undone or contained if it fails. Detail scales with the risk tier. For High risk, name the failure you are guarding against.

### Get the plan reviewed before building

At High risk, or when the plan is costly to change later, have a collaborator read the plan before work starts. Working alone, re-read it after a break, as a stranger would. Correcting a plan costs far less than correcting a finished change.

### Update the plan when facts change

When work shows an assumption was wrong or the scope has grown, revise the plan and say so. Do not continue silently on a plan that no longer matches the work.

## Exceptions

Urgent fixes may plan after the fact. State what was decided and why once the situation is stable.
