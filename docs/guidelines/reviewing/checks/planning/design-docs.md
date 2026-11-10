# Checks: design docs

Verifies [planning/design-docs](../../../planning/design-docs.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is there a design doc where a trigger applies, and none where no trigger does? | [write a design doc only when the design is the hard part](../../../planning/design-docs.md#write-a-design-doc-only-when-the-design-is-the-hard-part) | Medium |
| Does it cover the problem, design, rejected alternatives, interfaces, failure, testing and rollout, and open questions? | [cover the design, not the steps](../../../planning/design-docs.md#cover-the-design-not-the-steps) | Medium |
| Was the design read and disagreements resolved before work depended on it? | [settle the design before building on it](../../../planning/design-docs.md#settle-the-design-before-building-on-it) | High |
| Do the design and the work agree, or is the departure noted? | [say when the build departs from the design](../../../planning/design-docs.md#say-when-the-build-departs-from-the-design) | Medium |
| When the work ended, was what lasts moved out of the design doc? | [distill the design when the work ends](../../../planning/design-docs.md#distill-the-design-when-the-work-ends) | Medium |

## Blocking

At High risk, a trigger that applies without a design, or work that contradicts its design without a note, goes back to the author. A design doc where no trigger applies is a should fix. Finding classes are in [process](../../process.md#classify-each-finding).
