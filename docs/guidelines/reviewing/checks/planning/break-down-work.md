# Checks: break down work

Verifies [planning/break-down-work](../../../planning/break-down-work.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does each step deliver something that works end to end? | [split by outcome, not by layer](../../../planning/break-down-work.md#split-by-outcome-not-by-layer) | Medium |
| Does each step have its own check and one purpose? | [make each step verifiable on its own](../../../planning/break-down-work.md#make-each-step-verifiable-on-its-own) | Medium |
| Are prerequisites and unknowns ordered first? | [order by risk and dependency](../../../planning/break-down-work.md#order-by-risk-and-dependency) | Medium |
| Are dependencies between steps stated? | [make dependencies explicit](../../../planning/break-down-work.md#make-dependencies-explicit) | Medium |
| Is the system working after each step? | [keep every step safe to stop after](../../../planning/break-down-work.md#keep-every-step-safe-to-stop-after) | High |
| Can a reviewer judge each step as one unit? | [size steps to what can be reviewed](../../../planning/break-down-work.md#size-steps-to-what-can-be-reviewed) | Medium |
| Was the breakdown revised as work revealed new facts? | [revisit the breakdown as you learn](../../../planning/break-down-work.md#revisit-the-breakdown-as-you-learn) | Medium |

## Blocking

At High risk, a breakdown with a step that leaves the system broken and is not grouped with the steps it needs goes back to the author. Others are should fix. Finding classes are in [process](../../process.md#classify-each-finding).
