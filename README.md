[中文](README.zh-CN.md)

# Agent Trellis

Agent Trellis is a minimal agent governance system that grows with your codebase. It gives Codex a repository-local map of facts, ownership, validation, durable decisions, and temporary work without assuming a particular language, framework, or deployment model.

## Install

Ask Codex to use `$skill-installer` to install `skills/agent-trellis-init` from `le876/agent-trellis`. Start a new task after installation, then invoke `$agent-trellis-init` in the repository you want to initialize.

Version 1 targets Codex and intentionally has no CLI.

## How initialization works

The initializer follows a confirmation boundary:

1. Audit the repository without writing files.
2. Derive only facts supported by source, configuration, documentation, or observable commands. Leave conflicts and unverifiable claims unknown.
3. Present the proposed owner map and every file to create, merge, or preserve.
4. Wait for explicit confirmation.
5. Write the smallest useful governance layer and validate it.

It never overwrites existing rules, commits, pushes, or runs production, hardware, or other externally mutating operations. A later run performs a drift audit and proposes merges; it is not an upstream synchronizer and does not delete project customizations.

## Generated governance

The core output contains:

- a root `AGENTS.md`;
- owners for architecture, development, and testing facts;
- an Agent Note lifecycle for durable decisions;
- an Active Work lifecycle for temporary cross-session state; and
- generic project documentation, prose, review, simplification, and pre-push Skills.

Safety, security, data-contract, and other specialized owners are generated only when repository evidence requires them. Generated language follows the target repository's established documentation language; the initializer asks when the evidence is ambiguous.

## Repository layout

- [`skills/agent-trellis-init/`](skills/agent-trellis-init/SKILL.md) contains the installable Codex Skill.
- [`i18n/pairs.json`](i18n/pairs.json) declares English and Chinese document pairs. English is canonical; Chinese is a complete synchronized translation.
- [`scripts/validate.py`](scripts/validate.py) checks bilingual structure, links, placeholders, Skill metadata, templates, and fixtures without third-party dependencies.
- [`tests/scenarios.md`](tests/scenarios.md) defines the initialization acceptance scenarios.

## Validate

```sh
python3 scripts/validate.py
```

## License and provenance

Agent Trellis is licensed under the MIT License. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) for the fixed DeepSeek Harness adaptation baseline and its license notice.
