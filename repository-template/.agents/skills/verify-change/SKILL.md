---
name: verify-change
description: Verify a scoped code change using the repository's deterministic checks; use before drafting a PR, reviewing a diff, or claiming completion.
---

# Verify the authorized change

1. Confirm issue authorization and inspect the changed paths.
2. Read `AGENTS.md`, then run `make agent-verify` in the configured isolated environment.
3. Preserve the full command/exit code/test artifacts in the runner logs.
4. If a check fails, repair within the approved file scope and rerun. Never weaken a test to force success.
5. If setup is missing, report `BLOCKED`, not `PASS`; raise a prerequisite task.
6. Before PR handoff, describe the base SHA, changed paths, exact checks, their outcomes and unresolved risks.

The skill supplies instructions. Actual gatekeeping must be implemented by CI and trusted control-plane policy.
