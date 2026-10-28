# Moves & Effects

Every one of the moves Cobblemon knows has a real-time definition derived from the games' data, and
a datapack can change any of it. `/cac move <move>` shows one move's numbers.

## How a move goes off

| Kind | Examples | What it does |
| --- | --- | --- |
| Close range | Tackle, Close Combat | its key readies it for 3 s; a left click on an opponent in reach lands it when its windup ends |
| Projectile | Thunderbolt, Ember | flies from your Pokémon where you look; it can be outrun or sidestepped |
| Zone | Thunder, Blizzard | falls on the spot you aim at a moment later, a ring marking where |
| Area | Earthquake, Surf | hits everything around you |
| Self and status | Swords Dance, Thunder Wave | cast for a moment first; a flinch or a heavy hit breaks the cast |

A readied close-range move is outlined on the HUD. Its Stamina and cooldown are paid on the click, a
click with nothing in reach keeps it readied, and its key again lets it go.

Faster moves start sooner, so Quick Attack comes out well ahead of Tackle. A move that can miss in
the games sometimes **fumbles** instead: the animation plays and nothing happens. Stamina cost and
cooldown grow with a move's power, so a stronger move is a bigger hit per press, and a short
recovery follows every move.

## Damage

Damage follows the main series formula: level, power, Attack against Defense, the 85–100 % roll,
STAB, the type chart, critical hits and stat stages, scaled so an even level-50 duel lasts about 35
seconds per Pokémon. It comes off the Pokémon's real HP.

## Secondary effects and status

- **Stat stages** up to ±6, cleared when the Pokémon is recalled; **drain**, **recoil**,
  **multi-hit** (2-5 at the games' odds), **healing**, **recharge** (Hyper Beam stuns for 2 s) and
  **two-turn moves** (out of reach while flying or digging).
- **Burn, poison and paralysis** as Cobblemon's own status: burn and poison chip HP every 3 s, burn
  halves physical damage and drains Stamina, paralysis halves the pace and fails 25 % of moves.
- **Sleep and freeze** hold the Pokémon still for about 5 and 6 seconds, and each press of a move key
  shakes some of it off; **confusion** makes a third of its moves hit itself; a **flinch** breaks a
  cast.
- **Weather, terrain, screens and hazards**, inside the fight only: rain and sun scale Water and
  Fire, sandstorm chips, a terrain boosts its type, Reflect and Light Screen halve damage, and Stealth
  Rock, Spikes, Toxic Spikes and Sticky Web hit every Pokémon sent out after them. Side conditions
  like Tailwind and Safeguard show their timer but do nothing yet.
- About 250 moves run special logic of their own in the games; in a real-time fight they do their
  base damage and whatever effects their data lists.

## Abilities and held items

Damage abilities and items work as in the games (Huge Power, Adaptability, Technician, Sheer Force,
Choice Band and Specs, Life Orb, Expert Belt, type-boosting items and plates), and so do contact and
on-hit triggers (Static, Flame Body, Rough Skin, Rocky Helmet, Intimidate, Focus Sash, Sitrus Berry,
Weakness Policy) and field ones (Drizzle, Drought, Sand Stream, Snow Warning, Swift Swim, Chlorophyll,
Levitate, Leftovers, Black Sludge). Every other held item's tooltip says it is inactive in a
real-time fight; it still works in turn-based battles.

## Under water

A land Pokémon has 10 seconds of air under water, then loses 5 % of its HP each second until it comes
up. Water types and water-breathers never run out, and Fire types are hurt by water.

## Battle gimmicks

With **Cobblemon: Mega Showdown**, **Q** uses the one battle gimmick each Trainer gets per fight. It
picks by what the Pokémon holds and the key item you wear:

| Gimmick | Needs | What it does |
| --- | --- | --- |
| **Z-Move** | a Z-Crystal, a Z-Ring | arms the next move of the crystal's type as its Z-Move, once |
| **Mega Evolution** | its Mega Stone, a Mega Bracelet | Mega stats and ability; nothing hits it while it changes |
| **Terastallization** | a Tera Orb | defends as its Tera type, keeps STAB on its own types, ×2 STAB on a Tera type it had |
| **Dynamax** | a Dynamax Band | 20 s bigger, taking half damage, its moves Max Moves with their weather, terrain or stat change; Gigantamax Factor shows the G-Max form |

Every form and size goes back when the fight ends; a Dynamax ends early if the Pokémon is recalled.
Without Mega Showdown, Q does nothing. G-Max-specific moves are not in: a Gigantamax Pokémon uses
Max Moves.

## Block damage

Moves break the blocks where they land: a projectile where it stops, a zone move where it falls, an
area move around its user (never the ground under it).

| Block | Breaks with |
| --- | --- |
| Fragile (leaves, flowers, glass, ice, snow, grass, cobwebs) | any damaging move: Ember burns through leaves |
| Soft (dirt, sand, gravel, wool) | a move of power 60 or more |
| Stone, wood, ores | a move of power 100 or more |
| Anything harder, anything with a block entity (chests, furnaces) | never |

At most 12 blocks per hit, within 2 blocks of the impact, and they drop as a creeper's do.
**Nothing breaks** with the `mobGriefing` game rule off, with the feature switched off, or inside an
**arena**: `/cac arena add <name> <from> <to>` marks a box where nothing gives. Pack authors can add
blocks to the `#cobblemon_action_combat:fragile` and `#cobblemon_action_combat:unbreakable` tags.
