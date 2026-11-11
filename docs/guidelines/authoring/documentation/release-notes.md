# Release notes

## Scope

Documents that tell users what changed in a release, including deprecations and breaking changes. For how to change published interfaces safely, see [interfaces-and-compatibility](../interfaces-and-compatibility.md).

## Guidelines

### Write for the user's impact

Describe what changed from the user's side, not which code changed. Say what they can now do, what behaves differently, and what they must do.

### Group entries by kind

Group entries as added, changed, fixed, deprecated, removed, and security, so readers find what concerns them.

### Call out breaking changes first

Put breaking changes at the top, each with what breaks, who is affected, and the steps to migrate. Link to a [how-to guide](how-to-guides.md) when the migration is long.

### Announce deprecations with a path

For each deprecation, state what is deprecated, why, what replaces it, and when it will be removed ([interfaces-and-compatibility](../interfaces-and-compatibility.md)).

### Write the entry in the same change

Add the note when the behavior changes, not at release time ([update docs in the same change as behavior](documentation.md#update-docs-in-the-same-change-as-behavior)). Reconstructing it later loses detail.

### Keep sensitive details out

Describe security fixes by impact and the action to take. Do not include exploit details or private data before users can update ([keep sensitive data out of docs](documentation.md#keep-sensitive-data-out-of-docs)).

## Exceptions

Internal or unpublished changes may be omitted. Include them if users could notice them.
