# Planning for agents

## Scope

Extra rules for AI or automated agents that plan work. Agents also follow [plan a change](plan-a-change.md) and [break down work](break-down-work.md).

## Guidelines

### Explore without changing anything

While planning, only read. Do not edit files, run state-changing commands, or call external services until the plan is accepted or the [risk tier](../core/risk-tiers.md) lets you proceed without acceptance.

### Ground the plan in what you observed

Base the plan on code, documents, and results you have read, and mark each claim as observed or assumed. A plan built on guessed behavior fails when the guess is wrong.

### Ask instead of guessing

List open questions and put the ones where a wrong answer is costly to the user before presenting the plan. Do not fill gaps in the request with invented requirements.

### Present the plan in a fixed shape

State the goal, the approach, the steps, what is out of scope, the risks, how each step is verified, and how it is undone. Keep it short enough to read in one pass; detail scales with the risk tier.

### Wait for approval when the stakes require it

At High risk, or when the plan goes beyond what was asked, stop after presenting the plan and wait for explicit approval. At lower tiers, state the plan and proceed.

### Do not widen the request

Plan only what was asked. List related problems you noticed as separate items for the user to decide on.

### Stop and re-plan when work diverges

If a step fails, an assumption proves wrong, or the scope grows, pause, say what changed, and revise the plan before continuing. Report the revision; do not absorb it silently.

### Leave a plan another agent can resume

When work may continue in another session or by another agent, record the plan and its progress where the next reader will find it: what is done, what is next, and what is blocked.

### Give delegated work a self-contained brief

When splitting work between agents, give each one the goal, the scope, the inputs it needs, what it must not touch, and how its result will be checked. Keep the parts independent, and verify the combined result yourself; do not rely on each agent's report.

## Exceptions

If the user explicitly asks you to proceed without a plan or without waiting, follow them and state what you skipped.
