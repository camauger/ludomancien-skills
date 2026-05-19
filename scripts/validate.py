#!/usr/bin/env python3
"""Validation locale du marketplace Ludomancien Skills.

Vérifie que :
  - marketplace.json parse et déclare les champs requis
  - chaque plugin.json parse et déclare les champs requis
  - chaque SKILL.md a un frontmatter YAML valide avec name + description
  - chaque skill listé sur disque appartient bien à son plugin
  - chaque agent (fichier .md dans agents/) a un frontmatter YAML valide
    avec name + description
  - les noms dans les frontmatters correspondent aux noms de fichiers/dossiers

Usage:
    python scripts/validate.py

Exit code 0 si tout est OK, 1 sinon.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE_FILE = ROOT / ".claude-plugin" / "marketplace.json"
PLUGINS_DIR = ROOT / "plugins"

REQUIRED_MARKETPLACE_FIELDS = {"name", "owner", "plugins"}
REQUIRED_PLUGIN_FIELDS = {"name", "version", "description"}
REQUIRED_SKILL_FRONTMATTER = {"name", "description"}
REQUIRED_AGENT_FRONTMATTER = {"name", "description"}


@dataclass
class Report:
    """Collecte les erreurs et warnings rencontrés pendant la validation."""

    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    @property
    def ok(self) -> bool:
        return not self.errors


def parse_yaml_frontmatter(text: str) -> dict[str, str] | None:
    """Parse minimaliste du frontmatter YAML d'un SKILL.md.

    On évite de dépendre de PyYAML pour rester sans installation.
    Supporte :
      - paires `clé: valeur` sur une seule ligne
      - folded scalars `clé: >` et literal scalars `clé: |`
        (lignes suivantes indentées, jointes en un seul string)
    """
    if not text.startswith("---"):
        return None
    end_match = re.search(r"\n---\s*\n", text)
    if not end_match:
        return None
    block = text[3 : end_match.start()].strip("\n")
    lines = block.splitlines()
    result: dict[str, str] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in line:
            i += 1
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value in (">", "|", ">-", "|-"):
            # multi-line folded ou literal scalar
            collected: list[str] = []
            i += 1
            while i < len(lines) and (
                lines[i].startswith(("  ", "\t")) or not lines[i].strip()
            ):
                collected.append(lines[i].strip())
                i += 1
            joiner = "\n" if value.startswith("|") else " "
            result[key] = joiner.join(c for c in collected if c)
            continue
        result[key] = value.strip('"').strip("'")
        i += 1
    return result


def validate_marketplace(report: Report) -> dict | None:
    if not MARKETPLACE_FILE.exists():
        report.err(f"missing: {MARKETPLACE_FILE.relative_to(ROOT)}")
        return None
    try:
        data = json.loads(MARKETPLACE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.err(f"invalid JSON in marketplace.json: {exc}")
        return None
    missing = REQUIRED_MARKETPLACE_FIELDS - data.keys()
    if missing:
        report.err(f"marketplace.json missing fields: {sorted(missing)}")
    if not isinstance(data.get("plugins"), list):
        report.err("marketplace.json: 'plugins' must be a list")
    return data


def validate_plugin(plugin_dir: Path, report: Report) -> dict | None:
    manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    rel = plugin_dir.relative_to(ROOT)
    if not manifest.exists():
        report.err(f"missing plugin.json: {rel}")
        return None
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.err(f"invalid JSON in {rel}/plugin.json: {exc}")
        return None
    missing = REQUIRED_PLUGIN_FIELDS - data.keys()
    if missing:
        report.err(f"{rel}/plugin.json missing fields: {sorted(missing)}")
    if data.get("name") != plugin_dir.name:
        report.err(
            f"{rel}/plugin.json: name '{data.get('name')}' "
            f"doesn't match folder name '{plugin_dir.name}'"
        )
    return data


def validate_skill(skill_dir: Path, report: Report) -> None:
    skill_md = skill_dir / "SKILL.md"
    rel = skill_dir.relative_to(ROOT)
    if not skill_md.exists():
        report.err(f"missing SKILL.md: {rel}")
        return
    text = skill_md.read_text(encoding="utf-8")
    fm = parse_yaml_frontmatter(text)
    if fm is None:
        report.err(f"{rel}/SKILL.md: no valid YAML frontmatter")
        return
    missing = REQUIRED_SKILL_FRONTMATTER - fm.keys()
    if missing:
        report.err(f"{rel}/SKILL.md frontmatter missing: {sorted(missing)}")
        return
    if fm["name"] != skill_dir.name:
        report.err(
            f"{rel}/SKILL.md: frontmatter name '{fm['name']}' "
            f"doesn't match folder name '{skill_dir.name}'"
        )
    if len(fm.get("description", "")) < 30:
        report.warn(f"{rel}/SKILL.md: description suspiciously short")
    if len(fm.get("description", "")) > 1536:
        report.warn(
            f"{rel}/SKILL.md: description >1536 chars, "
            f"will be truncated by Claude Code"
        )


def validate_agent(agent_file: Path, report: Report) -> None:
    """Valide un fichier d'agent (markdown avec frontmatter YAML).

    Les agents sont des fichiers .md plats dans <plugin>/agents/, pas
    des dossiers. Le nom de l'agent (frontmatter `name`) doit
    correspondre au nom du fichier sans l'extension.
    """
    rel = agent_file.relative_to(ROOT)
    if agent_file.suffix != ".md":
        report.warn(f"{rel}: agent file is not markdown")
        return
    text = agent_file.read_text(encoding="utf-8")
    fm = parse_yaml_frontmatter(text)
    if fm is None:
        report.err(f"{rel}: no valid YAML frontmatter")
        return
    missing = REQUIRED_AGENT_FRONTMATTER - fm.keys()
    if missing:
        report.err(f"{rel} frontmatter missing: {sorted(missing)}")
        return
    expected_name = agent_file.stem
    if fm["name"] != expected_name:
        report.err(
            f"{rel}: frontmatter name '{fm['name']}' "
            f"doesn't match file name '{expected_name}'"
        )
    if len(fm.get("description", "")) < 30:
        report.warn(f"{rel}: description suspiciously short")
    if len(fm.get("description", "")) > 1536:
        report.warn(
            f"{rel}: description >1536 chars, "
            f"will be truncated by Claude Code"
        )


def main() -> int:
    report = Report()
    marketplace = validate_marketplace(report)
    if marketplace is None:
        _print_report(report)
        return 1

    declared_plugins = {p["name"] for p in marketplace.get("plugins", [])}
    found_plugins = {p.name for p in PLUGINS_DIR.iterdir() if p.is_dir()}

    only_declared = declared_plugins - found_plugins
    only_found = found_plugins - declared_plugins
    for name in sorted(only_declared):
        report.err(f"plugin declared in marketplace.json but missing on disk: {name}")
    for name in sorted(only_found):
        report.warn(f"plugin on disk but not declared in marketplace.json: {name}")

    for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
        if not plugin_dir.is_dir():
            continue
        validate_plugin(plugin_dir, report)
        skills_root = plugin_dir / "skills"
        if not skills_root.exists():
            report.warn(f"{plugin_dir.relative_to(ROOT)}: no skills/ folder")
        else:
            for skill_dir in sorted(skills_root.iterdir()):
                if skill_dir.is_dir():
                    validate_skill(skill_dir, report)
        agents_root = plugin_dir / "agents"
        if agents_root.exists():
            for agent_file in sorted(agents_root.iterdir()):
                if agent_file.is_file():
                    validate_agent(agent_file, report)

    _print_report(report)
    return 0 if report.ok else 1


def _print_report(report: Report) -> None:
    for warning in report.warnings:
        print(f"WARN  {warning}")
    for error in report.errors:
        print(f"ERROR {error}")
    if report.ok:
        print(
            f"OK    {len(report.warnings)} warning(s), no errors. "
            f"Marketplace valid."
        )


if __name__ == "__main__":
    sys.exit(main())
