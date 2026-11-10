# Design

## Scope

Structuring code inside a component: functions and types. For system-level structure see [architecture](architecture.md); for generalization see [abstraction](abstraction.md).

## Guidelines

### Give each unit one responsibility

A unit should have one reason to change and a name that says what it does. Units that do several things are hard to test and hard to change safely.

### Prefer composition

Combine small units rather than extending large ones through inheritance or shared base behavior, unless the repository's idiom is otherwise.

### Make invalid states hard to represent

Use types, constructors, or validation so illegal combinations cannot exist, instead of checking for them everywhere.

### Limit shared mutable state

Prefer passing data explicitly. Where shared state is needed, give it one owner and a narrow interface.

### Isolate side effects

Keep I/O, time, randomness, and global state at the edges so core logic is easy to test and reason about.

## Exceptions

Performance-critical or tightly constrained code may trade structure for speed or size. Confine the exception and document why.
