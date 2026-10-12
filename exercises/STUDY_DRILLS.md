# Practical study drills (work from the PDF)

1. **Draw the trust boundaries.** Place Linear, GitHub, Symphony, App Server, Codex, Claude, MCP, Context7, CI, policy DB, publisher and sandbox on a diagram. Mark which can create authority.
2. **Context design.** Reduce a 2,000-line AGENTS.md to a 100-line map, then construct a targeted plan for a one-endpoint bug.
3. **Skill design.** Make a verification skill that uses a real script. Show why the script's exit code matters more than the skill's prose.
4. **Prompt injection.** Put an instruction in an issue description demanding access to `~/.aws`. Demonstrate independent denial in the filesystem/process boundary.
5. **Context7.** Pick a real locked library version; show the local lockfile, the docs retrieval query and a verifying unit test.
6. **Lease expiry.** Reproduce A(epoch=51) / B(epoch=52). Verify A is refused by the trusted publisher.
7. **Crash reconciliation.** Pretend GitHub successfully created a draft PR but the broker lost the response. Ensure retry finds the PR instead of creating another.
8. **Rollout planning.** Design a six-repo eligibility table and name every high-risk operation that remains human gated.

Completion is demonstrated through artifacts and tests, not a declaration from the agent.
