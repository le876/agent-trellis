[中文](validation.zh-CN.md)

# Validation Contract

## Structural checks

After writing, verify that:

- every linked local file and heading exists;
- every durable fact has one clear owner;
- architecture describes only evidenced component and interface relationships;
- testing owns validation entry-point status and result interpretation;
- safety, when present, owns authorization and safety judgments rather than command documentation;
- development owns canonical commands and environment setup;
- Note and Work contracts define creation, update, completion, and archival behavior;
- each installed Skill has valid frontmatter with only `name` and `description`; and
- no unresolved double-braced template fields remain.

Use the target repository's existing validators when they are safe, available, and relevant. Add no dependency merely to validate initialization.

## Behavioral checks

Confirm from the final diff that existing instructions and user changes were preserved. Check that conditional owners have cited repository evidence and that unknown facts remain unknown. A second dry audit must propose no duplicate files or duplicated ownership.

Do not mark a check passed unless it was run and its result observed. Record unavailable or unsafe checks as not run, with the reason.

## Handoff

Report:

1. files created, merged, and preserved;
2. owner-map changes;
3. conditional owners and their evidence;
4. checks run with outcomes;
5. unresolved unknowns or conflicts; and
6. whether a repeated audit is idempotent.

Leave the target worktree uncommitted. Committing and pushing require a separate user request.
