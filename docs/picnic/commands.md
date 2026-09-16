# Commands & Config

Everything lives under one command: **`/picnic`**.

```
/picnic                                           # print every setting (anyone)
/picnic config                                    # the same listing, for an operator
/picnic config <feature>                          # one feature's settings (operator)
/picnic config <feature> <setting> <value>        # change one (operator)
/picnic config <feature> <setting> default        # put it back to its default (operator)
/picnic config <feature> reset                    # put the whole feature back (operator)
/picnic stats                                     # picnic statistics (anyone)
/picnic stats player|dimension|species <value>    # one slice of them (anyone)
/picnic stats shiny                               # just the shinies (anyone)
/picnic stats reset                               # clear the aggregates (operator)
/picnic reload                                    # re-read the config file from disk (operator)
/picnic reset                                     # restore every default (operator)
```

`default` works on **every** setting — you never have to look up what the shipped value was.

## `/picnic config` — the settings

Reading them is open to **everyone** through `/picnic`: knowing the shiny-aura multiplier and the
re-roll cooldown you're playing under is part of playing. Changing anything needs **operator** rank.

Every feature has an `enabled` switch, so a server can keep the picnic and drop any part of it.

```
/picnic config shinyaura multiplier 3             # a full table triples shiny odds
/picnic config shinyaura multiplier default       # back to ×2
/picnic config reroll enabled false               # switch the spawn re-roll off entirely
/picnic config reroll spawncap expert 16          # per-tier settings take the tier in the middle
/picnic config reroll protectshiny expert true    # per-rung settings take the rung
/picnic config wash reset                         # every washing setting back to its default
```

Tiers are `basic`, `advanced`, `expert`, `diving`, `hot` and `strange`. Rungs are `basic`, `advanced`
and `expert`; the Diving, Hot and Strange tables count as `expert`.

### Features and their settings

| Feature | Setting | Value | What it does |
|---------|---------|-------|--------------|
| `reroll` | `enabled` | true/false | The [spawn re-roll](spawn-rerolling.md) itself. *Default on.* |
| | `cooldown` | 0–3600 | Seconds between re-rolls, per table **and** per player. *Default 5. 0 disables.* |
| | `spawncap <tier>` | int | Max Pokémon per re-roll for that tier. |
| | `fuelcost <tier>` | int | Bread per re-roll for that tier (7 Basic, 5 Advanced, 3 above). `0` makes it free. |
| | `flyinglift` | 0–64 | How high re-rolled fliers are lifted off the ground (default `12`, `0` grounds them). Never changes *which* Pokémon spawn. |
| | `protectshiny <rung>` | true/false | The re-roll keeps **shiny** wild Pokémon instead of despawning them. *Default off.* |
| | `protectlegendary <rung>` | true/false | Keeps **legendary** wild Pokémon. *Default off.* |
| | `protectmythical <rung>` | true/false | Keeps **mythical** wild Pokémon. *Default off.* |
| | `protectultrabeast <rung>` | true/false | Keeps **Ultra Beast** wild Pokémon. *Default off.* |
| `snackbias` | `enabled` | true/false | A re-roll borrows the spawn influences of a nearby seasoned poke-snack. *Default off.* |
| `tmteach` | `enabled` | true/false | [Party TM teaching](spawn-rerolling.md#party-tm-teaching) on a re-roll. *Default on.* |
| | `chance` | 0..1 | Chance per re-roll. *Default 0.05.* |
| `shinyaura` | `enabled` | true/false | The [Shiny Aura](shiny-aura.md). *Default on.* |
| | `multiplier` | 1–100 | How many times better your shiny odds get at a **full table**. *Default 2 (double).* |
| `deploy` | `enabled` | true/false | Sitting down sends out your party. *Default on.* |
| | `mindistance` | 0–32 | Closest a party member lands, in blocks. *Default 4.* |
| | `maxdistance` | 0–32 | Furthest a party member lands. *Default 7.* Each Pokémon rolls its own distance in the band, and a max below the min is raised to it. |
| `peaceful` | `enabled` | true/false | While someone is seated, hostile mobs **flee** the table. *Default on.* |
| | `radius` | 0–128 | How far that reaches, in blocks. *Default 30.* |
| `wash` | `enabled` | true/false | [Washing](interactions-and-items.md), from the wheel or with a Poke-sponge. *Default on.* |
| | `friendship` | int | Friendship gained from a wash. |
| | `cooldown` | seconds | Wait between washes, **per Pokémon**. *Default 3.* |
| | `requirestable` | true/false | Need a nearby table to wash. Off also shows the option on the wheel everywhere. |
| `play` | `enabled` | true/false | [Playing fetch](interactions-and-items.md), from the wheel or with a thrown Fetchball. *Default on.* |
| | `friendship` | int | Friendship gained from a game. |
| | `breakchance` | 0..1 | Chance a slime ball splatters. A [Fetchball](interactions-and-items.md#fetchball) ignores this. |
| | `cooldown` | seconds | Wait between games, **per Pokémon**. *Default 3.* |
| | `requirestable` | true/false | Need a nearby table to play. Off also shows the option on the wheel everywhere. |
| `battleseeker` | `enabled` | true/false | The [Battle Seeker](interactions-and-items.md#battle-seeker). Off locks its slot and summons nobody; chests stop holding one after the next `/reload`. *Default on.* |
| | `matchlevel` | true/false | Scale summoned trainers to your party's level. |
| | `levelgap` | int | Level offset for summoned trainers. |
| `hazards` | `enabled` | true/false | What a table carries between dimensions — [burning, scorching, flooding and drifting](picnic-tables.md#where-each-table-can-go). Off, every table is plain furniture. *Default on.* |
| `table` | `light` | 0–15 | Light level emitted by the table. Re-place a table to relight it. |
| | `actiondistance` | number | How close a table has to be for the table-gated actions. |

The four `protect…` settings are **opt-in** and granular: turn on only the rarities you want the
re-roll to spare, on only the rungs you want. `peaceful` is **on by default**: sit at a table and
hostile mobs within `radius` blocks lose their target and run away, like a creeper fleeing a cat.

## `/picnic stats`

Available to **everyone**. Shows a summary of picnic activity:

- Total re-rolls, Pokémon spawned / despawned
- **Shinies** found (with ratio), **legendaries / mythicals**
- Snacks consumed, distinct species
- **Most common** and **rarest** species

```
/picnic stats          # show the summary
/picnic stats reset    # (operator) clear the aggregates
```

### Filters

Ask for one slice instead of the lot. Each filter reports its own re-roll count, what came out, and
the shiny rate for that slice alone — and for shinies, the species, level and coordinates of each one.
All of them are open to everyone.

```
/picnic stats player <name>       # everything one trainer's re-rolls produced
/picnic stats dimension <id>      # e.g. minecraft:the_nether
/picnic stats species <name>      # every appearance of one species
/picnic stats shiny               # just the shinies, and where they turned up
```

`species` tab-completes from what the log has actually seen. `player` and `dimension` are free text,
so you can ask about someone who's offline or a dimension that isn't loaded right now.

Statistics persist in `config/cobblemon_picnic_stats.json` (aggregates) and
`config/cobblemon_picnic_events.jsonl` (a granular per-re-roll log). The **summary** reads the
aggregates; the **filters** replay the log, which is the only place the per-re-roll detail survives —
so a filter can look back further than the last `stats reset`.

## The settings screen

With **[Cloth Config](https://modrinth.com/mod/cloth-config)** installed, the same values are editable
in a GUI — on Fabric via **[Mod Menu](https://modrinth.com/mod/modmenu) → Cobblemon Picnic → Settings**,
on NeoForge via the **Config** button in the mods list.

⚠️ On a **server** that screen only edits **your own** game's file, and says so at the top. Use
`/picnic config` to change the settings everyone plays under.

## The config file

```
config/cobblemon_picnic.json          # settings
config/cobblemon_picnic_stats.json    # statistics aggregates
config/cobblemon_picnic_events.jsonl  # granular per-re-roll log
```

Edit the first by hand if you like, then apply it with `/picnic reload` — no restart needed. If the
file can't be read, `/picnic reload` says why and changes nothing, and the mod leaves the file alone
until it is fixed: settings changed in the meantime last until the server stops.

## Defaults

| Tier | Spawn cap | Fuel/re-roll | Radius | Seats |
|------|:---------:|:------------:|:------:|:-----:|
| Basic | 5 | 7 | 32 | 2 |
| Advanced | 8 | 5 | 48 | 3 |
| Expert | 12 | 3 | 64 | 4 |
| Diving | 12 | 3 | 64 | 4 |
| Hot | 12 | 3 | 64 | 4 |
| Strange | 12 | 3 | 64 | 4 |

Seat counts are **fixed per tier** and not configurable. Elsewhere: re-roll cooldown **5 s**
(per-table *and* per-player), party TM cross-teach **5%**, full-table shiny multiplier **×2**, wash
and play cooldowns **3 s** each (per Pokémon), party deploy **4–7 blocks**.

### Picnic without the spawn manipulation

`/picnic config reroll enabled false` switches the re-roll off entirely — right-clicking a table then
spawns and
despawns nothing, and costs no bread. Seats, the [Shiny Aura](shiny-aura.md), baskets, the
[Battle Seeker](interactions-and-items.md#battle-seeker) and the
[care interactions](interactions-and-items.md) all keep working.
