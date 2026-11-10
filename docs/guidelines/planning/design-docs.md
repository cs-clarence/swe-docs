# Design docs

## Scope

A design doc is the part of a plan that explains how something should work and why it should work that way. Write it after the goal and scope are clear and before the steps are fixed, since the steps depend on the design. It is optional. Most changes need no plan, and most plans need no design doc. When a plan is needed is in [plan a change](plan-a-change.md), and how a plan is kept is in [write the plan](write-the-plan.md).

## Guidelines

### Write a design doc only when the design is the hard part

Write one when a wrong design would be costly to reverse or hard to review from the change alone. Typical triggers:

- Decisions others will build on, such as public contracts, data models, or trust boundaries.
- Several plausible approaches with unclear trade-offs.
- Work across components or collaborators that must agree on interfaces first.
- Large unknowns, where writing the design exposes gaps cheaply.
- A new project or [large work](approaches/large-work.md), where the design is usually the first thing to settle.

Otherwise put the design in the plan, or skip the plan ([match the plan to the risk](plan-a-change.md#match-the-plan-to-the-risk)). A design doc written out of habit costs more than it saves.

### Cover the design, not the steps

State the problem and its constraints, the proposed design, a worked example that exercises the hard parts ([define an example the finished work must handle](plan-a-change.md#define-an-example-the-finished-work-must-handle)), the alternatives rejected and why, the interfaces and data, how it fails, how it is tested and rolled out, and what is still open. Leave step ordering and progress to the plan ([break down work](break-down-work.md)).

### Settle the design before building on it

Have a collaborator read the design, or re-read it yourself after a break, and resolve disagreements before work depends on it. Changing a design is cheapest while it is still a document.

### Say when the build departs from the design

If the work diverges from the design, update the design or note the change and the reason ([update the plan when facts change](plan-a-change.md#update-the-plan-when-facts-change)). A design that no longer matches the work misleads whoever reads it next.

### Distill the design when the work ends

Move what lasts into decision records, structure docs, and code comments, and discard the rest ([distill what lasts, then discard the plan](write-the-plan.md#distill-what-lasts-then-discard-the-plan)). The format and location are the project's choice.

## Exceptions

A project may keep a design doc as living documentation, and then maintains it like any other doc. For an urgent fix, write the design after the fact, or record only the decision.
