# Checks: architecture

Verifies [authoring/architecture](../../../authoring/structure/architecture.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does the change follow the existing structure, or change it deliberately and separately? | [extend existing](../../../authoring/structure/architecture.md#extend-the-existing-architecture) | Medium |
| Is most new code in modules with a defined public interface, with the application layer only composing them? | [libraries](../../../authoring/structure/architecture.md#build-most-code-as-libraries) | Medium |
| Is framework-specific code confined to adapters at the edge? | [libraries](../../../authoring/structure/architecture.md#build-most-code-as-libraries) | Medium |
| Do things that change together live together? | [cohesion](../../../authoring/structure/architecture.md#group-by-cohesion) | Medium |
| Is it clear what crosses each boundary, with the rest private? | [boundaries](../../../authoring/structure/architecture.md#make-boundaries-explicit) | Medium |
| Do dependencies point toward contracts, without cycles? | [dependency direction](../../../authoring/structure/architecture.md#depend-inward-and-on-contracts) | Medium |
| Is the exposed interface the minimum needed? | [small interfaces](../../../authoring/structure/architecture.md#keep-interfaces-small) | Medium |
| Does each piece of knowledge have one home? | [single source](../../../authoring/structure/architecture.md#keep-one-source-of-truth) | Medium |
| Does any component depend on another's internals? | [internals](../../../authoring/structure/architecture.md#do-not-share-internals-across-boundaries) | Medium |
| Are hard-to-reverse choices made with evidence? | [reversible](../../../authoring/structure/architecture.md#prefer-reversible-decisions) | High |
| Is extensibility limited to concrete needs? | [known requirements](../../../authoring/structure/architecture.md#design-for-known-requirements) | Medium |
| Does a structural migration keep the system working at each step? | [evolve in steps](../../../authoring/structure/architecture.md#evolve-in-steps) | High |
| Is a significant, non-obvious decision recorded? | [record decisions](../../../authoring/structure/architecture.md#record-significant-decisions) | High |

## Blocking

Blocking: dependency cycles, cross-boundary dependence on internals of a contract-bearing component, and hard-to-reverse decisions without a stated rationale. Others are should fix or optional.
