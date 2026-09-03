[中文](discovery.zh-CN.md)

# Discovery Contract

## Scope before facts

Resolve the target path and its nearest Git root. Detect nested repositories and submodules without assuming that a parent status represents them. Record the current branch, HEAD, remotes, and dirty paths using read-only commands. Never expose secrets from configuration, history, or environment output.

## Evidence inventory

Inspect only what is needed to form the proposal:

- existing `AGENTS.md` files and instruction precedence;
- source and package boundaries;
- checked-in configuration and schemas;
- public and internal interfaces between components;
- build, test, lint, formatting, and release entry points;
- documentation and current fact owners;
- decision records and temporary work tracking; and
- operations that can alter production data, external services, credentials, financial state, messages, deployed systems, or physical devices.

Prefer bounded searches and manifest inspection. Non-mutating help, list, parse, and dry-run commands may be observed when their safety is evident. Do not install dependencies or run a command merely because a document names it.

## Evidence grades

- **Established:** directly supported by source, checked-in configuration, or observed output.
- **Documented:** asserted by an existing owner but not independently observed.
- **Unknown:** absent, conflicting, ambiguous, or unsafe to verify.

Do not silently resolve conflicts. Identify each source and keep the claim unknown until an owner or user resolves it.

## Proposal shape

Produce a concise proposal with:

1. Git and repository boundaries;
2. preserved existing and dirty files;
3. current components and developer entry points;
4. unknowns and conflicting claims;
5. the proposed owner map;
6. core files to create or merge;
7. evidence and rationale for conditional owners; and
8. the selected output language.

End by requesting explicit confirmation to write the listed changes. A changed scope requires a revised proposal and confirmation.
