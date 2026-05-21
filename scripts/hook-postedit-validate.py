#!/usr/bin/env python3
"""Hook PostToolUse appelé après Write/Edit.

Si le fichier édité matche `plugins/<plugin>/skills/<skill>/SKILL.md` ou
`plugins/<plugin>/agents/<agent>.md`, lance `scripts/validate.py` et
remonte les warnings/erreurs dans la session via `systemMessage`.

Pour tout autre fichier, no-op silencieux.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


TARGET_PATTERNS = [
    re.compile(r"plugins/[^/]+/skills/[^/]+/SKILL\.md$"),
    re.compile(r"plugins/[^/]+/agents/[^/]+\.md$"),
]


def extract_file_path(hook_input: dict) -> str:
    """Récupère le chemin de fichier depuis l'input du hook."""
    tool_input = hook_input.get("tool_input") or {}
    tool_response = hook_input.get("tool_response") or {}
    for candidate in (
        tool_input.get("file_path"),
        tool_response.get("filePath"),
        tool_response.get("file_path"),
    ):
        if isinstance(candidate, str) and candidate:
            return candidate
    return ""


def matches_target(file_path: str) -> bool:
    normalized = file_path.replace("\\", "/")
    return any(p.search(normalized) for p in TARGET_PATTERNS)


def main() -> int:
    # Lire l'input du hook depuis stdin (JSON).
    try:
        raw = sys.stdin.read()
        hook_input = json.loads(raw) if raw.strip() else {}
    except (json.JSONDecodeError, ValueError):
        return 0

    file_path = extract_file_path(hook_input)
    if not file_path or not matches_target(file_path):
        return 0

    repo_root = Path(__file__).resolve().parent.parent
    validate_script = repo_root / "scripts" / "validate.py"
    if not validate_script.exists():
        return 0

    result = subprocess.run(
        [sys.executable, str(validate_script)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(repo_root),
    )

    output = (result.stdout or "").strip()
    has_issues = (
        result.returncode != 0
        or "WARN" in output
        or "ERROR" in output
    )
    if not has_issues:
        # Tout va bien — silencieux.
        return 0

    # Remonter les défauts dans la session.
    short_path = file_path.replace("\\", "/").split("ludomancien-skills/", 1)[-1]
    message = f"validate.py après édition de {short_path} :\n{output}"

    hook_output = {
        "systemMessage": message,
        "suppressOutput": True,
    }
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    json.dump(hook_output, sys.stdout, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
