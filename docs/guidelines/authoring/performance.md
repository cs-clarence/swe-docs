# Performance

## Scope

Speed, memory, and resource use. Excludes design choices with no performance claim.

## Guidelines

### Measure before optimizing

Find the bottleneck with measurement. Guessed optimizations add complexity and may not help.

### State the target

Say what is fast enough: a latency, throughput, or resource budget. Without one, you cannot know when to stop.

### Avoid known accidental costs

Avoid repeated queries in loops, unbounded growth, and unneeded work on hot paths. These cost little to avoid.

### Bound resource use

Limit sizes, counts, and time for inputs and queues that outside actors control.

### Prove the improvement

Show before and after measurements for any optimization made for speed. Keep it only if it helps.

### Keep clarity unless measurement justifies otherwise

Do not trade readability for speed without evidence of need ([design](structure/design.md)).

## Exceptions

Hard real-time or resource-constrained code may need design-time performance work; state the constraint.
