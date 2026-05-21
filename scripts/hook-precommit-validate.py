#!/usr/bin/env python3
"""Hook PreToolUse appelé avant `git commit` (filtré par `if`).

Lance `scripts/validate.py` et BLOQUE le commit si la validation échoue.
En cas de succès, ne fait rien (le commit passe normalement).

Le hook reçoit du JSON sur stdin (tool_input, tool_name, etc.) mais n'en a
pas besoin ici — le filtrage par commande est fait côté Claude Code via le
champ `if` dans settings.local.json.

Output attendu en cas de blocage : JSON sur stdout avec
hookSpecificOutput.permissionDecision = "deny" et la raison.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    validate_script = repo_root / "scripts" / "validate.py"

    if not validate_script.exists():
        # Pas de validateur trouvé — ne bloque pas (silent pass).
        return 0

    # Drain stdin pour ne pas casser le pipe si Claude Code en envoie.
    try:
        sys.stdin.read()
    except Exception:
        pass

    result = subprocess.run(
        [sys.executable, str(validate_script)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(repo_root),
    )

    if result.returncode == 0:
        # Validation OK — commit passe.
        return 0

    # Blocage du commit avec la raison détaillée.
    stdout = (result.stdout or "").strip()
    stderr = (result.stderr or "").strip()
    reason_parts = ["validate.py a échoué — commit bloqué."]
    if stdout:
        reason_parts.append(stdout)
    if stderr:
        reason_parts.append(stderr)
    reason = "\n\n".join(reason_parts)

    hook_output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    # Important : stdout UTF-8 pour les accents français.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    json.dump(hook_output, sys.stdout, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
