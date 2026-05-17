#!/usr/bin/env python3
"""TTRPG Playtest Orchestrator.

Run a multi-pass playtest of a TTRPG scenario using the Anthropic API.

Pipeline
--------
1. Parse scenario input (Markdown, plain text).
2. Pass 1 — Mechanical audit (system-adapted; skipped in narrative mode).
3. Pass 2 — Simulated playthrough with five player personas (skipped in
   quick mode).
4. Pass 3 — Per-persona feedback (skipped in quick mode).
5. Pass 4 — Cross-referenced synthesis with verdict and ranked top fixes.
6. Render a Markdown report and a structured JSON sidecar.

Dry-run by default. Pass ``--run`` to actually call the API.

Usage
-----
    python playtest_orchestrator.py scenario.md
    python playtest_orchestrator.py scenario.md --run
    python playtest_orchestrator.py scenario.md --system osr --run
    python playtest_orchestrator.py scenario.md --mode quick --run
    python playtest_orchestrator.py scenario.md \\
        --party "4 PCs level 3, fighter+thief+cleric+MU" \\
        --output ./reports/ \\
        --run

Requirements
------------
    pip install anthropic

Environment
-----------
    ANTHROPIC_API_KEY must be set.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Literal

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic", file=sys.stderr)
    sys.exit(1)


# =============================================================================
# Constants
# =============================================================================

System = Literal["5e2024", "5e2014", "osr", "pbta", "fitd", "generic"]
Mode = Literal["full", "quick", "narrative"]
Severity = Literal["critical", "high", "medium", "low", "note"]

SEVERITY_ORDER: dict[Severity, int] = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
    "note": 4,
}

DEFAULT_MODEL = "claude-sonnet-4-6"
DEFAULT_PARTY = "4 PCs at scenario target level, mixed roles (1 tank, 1 healer, 1 striker, 1 utility/skills)"
MAX_TOKENS_PER_PASS: dict[str, int] = {
    "mechanical": 6000,
    "playthrough": 8000,
    "persona": 2500,
    "synthesis": 6000,
}


# =============================================================================
# Data models
# =============================================================================


@dataclass(frozen=True)
class Persona:
    """A player archetype used in passes 2 and 3."""

    key: str
    name: str
    archetype: str
    priorities: str
    watching_for: str
    voice: str

    def as_prompt_block(self) -> str:
        """Render the persona as a prompt-ready block."""
        return (
            f"### {self.name} — {self.archetype}\n"
            f"- Priorities: {self.priorities}\n"
            f"- Watching for: {self.watching_for}\n"
            f"- Voice: {self.voice}\n"
        )


@dataclass(frozen=True)
class Finding:
    """A single mechanical-audit finding."""

    severity: Severity
    location: str
    description: str
    fix: str

    def as_markdown(self) -> str:
        return (
            f"- **{self.location}** — {self.description} "
            f"**Fix:** {self.fix}"
        )


@dataclass
class PlaytestConfig:
    """Configuration for a single playtest run."""

    scenario_path: Path
    system: System = "5e2024"
    mode: Mode = "full"
    party: str = DEFAULT_PARTY
    model: str = DEFAULT_MODEL
    output_dir: Path = field(default_factory=lambda: Path("./playtest-reports"))
    dry_run: bool = True

    @property
    def scenario_slug(self) -> str:
        return self.scenario_path.stem.lower().replace(" ", "-")


@dataclass
class PlaytestReport:
    """Aggregated output of a playtest run."""

    scenario_title: str
    config: PlaytestConfig
    mechanical_raw: str = ""
    mechanical_findings: list[Finding] = field(default_factory=list)
    transcript: str = ""
    persona_feedback: dict[str, str] = field(default_factory=dict)
    synthesis_verdict: str = ""
    synthesis_coverage_map: str = ""
    synthesis_top_fixes: str = ""
    synthesis_what_works: str = ""
    synthesis_cross_patterns: str = ""
    synthesis_raw: str = ""
    generated_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def to_json_safe(self) -> dict[str, Any]:
        """Convert to a JSON-serializable dict."""
        data = asdict(self)
        data["config"]["scenario_path"] = str(self.config.scenario_path)
        data["config"]["output_dir"] = str(self.config.output_dir)
        return data


# =============================================================================
# Personas
# =============================================================================

PERSONAS: list[Persona] = [
    Persona(
        key="mael",
        name="Maël",
        archetype="The Tactician",
        priorities="Clear stakes; meaningful, consequential choices; consistent rule application; time to think.",
        watching_for="Illusory choice; DCs without context; combat trivialized by obvious tactics; hidden info the party can't access.",
        voice="Measured, precise, sometimes blunt. Names mechanics when they matter. Mixes IC and OOC freely.",
    ),
    Persona(
        key="salome",
        name="Salomé",
        archetype="The Method Actor",
        priorities="NPC interiority; room for dialogue and reaction; moral ambiguity; continuity in characterization.",
        watching_for="NPCs as info-dumps; scenes that skip the emotional beat; read-aloud that tells the party how their characters feel.",
        voice="Stays IC across transitions. Uses third person when in deep character voice. Reflective, sometimes slow.",
    ),
    Persona(
        key="jonas",
        name="Jonas",
        archetype="The Power Gamer",
        priorities="Encounters tuned to the party's actual capability; build payoff; mechanical clarity; varied challenge.",
        watching_for="Trivial fights; save-or-suck against single PCs; lethal spikes; plot armor overriding mechanics.",
        voice="Mechanically literate, fast, transactional. Drops vocabulary like 'save DC,' 'AC,' 'advantage' without context.",
    ),
    Persona(
        key="ines",
        name="Inès",
        archetype="The Storyteller",
        priorities="Clear narrative arc; themes engaged; callbacks; memorable beats.",
        watching_for="Episodic scenarios; weak climaxes; themes claimed but not honored; loot epilogues that fizzle the ending.",
        voice="Reflective, sometimes meta. Will narrate her own actions in prose. Comfortable shifting between IC and OOC.",
    ),
    Persona(
        key="tarek",
        name="Tarek",
        archetype="The Specialist",
        priorities="Pillar variety (combat/exploration/social); spotlight moments for niche expertise; opposition that engages his build.",
        watching_for="One-pillar scenarios; group skill-check rolls that make his +9 redundant; critical clues behind a single check.",
        voice="Knowledgeable, sometimes pedantic. Cites lore. Specific. Goes quiet in scenes that don't engage his niche.",
    ),
]


# =============================================================================
# System adapters
# =============================================================================

SYSTEM_DESCRIPTIONS: dict[System, str] = {
    "5e2024": (
        "D&D 5e 2024 rules. Use the 2024 encounter-budget tables (Low/Moderate/High XP per PC by "
        "level). Save DC tier bands: tier 1 (lvl 1-4) DC 11-15; tier 2 (5-10) DC 13-17; tier 3 "
        "(11-16) DC 15-19; tier 4 (17-20) DC 17-22. Boss fights need ≥3 turns/round opposing side "
        "OR legendary actions/resistance. Single-hit damage exceeding 2x PC HP is a flag. "
        "Action economy: party of 4 generates ~6-8 actions/round counting bonus actions."
    ),
    "5e2014": (
        "D&D 5e 2014 rules. Use the 2014 Easy/Medium/Hard/Deadly encounter budget with multipliers "
        "for monster count. Same tier bands as 2024. Pre-2024 solo bosses without legendary "
        "actions are significantly weaker than the math suggests — flag aggressively."
    ),
    "osr": (
        "OSR family (B/X, OSE, Knave, Cairn, Mausritter, Into the Odd, Mörk Borg). Lethality-and-"
        "attrition focused. Audit asks about: lethality calibration; resource attrition curve "
        "(torches, rations, HP, slots); fail-forward gates; turn-budget for dungeon/hexcrawl; "
        "treasure-as-XP economy where applicable; reaction/morale roll prescription. Do NOT audit "
        "for 5e-style encounter balance — that's not how OSR fights work."
    ),
    "pbta": (
        "Powered by the Apocalypse (Apocalypse World, Monsterhearts, Masks, Monster of the Week, "
        "etc.). Audit MC technique rather than numerical balance: threat type clarity; MC move "
        "opportunities in silences; snowball escalation; principles adherence; playbook engagement "
        "(every playbook gets a scene where their moves come up); custom move triggers."
    ),
    "fitd": (
        "Forged in the Dark (Blades in the Dark, Scum & Villainy, Band of Blades, etc.). Audit: "
        "faction tier vs. crew tier; score scale (fortune roll, single score, multi-stage op); "
        "clock slopes and tick-event pacing; position/effect calibration; downtime budget; heat "
        "consequences foreshadowed or dropped; engagement roll modifiers stated."
    ),
    "generic": (
        "Generic narrative or unknown system. Skip numerical balance entirely. Audit structurally: "
        "premise clarity; scene-to-scene change; stakes legibility at decision points; resolution "
        "mechanic bite; endgame shape. Flag mechanical concerns qualitatively, not numerically. "
        "Do not invent numbers for a system that doesn't use them."
    ),
}


# =============================================================================
# API wrapper
# =============================================================================


def with_retry(max_attempts: int = 3, base_delay: float = 2.0) -> Callable:
    """Retry a function with exponential backoff on transient API errors.

    Args:
        max_attempts: Maximum number of attempts before giving up.
        base_delay: Initial delay in seconds; doubles after each failure.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error: Exception | None = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (
                    anthropic.APITimeoutError,
                    anthropic.APIConnectionError,
                    anthropic.RateLimitError,
                    anthropic.InternalServerError,
                ) as err:
                    last_error = err
                    if attempt == max_attempts:
                        break
                    delay = base_delay * (2 ** (attempt - 1))
                    print(
                        f"  [retry {attempt}/{max_attempts - 1}] {type(err).__name__}: "
                        f"waiting {delay:.1f}s",
                        file=sys.stderr,
                    )
                    time.sleep(delay)
            raise RuntimeError(f"API call failed after {max_attempts} attempts") from last_error

        return wrapper

    return decorator


@with_retry()
def call_claude(
    client: anthropic.Anthropic,
    model: str,
    system_prompt: str,
    user_prompt: str,
    max_tokens: int,
) -> str:
    """Call Claude and return the assistant's text response.

    Args:
        client: An initialized Anthropic client.
        model: Model identifier.
        system_prompt: System instructions.
        user_prompt: User message content.
        max_tokens: Maximum tokens in the response.

    Returns:
        The first text block of the assistant's response.
    """
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    parts = [block.text for block in response.content if block.type == "text"]
    return "\n".join(parts).strip()


# =============================================================================
# Passes
# =============================================================================


def pass_mechanical_audit(
    client: anthropic.Anthropic,
    config: PlaytestConfig,
    scenario_text: str,
) -> tuple[str, list[Finding]]:
    """Run the system-adapted mechanical audit.

    Returns:
        Tuple of (raw markdown response, parsed list of Findings).
    """
    system_prompt = (
        "You are a senior TTRPG developmental editor with deep experience running and tuning "
        "scenarios at the table. You are NOT reviewing prose. You are doing a mechanical audit "
        "before publication or before a session.\n\n"
        f"System context: {SYSTEM_DESCRIPTIONS[config.system]}\n\n"
        "Output format: a Markdown report with one section per severity (Critical, High, Medium, "
        "Low, Notes). Each finding is a bullet with three required parts:\n"
        "- **{Location}** — {What is mechanically wrong, specific, with numbers or fictional "
        "facts.} **Fix:** {Concrete change. Not 'rebalance' — actual numerical or structural "
        "change.}\n\n"
        "Hard rules:\n"
        "1. Every finding MUST have a specific location (scene name, NPC name, room, encounter).\n"
        "2. Every finding MUST have a concrete fix. 'Adjust the DC' is not a fix. 'Lower DC 18 → 15' is.\n"
        "3. Do not flag prose, word choice, or style — those are not playtest findings.\n"
        "4. Do not invent content the scenario doesn't have.\n"
        "5. If a finding spans multiple severities, pick the highest applicable.\n"
        "6. If you find fewer than 5 findings, audit harder — most scenarios have more.\n"
        "7. If the system is 'generic', flag concerns qualitatively without inventing numbers."
    )

    user_prompt = (
        f"Party: {config.party}\n"
        f"System: {config.system}\n\n"
        "---\n\n"
        f"SCENARIO:\n\n{scenario_text}\n\n"
        "---\n\n"
        "Produce the mechanical audit now."
    )

    raw = call_claude(
        client,
        model=config.model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=MAX_TOKENS_PER_PASS["mechanical"],
    )
    findings = _parse_findings_from_markdown(raw)
    return raw, findings


def pass_simulated_playthrough(
    client: anthropic.Anthropic,
    config: PlaytestConfig,
    scenario_text: str,
) -> str:
    """Produce a simulated playthrough transcript with five personas."""
    personas_block = "\n".join(p.as_prompt_block() for p in PERSONAS)

    system_prompt = (
        "You are simulating a tabletop session for playtest purposes. Five player personas play "
        "the scenario at the table, with a GM running it as written.\n\n"
        "FIVE PERSONAS (each must be distinct in voice and concern):\n\n"
        f"{personas_block}\n\n"
        "Format the transcript scene by scene. For each scene:\n"
        "- '### Scene N — {scene name}'\n"
        "- One-line GM frame.\n"
        "- Short quoted dialogue from 2-4 personas (don't force all five into every scene).\n"
        "- Brief action description as needed.\n\n"
        "INLINE ANNOTATIONS (essential — this is the playtest value):\n"
        "- `[FLAG: ...]` — anything that emerged in play that wouldn't show in a manuscript read: "
        "a persona with nothing to do; single-NPC info bottleneck; converging 'choices'; "
        "trivialized combat; unclear next step; dead-end skill check.\n"
        "- `[BRANCH: ...]` — when the party reaches a decision point, note 2-3 alternative paths "
        "and which have problems. Follow the most likely path in the transcript itself.\n\n"
        "Hard rules:\n"
        "1. Length: 1500-3500 words for a one-shot, scaled for longer scenarios. Don't pad.\n"
        "2. Persona voices must be distinct. If two personas could be swapped, you've failed.\n"
        "3. Do not novelize. This is shorthand transcript, not prose.\n"
        "4. Flag at least 4 issues inline. If you find fewer, look harder at converging choices, "
        "redundant clues, and combat trivializations.\n"
        "5. Do not change the scenario. Run it as written, even when written badly.\n"
        "6. End with a one-paragraph 'Session epilogue' noting outcome and lingering threads."
    )

    user_prompt = (
        f"Party: {config.party}\n"
        f"System: {config.system}\n\n"
        "---\n\n"
        f"SCENARIO:\n\n{scenario_text}\n\n"
        "---\n\n"
        "Simulate the session now."
    )

    return call_claude(
        client,
        model=config.model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=MAX_TOKENS_PER_PASS["playthrough"],
    )


def pass_persona_feedback(
    client: anthropic.Anthropic,
    config: PlaytestConfig,
    scenario_text: str,
    transcript: str,
) -> dict[str, str]:
    """Generate per-persona feedback paragraphs.

    Returns a dict keyed by persona.key with one ~150-word paragraph per persona.
    """
    feedback: dict[str, str] = {}

    for persona in PERSONAS:
        system_prompt = (
            f"You are {persona.name}, {persona.archetype}, giving honest post-session feedback "
            "about a TTRPG scenario you just played. Stay in voice. This is not a review of "
            "the prose — it's a player's reaction to the experience.\n\n"
            f"Your priorities: {persona.priorities}\n"
            f"You watch for: {persona.watching_for}\n"
            f"Voice: {persona.voice}\n\n"
            "Format: ONE paragraph, 120-200 words, in your voice. No bullet points, no headers. "
            "Be specific — reference scenes, NPCs, decisions. Be honest — praise what worked and "
            "name what didn't. Don't be diplomatic past the point of usefulness."
        )

        user_prompt = (
            f"SCENARIO (for reference):\n\n{scenario_text}\n\n"
            "---\n\n"
            f"SESSION TRANSCRIPT (what just happened at the table):\n\n{transcript}\n\n"
            "---\n\n"
            f"Now give your feedback as {persona.name}."
        )

        text = call_claude(
            client,
            model=config.model,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            max_tokens=MAX_TOKENS_PER_PASS["persona"],
        )
        feedback[persona.key] = text

    return feedback


def pass_synthesis(
    client: anthropic.Anthropic,
    config: PlaytestConfig,
    scenario_text: str,
    report: PlaytestReport,
) -> dict[str, str]:
    """Cross-reference findings and produce the synthesis.

    Returns:
        Dict with keys: verdict, coverage_map, top_fixes, what_works,
        cross_patterns, raw.
    """
    findings_block = (
        "\n".join(f.as_markdown() for f in report.mechanical_findings)
        if report.mechanical_findings
        else "(skipped or no findings)"
    )
    feedback_block = (
        "\n\n".join(
            f"### {p.name} ({p.archetype})\n{report.persona_feedback.get(p.key, '(skipped)')}"
            for p in PERSONAS
        )
        if report.persona_feedback
        else "(skipped)"
    )
    transcript_block = report.transcript if report.transcript else "(skipped)"

    system_prompt = (
        "You are synthesizing the output of a multi-pass TTRPG playtest. You have access to:\n"
        "- The mechanical audit findings (pass 1).\n"
        "- The simulated playthrough transcript (pass 2).\n"
        "- The five personas' feedback (pass 3).\n\n"
        "Your job: produce the final synthesis. Required sections IN ORDER:\n\n"
        "## Verdict\n"
        "One of exactly these: 'Ready to run', 'Ready with minor fixes', 'Needs targeted "
        "revision', 'Needs structural revision', 'Not ready'. Then one paragraph of justification.\n\n"
        "## Persona Coverage Map\n"
        "A 5-row Markdown table — Persona | Archetype | Coverage (✅ / ⚠️ / ❌) | Note. A ❌ for "
        "any persona is a structural finding, not a small one.\n\n"
        "## Top 5 Fixes (ranked by impact/effort)\n"
        "Numbered list. Each item: bold title, location, then one paragraph of what to change "
        "and why. Specific and actionable.\n\n"
        "## What Works\n"
        "At least three concrete strengths. Specific scenes, NPCs, mechanics, or structural "
        "choices the playtest validated. A report that finds no strengths is editorially "
        "dishonest.\n\n"
        "## Cross-Pass Patterns\n"
        "Issues that appeared in two or more passes. These are structural, not local. If the "
        "mechanical audit flagged the climax as undertuned AND the transcript showed it "
        "trivialized AND personas mentioned it — that's ONE structural finding, not three.\n\n"
        "Hard rules:\n"
        "1. Be specific — reference scenes, NPCs, locations by name.\n"
        "2. The Top 5 Fixes must be ordered by impact/effort, not severity alone.\n"
        "3. Cross-Pass Patterns must cite the passes in which each pattern appeared.\n"
        "4. Do not invent content. Synthesize what's in the passes; don't add new findings."
    )

    user_prompt = (
        f"System: {config.system}\n"
        f"Party: {config.party}\n"
        f"Mode: {config.mode}\n\n"
        "---\n\n"
        f"SCENARIO (excerpt for reference):\n\n{scenario_text[:8000]}\n\n"
        "---\n\n"
        f"PASS 1 — Mechanical findings:\n\n{findings_block}\n\n"
        "---\n\n"
        f"PASS 2 — Simulated playthrough:\n\n{transcript_block}\n\n"
        "---\n\n"
        f"PASS 3 — Persona feedback:\n\n{feedback_block}\n\n"
        "---\n\n"
        "Produce the synthesis now, with all five required sections in order."
    )

    raw = call_claude(
        client,
        model=config.model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=MAX_TOKENS_PER_PASS["synthesis"],
    )
    return _split_synthesis_sections(raw)


# =============================================================================
# Parsers
# =============================================================================


def _parse_findings_from_markdown(text: str) -> list[Finding]:
    """Extract Finding objects from a Markdown audit response.

    The audit produces sections like '### Critical' / '### High' etc. with bullets.
    This parser is forgiving: missing 'Fix:' becomes empty string; misformatted
    bullets are skipped.
    """
    findings: list[Finding] = []
    current_severity: Severity | None = None

    severity_headers: dict[str, Severity] = {
        "critical": "critical",
        "high": "high",
        "medium": "medium",
        "low": "low",
        "low / notes": "low",
        "notes": "note",
        "note": "note",
    }

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("#"):
            heading = line.lstrip("#").strip().lower()
            heading = heading.replace("*", "").strip()
            for key, sev in severity_headers.items():
                if heading == key or heading.startswith(key + " "):
                    current_severity = sev
                    break
            continue

        if not line.startswith(("-", "*")) or current_severity is None:
            continue

        content = line.lstrip("-*").strip()
        location, description, fix = _split_finding_bullet(content)
        if not location and not description:
            continue
        findings.append(Finding(
            severity=current_severity,
            location=location,
            description=description,
            fix=fix,
        ))

    findings.sort(key=lambda f: (SEVERITY_ORDER[f.severity], f.location))
    return findings


def _split_finding_bullet(text: str) -> tuple[str, str, str]:
    """Split a finding bullet into (location, description, fix).

    Expected shape: '**Location** — description. **Fix:** fix text.'
    Tolerant of variations.
    """
    location = ""
    description = text
    fix = ""

    if text.startswith("**"):
        end = text.find("**", 2)
        if end != -1:
            location = text[2:end].strip()
            description = text[end + 2:].lstrip(" —-:").strip()

    fix_marker_lower = description.lower()
    for marker in ("**fix:**", "**fix :**", "fix:"):
        idx = fix_marker_lower.find(marker)
        if idx != -1:
            fix = description[idx + len(marker):].strip().lstrip("*").strip()
            description = description[:idx].strip().rstrip(".").rstrip()
            break

    return location, description, fix


def _split_synthesis_sections(text: str) -> dict[str, str]:
    """Split the synthesis response into its named sections."""
    sections: dict[str, str] = {
        "verdict": "",
        "coverage_map": "",
        "top_fixes": "",
        "what_works": "",
        "cross_patterns": "",
        "raw": text,
    }
    section_map = {
        "verdict": "verdict",
        "persona coverage map": "coverage_map",
        "coverage map": "coverage_map",
        "top 5 fixes": "top_fixes",
        "top fixes": "top_fixes",
        "what works": "what_works",
        "cross-pass patterns": "cross_patterns",
        "cross pass patterns": "cross_patterns",
    }

    current_key: str | None = None
    buffer: list[str] = []

    def flush() -> None:
        if current_key and buffer:
            sections[current_key] = "\n".join(buffer).strip()

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("## "):
            flush()
            heading = line[3:].strip().lower().replace("(", "").replace(")", "")
            heading = heading.split(" — ")[0].split("ranked")[0].strip()
            current_key = next(
                (key for k, key in section_map.items() if heading.startswith(k)),
                None,
            )
            buffer = []
        else:
            buffer.append(line)
    flush()

    return sections


def parse_scenario(path: Path) -> tuple[str, str]:
    """Read the scenario file and extract a title.

    Args:
        path: Path to the scenario file.

    Returns:
        Tuple of (full text, inferred title). Title falls back to the file stem.
    """
    if not path.exists():
        raise FileNotFoundError(f"Scenario not found: {path}")

    text = path.read_text(encoding="utf-8")
    title = path.stem.replace("-", " ").replace("_", " ").title()

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped.lstrip("#").strip()
            break

    return text, title


# =============================================================================
# Renderer
# =============================================================================


def render_report(report: PlaytestReport) -> str:
    """Render a PlaytestReport as Markdown.

    Args:
        report: The completed report.

    Returns:
        A Markdown string ready to write to disk.
    """
    cfg = report.config
    parts: list[str] = []

    parts.append(f"# Playtest Report — {report.scenario_title}\n")
    parts.append(
        f"**System:** {cfg.system}  \n"
        f"**Party simulated:** {cfg.party}  \n"
        f"**Mode:** {cfg.mode}  \n"
        f"**Date:** {report.generated_at}  \n"
        f"**Model:** {cfg.model}\n"
    )
    parts.append("\n---\n")

    parts.append("\n## Verdict\n")
    parts.append(report.synthesis_verdict or "_(synthesis missing)_\n")

    parts.append("\n## Persona Coverage Map\n")
    parts.append(report.synthesis_coverage_map or "_(synthesis missing)_\n")

    parts.append("\n## Top 5 Fixes\n")
    parts.append(report.synthesis_top_fixes or "_(synthesis missing)_\n")

    parts.append("\n## What Works\n")
    parts.append(report.synthesis_what_works or "_(synthesis missing)_\n")

    if cfg.mode != "narrative":
        parts.append("\n## Mechanical Findings (Pass 1)\n")
        if report.mechanical_findings:
            parts.append(_render_findings_by_severity(report.mechanical_findings))
        else:
            parts.append(report.mechanical_raw or "_(no findings)_\n")

    if cfg.mode != "quick":
        parts.append("\n## Simulated Playthrough (Pass 2)\n")
        parts.append(report.transcript or "_(skipped)_\n")

        parts.append("\n## Per-Persona Feedback (Pass 3)\n")
        for persona in PERSONAS:
            parts.append(f"\n### {persona.name} ({persona.archetype})\n")
            parts.append(report.persona_feedback.get(persona.key, "_(skipped)_") + "\n")

    parts.append("\n## Cross-Pass Patterns\n")
    parts.append(report.synthesis_cross_patterns or "_(synthesis missing)_\n")

    parts.append("\n---\n")
    parts.append("\n## Provenance\n")
    parts.append(
        f"- Source file: `{cfg.scenario_path}`\n"
        f"- System: {cfg.system}\n"
        f"- Party: {cfg.party}\n"
        f"- Mode: {cfg.mode}\n"
        f"- Model: {cfg.model}\n"
        f"- Generated: {report.generated_at}\n"
    )

    return "\n".join(parts)


def _render_findings_by_severity(findings: list[Finding]) -> str:
    """Group findings by severity into Markdown sections."""
    groups: dict[Severity, list[Finding]] = {
        "critical": [],
        "high": [],
        "medium": [],
        "low": [],
        "note": [],
    }
    for f in findings:
        groups[f.severity].append(f)

    labels: dict[Severity, str] = {
        "critical": "Critical",
        "high": "High",
        "medium": "Medium",
        "low": "Low",
        "note": "Notes",
    }

    parts: list[str] = []
    for severity in ("critical", "high", "medium", "low", "note"):
        items = groups[severity]
        if not items:
            continue
        parts.append(f"\n### {labels[severity]}\n")
        for f in items:
            parts.append(f.as_markdown())
    return "\n".join(parts) + "\n"


# =============================================================================
# Orchestrator
# =============================================================================


def run_playtest(config: PlaytestConfig) -> PlaytestReport:
    """Execute the full playtest pipeline.

    Args:
        config: The playtest configuration.

    Returns:
        A completed PlaytestReport.
    """
    scenario_text, scenario_title = parse_scenario(config.scenario_path)
    report = PlaytestReport(scenario_title=scenario_title, config=config)

    client = anthropic.Anthropic()

    if config.mode != "narrative":
        print("→ Pass 1: mechanical audit", file=sys.stderr)
        raw, findings = pass_mechanical_audit(client, config, scenario_text)
        report.mechanical_raw = raw
        report.mechanical_findings = findings
        print(f"  {len(findings)} findings", file=sys.stderr)

    if config.mode != "quick":
        print("→ Pass 2: simulated playthrough", file=sys.stderr)
        report.transcript = pass_simulated_playthrough(client, config, scenario_text)

        print("→ Pass 3: per-persona feedback", file=sys.stderr)
        report.persona_feedback = pass_persona_feedback(
            client, config, scenario_text, report.transcript
        )

    print("→ Pass 4: synthesis", file=sys.stderr)
    synth = pass_synthesis(client, config, scenario_text, report)
    report.synthesis_verdict = synth["verdict"]
    report.synthesis_coverage_map = synth["coverage_map"]
    report.synthesis_top_fixes = synth["top_fixes"]
    report.synthesis_what_works = synth["what_works"]
    report.synthesis_cross_patterns = synth["cross_patterns"]
    report.synthesis_raw = synth["raw"]

    return report


def write_outputs(report: PlaytestReport) -> tuple[Path, Path]:
    """Write the Markdown report and JSON sidecar.

    Args:
        report: The completed report.

    Returns:
        Tuple of (markdown_path, json_path).
    """
    output_dir = report.config.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    slug = report.config.scenario_slug
    md_path = output_dir / f"{slug}-playtest-{timestamp}.md"
    json_path = output_dir / f"{slug}-playtest-{timestamp}.json"

    md_path.write_text(render_report(report), encoding="utf-8")
    json_path.write_text(
        json.dumps(report.to_json_safe(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return md_path, json_path


# =============================================================================
# CLI
# =============================================================================


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run a multi-pass TTRPG playtest using the Anthropic API.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("scenario", type=Path, help="Path to the scenario file (Markdown or text).")
    parser.add_argument(
        "--system",
        choices=["5e2024", "5e2014", "osr", "pbta", "fitd", "generic"],
        default="5e2024",
        help="TTRPG system family (default: 5e2024).",
    )
    parser.add_argument(
        "--mode",
        choices=["full", "quick", "narrative"],
        default="full",
        help="Pipeline mode (default: full).",
    )
    parser.add_argument(
        "--party",
        default=DEFAULT_PARTY,
        help="Party composition (e.g., '4 PCs level 3, fighter+thief+cleric+MU').",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Claude model identifier (default: {DEFAULT_MODEL}).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("./playtest-reports"),
        help="Output directory for reports (default: ./playtest-reports).",
    )
    parser.add_argument(
        "--run",
        action="store_true",
        help="Actually call the API. Without this flag, runs in dry-run mode.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = parse_args(argv)

    config = PlaytestConfig(
        scenario_path=args.scenario.expanduser().resolve(),
        system=args.system,
        mode=args.mode,
        party=args.party,
        model=args.model,
        output_dir=args.output.expanduser().resolve(),
        dry_run=not args.run,
    )

    if not config.scenario_path.exists():
        print(f"Error: scenario file not found: {config.scenario_path}", file=sys.stderr)
        return 2

    if config.dry_run:
        print("DRY RUN — no API calls. Pass --run to execute.\n")
        print(f"  Scenario : {config.scenario_path}")
        print(f"  System   : {config.system}")
        print(f"  Mode     : {config.mode}")
        print(f"  Party    : {config.party}")
        print(f"  Model    : {config.model}")
        print(f"  Output   : {config.output_dir}")
        print()
        print("Passes that would run:")
        if config.mode != "narrative":
            print("  1. Mechanical audit")
        if config.mode != "quick":
            print("  2. Simulated playthrough")
            print("  3. Per-persona feedback (×5)")
        print("  4. Synthesis")
        print()
        print("Output files would be:")
        slug = config.scenario_slug
        print(f"  {config.output_dir}/{slug}-playtest-<timestamp>.md")
        print(f"  {config.output_dir}/{slug}-playtest-<timestamp>.json")
        return 0

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable is not set.", file=sys.stderr)
        return 2

    try:
        report = run_playtest(config)
    except FileNotFoundError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 2
    except RuntimeError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1

    md_path, json_path = write_outputs(report)
    print(f"\n✓ Wrote {md_path}")
    print(f"✓ Wrote {json_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
