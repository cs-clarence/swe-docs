# Checks: data retention and deletion

Verifies [authoring/data-retention-and-deletion](../../../authoring/security/data-retention-and-deletion.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does each category of sensitive data have a retention period and reason? | [decide how long each kind of data is kept](../../../authoring/security/data-retention-and-deletion.md#decide-how-long-each-kind-of-data-is-kept) | Medium |
| Is deletion automatic and triggered by valid requests? | [delete when the period ends or on valid request](../../../authoring/security/data-retention-and-deletion.md#delete-when-the-period-ends-or-on-valid-request) | High |
| Are all copies, including derived data and third parties, covered? | [delete everywhere the data lives](../../../authoring/security/data-retention-and-deletion.md#delete-everywhere-the-data-lives) | High |
| Are backup retention and restore handling of deletions defined? | [define how backups age out](../../../authoring/security/data-retention-and-deletion.md#define-how-backups-age-out) | High |
| Is real deletion used where deletion is required? | [do not treat hiding as deleting](../../../authoring/security/data-retention-and-deletion.md#do-not-treat-hiding-as-deleting) | Medium |
| Does anonymized data resist re-identification? | [make anonymization resistant to re-identification](../../../authoring/security/data-retention-and-deletion.md#make-anonymization-resistant-to-re-identification) | High |
| Is deletion recorded without keeping the data? | [record that deletion happened, not what was deleted](../../../authoring/security/data-retention-and-deletion.md#record-that-deletion-happened-not-what-was-deleted) | Medium |
| Are retention duties identified, stated, and ended? | [honor holds and obligations](../../../authoring/security/data-retention-and-deletion.md#honor-holds-and-obligations) | High |

## Blocking

Blocking: sensitive data with no retention decision, deletion that leaves copies behind, and backups that restore deleted data without re-applying deletions. Others are should fix.
