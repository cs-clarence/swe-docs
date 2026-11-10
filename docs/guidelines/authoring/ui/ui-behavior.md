# UI behavior

## Scope

Products with a graphical interface: what the interface does as data and conditions change. Accessibility and translation are in [accessibility-and-i18n](accessibility-and-i18n.md). Skip for products with none.

## Guidelines

### Design every state, not only the loaded one

Define loading, empty, partial, error, and offline states for each view. Unplanned states show blanks, spinners that never end, or raw errors.

### Give feedback for every action

Show that an action was received, is in progress, and finished or failed. Users repeat actions that seem ignored.

### Prevent duplicate submission

Disable or ignore repeated triggers while an action is in flight, and back it with a server-side guard ([make retried operations safe](../interfaces-and-compatibility.md#make-retried-operations-safe)).

### Make failures recoverable

Say what went wrong in user terms and offer a next step, and keep the user's input ([handle errors where they can be handled](../error-handling.md)).

### Confirm destructive actions or make them undoable

Prefer undo; otherwise ask for confirmation that names what will be lost. Mistaken deletes are common and often permanent.

### Keep the screen consistent with the data

Update or invalidate displayed data after changes, and handle stale or concurrent edits instead of silently overwriting ([give each piece of data one owner](../database/data-and-state.md#give-each-piece-of-data-one-owner)).

### Validate input where the user can fix it

Check input as early as is helpful, show the problem beside the field, and still validate at the boundary ([validate at the boundary](../security/input-handling.md)).

### Keep the interface responsive

Do slow work off the interaction path, and show progress for work over about a second ([bound resource use](../performance.md#bound-resource-use)).

### Do not lose user work

Preserve unsaved input across errors, navigation, and reloads where practical, or warn before it is lost.

## Exceptions

Prototypes and internal tools may skip some states. State which.
