# Checks: modularity

Verifies [authoring/modularity](../../../authoring/structure/modularity.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does each new module have a concrete reason to be separate? | [split for a reason](../../../authoring/structure/modularity.md#split-for-a-reason) | Medium |
| Was a proposed module checked against reason, name, interface, direction, and cost, and kept in place if any failed? | [confirm before extracting](../../../authoring/structure/modularity.md#confirm-before-extracting) | Medium |
| Is each module named for the capability it provides, not its technology, layer, or origin? | [naming](../../../authoring/structure/modularity.md#name-for-what-it-provides) | Low |
| Does each module own one nameable capability, neither too broad nor too tiny? | [one capability](../../../authoring/structure/modularity.md#size-modules-to-one-capability) | Medium |
| Was the public interface defined before code moved, and is it enforced by visibility or tooling? | [public interface](../../../authoring/structure/modularity.md#define-the-public-interface-first) | Medium |
| Are dependency cycles resolved by merging, extracting, or inverting? | [break cycles](../../../authoring/structure/modularity.md#break-dependency-cycles) | Medium |
| Was a `utils`, `common`, or `shared` catch-all added or grown? | [dumping grounds](../../../authoring/structure/modularity.md#avoid-shared-dumping-grounds) | Medium |
| Was a split done in verifiable steps with behavior unchanged? | [seams, in steps](../../../authoring/structure/modularity.md#split-along-seams-in-steps) | High |
| Did tests move with the code and exercise the public interface? | [tests move](../../../authoring/structure/modularity.md#move-tests-with-the-code) | Medium |
| Is the split too fine, adding wiring cost without benefit? | [over-split](../../../authoring/structure/modularity.md#do-not-over-split) | Medium |
| Should two always-co-changing modules be merged? | [merge](../../../authoring/structure/modularity.md#merge-when-a-split-stops-paying) | Medium |

## Blocking

Blocking: a structural split without a working, verified path. Cycles and reaching into internals are blocking per [architecture checks](architecture.md). Others are should fix or optional.
