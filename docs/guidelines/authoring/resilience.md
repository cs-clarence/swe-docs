# Resilience

## Scope

Staying correct and useful when dependencies are slow, failing, or overloaded. Failure reporting is in [error-handling](error-handling.md).

## Guidelines

### Set a timeout on every remote call

Bound each call to another system. A missing timeout turns a slow dependency into an outage ([bound waiting](concurrency.md#bound-waiting-with-timeouts)).

### Retry with backoff and a limit

Retry only safe operations ([retry what is safe](error-handling.md#retry-only-what-is-safe-and-bounded)), with growing, randomized delays, so retries do not add load to a struggling dependency.

### Stop calling a failing dependency

Use a circuit breaker or equivalent so repeated failures fail fast and recover gradually.

### Degrade deliberately

Decide what the system does without each dependency: a reduced result, cached data, or a clear failure. State which.

### Limit load you accept

Shed or queue excess work with a bound instead of accepting everything ([bound parallelism and queues](concurrency.md#bound-parallelism-and-queues)).

### Test failure modes

Test timeouts, errors, and slow responses from dependencies, not only success.

## Exceptions

Internal calls within one process need no timeouts or breakers.
