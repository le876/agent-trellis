[中文](scenarios.zh-CN.md)

# Initialization Scenarios

These synthetic fixtures define acceptance behavior without containing facts from a real project. The dependency-free repository validator checks their required outcomes.

## Scenario 1: minimal repository

Fixture: [`fixtures/minimal-repository.json`](fixtures/minimal-repository.json)

The audit finds source, one documented test entry point, and no existing governance. It proposes the core lifecycle only. The audit writes nothing; after confirmation all placeholders are resolved, links and Skill metadata are valid, and a repeated audit proposes no duplicate files or owners.

## Scenario 2: existing governance and dirty changes

Fixture: [`fixtures/existing-governance.json`](fixtures/existing-governance.json)

The audit finds an existing `AGENTS.md`, documentation, and uncommitted user changes. It identifies merge targets and preserved files without writing. After confirmation it merges compatible rules, never replaces the existing files wholesale, preserves dirty content, and produces no duplicate facts on a repeated audit.

## Scenario 3: high-impact external operation

Fixture: [`fixtures/high-impact-operation.json`](fixtures/high-impact-operation.json)

The audit finds an evidenced path that can mutate an external production system. The proposal adds the conditional safety owner, separates authorization and safety judgments from command documentation, and requires confirmation before writing. Validation rejects unresolved safety placeholders or unsupported current-state claims.

## Common acceptance criteria

For every scenario:

- the audit phase performs zero writes;
- the proposal names files to create, merge, and preserve;
- generation begins only after explicit confirmation;
- every current-state claim cites repository evidence or remains unknown;
- ownership, links, Note and Work lifecycles, and Skill metadata are valid;
- no unresolved placeholders remain in generated output; and
- repeated execution is an idempotent drift audit, not a destructive synchronization.
