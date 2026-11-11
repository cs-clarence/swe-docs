# Write the plan

## Scope

What a written plan contains, how it is kept while work runs, and what happens to it afterward. A plan is a temporary working document. The format and location are the project's choice: a document, an issue, a note, or a message all work. When a plan is needed and how large it is are in [plan a change](plan-a-change.md).

## Guidelines

### Keep the plan where the work and its readers can find it

Put the plan somewhere durable that anyone who works on or reviews the change can reach. A plan that lives only in your head cannot be checked, resumed, or corrected.

### Find where the plan belongs before writing it

Use the location the project names for plans. If it names none, use where the project already keeps similar plans. If there is no precedent, agree a location with the collaborators who will review the work, and record where the plan went.

### Cover the same points every time

Include the goal, what is in and out of scope, the approach, the steps, the risks, how each step is verified, how it is undone, and the open questions. A fixed set of points shows what is missing.

- **Goal:** the outcome wanted and how you will know it is reached ([state the goal and what done means](plan-a-change.md#state-the-goal-and-what-done-means)).
- **Scope:** what is included, and what is excluded on purpose.
- **Assumptions and open questions:** what you are taking as true without proof, and what still needs an answer, with who can answer it ([list assumptions and open questions](plan-a-change.md#list-assumptions-and-open-questions)).
- **Impact:** the components, callers, data, and users the work touches ([find what the change touches](plan-a-change.md#find-what-the-change-touches)).
- **Approach:** the chosen approach and the reason, with the options rejected when the decision is costly to reverse ([compare options before choosing](plan-a-change.md#compare-options-before-choosing)).
- **Steps:** the ordered steps and what each depends on ([break down work](break-down-work.md)).
- **Risks:** what could go wrong, how likely and how bad, and what you do about it. Name the riskiest part and when it is tested first.
- **Verification:** the check that shows each step is done ([plan verification and undo](plan-a-change.md#plan-verification-and-undo)).
- **Undo:** how each step is reversed, or why it cannot be.
- **Status:** what is done, in progress, changed, dropped, or blocked.

### Size the plan to the risk

Write sentences for Medium risk and a fuller document for High, as set in [match the plan to the risk](plan-a-change.md#match-the-plan-to-the-risk). Leave out points that do not apply, and say they were left out on purpose.

### Keep the plan current

Mark steps as done, changed, or dropped as work proceeds, and note why the plan changed ([update the plan when facts change](plan-a-change.md#update-the-plan-when-facts-change)). An outdated plan misleads the next reader more than no plan.

### Link the plan to the work while it is live

Point from the change to its plan while work is in progress, so reviewers and collaborators can find it. Record decisions that outlive the work as [decision records](../core/decision-records.md) instead of leaving them in the plan.

### Distill what lasts, then discard the plan

When the work is done or abandoned, move whatever stays useful to where readers will look for it, and delete the plan. Plans describe intent, and left behind they go stale and contradict the code.

- Reasons for a costly or surprising decision: a [decision record](../core/decision-records.md).
- Why a piece of code is the way it is: a comment next to that code.
- How the system is structured or used: the project's overview and reference docs.
- Changes users or integrators must know about: user-facing docs and release notes.
- Follow-up work and known gaps: the project's backlog.

If nothing in the plan is needed after the work, discard it whole.

## Exceptions

Low-risk work needs no written plan. A project may set its own format, as long as the points above are covered. Keep a plan beyond the work only when the project has a reason to, such as a recurring procedure, and then treat it as documentation.
