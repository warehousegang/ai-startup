# Fencing, idempotency and the publication boundary

A **lease** is a time-limited ownership claim. A **fencing epoch** is a monotonically increasing generation. An expired worker can keep running, so the generation must be checked at the **protected mutation boundary** every time.

## Controlled concurrency example

1. Run A claims issue X, epoch 51. A calculates a proposed branch update but stalls.
2. Lease expires. A has not stopped running. Run B claims X, epoch 52.
3. B completes verification and asks the broker to publish a draft PR. The broker checks epoch 52 is current, issue approval is current, repo is allowed, and target SHA matches.
4. A wakes and asks the broker to publish with epoch 51. The broker **denies** it, even if A's diff is valid.
5. If A holds a generic GitHub write credential or unrestricted GitHub MCP write capability, it might bypass the broker. **That breaks fencing**. Remove this bypass.

## The important gap: GitHub is external to the control DB

A trusted broker can atomically verify and enqueue an intent in its own DB, but a GitHub API call is not part of that DB transaction. Between a DB check and the remote call, ownership might change. Design a serialized per-issue/per-resource publisher, protect publish intent with an epoch and expected branch SHA, maintain an idempotency key, and reconcile remote PR/branch state after ambiguous failures. These are not automatically a formally atomic cross-service transaction.

For stricter semantics, the protected system itself must be able to compare generations atomically, or a trusted single-writer gateway must mediate *every* mutation with replay-safe side effects. Some nonreversible APIs do not support full fencing; they may need a stronger action-specific policy, quarantine or human gate.

**Minimum acceptance tests**

- Two workers cannot both hold the authoritative active epoch for one issue.
- Old A cannot publish after B owns newer epoch.
- Revoked approval denies new protected side effects even when existing local code is complete.
- Retried publish cannot create duplicate PRs after timeout.
- Change to branch SHA between prepare and push denies or forces a safe retry.
- Agent with sandbox access cannot discover a direct generic write token bypass.
- Crash after GitHub success but before ledger update is recovered by remote-state reconciliation.

See Martin Kleppmann, [How to do distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html).
