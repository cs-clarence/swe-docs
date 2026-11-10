# Checks: planning for agents

Verifies [planning/agents](../../../planning/agents.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Did the agent change nothing before the plan was accepted or allowed to proceed? | [explore without changing anything](../../../planning/agents.md#explore-without-changing-anything) | Medium |
| Are plan claims marked as observed or assumed, with evidence for the observed ones? | [ground the plan in what you observed](../../../planning/agents.md#ground-the-plan-in-what-you-observed) | Medium |
| Were costly open questions put to the user instead of guessed? | [ask instead of guessing](../../../planning/agents.md#ask-instead-of-guessing) | Medium |
| Does the plan state goal, approach, steps, scope limit, risks, verification, and undo? | [present the plan in a fixed shape](../../../planning/agents.md#present-the-plan-in-a-fixed-shape) | Medium |
| Did the agent wait for approval at High risk or when going beyond the request? | [wait for approval when the stakes require it](../../../planning/agents.md#wait-for-approval-when-the-stakes-require-it) | High |
| Is the plan limited to the request, with related problems listed separately? | [do not widen the request](../../../planning/agents.md#do-not-widen-the-request) | Low |
| Was a divergence reported and the plan revised? | [stop and re-plan when work diverges](../../../planning/agents.md#stop-and-re-plan-when-work-diverges) | Medium |
| Can another agent resume from the recorded plan and progress? | [leave a plan another agent can resume](../../../planning/agents.md#leave-a-plan-another-agent-can-resume) | Medium |
| Does each delegated brief stand alone, and was the combined result verified directly? | [give delegated work a self-contained brief](../../../planning/agents.md#give-delegated-work-a-self-contained-brief) | Medium |

## Blocking

At High risk, an agent that changed things before approval, or went beyond the request without asking, goes back to the author. Agent claims are verified as in [reviewing agents](../../agents.md). Others are should fix. Finding classes are in [process](../../process.md#classify-each-finding).
