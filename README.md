# Autonomous Engineering - Agent-Ready Repository Starter

**Status: educational scaffolding, not an authorized running orchestration service.**

This companion accompanies *Autonomous Engineering: Control Planes and Agent-Ready Repositories* (October 2026). It supplies a small, reviewable starting point for **one repository at a time** and an illustrative control-plane blueprint.

## First adoption path (do this in order)

1. Identify **one** pilot repository and a single approved test issue. Confirm who is responsible for its source, CI and secrets.
2. Copy `repository-template/` **contents** into a branch of that repo. Resolve placeholder information in `AGENTS.md`, `ARCHITECTURE.md`, `docs/PRODUCT.md` and `docs/SECURITY.md`.
3. Supply `scripts/verify-local.sh` with the **real**, deterministic checks for that repo; the included `scripts/verify.sh` deliberately fails without it. Validate clean and intentionally failing changes.
4. Configure GitHub required checks and approvals in GitHub settings. The sample GitHub Actions job **does not** modify branch protection or grant permissions.
5. Review the `control-plane/` documentation with the owner of the existing Symphony deployment. Make write credentials, approval and stale-run denial independent of agent text or local files.
6. Test one isolated ticket-to-draft-PR cycle. Then test revoked approval, agent crash, out-of-budget, bad CI and stale-epoch scenarios **before** enrolling another repo.

## Key boundaries

- `AGENTS.md`, `CLAUDE.md`, `SKILL.md` and instructions are **guidance**, not an authority or a security sandbox.
- A Git worktree is **not** a sandbox. Isolate the process, host mounts, credentials, network and tool access separately.
- The agent must not possess generic GitHub, Linear, cloud or production write credentials. Route consequential changes through a trusted broker with current authorization.
- A fencing epoch only protects a resource if the **resource or a mandatory broker** checks it on each protected mutation. If the sandbox can bypass the broker, the fence does not work.
- GitHub cannot natively enforce an arbitrary external fencing epoch. Use mutation-time checks, conditional SHA updates, constrained credentials, idempotency and recovery; do not mistake these for a distributed transaction across GitHub and your DB.
- Keep patient/production data and long-lived keys out of test sandboxes. Default to synthetic/de-identified fixtures.

## Package layout

- `repository-template/` - concise instructions, security/docs skeleton, local validation contract, CI example and on-demand skills.
- `control-plane/` - state model, request/approval schema, fencing boundaries and example policy (not a runnable policy engine).
- `exercises/` - acceptance and adversarial tests, a learning checklist, and an API-free stale epoch demonstration.

## Status of the example CI

The sample CI job intentionally runs `make agent-verify`, which fails with exit status 2 until the repository owner supplies an executable `scripts/verify-local.sh`. It is a **fail-closed baseline**. Do not weaken the script to make CI green.

## Where to begin reading

Read PDF chapters 4-5, 6-7, 9-11 and 14 before changing orchestration settings. The PDF has official source links (OpenAI, Anthropic, MCP, Context7 and fencing-token research).

Author: Thomas Howard