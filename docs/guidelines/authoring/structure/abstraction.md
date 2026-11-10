# Abstraction

## Scope

Deciding whether to introduce, change, or remove an abstraction: an interface, base type, wrapper, generic helper, configuration option, or layer. For system structure, see [architecture](architecture.md).

## Guidelines

### Abstract on evidence

Introduce an abstraction when real uses show what varies and what stays the same, typically at least two or three, or when a boundary demands it. One use does not show what varies.

### Prefer duplication to the wrong abstraction

Small duplication is cheap to fix later. A wrong abstraction is expensive: every caller must adapt to it. If similar code differs for reasons that may diverge, keep the copies.

### Hide what varies, expose what is stable

Define the abstraction by what consumers need, not by how one implementation works. Its interface should survive swapping the implementation.

### State the contract

An abstraction must say what it guarantees, assumes, and how it fails ([contract](../../core/glossary.md)). Callers must not need to read the implementation to use it correctly.

### Do not leak implementation details

If callers must know which implementation is behind the abstraction, it is leaking. Fix the boundary, or document the unavoidable leak (such as ordering, cost, or failure modes).

### Keep one level of abstraction per unit

A unit should not mix high-level intent with low-level detail. Extract the detail behind a named step.

### Name for purpose

Name abstractions by the role they play for consumers, not their implementation or mechanism ([style](../style.md#name-for-intent)).

### Do not generalize speculatively

Do not add parameters, options, flags, type parameters, or extension hooks for needs that have not appeared. Unused flexibility is complexity with no benefit.

### Keep layers thin and earning their place

Each layer must add something: a boundary, a contract, a translation, or a simplification. Remove pass-through layers that only forward calls.

### Isolate volatile dependencies

Wrap a third-party or fast-changing dependency behind your own small contract when it is used widely or likely to change. For a stable or narrowly used one, use it directly.

### Remove abstractions that no longer pay

When an abstraction has one implementation that will not vary, or callers routinely work around it, inline or simplify it. Doing so is a refactor ([approach](../approach.md#preserve-behavior-in-refactors)).

## Examples

| Situation | Decision |
| --- | --- |
| Two functions share most lines but handle different business rules | Keep separate; the rules may diverge. |
| Three call sites share one structure and vary in two clear ways | Extract, parameterize those two ways. |
| An interface with one implementation and no test double | Likely premature; use the concrete type. |
| A `process(options)` helper whose options are all booleans | Split into named functions. |

## Exceptions

A public contract, a plugin point, or a testing seam may be abstracted before several uses exist when the need is concrete and the boundary is genuine. State why.
