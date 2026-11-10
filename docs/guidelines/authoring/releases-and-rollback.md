# Releases and rollback

## Scope

Getting a change to users and being able to undo it. Order of data changes is in [data-and-state](database/data-and-state.md#roll-out-in-compatible-steps).

## Guidelines

### Know how to undo before shipping

State the rollback path, or say why the change cannot be undone and what applies instead. A release you cannot undo needs more care, not less.

### Separate shipping from enabling

Ship code switched off, then turn it on ([give flags an owner and an end](configuration.md#give-flags-an-owner-and-an-end)). Turning off is faster than redeploying.

### Expose gradually when risk is high

At High risk, expose a small share first and widen only after checking the signals. A small blast radius turns a failure into a minor incident.

### Order dependent changes so any step can stop

Release schema, code, and cleanup in steps where each works with the one before and after ([roll out in compatible steps](database/data-and-state.md#roll-out-in-compatible-steps)).

### Decide the failure signals first

Name the metrics or errors that mean "roll back" before release ([emit what operators need to diagnose](observability.md#emit-what-operators-need-to-diagnose)). Deciding during an incident is slow and biased.

### Watch after release

Have someone or something observe those signals for a stated period after release.

### Do not let rollback lose data

Rolling back code must not require discarding what users wrote meanwhile ([protect existing data](database/data-and-state.md#protect-existing-data)).

### Make the running version identifiable

Expose which version is running so diagnosis starts from facts.

### Rehearse the rollback for High-risk changes

Try the undo path before it is needed. An untested rollback is a guess.

## Exceptions

Prototypes and throwaway tools may skip staged rollout. State it.
