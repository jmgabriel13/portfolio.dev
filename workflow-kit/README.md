# AI Engineering Workflow Kit

This kit shows how I structure AI-assisted engineering work with short, reusable instructions and reviewable task chains.

## Goal

Use Codex and Claude Code as engineering assistants without losing architecture rules, context control, or human review.

## Principles

- Keep project rules short and enforceable.
- Use task-specific skills instead of one large prompt.
- Chain work from planning to implementation to validation.
- Treat AI output as a draft that must be reviewed, tested, and corrected.
- Prefer small context files that are easy to maintain.

## Contents

- `AGENTS.md` - default engineering behavior for a project.
- `skills/plan-feature.md` - feature planning skill.
- `skills/implement-change.md` - implementation skill.
- `skills/review-change.md` - code review skill.
- `workflows/feature-delivery.md` - end-to-end feature workflow.
- `examples/context-budgeting.md` - example of keeping instructions short but useful.

## Example Chain

1. Understand the request and inspect source-of-truth docs.
2. Produce a short implementation plan.
3. Implement only the scoped change.
4. Run targeted validation.
5. Review for architecture, error handling, tests, and maintainability.
6. Update only the documentation that changed behavior requires.
