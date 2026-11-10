# Modularity

## Scope

Deciding when and how to split code into modules, how big modules should be, and when to merge them. A module is any unit with a defined public interface: a package, library, namespace, or directory with an entry point. For structural rules that apply to all modules (boundaries, dependency direction, interfaces), see [architecture](architecture.md). For abstraction, see [abstraction](abstraction.md).

## Guidelines

### Split for a reason

Create a module when code has a reason to be separate: it changes for different reasons or at a different pace than its neighbors, is reused or likely to be, has a different owner, needs isolated testing, or must build or deploy separately. Do not split for tidiness alone; every module adds a boundary to maintain.

### Confirm before extracting

When something seems to deserve its own module, check it against these before extracting:

1. Can you name a concrete reason from [split for a reason](#split-for-a-reason)?
2. Can you name it as a capability ([name for what it provides](#name-for-what-it-provides))?
3. Can you list its public interface in a few lines, and would consumers need nothing else?
4. Does it depend on nothing that depends on it?
5. Is the wiring and maintenance of one more boundary smaller than the benefit?

If any answer is no, keep it where it is, as a clearly separated part of the current module, and revisit when evidence appears. If all are yes, extract it ([split along seams](#split-along-seams-in-steps)).

### Name for what it provides

Name a module for the capability or domain concept it provides, in the language of its consumers. Do not name it for its technology, its layer, its origin, or its leftovers. General naming rules are in [style](../style.md#name-for-intent). A good module name tells a consumer what to expect without opening it, and states the module's boundary: if a new function does not fit the name, it belongs elsewhere.

### Size modules to one capability

A module should own one coherent capability. If it cannot be named without "and" or "misc" ([naming](#name-for-what-it-provides)), it is too broad. If most changes touch it together with another module, it is too small.

### Define the public interface first

Decide what the module exposes and what it hides before moving code in, following [small interfaces](architecture.md#keep-interfaces-small) and [no shared internals](architecture.md#do-not-share-internals-across-boundaries). Consumers import only the public interface. Enforce this with the language's visibility or the repository's tooling where available.

### Break dependency cycles

Direction and acyclicity are in [dependency direction](architecture.md#depend-inward-and-on-contracts). If two modules need each other, merge them, extract what they share into a third, or invert one dependency behind a contract.

### Avoid shared dumping grounds

Do not create catch-all modules (`utils`, `common`, `helpers`, `shared`). Give each piece of shared code to the module that owns its concept; if none does, that is a missing module, so name it.

### Split along seams, in steps

To modularize existing code, find where coupling is already low (the seams), put the new public interface in front of the code, then move code behind it in small, individually verifiable steps. Keep behavior unchanged and the system working at each step ([refactors](../approach.md#preserve-behavior-in-refactors), [evolve in steps](architecture.md#evolve-in-steps)).

### Move tests with the code

Tests for a module live with it and exercise its public interface ([test internal modules as libraries](../testing/test-strategy.md#test-internal-modules-as-libraries)). A split that leaves tests behind has not finished.

### Do not over-split

Too many tiny modules make wiring and navigation harder. Group code that is always changed and used together, even if it could be separated.

### Merge when a split stops paying

If two modules are always changed together, share most of their types, or one exists only to serve the other, merge them. Merging is a refactor like any other.

## Examples

### Worth its own module

| Code | Why | Module name |
| --- | --- | --- |
| Pricing and discount rules, used by checkout, quotes, and invoices | Reused, changes for business reasons, easy to test alone. | `pricing` |
| Retry-with-backoff logic duplicated in four clients | Reused, one concept, clear interface (`retry(operation, policy)`). | `retry` |
| Email sending, with templates and provider integration | Volatile dependency, different change pace, needs a test seam ([isolate volatile dependencies](abstraction.md#isolate-volatile-dependencies)). | `notifications` |
| Parsing and validating a file format | Self-contained, benefits from property tests, may be published. | `invoice-format` |

### Not worth its own module

| Code | Why not | Instead |
| --- | --- | --- |
| A 30-line helper used in one place | No reuse, no different change reason. | Keep it private next to its only caller. |
| A set of types used only by one module | They change with it; a module split adds wiring. | Keep inside that module. |
| Code that "might be reused someday" | Speculative ([abstract on evidence](abstraction.md#abstract-on-evidence)). | Wait for the second real use. |
| Two modules that must be changed together every time | One concept split in two. | Merge them. |
| A grab bag of unrelated functions | No capability to name. | Place each with the module that owns its concept. |
| Orders and Billing import each other | A cycle; neither is independent. | Extract the shared concept, or invert one dependency behind a contract ([break cycles](#break-dependency-cycles)). |
| Code that depends on its would-be consumer | Fails the direction test; it is not independent. | Invert the dependency behind a contract first, or leave it in place. |

### Naming

| Avoid | Prefer | Why |
| --- | --- | --- |
| `utils`, `common`, `helpers`, `misc` | `pricing`, `retry`, `dates` | A name that says nothing invites everything. |
| `postgres-stuff`, `redis-layer` | `order-storage`, `session-cache` | Name the capability, not the technology, so the implementation can change. |
| `service-layer`, `controllers` | `ordering`, `accounts` | Group by capability, not by technical role, unless the repository's idiom is layered. |
| `new-billing`, `billing-v2` | `billing` | Do not name for history or origin. |
| `data-and-ui-and-rules` | Three modules | "and" signals more than one capability. |

Name length and style follow the repository's conventions.

## Exceptions

Small projects and early prototypes may stay in one module; split when a reason in [split for a reason](#split-for-a-reason) appears. Generated code and vendored third-party code keep their own structure.
