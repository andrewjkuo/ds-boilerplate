# Domain Docs

How engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- `CONTEXT.md` at the repo root.
- `docs/adr/` for ADRs that touch the area about to change.

If either file or directory is still empty, proceed silently. Do not create domain language or decisions just to satisfy this scaffold.

## Source-of-truth boundaries

- `CONTEXT.md` is for domain truth: concepts, invariants, workflows, vocabulary, constraints, and data semantics.
- `AGENTS.md` is for repo operating instructions: commands, structure, workflow boundaries, risks, conventions, and verification expectations.
- `docs/adr/` is for durable decisions and their consequences.
- GitHub Issues are for backlog, PRDs, implementation tickets, prioritization, and status.
- `tasks/todo.md` is for temporary session planning.
- `tasks/lessons.md` is for repo-specific lessons learned from corrections, bugs, failed attempts, or recurring gotchas.

## When to update `CONTEXT.md`

Update `CONTEXT.md` when work reveals a reusable domain fact: a term of art, invariant, lifecycle, unit, identifier, data contract, modelling assumption, or business rule.

Do not put commands, coding style, verification steps, issue status, backlog, or architecture decisions in `CONTEXT.md`.

## When to update `AGENTS.md`

Update `AGENTS.md` when future agents need repo-specific operating guidance: setup commands, test commands, layout, risk areas, source-of-truth boundaries, external services, or verification expectations.

Do not put domain glossary entries, business concepts, or detailed decision rationale in `AGENTS.md`; link to `CONTEXT.md` or an ADR instead.

## Use the project's vocabulary

When output names a domain concept in an issue title, refactor proposal, hypothesis, or test name, use the term as defined in `CONTEXT.md`.

If the needed concept is not in the glossary yet, either use the clearest existing project language or note the gap for a future documentation pass.

## Flag ADR conflicts

If proposed work contradicts an existing ADR, surface the conflict explicitly instead of silently overriding it.
