# Choose the approach

## Scope

Deciding which kind of approach fits the work: [small work](small-work.md), [medium work](medium-work.md), [large work](large-work.md), or [new project](new-project.md). Applies before planning in detail.

## Guidelines

### Assess the work on four questions

Ask how much will change (components, contracts, data), how much is unknown, how hard it is to undo, and how many collaborators and how much time it needs. The answers, not a guess at effort, decide the kind.

### Take rigor from the risk tier, not the size

Size sets the shape of the plan; the [risk tier](../../core/risk-tiers.md) sets how much verification and review it gets. A small change to authentication is still High risk.

### Pick the lightest approach that fits

Use the smallest kind that covers the work, so planning effort stays below the cost of the change. When unsure between two kinds, choose the larger.

### Resolve unknowns before choosing

When the unknowns dominate, run a short, bounded experiment on the riskiest one, then assess again ([tackle the riskiest part first](../plan-a-change.md#tackle-the-riskiest-part-first)). Choosing a kind on guesses fails when the guesses are wrong.

### State the chosen kind and why

Put the kind and the reason in the plan or description. A reviewer can then challenge the choice.

### Reassess as the work grows

When the work touches more than assessed, move up a kind and revise the plan ([update the plan when facts change](../plan-a-change.md#update-the-plan-when-facts-change)). Do not finish a larger change under a smaller plan.

## Examples

| Kind | Typical signs | Plan | Steps | Verification |
| --- | --- | --- | --- | --- |
| Small work | One component, contained, easy to undo, understood. | A sentence or two. | One. | A check that fails without the change. |
| Medium work | A few components, some unknowns, reviewable in several steps. | A short written plan. | Two to five, each reviewable. | At each step. |
| Large work | Many components or collaborators, hard to undo, runs for weeks. | A written plan and decision records. | Many, released in stages. | At each step and at each milestone. |
| New project | No existing system to preserve. | Purpose, assumptions, and first slice. | A thin end-to-end slice first. | Automated from the start. |

## Exceptions

When the work is urgent, choose the smallest approach that is safe and say what was left out.
