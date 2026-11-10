# Concurrency

## Scope

Code that runs work in parallel or interleaved: threads, async tasks, processes, and distributed calls.

## Guidelines

### Minimize shared mutable state

Prefer immutable data, ownership transfer, or message passing. Shared mutable state needs synchronization and invites races.

### Protect what must be shared

Guard shared state with one clear mechanism, and document what it protects and the lock order.

### Bound waiting with timeouts

Give every wait on another party a timeout. Unbounded waits hang the system.

### Support cancellation

Let long-running work stop, and clean up when it does ([clean up](error-handling.md#clean-up-on-every-path)).

### Do not rely on timing or ordering

Make correctness independent of scheduling, or state the ordering guarantee and enforce it.

### Bound parallelism and queues

Limit concurrent work and queue length so load cannot exhaust resources.

## Exceptions

Single-threaded scripts need none of this.
