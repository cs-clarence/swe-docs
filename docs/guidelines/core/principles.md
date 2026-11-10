# Principles

## Scope

Baseline for every change, by anyone. Other guidelines apply these to specific activities.

## Guidelines

### Correctness first

Code must do what it is meant to do, including on failure and edge paths. Speed, elegance, and brevity do not justify incorrect behavior.

### Clarity over cleverness

Write for the next reader. Prefer the obvious construction; choose a clever one only when measurably needed, and explain it.

### Simplest sufficient solution

Solve the stated problem with the least machinery that works. Do not add generality, options, or layers for needs that have not appeared.

### Proportional change

Size the change, its verification, and its review to the problem and its risk ([risk tiers](risk-tiers.md)). Do not rewrite what you were not asked to change.

### Respect what exists

Follow the repository's existing conventions and structure unless they cause the problem. Consistency beats personal preference.

### Leave it maintainable

Another person should be able to understand, change, and verify the result without you. Remove what you made obsolete; document what is not evident.

### Be honest about uncertainty

State assumptions, unverified claims, and known limits. Never present a guess as fact or untested work as tested.

## Exceptions

Principles can conflict (for example, simplicity versus a hard performance requirement). Choose the option that protects correctness and users, and state the trade-off in the change description.
