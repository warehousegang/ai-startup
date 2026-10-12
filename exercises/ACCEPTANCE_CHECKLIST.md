# Agentic engineering - minimum acceptance gates

## Admission
- [ ] Unapproved ticket never launches.
- [ ] Ticket targeting a seventh/unrecognized repository is denied.
- [ ] Approval revocation prevents new mutations.
- [ ] Tickets with missing acceptance criteria or ambiguous repo fail closed.

## Environment
- [ ] Process has no access to host SSH agent, cloud profiles, production secrets or patient data.
- [ ] Sandbox cannot reach a disallowed external endpoint.
- [ ] Agent cannot rewrite branch protection, production deploy settings or security enforcement.
- [ ] Every run has an isolated checkout and immutable base revision.

## Correctness
- [ ] `make agent-verify` fails in an unconfigured repo.
- [ ] Required CI checks are independently protected.
- [ ] PR includes evidence tied to issue/run/repo/SHA.
- [ ] Reviewer can reproduce relevant behavior with synthetic fixtures.

## Concurrency / operations
- [ ] Two attempts cannot both publish using the same issue approval.
- [ ] Stale epoch after crash/lease expiry cannot write.
- [ ] Duplicate publication attempt does not make duplicate PRs.
- [ ] Process crash and remote API ambiguity are reconciled.
- [ ] Budget exhaustion stops execution and requires fresh authorization.
- [ ] Kill switch stops dispatch and denies protected mutations without cooperation by agents.

## Release
- [ ] Auto-merge disabled until protected policy is explicit.
- [ ] Production release uses a separate environment and authorization boundary.
- [ ] Cross-repo edits require a dependency/scope approval model, not implicit agent discretion.
