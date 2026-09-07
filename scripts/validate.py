#!/usr/bin/env python3
"""Validate the Agent Trellis distribution with the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAIR_MANIFEST = ROOT / "i18n" / "pairs.json"
HEADING_RE = re.compile(r"^(#{1,6})\s+", re.MULTILINE)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z][A-Z0-9_]*\}\}")
SKILL_FILES = (
    *sorted((ROOT / "skills").glob("*/SKILL.md")),
    *sorted((ROOT / "skills" / "agent-trellis-init" / "assets").rglob("SKILL.md.tmpl")),
)


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def validate_pairs(check: Validation) -> None:
    manifest = json.loads(read(PAIR_MANIFEST))
    declared: set[str] = set()

    check.require(manifest.get("canonical_language") == "en", "English must be canonical")
    check.require(manifest.get("translation_language") == "zh-CN", "Chinese locale must be zh-CN")

    for pair in manifest.get("pairs", []):
        en = ROOT / pair["en"]
        zh = ROOT / pair["zh"]
        declared.update((pair["en"], pair["zh"]))
        check.require(en.is_file(), f"missing English pair: {pair['en']}")
        check.require(zh.is_file(), f"missing Chinese pair: {pair['zh']}")
        if not en.is_file() or not zh.is_file():
            continue

        en_text = read(en)
        zh_text = read(zh)
        check.require(
            HEADING_RE.findall(en_text) == HEADING_RE.findall(zh_text),
            f"heading structure differs: {pair['en']} / {pair['zh']}",
        )
        check.require(
            sorted(PLACEHOLDER_RE.findall(en_text)) == sorted(PLACEHOLDER_RE.findall(zh_text)),
            f"placeholder set differs: {pair['en']} / {pair['zh']}",
        )
        check.require(
            len(LINK_RE.findall(en_text)) == len(LINK_RE.findall(zh_text)),
            f"link structure differs: {pair['en']} / {pair['zh']}",
        )
        if pair.get("navigable"):
            check.require(zh.name in en_text, f"English file does not link Chinese pair: {pair['en']}")
            check.require(en.name in zh_text, f"Chinese file does not link English pair: {pair['zh']}")

    markdown = {
        relative(path)
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and (path.name.endswith(".md") or path.name.endswith(".md.tmpl"))
    }
    for path in sorted(markdown - declared):
        check.errors.append(f"Markdown file is not declared in i18n/pairs.json: {path}")
    for path in sorted(declared - markdown):
        check.errors.append(f"i18n pair does not resolve to Markdown: {path}")


def validate_links(check: Validation) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for raw_target in LINK_RE.findall(read(path)):
            target = raw_target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            check.require(resolved.exists(), f"broken link in {relative(path)}: {raw_target}")


def template_output_path(seed: Path, template: Path) -> Path:
    output = Path(template.relative_to(seed).as_posix().removesuffix(".tmpl"))
    if output.parts and output.parts[0] == "conditional":
        output = Path(*output.parts[1:])
    return output


def validate_template_trees(check: Validation) -> None:
    required = {
        Path("AGENTS.md"),
        Path("docs/AGENTS.md"),
        Path("docs/architecture.md"),
        Path("docs/development.md"),
        Path("docs/testing.md"),
        Path(".agents/notes/README.md"),
        Path(".agents/notes/AGENTS.md"),
        Path(".agents/notes/implemented/process/YYYY-MM-DD-adopt-agent-trellis.md"),
        Path(".agents/work/README.md"),
        Path(".agents/work/AGENTS.md"),
        Path(".agents/skills/project-doc/SKILL.md"),
        Path(".agents/skills/project-prose-standard/SKILL.md"),
        Path(".agents/skills/project-trim-cot-leakage/SKILL.md"),
        Path(".agents/skills/project-code-review/SKILL.md"),
        Path(".agents/skills/project-find-simplifications/SKILL.md"),
        Path(".agents/skills/project-pre-push-checks/SKILL.md"),
        Path("docs/safety.md"),
        Path("docs/contracts.md"),
    }

    for locale in ("en", "zh-CN"):
        seed = ROOT / "skills" / "agent-trellis-init" / "assets" / locale / "seed"
        templates = list(seed.rglob("*.tmpl"))
        outputs = {template_output_path(seed, path): path for path in templates}
        check.require(set(outputs) == required, f"{locale} template output set is incomplete or unexpected")

        for output, source in outputs.items():
            for raw_target in LINK_RE.findall(read(source)):
                target = raw_target.split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = Path((output.parent / target).as_posix())
                check.require(resolved in outputs, f"broken materialized link in {relative(source)}: {raw_target}")


def parse_frontmatter(path: Path, check: Validation) -> dict[str, str]:
    lines = read(path).splitlines()
    check.require(bool(lines) and lines[0] == "---", f"missing frontmatter start: {relative(path)}")
    try:
        end = lines.index("---", 1)
    except ValueError:
        check.errors.append(f"missing frontmatter end: {relative(path)}")
        return {}

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            check.errors.append(f"invalid frontmatter line in {relative(path)}: {line}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate_skills(check: Validation) -> None:
    for path in SKILL_FILES:
        fields = parse_frontmatter(path, check)
        check.require(set(fields) == {"name", "description"}, f"invalid Skill fields: {relative(path)}")
        name = fields.get("name", "")
        description = fields.get("description", "")
        check.require(bool(re.fullmatch(r"[a-z0-9-]{1,64}", name)), f"invalid Skill name: {relative(path)}")
        check.require(1 <= len(description) <= 1024, f"invalid Skill description: {relative(path)}")

    catalog = read(ROOT / "skills" / "agent-trellis-init" / "agents" / "openai.yaml")
    check.require('display_name: "Agent Trellis Init"' in catalog, "Skill catalog display name is missing")
    check.require('short_description: "Bootstrap repository-native Codex governance"' in catalog, "Skill catalog description is missing")
    check.require("$agent-trellis-init" in catalog, "Skill catalog prompt must invoke $agent-trellis-init")


def validate_placeholders(check: Validation) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.name.endswith(".tmpl"):
            continue
        if path.suffix not in {".md", ".py", ".yml", ".yaml", ".json"}:
            continue
        check.require(not PLACEHOLDER_RE.search(read(path)), f"unresolved placeholder in {relative(path)}")


def validate_fixtures(check: Validation) -> None:
    fixture_dir = ROOT / "tests" / "fixtures"
    fixtures = {path.stem: json.loads(read(path)) for path in fixture_dir.glob("*.json")}
    check.require(
        set(fixtures) == {"minimal-repository", "existing-governance", "high-impact-operation"},
        "fixture set must cover the three initialization scenarios",
    )
    for name, fixture in fixtures.items():
        expected = fixture.get("expected", {})
        check.require(expected.get("audit_writes") == 0, f"{name}: audit must be read-only")
        check.require(expected.get("confirmation_required") is True, f"{name}: confirmation is required")
        check.require(expected.get("repeat_action") == "drift-audit", f"{name}: repeat must audit drift")
    existing = fixtures.get("existing-governance", {}).get("expected", {})
    check.require(existing.get("overwrite_existing") is False, "existing governance must not be overwritten")
    check.require(existing.get("preserve_dirty") is True, "dirty changes must be preserved")
    high_impact = fixtures.get("high-impact-operation", {}).get("expected", {})
    check.require(
        "docs/safety.md" in high_impact.get("conditional_owners", []),
        "high-impact fixture must require a safety owner",
    )


def main() -> int:
    check = Validation()
    validate_pairs(check)
    validate_links(check)
    validate_template_trees(check)
    validate_skills(check)
    validate_placeholders(check)
    validate_fixtures(check)

    if check.errors:
        for error in check.errors:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(check.errors)} error(s).")
        return 1

    print("Validation passed: i18n, links, Skills, placeholders, and fixtures are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
