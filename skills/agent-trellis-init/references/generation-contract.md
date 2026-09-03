[中文](generation-contract.zh-CN.md)

# Generation Contract

## Select and materialize templates

Use `assets/en/seed/` for English output or `assets/zh-CN/seed/` for Chinese output. Preserve the relative path and remove the `.tmpl` suffix. For an evidence-backed file under `conditional/`, also remove the leading `conditional/` path segment. Replace every double-braced template field; no unresolved placeholder may enter the target repository.

Generate one language, following the target's established documentation language. Do not install the distribution repository's bilingual pairing policy into the target unless the target already maintains that policy.

## Core lifecycle

The default proposal contains:

- root `AGENTS.md` for boundaries, ownership, workflow, and safety routing;
- `docs/AGENTS.md` for documentation rules;
- `docs/architecture.md` for current component and interface relationships;
- `docs/development.md` for environment and canonical developer commands;
- `docs/testing.md` for validation entry-point status and result interpretation;
- `.agents/notes/` for durable decisions, with its contract, local instructions, and one adoption Note;
- `.agents/work/` for temporary cross-session execution state and its local instructions; and
- the six project Skills supplied by the selected asset tree.

Do not create an Active Work Item unless the initialization itself will span sessions or requires an explicit handoff.

## Conditional owners

Create `docs/safety.md` when evidence reveals high-impact external operations whose authorization and safe boundary need a durable owner. Create `docs/contracts.md` when multiple components depend on a shared schema, protocol, identity, ordering, unit, coordinate, or time convention that lacks an adequate owner.

Security, privacy, deployment, migration, compliance, and other specialized documents follow the same rule: add one only for an established need, and define its exact ownership. Never copy a speculative checklist into the current-state documentation.

## Merge policy

- Preserve all existing content until its intent and owner are understood.
- Add links to an existing adequate owner instead of creating a competing document.
- Merge rules at the narrowest applicable `AGENTS.md` scope.
- Keep current-state facts in owning documents, durable reasons in Agent Notes, and temporary execution state in Active Work Items.
- Record an unknown explicitly when correctness depends on it; omit trivia that has no operational consequence.
- Never modify source, product configuration, or unrelated documentation during initialization.

The adoption Note records the accepted governance boundary and tradeoffs. It must not narrate the editing session or claim validation that was not performed.
