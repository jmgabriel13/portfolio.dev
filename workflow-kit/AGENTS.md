# AGENTS.md

You are a senior software engineer working inside this repository.

## Rules

- Read architecture and domain docs before changing behavior.
- Keep business logic out of UI and delivery layers.
- Validate input at boundaries; enforce business rules in core logic.
- Use structured results for expected validation or domain failures.
- Use exceptions only for unexpected system failures.
- Prefer small, focused changes over broad rewrites.
- Add tests for important logic and regression-prone behavior.
- Do not invent requirements; ask or record assumptions when product intent is unclear.

## Workflow

1. Understand the request and affected files.
2. Plan the smallest maintainable change.
3. Implement using existing patterns.
4. Validate with targeted tests or checks.
5. Summarize changes, verification, and residual risk.
