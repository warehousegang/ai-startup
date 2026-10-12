# Symphony WORKFLOW.md design notes

**Not a runnable `WORKFLOW.md`.** Before configuring anything, consult the exact deployed version of the [Symphony specification](https://github.com/openai/symphony/blob/main/SPEC.md) and runtime's supported front matter and path syntax.

A safe workflow specification should specify:

- Explicit eligible Linear issue state/labels, exact owner, and exactly one allowlisted repository.
- Immutable issue snapshot / current-version validation before each dispatch and protected publication.
- Per-issue isolated workspace, bounded concurrency, retries and run timeout.
- Prompt comprising issue details, acceptance criteria, repo map, read-only documentation and required final evidence.
- No generic GitHub/AWS/production tokens in the agent environment, no `--dangerously-skip-permissions` with unrestricted host privileges.
- Readiness check for repo verification adapter and no unreviewed protected CI edits.
- Trusted, epoch-aware publication and audit ledger OUTSIDE the agent's instruction scope.
- Explicit cancellation reconciliation and operator kill switch.

Do not replace an existing working Symphony deployment or lose its execution ledgers while adding this policy. Validate the deployed semantics and test a disposable issue first.
