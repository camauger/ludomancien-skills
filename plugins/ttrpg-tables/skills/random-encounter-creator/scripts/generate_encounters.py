#!/usr/bin/env python3
"""
Random Encounter Table Generator
Generates large-scale encounter tables for dark fantasy cities using the Anthropic API.

Usage:
    python generate_encounters.py --size 100 --output encounters.md
    python generate_encounters.py --size 200 --focus "docks, night" --tone "high horror"
    python generate_encounters.py --config config.json

Requirements:
    pip install anthropic
    
Environment:
    ANTHROPIC_API_KEY must be set
"""

import argparse
import json
import os
import random
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)


# =============================================================================
# Configuration
# =============================================================================

@dataclass
class TableConfig:
    """Configuration for encounter table generation."""
    size: int = 100
    output: str = "encounters.md"
    table_name: str = "Urban Encounters"
    batch_size: int = 20
    
    # Distribution targets (percentages)
    tier_distribution: dict = field(default_factory=lambda: {
        "tier1": 60,  # Vignettes
        "tier2": 30,  # Developed
        "tier3": 10   # Mini-scenes
    })
    
    type_distribution: dict = field(default_factory=lambda: {
        "Social": 25,
        "Danger": 15,
        "Mystery": 15,
        "Horror": 15,
        "Environmental": 15,
        "Event": 15
    })
    
    time_distribution: dict = field(default_factory=lambda: {
        "Day": 40,
        "Night": 35,
        "Dawn": 10,
        "Dusk": 15
    })
    
    danger_distribution: dict = field(default_factory=lambda: {
        "None": 40,
        "Low": 30,
        "Medium": 20,
        "High": 10
    })
    
    districts: list = field(default_factory=lambda: [
        "Slums", "Market", "Temple", "Noble", "Docks", "Artisan", "Necropolis"
    ])
    
    # Optional focus/filters
    focus_district: Optional[str] = None
    focus_time: Optional[str] = None
    focus_type: Optional[str] = None
    
    # Tone adjustments
    horror_multiplier: float = 1.0  # 1.5 = 50% more horror
    danger_multiplier: float = 1.0  # 0.5 = 50% less danger
    
    # API settings
    model: str = "claude-sonnet-4-20250514"
    max_retries: int = 3


# =============================================================================
# Variety Tracking
# =============================================================================

class VarietyTracker:
    """Tracks used elements to avoid repetition."""
    
    def __init__(self, window_size: int = 20):
        self.window_size = window_size
        self.recent_npcs: list[str] = []
        self.recent_creatures: list[str] = []
        self.recent_objects: list[str] = []
        self.recent_weather: list[str] = []
        self.recent_concepts: list[str] = []
    
    def add_encounter(self, encounter_text: str):
        """Extract and track elements from an encounter."""
        text_lower = encounter_text.lower()
        
        # Track NPC types
        npc_patterns = [
            "beggar", "merchant", "guard", "noble", "priest", "sailor",
            "thief", "child", "elder", "woman", "man", "servant", "soldier",
            "artisan", "drunk", "prostitute", "cultist", "monk"
        ]
        for npc in npc_patterns:
            if npc in text_lower:
                self._add_to_list(self.recent_npcs, npc)
        
        # Track creatures
        creature_patterns = [
            "rat", "cat", "dog", "crow", "raven", "spider", "snake",
            "horse", "mule", "pig", "chicken", "undead", "ghost"
        ]
        for creature in creature_patterns:
            if creature in text_lower:
                self._add_to_list(self.recent_creatures, creature)
        
        # Track weather/atmosphere
        weather_patterns = [
            "fog", "rain", "thunder", "wind", "cold", "heat", "mist",
            "storm", "lightning", "snow", "ice"
        ]
        for weather in weather_patterns:
            if weather in text_lower:
                self._add_to_list(self.recent_weather, weather)
    
    def _add_to_list(self, lst: list, item: str):
        """Add item to tracking list, maintaining window size."""
        lst.append(item)
        if len(lst) > self.window_size:
            lst.pop(0)
    
    def get_avoidance_prompt(self) -> str:
        """Generate prompt section listing elements to avoid."""
        avoid_parts = []
        
        if self.recent_npcs:
            avoid_parts.append(f"NPCs to avoid (used recently): {', '.join(set(self.recent_npcs[-10:]))}")
        if self.recent_creatures:
            avoid_parts.append(f"Creatures to avoid: {', '.join(set(self.recent_creatures[-5:]))}")
        if self.recent_weather:
            avoid_parts.append(f"Weather to avoid: {', '.join(set(self.recent_weather[-3:]))}")
        
        if avoid_parts:
            return "\n\n**VARIETY CONSTRAINTS** (do not repeat these recently-used elements):\n" + "\n".join(f"- {p}" for p in avoid_parts)
        return ""


# =============================================================================
# Distribution Calculator
# =============================================================================

class DistributionCalculator:
    """Calculates target counts for each category."""
    
    def __init__(self, config: TableConfig):
        self.config = config
        self.size = config.size
    
    def calculate_targets(self) -> dict:
        """Calculate target counts for all categories."""
        targets = {
            "tiers": self._calculate_tiers(),
            "types": self._calculate_types(),
            "times": self._calculate_times(),
            "dangers": self._calculate_dangers()
        }
        return targets
    
    def _calculate_tiers(self) -> dict:
        dist = self.config.tier_distribution
        return {
            "tier1": int(self.size * dist["tier1"] / 100),
            "tier2": int(self.size * dist["tier2"] / 100),
            "tier3": int(self.size * dist["tier3"] / 100)
        }
    
    def _calculate_types(self) -> dict:
        dist = self.config.type_distribution.copy()
        
        # Apply horror multiplier
        if self.config.horror_multiplier != 1.0:
            dist["Horror"] = int(dist["Horror"] * self.config.horror_multiplier)
            # Normalize
            total = sum(dist.values())
            dist = {k: int(v * 100 / total) for k, v in dist.items()}
        
        # Apply focus
        if self.config.focus_type:
            dist[self.config.focus_type] = min(50, dist.get(self.config.focus_type, 15) * 2)
        
        return {k: int(self.size * v / 100) for k, v in dist.items()}
    
    def _calculate_times(self) -> dict:
        dist = self.config.time_distribution.copy()
        
        if self.config.focus_time:
            dist[self.config.focus_time] = 60
            for k in dist:
                if k != self.config.focus_time:
                    dist[k] = 40 // (len(dist) - 1)
        
        return {k: int(self.size * v / 100) for k, v in dist.items()}
    
    def _calculate_dangers(self) -> dict:
        dist = self.config.danger_distribution.copy()
        
        # Apply danger multiplier to Medium and High
        if self.config.danger_multiplier != 1.0:
            dist["Medium"] = int(dist["Medium"] * self.config.danger_multiplier)
            dist["High"] = int(dist["High"] * self.config.danger_multiplier)
            dist["None"] = 100 - dist["Low"] - dist["Medium"] - dist["High"]
        
        return {k: int(self.size * v / 100) for k, v in dist.items()}


# =============================================================================
# Prompt Builder
# =============================================================================

class PromptBuilder:
    """Builds prompts for encounter generation."""
    
    SYSTEM_PROMPT = """You are an expert TTRPG content creator specializing in dark fantasy urban encounters. 
You create evocative, atmospheric encounters for random tables.

CRITICAL RULES:
1. Never use proper nouns or specific names. Use generic references:
   - "the Guard" not "the City Watch of Valdris"
   - "a guard captain" not "Captain Marcus"
   - "the Temple" not "the Temple of Khor"
   - "the Syndicate" not "the Black Hand"

2. Match tier complexity exactly:
   - Tier 1: 1-2 sentences, pure atmosphere, no mechanics
   - Tier 2: 3-5 sentences, potential interaction, minor hook
   - Tier 3: 2-3 paragraphs, flash NPC stats, multiple outcomes

3. Dark fantasy tone: corruption, moral ambiguity, dread, beauty in decay

4. Output ONLY valid JSON array. No markdown, no explanation."""

    def build_batch_prompt(
        self,
        batch_size: int,
        targets: dict,
        tracker: VarietyTracker,
        batch_number: int,
        config: TableConfig
    ) -> str:
        """Build prompt for generating a batch of encounters."""
        
        # Determine what this batch needs
        batch_specs = self._calculate_batch_specs(batch_size, targets, batch_number, config)
        
        prompt = f"""Generate exactly {batch_size} dark fantasy urban encounters.

**BATCH SPECIFICATIONS:**
{self._format_specs(batch_specs)}

**DISTRICTS TO USE:** {', '.join(config.districts)}

**OUTPUT FORMAT:**
Return a JSON array with exactly {batch_size} objects:
```json
[
  {{
    "tier": 1,
    "type": "Environmental",
    "district": "Market",
    "time": "Day",
    "danger": "None",
    "text": "The smell of burnt sugar drifts from a confectioner's stall."
  }},
  ...
]
```

{tracker.get_avoidance_prompt()}

**TIER EXAMPLES:**

Tier 1 (vignette):
{{"tier": 1, "type": "Horror", "district": "Slums", "time": "Night", "danger": "Low", "text": "A child's laughter echoes from an alley that leads to a dead end. There's no child visible."}}

Tier 2 (developed):
{{"tier": 2, "type": "Mystery", "district": "Noble", "time": "Dusk", "danger": "Low", "text": "A servant in House livery approaches, pressing a sealed letter into your hand before vanishing. The seal bears no sigil—just a thumbprint in red wax. The letter contains only: 'The third bell. The fountain. Come alone.'"}}

Tier 3 (mini-scene):
{{"tier": 3, "type": "Danger", "district": "Docks", "time": "Night", "danger": "High", "text": "Three figures block the alley ahead, curved blades glinting. 'Toll for passage,' the leader says. 'Coin or blood.'\\n\\n**The Toll-Takers** (3 thugs): AC 12, HP 11, shortsword +3 (1d6+1). Will accept 5gp total. Fight to half HP then flee. Leader carries a map marking other 'toll points.'\\n\\n**If Paid**: They honor the deal but word spreads you're easy marks. +2 to future robbery encounters this district.\\n**If Fought**: Noise attracts the Guard (50%) or rival gang (50%). Bodies must be hidden or explained."}}

Generate the encounters now. Return ONLY the JSON array."""
        
        return prompt
    
    def _calculate_batch_specs(
        self,
        batch_size: int,
        targets: dict,
        batch_number: int,
        config: TableConfig
    ) -> dict:
        """Calculate specifications for this batch."""
        # Simplified: distribute evenly with some randomization
        specs = {
            "tier1": int(batch_size * 0.6),
            "tier2": int(batch_size * 0.3),
            "tier3": batch_size - int(batch_size * 0.6) - int(batch_size * 0.3),
            "types": {},
            "times": {},
            "dangers": {}
        }
        
        # Distribute types
        type_count = batch_size // len(config.type_distribution)
        for t in config.type_distribution:
            specs["types"][t] = type_count
        
        # Distribute times
        specs["times"] = {
            "Day": int(batch_size * 0.4),
            "Night": int(batch_size * 0.35),
            "Dawn": int(batch_size * 0.1),
            "Dusk": int(batch_size * 0.15)
        }
        
        # Distribute dangers
        specs["dangers"] = {
            "None": int(batch_size * 0.4),
            "Low": int(batch_size * 0.3),
            "Medium": int(batch_size * 0.2),
            "High": int(batch_size * 0.1)
        }
        
        return specs
    
    def _format_specs(self, specs: dict) -> str:
        """Format specifications for prompt."""
        lines = []
        lines.append(f"- Tier 1 (vignettes): ~{specs['tier1']} entries")
        lines.append(f"- Tier 2 (developed): ~{specs['tier2']} entries")
        lines.append(f"- Tier 3 (mini-scenes): ~{specs['tier3']} entries")
        lines.append(f"- Types: mix of {', '.join(specs['types'].keys())}")
        lines.append(f"- Times: {', '.join(f'{k}({v})' for k, v in specs['times'].items())}")
        lines.append(f"- Danger levels: {', '.join(f'{k}({v})' for k, v in specs['dangers'].items())}")
        return "\n".join(lines)


# =============================================================================
# Generator
# =============================================================================

class EncounterGenerator:
    """Main generator class orchestrating the process."""
    
    def __init__(self, config: TableConfig):
        self.config = config
        self.client = anthropic.Anthropic()
        self.tracker = VarietyTracker()
        self.calculator = DistributionCalculator(config)
        self.prompt_builder = PromptBuilder()
        self.encounters: list[dict] = []
    
    def generate(self) -> list[dict]:
        """Generate all encounters."""
        targets = self.calculator.calculate_targets()
        num_batches = (self.config.size + self.config.batch_size - 1) // self.config.batch_size
        
        print(f"Generating {self.config.size} encounters in {num_batches} batches...")
        print(f"Distribution targets: {json.dumps(targets, indent=2)}")
        
        for batch_num in range(num_batches):
            remaining = self.config.size - len(self.encounters)
            batch_size = min(self.config.batch_size, remaining)
            
            if batch_size <= 0:
                break
            
            print(f"\nBatch {batch_num + 1}/{num_batches} ({batch_size} encounters)...")
            
            batch = self._generate_batch(batch_size, targets, batch_num)
            self.encounters.extend(batch)
            
            # Update tracker
            for enc in batch:
                self.tracker.add_encounter(enc.get("text", ""))
            
            print(f"  Generated {len(batch)} encounters. Total: {len(self.encounters)}")
        
        return self.encounters
    
    def _generate_batch(self, batch_size: int, targets: dict, batch_num: int) -> list[dict]:
        """Generate a single batch of encounters."""
        prompt = self.prompt_builder.build_batch_prompt(
            batch_size, targets, self.tracker, batch_num, self.config
        )
        
        for attempt in range(self.config.max_retries):
            try:
                response = self.client.messages.create(
                    model=self.config.model,
                    max_tokens=4096,
                    system=PromptBuilder.SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                content = response.content[0].text
                
                # Extract JSON from response
                encounters = self._parse_response(content)
                
                if encounters and len(encounters) > 0:
                    return encounters
                
                print(f"  Retry {attempt + 1}: No valid encounters parsed")
                
            except Exception as e:
                print(f"  Retry {attempt + 1}: {e}")
        
        print("  WARNING: Batch generation failed after retries")
        return []
    
    def _parse_response(self, content: str) -> list[dict]:
        """Parse JSON encounters from response."""
        # Try direct JSON parse
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            pass
        
        # Try to extract JSON array from markdown code blocks
        json_match = re.search(r'```(?:json)?\s*(\[[\s\S]*?\])\s*```', content)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass
        
        # Try to find raw JSON array
        array_match = re.search(r'\[[\s\S]*\]', content)
        if array_match:
            try:
                return json.loads(array_match.group(0))
            except json.JSONDecodeError:
                pass
        
        return []


# =============================================================================
# Output Formatter
# =============================================================================

class OutputFormatter:
    """Formats encounters into Markdown tables."""
    
    def format_markdown(self, encounters: list[dict], config: TableConfig) -> str:
        """Format encounters as a Markdown table."""
        lines = [
            f"# {config.table_name} - d{len(encounters)}",
            "",
            "| Roll | Type | District | Time | Danger | Encounter |",
            "|------|------|----------|------|--------|-----------|"
        ]
        
        # Shuffle encounters for randomness
        shuffled = encounters.copy()
        random.shuffle(shuffled)
        
        for i, enc in enumerate(shuffled, 1):
            text = enc.get("text", "").replace("\n", "<br>").replace("|", "\\|")
            line = f"| {i} | {enc.get('type', 'Social')} | {enc.get('district', 'Market')} | {enc.get('time', 'Day')} | {enc.get('danger', 'None')} | {text} |"
            lines.append(line)
        
        # Add statistics
        lines.extend([
            "",
            "---",
            "",
            "## Generation Statistics",
            "",
            f"- **Total entries**: {len(encounters)}",
            f"- **Tier distribution**: " + ", ".join(
                f"Tier {t}: {sum(1 for e in encounters if e.get('tier') == t)}"
                for t in [1, 2, 3]
            ),
            f"- **Type distribution**: " + ", ".join(
                f"{t}: {sum(1 for e in encounters if e.get('type') == t)}"
                for t in ["Social", "Danger", "Mystery", "Horror", "Environmental", "Event"]
            )
        ])
        
        return "\n".join(lines)
    
    def format_json(self, encounters: list[dict]) -> str:
        """Format encounters as JSON."""
        return json.dumps(encounters, indent=2, ensure_ascii=False)


# =============================================================================
# CLI
# =============================================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate random encounter tables for dark fantasy cities"
    )
    
    parser.add_argument(
        "--size", "-s",
        type=int,
        default=100,
        help="Number of encounters to generate (default: 100)"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="encounters.md",
        help="Output file path (default: encounters.md)"
    )
    
    parser.add_argument(
        "--name", "-n",
        type=str,
        default="Urban Encounters",
        help="Table name (default: 'Urban Encounters')"
    )
    
    parser.add_argument(
        "--focus",
        type=str,
        help="Focus area (e.g., 'docks, night' or 'horror, slums')"
    )
    
    parser.add_argument(
        "--tone",
        type=str,
        help="Tone adjustments (e.g., 'high horror' or 'low danger')"
    )
    
    parser.add_argument(
        "--batch-size",
        type=int,
        default=20,
        help="Encounters per API call (default: 20)"
    )
    
    parser.add_argument(
        "--model",
        type=str,
        default="claude-sonnet-4-20250514",
        help="Claude model to use"
    )
    
    parser.add_argument(
        "--config",
        type=str,
        help="JSON config file (overrides other options)"
    )
    
    parser.add_argument(
        "--json",
        action="store_true",
        help="Also output raw JSON"
    )
    
    return parser.parse_args()


def main():
    args = parse_args()
    
    # Check API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
    
    # Build config
    if args.config:
        with open(args.config) as f:
            config_dict = json.load(f)
        config = TableConfig(**config_dict)
    else:
        config = TableConfig(
            size=args.size,
            output=args.output,
            table_name=args.name,
            batch_size=args.batch_size,
            model=args.model
        )
        
        # Parse focus
        if args.focus:
            focus_lower = args.focus.lower()
            for district in config.districts:
                if district.lower() in focus_lower:
                    config.focus_district = district
            for time in ["day", "night", "dawn", "dusk"]:
                if time in focus_lower:
                    config.focus_time = time.capitalize()
            for typ in config.type_distribution:
                if typ.lower() in focus_lower:
                    config.focus_type = typ
        
        # Parse tone
        if args.tone:
            tone_lower = args.tone.lower()
            if "high horror" in tone_lower:
                config.horror_multiplier = 1.5
            elif "low horror" in tone_lower:
                config.horror_multiplier = 0.5
            if "high danger" in tone_lower:
                config.danger_multiplier = 1.5
            elif "low danger" in tone_lower:
                config.danger_multiplier = 0.5
    
    # Generate
    generator = EncounterGenerator(config)
    encounters = generator.generate()
    
    if not encounters:
        print("Error: No encounters generated")
        sys.exit(1)
    
    # Format and save
    formatter = OutputFormatter()
    
    markdown = formatter.format_markdown(encounters, config)
    output_path = Path(config.output)
    output_path.write_text(markdown, encoding="utf-8")
    print(f"\nMarkdown saved to: {output_path}")
    
    if args.json:
        json_path = output_path.with_suffix(".json")
        json_path.write_text(formatter.format_json(encounters), encoding="utf-8")
        print(f"JSON saved to: {json_path}")
    
    print(f"\nGeneration complete! {len(encounters)} encounters created.")


if __name__ == "__main__":
    main()
