---
name: agent-trellis-init
description: Initialize or audit a repository-local Codex governance layer from evidence in an existing codebase. Use when a user wants to bootstrap AGENTS.md, documentation ownership, decision and work lifecycles, or reusable project Skills without overwriting existing rules.
---

[中文](SKILL.zh-CN.md)

# Agent Trellis Init

Build the smallest governance layer that accurately describes the target repository today and can grow through use.

## Non-negotiable boundary

Follow two separate phases:

1. Perform a read-only audit and present an initialization proposal.
2. Write only after the user explicitly confirms that proposal.

A request to “initialize” starts phase one; it is not confirmation for phase two. Before confirmation, do not create, modify, rename, or delete files.

Never commit, push, rewrite history, contact production services, operate physical systems, or perform other externally mutating actions as part of this Skill. Preserve existing rules and dirty changes.

## Phase one: audit and propose

Read [the discovery contract](references/discovery.md) completely before inspecting the target. Establish the Git boundary and inspect existing instructions, source, configuration, tests, documentation, build entry points, component relationships, and high-impact operations.

Treat source, checked-in configuration, and observed non-mutating command output as evidence. Record conflicts and unverifiable claims as unknown. Do not turn names or plausible conventions into facts.

Determine the target documentation language from established project documentation. Ask the user when it is ambiguous.

Present:

- repository boundaries and preserved dirty changes;
- the evidence-backed current-state summary and unknowns;
- a single-owner map for durable facts; and
- every file to create, merge, or leave unchanged.

Explain which conditional owners are justified. Wait for explicit confirmation.

## Phase two: generate and validate

After confirmation, read [the generation contract](references/generation-contract.md) completely. Use the matching language tree under `assets/`. Replace every placeholder with an evidenced value or an explicit unknown that the owning document can safely retain.

Merge deliberately with existing files. Do not replace an existing `AGENTS.md`, policy, documentation owner, or project Skill wholesale. When a conflict requires a user decision, stop and present it.

Create only the core lifecycle and evidence-backed conditional owners. Keep one owner for each fact and use links elsewhere.

Then read and follow [the validation contract](references/validation.md). Report created, merged, and preserved files separately, together with checks actually run and unresolved unknowns.

## Later runs

On an initialized repository, repeat the read-only audit and propose drift repairs. Do not behave as an upstream template synchronizer, remove project customizations, or create duplicate owners, notes, work items, or Skills.
