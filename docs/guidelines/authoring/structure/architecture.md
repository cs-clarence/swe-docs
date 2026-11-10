# Architecture

## Scope

Structure of a system or component and how its parts relate: modules, layers, boundaries, dependencies. For splitting and sizing modules, see [modularity](modularity.md). For structure inside a unit, see [design](design.md). For when and how to generalize, see [abstraction](abstraction.md).

## Guidelines

### Extend the existing architecture

Add to the structure that exists and follow its patterns. A second competing pattern for the same problem costs more than a slightly imperfect shared one. If the architecture is the problem, change it deliberately, as its own change, not as a side effect of a feature.

### Build most code as libraries

Structure most of an application as cohesive modules that behave like libraries: a defined public interface, no knowledge of the application's entry points, and usable and testable on their own. This holds whether the module is external, shared internally, or private to one application. The application is the thin layer that composes them: entry points, wiring, configuration, and the framework glue.

Why: library-shaped code has explicit boundaries, so you can test it through its public interface, reuse it, and replace it, and the application stays easy to change.

Keep framework-specific code at the edges, in adapters, so logic does not depend on the framework that calls it ([design](design.md#isolate-side-effects)).

### Group by cohesion

Put together what changes together and separate what changes for different reasons. Organize around domain concepts or capabilities unless the repository's idiom is layered by technical role.

### Make boundaries explicit

Define what crosses each boundary (inputs, outputs, errors, side effects) and keep everything else private. Hidden coupling makes changes spread.

### Depend inward and on contracts

Higher-level logic must not depend on low-level details; depend on a [contract](../../core/glossary.md) the detail satisfies. Keep the dependency graph acyclic.

### Keep interfaces small

Expose the minimum consumers need. Every public element is something you must keep working.

### Keep one source of truth

Each piece of knowledge (a rule, a format, a constant, a piece of state) has one authoritative home. Others derive from or reference it; copies drift.

### Do not share internals across boundaries

Do not let other components depend on your storage layout, internal types, or incidental behavior. Translate at the boundary so each side can change independently.

### Prefer reversible decisions

Choose options that are cheap to undo. For hard-to-reverse choices (data formats, public contracts, vendor lock-in), decide with more evidence and care ([high risk](../../core/risk-tiers.md)).

### Design for known requirements

Build for what is needed now and what is concretely expected. Extension points and generalization follow [abstraction](abstraction.md#do-not-generalize-speculatively).

### Evolve in steps

Change architecture incrementally, keeping the system working at each step. Run old and new side by side during migration when a cut-over is risky.

### Record significant decisions

When a choice shapes the system and is not obvious from the code, note what was decided, why, and what was rejected, in the place the repository keeps such notes or in the change description.

## Examples

| Avoid | Prefer |
| --- | --- |
| Business logic that imports the web framework and reads request objects | Logic in a module with plain inputs and outputs; a thin adapter translates the framework's request into them. |
| Component B reads component A's tables directly | B calls A's contract; A owns its storage. |
| A new feature introduces its own error-reporting style | Reuse the existing one, or change it everywhere, separately. |
| Same pricing rule in three modules | One module owns it; others call it. |

## Exceptions

Small scripts, prototypes, and spikes may keep everything in one place and skip structure; split once the code is reused or grows. Mark prototypes as such and do not let them become the architecture unreviewed. Hard constraints (latency, memory, regulation) may justify breaking a rule here; document the constraint and confine the exception.
