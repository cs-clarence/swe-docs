# Checks: interfaces and compatibility

Verifies [authoring/interfaces-and-compatibility](../../authoring/interfaces-and-compatibility.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is it clear which behavior consumers depend on? | [treat published interfaces as promises](../../authoring/interfaces-and-compatibility.md#treat-published-interfaces-as-promises) | Medium |
| Is the change additive where possible? | [prefer additive changes](../../authoring/interfaces-and-compatibility.md#prefer-additive-changes) | Medium |
| Are breaking changes marked, with a migration path? | [mark breaking changes and give a migration path](../../authoring/interfaces-and-compatibility.md#mark-breaking-changes-and-give-a-migration-path) | High |
| Is removal preceded by deprecation? | [deprecate before removing](../../authoring/interfaces-and-compatibility.md#deprecate-before-removing) | Medium |
| Are consumer-pinned interfaces versioned? | [version what consumers pin](../../authoring/interfaces-and-compatibility.md#version-what-consumers-pin) | High |
| Do names, shapes, and errors follow one convention? | [keep names, shapes, and errors consistent](../../authoring/interfaces-and-compatibility.md#keep-names-shapes-and-errors-consistent) | Low |
| Are retried operations safe to repeat? | [make retried operations safe](../../authoring/interfaces-and-compatibility.md#make-retried-operations-safe) | Medium |

## Blocking

Blocking: unannounced breaking changes and removal without deprecation. Convention nits are optional.
