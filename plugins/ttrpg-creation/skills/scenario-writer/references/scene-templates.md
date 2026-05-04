# Scene Templates

Complete micro-structures for different scene types. Each template ensures consistent, GM-friendly formatting.

## Universal Scene Structure

Every scene includes these elements:

```markdown
## Scene [N]: [Evocative Title]

> *[Read-aloud: 3-5 lines, sensory details, present tense, no mechanics]*

**Stakes**: [One sentence: why are the PCs here, what do they need]

**NPCs Present**: [Name (attitude)] — [Name (attitude)]

**Events**: [What can happen in this scene]

**Clues Available**:
- [Clue 1]: [How to obtain] (DC [X] [Skill] or [alternative])
- [Clue 2]: [How to obtain]
- [Clue 3]: [How to obtain]

**Rewards**: [What PCs gain here]
```

## Scene Type Templates

### Investigation Scene

```markdown
## Scene 2: The Ransacked Study

> *Books lie scattered like fallen soldiers across the oak floor. A desk 
> drawer hangs open, emptied. The smell of old paper mixes with something 
> metallic—blood, perhaps, or ink from a shattered bottle. Moonlight 
> streams through a window left carelessly ajar.*

**Stakes**: Discover what the victim was researching and who attacked them.

**NPCs Present**: None (but the housekeeper, Marta, can be summoned)

**Events**:
- Initial search reveals obvious chaos
- Closer inspection finds hidden compartment (DC 15 Investigation)
- Magical detection reveals lingering abjuration aura
- If PCs take too long (30+ min), city watch arrives

**Clues Available**:
- **The victim's journal** (final entry): Found in hidden compartment (DC 15 Investigation), or Marta knows about it (DC 12 Persuasion), or *detect magic* reveals the hiding spot
- **Cult symbol** scratched into desk: DC 12 Perception to notice, DC 14 Religion to identify as Orcus worship
- **Appointment ledger**: Shows meeting scheduled with "V." at the Drowned Rat tavern

**Skill Checks**:
| Check | DC | Success | Failure |
|-------|-----|---------|---------|
| Investigation (room) | 12 | Find journal location clue | Miss hidden compartment |
| Perception (desk) | 12 | Notice cult symbol | Symbol found later by watch |
| Arcana (aura) | 14 | Identify protection spell | Know magic was used, not type |

> **🎭 Ambiance**  
> Describe this scene in whispers. Let silences linger. If players 
> rush, have a floorboard creak ominously—it's just the old house, 
> but they don't know that.

**Rewards**: Information leading to Scene 3 (Tavern) or Scene 4 (Temple)
```

### Combat Scene

```markdown
## Scene 5: Ambush at the Bridge

> *The stone bridge arches over black water, its torches guttering in 
> the river wind. Halfway across, shadows detach from the pillars—four 
> figures in dark leather, blades already drawn. Behind you, two more 
> emerge from the fog.*

**Stakes**: Survive the ambush; capture or interrogate at least one attacker.

**NPCs Present**: 
- 4 Cult Assassins (hostile, professional)
- 2 Cult Thugs (hostile, nervous)

**Events**:
- Assassins attack from front, thugs block retreat
- Round 3: Reinforcement horn if not silenced (DC 14 Stealth to approach silently before combat)
- If losing, leader attempts to flee with message
- Captured cultist can reveal safehouse location

**Tactical Setup**:
```
[FOG] [THUG] [THUG] [FOG]
         ↑
    [PC START]
         ↓
[PILLAR] [ASSASSIN×2] [PILLAR]
    [BRIDGE - 60ft long, 15ft wide]
[PILLAR] [ASSASSIN×2] [PILLAR]
         ↓
      [RIVER]
```

**Enemy Tactics**:
- Assassins: Focus fire on spellcasters, use pillars for cover
- Thugs: Grapple and shove toward river (DC 12 Athletics to resist, 20ft fall + 2d6 damage + swimming)
- All: Flee at 2 deaths, fight to death if cornered

> **⚔️ Tactics**  
> The assassins are professionals—they'll focus the biggest threat 
> first. The thugs are muscle, not fighters; they'll surrender if 
> isolated. If a PC falls in the river, describe the cold shock and 
> strong current (DC 12 Athletics each round to swim to shore).

**Clues Available**:
- **Cult orders** on leader's body: Names the safehouse
- **Matching tattoos**: DC 12 Medicine to identify ritual scarification (connects to Scene 6)
- **Captured cultist interrogation**: DC 14 Intimidation or DC 16 Persuasion reveals patrol schedules

**Rewards**: 
- XP: 450 per assassin, 100 per thug
- Loot: 15 gp each, leader has *potion of healing* and coded message
```

### Social Scene

```markdown
## Scene 3: The Fence's Proposition

> *Silken Tam's parlor smells of incense and old money. Velvet drapes 
> muffle the street noise. The fence herself reclines on a chaise, 
> rings glittering as she gestures you toward seats that are 
> deliberately lower than hers.*

**Stakes**: Convince Tam to reveal who bought the stolen artifact.

**NPCs Present**:
- Silken Tam (cautious, amused, greedy)
- Two bodyguards (alert, silent)

**Events**:
- Tam tests the PCs with small talk, gauging their worth
- She knows who bought the artifact but won't share for free
- Multiple approaches can work (see below)
- If threatened, bodyguards intervene; Tam has panic button to city watch

**Social Approaches**:

| Approach | Method | DC | Outcome |
|----------|--------|-----|---------|
| Bribery | 50+ gp | Auto | Full information |
| Persuasion | Appeal to self-interest | 16 | Information for a favor |
| Deception | Pose as fellow criminals | 14 | Partial info, suspicion |
| Intimidation | Threaten exposure | 18 | Info, but makes enemy |
| Trade | Offer valuable information | — | Depends on value |

**Tam's Responses**:
- **Friendly (bribed/persuaded)**: Names buyer, gives location, offers future work
- **Neutral (deceived)**: Names buyer only, watches PCs afterward
- **Hostile (intimidated)**: Full info, but tips off buyer, sends assassins later
- **Refused**: Calls guards, PCs must find info elsewhere (extends timeline by 1 day)

> **🎭 Ambiance**  
> Play Tam as someone who's heard every threat and seen every 
> angle. She's unflappable but not cruel—she respects competence. 
> Let her finish her wine before answering important questions.

**Clues Available**:
- **Buyer's identity**: The methods above
- **Buyer's motivation**: DC 18 Insight during conversation (Tam knows more than she's saying)
- **Tam's network**: If PCs impress her, she offers ongoing information for 10 gp/month

**Rewards**: Information leading to Scene 6 (Buyer's Manor) or Scene 7 (Warehouse)
```

### Information Gathering Scene (Noir Style)

For investigation-heavy scenarios where information is currency:

```markdown
## Scene 5: The Iron Rose Tavern

> *The Iron Rose sits at the border between districts—not quite anywhere. 
> Deliberately so. Inside, the air tastes of ale and secrets. Sturdy 
> tables, simple chairs, clean floors. No decoration. No music. Just 
> people talking in low voices. Information brokers gather in corners, 
> their conversations a dance of half-truths. You recognize faces: a 
> Watch captain, a known revolutionary, a merchant prince playing cards 
> with someone who's definitely a crime boss. They're all here. They all 
> know each other. And not one of them will touch the others.*

**Stakes**: Gather information about recent disappearances, Church movements, 
and rumors about the "whispered confession."

**NPCs Present**:
- Garrick Vale (proprietor, maintains neutrality absolutely)
- Various information brokers (background, can be approached)
- Verity "Coins" Thrace (if PCs seek her specifically)

**Events**:
- PCs can approach various information brokers
- Garrick enforces no-violence rule absolutely
- Information costs money, favors, or other information
- If PCs cause trouble, Garrick ejects them (see consequences)

**Clues Available** (three methods each):
- **Recent disappearances**: Several people have vanished, all connected to 
  Church (DC 12 Persuasion with 5 gp, or DC 14 Insight to read broker's tells, 
  or trade information about the missing woman)
- **Church movements**: Unusual activity in Cathedral District, Bishop acting 
  strangely (DC 14 Persuasion with 10 gp, or DC 16 Investigation of public 
  records, or DC 12 Deception posing as Church official)
- **"Whispered confession" rumor**: Powerful people are nervous, someone knows 
  something dangerous (DC 12 Persuasion with 3 gp, or DC 15 Insight during 
  conversation, or overhear if PCs wait and listen)

**Skill Checks**:

| Check | DC | Success | Failure |
|-------|-----|---------|---------|
| Persuasion (disappearances) | 12 | Learn about vanishings | Broker wants more money |
| Insight (broker) | 14 | Read tells, get info cheaper | Broker's price increases |
| Persuasion (Church) | 14 | Learn about Church movements | Broker is cautious |
| Deception (official) | 12 | Pose as official, get info | Identity questioned |
| Perception (overhear) | 10 | Overhear relevant talk | Conversations too hushed |

> **🎭 Ambiance**
>
> The Iron Rose is neutral ground—use that. Let players feel the weight 
> of the rules. Everyone here has something to hide, but violence is 
> absolutely forbidden. Information is currency. Every question costs 
> something. Make them choose what they're willing to pay.

**Rewards**: Information about disappearances, Church movements, and the 
conspiracy rumors. Potential contact with information broker for future use.
```

### Exploration Scene

```markdown
## Scene 4: The Flooded Crypts

> *Water laps at the worn steps descending into darkness. The smell 
> of stagnant water and old stone rises to meet you. Somewhere below, 
> something splashes—too large to be a rat.*

**Stakes**: Navigate the crypts to reach the hidden shrine; recover the relic before the water rises further.

**NPCs Present**: None (but creatures lurk)

**Events**:
- Water level rises 1 foot per hour (currently 2ft deep)
- Three chambers to navigate, each with obstacles
- Final chamber holds shrine and guardian

**Environmental Hazards**:
| Hazard | Effect | Mitigation |
|--------|--------|------------|
| Deep water (4ft+) | Difficult terrain, Small creatures must swim | Find alternate routes |
| Unstable ceiling | DC 12 Dex save or 2d6 bludgeoning | Move carefully, detect with Investigation |
| Poisonous gas pocket | DC 14 Con save or poisoned 1 hour | Detect with smell (DC 12 Perception), disperse with wind magic |

**Chamber Breakdown**:

**Chamber 1 - The Antechamber**:
- 2ft water, broken sarcophagi
- Hidden passage behind false wall (DC 14 Investigation)
- 2 **Giant Rats** (aggressive if disturbed)

**Chamber 2 - The Flooded Hall**:
- 4ft water, submerged pillars
- Main path blocked by collapse
- Underwater tunnel (DC 12 Athletics, 30ft, Con check for breath)
- Contains waterlogged corpse with *ring of swimming*

**Chamber 3 - The Shrine**:
- 3ft water, raised dais (dry)
- Relic on altar, protected by glyph (DC 15 to detect, DC 14 to disarm)
- **Water Weird** guardian attacks if glyph triggered

> **🎭 Ambiance**  
> Echo every sound. Dripping water, distant splashes, the PCs' own 
> breathing. Describe the cold seeping through armor. This place 
> has been forgotten for centuries—until now.

**Clues Available**:
- **Waterlogged journal**: In Chamber 2 corpse, describes original burial (DC 12 History to decipher)
- **Wall carvings**: Tell story of what's buried here (connects to main plot)
- **The relic itself**: Confirms antagonist's plan when examined with *identify*

**Rewards**:
- The relic (plot item)
- *Ring of swimming* (if found)
- 150 gp in ancient coins scattered through crypts
```

## Read-Aloud Guidelines

**Do:**
- Use present tense
- Engage multiple senses (sight, sound, smell, touch)
- Create atmosphere, not inventory
- Keep to 3-5 lines maximum
- End with something that invites action

**Don't:**
- Include mechanical information (DCs, distances)
- Describe things PCs wouldn't immediately notice
- Tell PCs how they feel
- Overwrite—leave room for questions

**Sensory Checklist:**
- What do they SEE first? (lighting, movement, scale)
- What do they HEAR? (ambient, sudden, absent)
- What do they SMELL? (pleasant, warning, memory)
- What do they FEEL? (temperature, texture, instinct)
