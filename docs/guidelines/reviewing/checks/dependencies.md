# Checks: dependencies

Verifies [authoring/dependencies](../../authoring/dependencies.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is the need real and not met by existing code? | [add a dependency only for a real need](../../authoring/dependencies.md#add-a-dependency-only-for-a-real-need) | Medium |
| Were maintenance, license, and security checked? | [vet before adding](../../authoring/dependencies.md#vet-before-adding) | Medium |
| Are versions pinned or locked? | [pin versions reproducibly](../../authoring/dependencies.md#pin-versions-reproducibly) | Low |
| Is a widely used dependency isolated behind an interface? | [isolate behind your own interface](../../authoring/dependencies.md#isolate-behind-your-own-interface) | Medium |
| Are unused dependencies removed? | [remove what is unused](../../authoring/dependencies.md#remove-what-is-unused) | Low |

## Blocking

Blocking: unvetted dependencies in High-risk code, and license conflicts. Others are should fix.
