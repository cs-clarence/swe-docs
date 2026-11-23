# Checks: change description

Verifies [authoring/change-description](../../authoring/change-description.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does the description open with what changed and why, linking the request or plan? | [lead with a summary a reviewer can act on](../../authoring/change-description.md#lead-with-a-summary-a-reviewer-can-act-on) | Low |
| For a High-risk change, does the description say how to undo it? | [report verification, risk, and how to undo](../../authoring/change-description.md#report-verification-risk-and-how-to-undo) | High |
| Are the alternatives rejected for each significant choice named, with why? | [list alternatives at Medium risk and above](../../authoring/change-description.md#list-alternatives-at-medium-risk-and-above) | Medium |
| Does a change with wide blast radius, several systems, or altered architecture have a design section? | [add a design section when the change reaches wide](../../authoring/change-description.md#add-a-design-section-when-the-change-reaches-wide) | Medium |
| Does the design section give shape, blast radius, specific files or snippets to look at with why, and what is out of scope, without retelling the diff? | [add a design section when the change reaches wide](../../authoring/change-description.md#add-a-design-section-when-the-change-reaches-wide) | Medium |
| Is the description's detail proportionate to the risk tier? | [match detail to the tier](../../authoring/change-description.md#match-detail-to-the-tier) | Low |

## Blocking

Verification and unverified parts are checked in [approach](approach.md) and [self-review](self-review.md). A High-risk change with no risks, undo path, or design section where one applies goes back to the author. Others are should fix. Finding classes are in [process](../process.md#classify-each-finding).
