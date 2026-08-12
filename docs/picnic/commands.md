# Commands & Config

Everything lives under one command: **`/picnic`**.

```
/picnic                             # print every setting (anyone)
/picnic <attribute> <value>         # change one setting (operator)
/picnic <attribute> default         # put that one setting back to its default (operator)
/picnic stats                       # picnic statistics (anyone)
/picnic stats player|dimension|species <value>   # one slice of them (anyone)
/picnic stats shiny                 # just the shinies (anyone)
/picnic stats reset                 # clear the aggregates (operator)
/picnic reload                      # re-read the config file from disk (operator)
/picnic reset                       # restore every default (operator)
```

`default` works on **every** attribute — you never have to look up what the shipped value was.

## `/picnic` — the settings

Open to **everyone**: knowing the shiny-aura multiplier and the re-roll cooldown you're playing under
is part of playing. Changing anything needs **operator** rank.

```
/picnic auramultiplier 3          # a full table triples shiny odds
/picnic auramultiplier default    # back to ×2
/picnic reroll false              # switch the spawn re-roll off entirely
/picnic spawncap glamping 16      # per-tier settings take the tier in the middle
/picnic spawncap glamping default
```

### Attributes

| Attribute | Value | What it does |
|-----------|-------|--------------|
| `reroll` | true/false | Master switch for the [spawn re-roll](spawn-rerolling.md) itself. *Default on.* |
| `spawncap <tier>` | int | Max Pokémon per re-roll for that tier. |
| `fuelcost <tier>` | int | Bread consumed per re-roll for that tier (7 for Basic, 5 for Camping, 3 above). |
| `rerollcooldown` | 0–3600 | Seconds between re-rolls (per-table **and** per-player). *Default 5. 0 disables.* |
| `tmteachchance` | 0..1 | Chance per re-roll a party Pokémon teaches another a legal move. *Default 0.05. 0 disables.* |
| `shinyaura` | true/false | Master switch for the [Shiny Aura](shiny-aura.md). |
| `auramultiplier` | 1–100 | How many times better your shiny odds get at a **full table**. *Default 2 (double).* |
| `light` | 0–15 | Light level emitted by the table. |
| `deployonsit` | true/false | Whether sitting deploys your party. |
| `deploydistance <min> <max>` | two numbers | How far out party members land when you sit (default `4 7`). Each Pokémon rolls its own distance in the band. |
| `actiondistance` | number | Interaction range for picnic actions. |
| `washfriendship` | int | Friendship gained from [washing](interactions-and-items.md). |
| `washrequirestable` | true/false | Require a nearby table to wash. Off also shows the option on the wheel everywhere. |
| `washcooldown` | seconds | Wait between washes, **per Pokémon** (default `3`). |
| `slimeballfriendship` | int | Friendship gained from [playing](interactions-and-items.md). |
| `slimeballbreakchance` | 0..1 | Chance the slime ball breaks when playing. A [Fetchball](interactions-and-items.md#fetchball) ignores this. |
| `slimeballrequirestable` | true/false | Require a nearby table to play. Off also shows the option on the wheel everywhere. |
| `playcooldown` | seconds | Wait between plays, **per Pokémon** (default `3`). |
| `flyingspawnlift` | blocks | How high re-rolled fliers are lifted off the ground (default `12`, `0` grounds them). Never changes *which* Pokémon spawn. |
| `spawnappropriatelvltrainer` | true/false | Scale [Battle Seeker](interactions-and-items.md#battle-seeker) trainers to your level. |
| `trainerlevelgap` | int | Level offset for summoned trainers. |
| `protectshiny` | true/false | Re-roll keeps **shiny** wild Pokémon instead of despawning them. *Default off.* |
| `protectlegendary` | true/false | Re-roll keeps **legendary** wild Pokémon. *Default off.* |
| `protectmythical` | true/false | Re-roll keeps **mythical** wild Pokémon. *Default off.* |
| `protectultrabeast` | true/false | Re-roll keeps **Ultra Beast** wild Pokémon. *Default off.* |
| `disableseatedaggro` | true/false | While someone is seated, hostile mobs **flee** the table. *Default on.* |
| `seatedrepelradius` | 0–128 | How far (blocks) the seated mob-repulsion reaches. *Default 30.* |

The four `protect…` toggles are **opt-in** and granular — turn on only the rarities you want the
re-roll to spare. `disableseatedaggro` is **on by default**: sit at a table and hostile mobs within
`seatedrepelradius` blocks lose their target and run away, like a creeper fleeing a cat.

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

⚠️ On a **dedicated server** that screen only edits **your own** client's file. Use the commands above
to change the settings everyone plays under.

## The config file

```
config/cobblemon_picnic.json          # settings
config/cobblemon_picnic_stats.json    # statistics aggregates
config/cobblemon_picnic_events.jsonl  # granular per-re-roll log
```

Edit the first by hand if you like, then apply it with `/picnic reload` — no restart needed.

## Defaults

| Tier | Spawn cap | Fuel/re-roll | Radius | Seats |
|------|:---------:|:------------:|:------:|:-----:|
| Basic | 5 | 7 | 32 | 2 |
| Camping | 8 | 5 | 48 | 3 |
| Glamping | 12 | 3 | 64 | 4 |
| Diving | 12 | 3 | 64 | 4 |
| Hot | 12 | 3 | 64 | 4 |
| Strange | 12 | 3 | 64 | 4 |

Seat counts are **fixed per tier** and not configurable. Elsewhere: re-roll cooldown **5 s**
(per-table *and* per-player), party TM cross-teach **5%**, full-table shiny multiplier **×2**, wash
and play cooldowns **3 s** each (per Pokémon), party deploy **4–7 blocks**.

### Picnic without the spawn manipulation

`/picnic reroll false` switches the re-roll off entirely — left-clicking a table then spawns and
despawns nothing, and costs no bread. Seats, the [Shiny Aura](shiny-aura.md), baskets, the
[Battle Seeker](interactions-and-items.md#battle-seeker) and the
[care interactions](interactions-and-items.md) all keep working.
