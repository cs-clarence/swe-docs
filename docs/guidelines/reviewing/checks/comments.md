# Checks: comments

Verifies [authoring/comments](../../authoring/comments.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Do comments explain why rather than restate the code? | [why, not what](../../authoring/comments.md#explain-why-not-what) | Low |
| Is a comment compensating for code that could be clearer? | [fix the code first](../../authoring/comments.md#fix-the-code-before-commenting-it) | Low |
| Are workarounds, invariants, ordering, and ignored errors explained? | [what code cannot say](../../authoring/comments.md#comment-what-the-code-cannot-say) | Medium |
| Do public elements state purpose, errors, side effects, and guarantees? | [public contracts](../../authoring/comments.md#document-public-contracts) | Medium |
| Do comments near changed code still match it? | [accurate](../../authoring/comments.md#keep-comments-accurate) | Low |
| Does each new TODO say what, why, and who or when? | [TODOs](../../authoring/comments.md#give-todos-a-handle) | Low |
| Do comments describe current behavior and not who changed what? | [do not record history or credit](../../authoring/comments.md#do-not-record-history-or-credit) | Low |

## Blocking

Blocking: comments that are wrong or misleading about changed behavior, undocumented public contracts at high tier. Others are should fix or optional.
