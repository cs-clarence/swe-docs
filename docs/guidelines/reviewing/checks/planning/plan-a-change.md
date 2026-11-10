# Checks: plan a change

Verifies [planning/plan-a-change](../../../planning/plan-a-change.md). Use these to review a plan before work starts, or to check that work followed one. Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is the plan sized to the risk tier? | [match the plan to the risk](../../../planning/plan-a-change.md#match-the-plan-to-the-risk) | Medium |
| Are the goal, finish line, and out-of-scope items stated? | [state the goal and what done means](../../../planning/plan-a-change.md#state-the-goal-and-what-done-means) | Medium |
| Are assumptions and open questions listed, with costly ones raised? | [list assumptions and open questions](../../../planning/plan-a-change.md#list-assumptions-and-open-questions) | Medium |
| Are affected components, callers, data, and users named? | [find what the change touches](../../../planning/plan-a-change.md#find-what-the-change-touches) | Medium |
| Were options compared and the choice reasoned for costly decisions? | [compare options before choosing](../../../planning/plan-a-change.md#compare-options-before-choosing) | High |
| Is the riskiest part identified and tested early? | [tackle the riskiest part first](../../../planning/plan-a-change.md#tackle-the-riskiest-part-first) | High |
| Are verification and undo planned? | [plan verification and undo](../../../planning/plan-a-change.md#plan-verification-and-undo) | Medium |
| Was the plan reviewed by someone else before building? | [get the plan reviewed before building](../../../planning/plan-a-change.md#get-the-plan-reviewed-before-building) | High |
| Was the plan revised when facts changed? | [update the plan when facts change](../../../planning/plan-a-change.md#update-the-plan-when-facts-change) | Medium |

## Blocking

At High risk, a plan with no verification or undo, or one that leaves a costly assumption untested, goes back to the author. Others are should fix. Finding classes are in [process](../../process.md#classify-each-finding).
