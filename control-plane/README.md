# Governed control plane - illustrative blueprint

Use this to **review and extend an existing orchestrator**, not to introduce a second competing dispatcher. In a Symphony-based setup, use Symphony for polling, workspace lifecycle and driving Codex; insert external policy, authorization, credential brokering and evidence controls where the reference implementation does not guarantee them.

## Boundary map

- **Linear (intent):** requested issues, approval labels, current issue fields and acceptance criteria. A label is a prerequisite, not a cryptographic proof of authorization.
- **Control store (authority):** ticket version, allowed repository, approval decision, policy version, run owner, fencing epoch, expiration, cancellation and audit history.
- **Agent runtime (work):** compute and tools with constrained network/filesystem; no direct broad write credentials.
- **Publisher (side effects):** mandatory trusted broker that checks the current epoch, ticket state, target repo, allowed action and SHA before GitHub calls. It must implement durable idempotency/recovery for uncertain external outcomes.
- **GitHub / CI (facts and gates):** branch SHA, PR metadata, required checks and protected merge settings.
- **Deployment pipeline (release):** separate environment-level approval, release identity, audit and rollback; default denied to code agents.

## Authoritative state diagram

`DISCOVERED -> APPROVED -> CLAIMED -> RUNNING -> VERIFYING -> DRAFT_PR -> REVIEW` 

On lost approval, canceled task, policy violation or expired current lease, active attempts move to `CANCELLED` / `STALE` and must be denied write effects. A privileged operator can stop dispatch and revoke broker access without cooperation from the agent.

## Required request schema (conceptual)

```json
{
  "issue_id": "GTM-EXAMPLE",
  "issue_revision": "immutable_snapshot_or_revision",
  "repo_id": "exact_allowlisted_org/repo",
  "acceptance_criteria": ["observable acceptance check"],
  "approval_id": "auditable_approval_event",
  "approval_scope": ["edit", "test", "draft_pr"],
  "approval_expires_at": "RFC3339_timestamp",
  "risk_class": "low",
  "base_sha": "immutable_commit_sha"
}
```

A missing field must not be silently filled with guessed permissions. Fetch updated issue state before protected mutations.

## Admission pseudocode

```text
if issue.repo_id not in exact_allowlist: DENY
if issue.approval invalid, expired, revoked or scope missing: DENY
if issue.risk_class != 'low': REQUIRE HUMAN REVIEW
if repository verification adapter unavailable: BLOCK
run_id, epoch = CONTROL_DB.atomic_claim(issue.id, issue.revision)
sandbox = provision_no_host_secrets_and_egress_allowlist(...)
agent_run = invoke_harness_in_sandbox(...)
```

## Don't claim these are already provided by Symphony

Symphony's published spec provides issue-orchestrator operations, concurrency, workspace lifecycle and runner hooks. It explicitly distinguishes workspace isolation from security sandboxing. The policy/identity/side-effect mechanisms described here are an additional recommended architecture and must be tested for the deployed implementation.
