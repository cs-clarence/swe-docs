# Flaky tests

## Scope

Tests that pass and fail without a change to the code. Writing deterministic tests is in [testing](testing.md#keep-tests-deterministic).

## Guidelines

### Treat a flaky test as a defect

Fix it or delete it. A test people learn to ignore stops protecting anything.

### Do not retry a test to make it pass

Do not rerun until green ([never weaken a test to pass](testing.md#never-weaken-a-test-to-pass)). A retry hides whether the product or the test is wrong. Rerun only to gather evidence.

### Look at the usual causes first

Check time, ordering, shared state, concurrency, network, resource limits, and random data. Most flakiness comes from one of them.

### Control time and randomness

Inject the clock ([take the clock as a dependency](../time-and-numbers.md#take-the-clock-as-a-dependency)), seed random values, and log the seed.

### Wait for a condition, not a duration

Poll for the state with a bounded timeout instead of a fixed sleep ([bound waiting with timeouts](../concurrency.md#bound-waiting-with-timeouts)).

### Quarantine with an owner and an end date

If it cannot be fixed now, remove it from blocking results, record who owns it and until when, and state that the behavior is unverified meanwhile.

### Capture evidence on failure

Keep logs, inputs, and seeds so the failure can be reproduced ([make failures diagnosable](testing.md#make-failures-diagnosable)).

### Consider that the product may be flaky

An intermittent failure can be a real race or ordering bug. Check [concurrency](../concurrency.md) before blaming the test.

## Exceptions

A test of an external service that cannot be made stable may run without blocking, if stated.
