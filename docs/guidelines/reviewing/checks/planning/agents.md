# Checks: planning for agents

Verifies [planning/agents](../../../planning/agents.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Did the agent change nothing before the plan was accepted or allowed to proceed? | [explore without changing anything](../../../planning/agents.md#explore-without-changing-anything) | Medium |
| Are plan claims marked as observed or assumed, with evidence for the observed ones? | [ground the plan in what you observed](../../../planning/agents.md#ground-the-plan-in-what-you-observed) | Medium |
| Were costly open questions put to the user instead of guessed? | [ask instead of guessing](../../../planning/agents.md#ask-instead-of-guessing) | Medium |
| Does the plan state goal, approach, steps, scope limit, risks, verification, and undo? | [present the plan in a fixed shape](../../../planning/agents.md#present-the-plan-in-a-fixed-shape) | Medium |
| At High risk, did the agent wait for explicit approval before proceeding? | [wait for approval when the stakes require it](../../../planning/agents.md#wait-for-approval-when-the-stakes-require-it) | High |
| If the plan went beyond the request, did the agent get approval first? | [wait for approval when the stakes require it](../../../planning/agents.md#wait-for-approval-when-the-stakes-require-it) | Low |
| Is the plan limited to the request, with related problems listed separately? | [do not widen the request](../../../planning/agents.md#do-not-widen-the-request) | Low |
| Was a divergence reported and the plan revised? | [stop and re-plan when work diverges](../../../planning/agents.md#stop-and-re-plan-when-work-diverges) | Medium |
| Can another agent resume from the recorded plan and progress? | [leave a plan another agent can resume](../../../planning/agents.md#leave-a-plan-another-agent-can-resume) | Medium |
| Was small work kept with one agent, and was larger work split only where parts were independent and checkable, with integration and verification kept with one agent? | [split work between agents only when it pays](../../../planning/agents.md#split-work-between-agents-only-when-it-pays) | Medium |
| At High risk, was every agent-authored part, including the coordinating agent's own, checked by someone other than its author? | [split work between agents only when it pays](../../../planning/agents.md#split-work-between-agents-only-when-it-pays) | High |
| Does each delegated brief stand alone, and was the combined result verified directly? | [give delegated work a self-contained brief](../../../planning/agents.md#give-delegated-work-a-self-contained-brief) | Medium |

## Blocking

At High risk, an agent that changed things before approval goes back to the author. At any tier, so does an agent that went beyond the request without asking. Agent claims are verified as in [reviewing agents](../../agents.md). Others are should fix. Finding classes are in [process](../../process.md#classify-each-finding).
