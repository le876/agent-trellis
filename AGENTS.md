[中文](AGENTS.zh-CN.md)

# Repository Instructions

This repository distributes Agent Trellis, not the facts of any repository initialized with it.

## Ownership

- `README.md` owns the public product description and installation entry point.
- `skills/agent-trellis-init/SKILL.md` owns initializer behavior.
- The Skill references own discovery, generation, and validation details.
- English documents and English templates are canonical. Chinese files are complete synchronized translations declared in `i18n/pairs.json`.
- `THIRD_PARTY_NOTICES.md` owns third-party provenance.

Keep each fact in one owner and link to it elsewhere.

## Change rules

- Update both languages in the same change. Preserve heading structure and placeholders across each declared pair.
- Keep public history and distributable assets free of target-repository names, paths, remotes, architecture, commit identifiers, and implementation facts.
- Templates may contain explicit double-braced fields; published documents may not.
- Do not add framework-specific defaults to the core output. Add conditional owners only when the target repository provides evidence for them.
- The initializer must preserve existing user rules and dirty changes, and must require explicit confirmation before writing.

## Validation

Run `python3 scripts/validate.py` before committing or pushing. Report only checks actually run. Do not commit, push, or perform externally mutating operations on behalf of an initialized repository unless its user separately authorizes them.
