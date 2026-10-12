# Security boundaries - OWNER INPUT REQUIRED

- Data classification and synthetic fixtures: TODO.
- Paths and subsystems considered privileged: TODO.
- Allowed outbound service list in disposable sandbox: TODO.
- Required code owners and change classes: TODO.
- Logging / redaction requirements: TODO.

**Default-denied:** production deploy/apply, secrets, IAM, infrastructure, database schema/data mutations, protected GitHub Actions settings, cross-repo writes, access to patient/protected data. These need independent policy and owner authorization; adding a line to this document cannot grant it.

A worktree is not a sandbox. No host home directory/cloud credential mounts; use scoped read-only services where necessary and mutation brokering for consequential actions.
