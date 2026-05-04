# Stat Block Templates

D&D 5e stat block frameworks at different complexity levels. Choose tier based on NPC's importance and expected interaction type.

## Tier 1: Background NPC (No Combat Expected)

**Use for:** Shopkeepers, servants, random citizens, one-scene characters

**Include:**
- Name and creature type
- Brief ability scores (just modifiers, not full scores)
- 1-2 relevant skills
- Key trait or two
- No combat abilities needed

**Example:**

```
# Mira the Baker
*Medium humanoid (human), neutral good*

**Skills** Insight +3, Persuasion +4
**Languages** Common, Dwarvish

### Traits
**Local Gossip.** Mira has advantage on Intelligence checks to recall 
information about local events and residents.

**Generous Spirit.** Mira tends to give regulars extra pastries and 
has developed loyal customer base.
```

---

## Tier 2: Significant NPC (Social Focus, Possible Combat)

**Use for:** Quest givers, allies, recurring characters, social encounters

**Include:**
- Full stat block header (AC, HP, Speed)
- Ability scores
- Relevant saving throws and skills
- 2-3 traits that support their role
- 1-2 social abilities
- Basic combat actions if needed
- Proficiency bonus

**Example:**

```
# Magistrate Vorn
*Medium humanoid (human), lawful neutral*

**Armor Class** 12 (fine clothing)
**Hit Points** 27 (6d8)
**Speed** 30 ft.

| STR | DEX | CON | INT | WIS | CHA |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 10 (+0) | 12 (+1) | 10 (+0) | 16 (+3) | 14 (+2) | 15 (+2) |

**Saving Throws** Int +5, Wis +4
**Skills** Insight +6, Intimidation +4, Persuasion +6, History +5
**Senses** Passive Perception 12
**Languages** Common, Elvish, Draconic
**Challenge** 1 (200 XP) - Proficiency Bonus +2

### Traits
**Legal Authority.** Magistrate Vorn can issue arrest warrants and has 
advantage on Charisma checks when dealing with city officials.

**Burden of Guilt.** Vorn takes bribes but suffers for it. He has 
disadvantage on Wisdom saves against effects that exploit guilt or shame.

### Actions
**Rapier.** Melee Weapon Attack: +3 to hit, reach 5 ft., one target.
Hit: 5 (1d8 + 1) piercing damage.

**Call for Guards.** Vorn summons 1d4 guards who arrive in 1d4 rounds.
```

---

## Tier 3: Major NPC (Full Combat Capable)

**Use for:** Bosses, major allies/enemies, complex recurring characters

**Include:**
- Complete stat block with all defenses
- Full ability array
- Condition immunities/resistances where appropriate
- 3-5 traits that define their capabilities
- Multiple action options
- Bonus actions
- Reactions
- Legendary actions if appropriate (CR 5+)
- Equipment list

**Example Structure:**

```
# [Name]
*[Size] [type], [alignment]*

**Armor Class** [number] ([armor type/explanation])
**Hit Points** [number] ([hit dice calculation])
**Speed** [speed]

| STR | DEX | CON | INT | WIS | CHA |
|:---:|:---:|:---:|:---:|:---:|:---:|
| X (+X) | X (+X) | X (+X) | X (+X) | X (+X) | X (+X) |

**Saving Throws** [list with bonuses]
**Skills** [list with bonuses]
**Damage Resistances** [if any]
**Damage Immunities** [if any]
**Condition Immunities** [if any]
**Senses** [vision types], Passive Perception [number]
**Languages** [list]
**Challenge** [number] ([XP]) - Proficiency Bonus +[number]

### Traits
[3-5 defining mechanical traits]

### Actions
**Multiattack.** [if appropriate]
[2-4 combat actions]

### Bonus Actions
[1-2 bonus actions if appropriate]

### Reactions
[1-2 reactions if appropriate]

### Legendary Actions (if CR 5+)
[Name] can take 3 legendary actions, choosing from below...
[2-3 legendary action options]

### Equipment
[Relevant gear, magic items]
```

---

## Spellcasting NPCs

### Divine Casters (Clerics, Paladins)

**Spellcasting Trait Format:**

```
**Spellcasting.** [Name] is a [level]th-level cleric. Their spellcasting 
ability is Wisdom (spell save DC [number], +[number] to hit with spell attacks). 
They have the following cleric spells prepared:

- Cantrips (at will): [list]
- 1st level ([slots] slots): [list]
- 2nd level ([slots] slots): [list]
[etc.]
```

**Choosing Spells:**
- Match spells to character concept and role
- Include utility spells for non-combat scenes
- Healing for support NPCs
- Offensive spells for combat threats
- Thematic spells (death domain for necromancer, trickery for spy)

### Arcane Casters (Wizards, Sorcerers, Warlocks)

Same format but note:
- Wizards use Intelligence
- Sorcerers/Warlocks use Charisma
- Warlocks have limited spell slots but regain on short rest
- Consider including signature spells that define the character

---

## Challenge Rating Guidelines

**CR 0-1/4:** Commoners, basic guards, servants
- HP: 1-10
- Attack bonus: +2 to +4
- Damage: 1d6+modifier
- AC: 10-13

**CR 1/2-2:** Skilled professionals, minor threats
- HP: 11-50
- Attack bonus: +3 to +5
- Damage: 1d8-2d6+modifier
- AC: 12-15
- 1-2 special abilities

**CR 3-5:** Veteran warriors, mid-level casters, significant threats
- HP: 51-100
- Attack bonus: +4 to +7
- Damage: 2d8-3d8+modifier
- AC: 13-17
- 2-3 special abilities
- Possibly multiattack

**CR 6-10:** Elite warriors, high-level casters, boss-tier enemies
- HP: 100-200
- Attack bonus: +6 to +9
- Damage: 3d8-4d10+modifier
- AC: 15-19
- 3-5 special abilities
- Multiattack likely
- Legendary actions possible

**CR 11+:** Epic threats, major campaign villains
- HP: 200+
- Attack bonus: +8 to +13
- Damage: 4d10+modifier or higher
- AC: 17-22
- 4-6 special abilities
- Multiattack standard
- Legendary actions recommended
- Lair actions if appropriate

---

## Special Ability Design

### Combat Abilities

**Offensive:**
- Extra damage on specific conditions
- Area effects
- Debuffs/conditions
- Multi-target abilities

**Defensive:**
- Damage resistance/immunity
- Regeneration
- Counter-attacks
- Escape mechanisms

**Utility:**
- Mobility enhancements
- Battlefield control
- Support for allies
- Information gathering

### Social Abilities

**Insight-Based:**
```
**Read Intentions.** [Name] has advantage on Wisdom (Insight) checks 
to determine if someone is lying or hiding something.
```

**Persuasion-Based:**
```
**Silver Tongue.** Once per day, [Name] can automatically succeed on 
a Charisma (Persuasion) check of DC 20 or lower.
```

**Intimidation-Based:**
```
**Terrifying Presence.** Creatures within 30 feet that can see [Name] 
must succeed on DC X Wisdom save or be frightened for 1 minute.
```

### Thematic Abilities

Match abilities to character concept:

**Courtesan Example:**
```
**Alluring Presence.** Creatures of [Name]'s choice within 10 feet have 
disadvantage on Wisdom (Perception) checks to notice anything other than 
[Name].
```

**Corrupt Official Example:**
```
**Web of Influence.** [Name] can make a DC 15 Charisma check to call 
in a favor from a city official, gaining information or minor assistance.
```

**Veteran Soldier Example:**
```
**Battle Commands.** As bonus action, [Name] can grant an ally within 
60 feet advantage on their next attack roll.
```

---

## Balancing Guidelines

**Offensive CR = (Average Damage per Round × 3) ÷ 2**
- Round 1: Strongest attack
- Round 2: Typical attack
- Round 3: Weakest attack
- Average these, multiply by 3, divide by 2

**Defensive CR = Hit Points ÷ Expected Damage per Level**
- Adjust for AC (higher AC = effectively more HP)
- Adjust for resistances/immunities

**Final CR = (Offensive CR + Defensive CR) ÷ 2**

Adjust up for:
- Multiple powerful abilities
- Legendary actions
- Regeneration
- Crowd control

Adjust down for:
- Glass cannon (high damage, low HP)
- Limited uses per day
- Requires setup rounds

---

## Quick Reference: NPC Tier Selection

**Just name-dropped once?** → Tier 1 (or just description)
**Appears 2-3 times, social role?** → Tier 2
**Central to quest/arc, combat likely?** → Tier 3
**Campaign-level importance?** → Tier 3 + Legendary Actions

**Time-saving tip:** Start with Tier 2 for most NPCs. Add Tier 3 details only when combat becomes likely. You can always upgrade an NPC between sessions.
