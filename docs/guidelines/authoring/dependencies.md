# Dependencies

## Scope

Adding, updating, and removing third-party libraries and services. Using vetted security libraries is in [security-and-privacy](security/security-and-privacy.md#use-vetted-libraries-and-protocols).

## Guidelines

### Add a dependency only for a real need

Prefer the standard library or existing dependencies when they suffice. Each dependency adds maintenance, risk, and weight.

### Vet before adding

Check maintenance, license, security history, and size. Record why it was chosen.

### Pin versions reproducibly

Make builds reproducible by pinning or locking versions, and update deliberately.

### Isolate behind your own interface

Wrap dependencies that are likely to change or that leak into many modules ([architecture](structure/architecture.md#depend-inward-and-on-contracts)).

### Remove what is unused

Delete dependencies the code no longer uses.

## Exceptions

Prototypes may skip vetting; do not ship them without it.
