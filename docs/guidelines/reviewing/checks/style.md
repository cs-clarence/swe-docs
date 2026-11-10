# Checks: style

Verifies [authoring/style](../../authoring/style.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Do automated tools pass, and are style disputes left to them? | [defer to automated tools](../../authoring/style.md#defer-to-automated-tools) | Low |
| Does the change match surrounding code? | [match surrounding code](../../authoring/style.md#match-surrounding-code) | Low |
| Do names say what things are for? | [name for intent](../../authoring/style.md#name-for-intent) | Low |
| Is control flow shallow? | [keep control flow shallow](../../authoring/style.md#keep-control-flow-shallow) | Low |
| Can each unit be held in mind? | [keep units small enough to hold in mind](../../authoring/style.md#keep-units-small-enough-to-hold-in-mind) | Low |
| Are magic values replaced with named ones? | [replace magic values](../../authoring/style.md#replace-magic-values) | Low |
| Is dead code removed? | [remove dead code](../../authoring/style.md#remove-dead-code) | Low |

## Blocking

Style issues are should fix or optional, unless they hide a defect.
