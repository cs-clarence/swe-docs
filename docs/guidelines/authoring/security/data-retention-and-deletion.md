# Data retention and deletion

## Scope

How long data is kept and how it is removed, for personal and other sensitive data. Collecting less is in [security-and-privacy](security-and-privacy.md#minimize-sensitive-data).

## Guidelines

### Decide how long each kind of data is kept

State a retention period and a reason for each category of sensitive data. Data without an end date is kept by accident.

### Delete when the period ends or on valid request

Make deletion happen automatically at the end of the period, and on a valid request, instead of relying on someone to remember.

### Delete everywhere the data lives

Include caches, search indexes, derived data, logs, exports, replicas, and third parties. A copy left behind is still a copy.

### Define how backups age out

State how long backups keep deleted data, and make restores re-apply deletions. Otherwise a restore brings deleted data back.

### Do not treat hiding as deleting

A flag that hides a record is not deletion. Use real removal when removal is required, and use hiding only when the data may stay.

### Make anonymization resistant to re-identification

Remove or generalize fields so combining the rest with other data does not identify a person, or treat the data as still personal.

### Record that deletion happened, not what was deleted

Keep an audit entry of the event without the removed content ([keep sensitive data out of telemetry](../observability.md#keep-sensitive-data-out-of-telemetry)).

### Honor holds and obligations

Keep data that a legal or contractual duty requires, state which duty, and delete it when the duty ends.

## Exceptions

Data with no personal or sensitive content and no cost to keep may be kept without a period; state that.
