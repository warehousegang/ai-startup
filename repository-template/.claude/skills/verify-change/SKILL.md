---
name: verify-change
description: Verify a scoped code change using the repository's deterministic checks; use before drafting a PR, reviewing a diff, or claiming completion.
---

# Verify a change

Read the short repo `AGENTS.md` first. Run `make agent-verify`, capture its true exit code and logs, never weaken tests and report `BLOCKED` if checks cannot execute. Scope is limited to the approved issue; this skill grants no write, merge or deployment authority.
