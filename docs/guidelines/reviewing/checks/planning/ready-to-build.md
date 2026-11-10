# Checks: ready to build

Verifies [planning/ready-to-build](../../../planning/ready-to-build.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Could someone who did not write it begin the first step without asking you anything? | [test whether someone else could start without asking](../../../planning/ready-to-build.md#test-whether-someone-else-could-start-without-asking) | Medium |
| Are the outcome, exclusions, and finish check stated, as a worked example for large work? | [make the goal, scope, and finish line checkable](../../../planning/ready-to-build.md#make-the-goal-scope-and-finish-line-checkable) | Medium |
| Is each open question non-blocking and owned, and each assumption checked or checkable? | [leave no open question that blocks the first step](../../../planning/ready-to-build.md#leave-no-open-question-that-blocks-the-first-step) | Medium |
| Was the riskiest part tested or made the first step? | [deal with the riskiest part first](../../../planning/ready-to-build.md#deal-with-the-riskiest-part-first) | High |
| Does every step have a check and an undo, or a stated reason for none? | [give every step a check and an undo](../../../planning/ready-to-build.md#give-every-step-a-check-and-an-undo) | High |
| Were costly choices decided and recorded before work started? | [decide the costly choices before starting](../../../planning/ready-to-build.md#decide-the-costly-choices-before-starting) | High |
| Do the design's interfaces and data shapes let two people build parts that fit? | [specify interfaces well enough to build compatible parts](../../../planning/ready-to-build.md#specify-interfaces-well-enough-to-build-compatible-parts) | High |
| Was the gate sized to the work and its risk tier, with the required review done? | [match the gate to the size and risk](../../../planning/ready-to-build.md#match-the-gate-to-the-size-and-risk) | Medium |
| When a test failed, was the document revised or the question asked before starting? | [close the gap or ask when the gate fails](../../../planning/ready-to-build.md#close-the-gap-or-ask-when-the-gate-fails) | Medium |

## Blocking

At High risk, work that began from a plan or design failing the tests goes back to the author. Others are should fix. Finding classes are in [process](../../process.md#classify-each-finding).
