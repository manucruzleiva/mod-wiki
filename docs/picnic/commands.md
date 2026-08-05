# Commands

Everything lives under one command: **`/picnic`**.

```
/picnic                             # print every setting (anyone)
/picnic <attribute> <value>         # change one setting (operator)
/picnic <attribute> default         # put that one setting back to its default (operator)
/picnic stats                       # picnic statistics (anyone)
/picnic stats reset                 # clear the aggregates (operator)
/picnic reload                      # re-read the config file from disk (operator)
/picnic reset                       # restore every default (operator)
```

`default` works on **every** attribute — you never have to look up what the shipped value was.

## `/picnic` — the settings

Open to **everyone**: knowing the shiny-aura multiplier and the re-roll cooldown you're playing under
is part of playing. Changing anything needs **operator** rank.

```
/picnic auramultiplier 3          # a full table now triples shiny odds
/picnic auramultiplier default    # back to ×2
/picnic reroll false              # switch the spawn re-roll off entirely
/picnic spawncap glamping 16      # per-tier settings take the tier in the middle
/picnic spawncap glamping default
```

### Attributes

| Attribute | Value | What it does |
|-----------|-------|--------------|
| `reroll` | true/false | Master switch for the [spawn re-roll](spawn-rerolling.md) itself. *Default on.* |
| `spawncap <basic\|camping\|glamping\|diving>` | int | Max Pokémon per re-roll for that tier. |
| `fuelcost <tier>` | int | Bread consumed per re-roll for that tier (defaults **7 / 5 / 3 / 3**). |
| `rerollcooldown` | 0–3600 | Seconds between re-rolls (per-table **and** per-player). *Default 5. 0 disables.* |
| `tmteachchance` | 0..1 | Chance per re-roll a party Pokémon teaches another a legal move. *Default 0.05. 0 disables.* |
| `shinyaura` | true/false | Master switch for the [Shiny Aura](shiny-aura.md). |
| `auramultiplier` | 1–100 | How many times better your shiny odds get at a **full table**. *Default 2 (double).* |
| `light` | 0–15 | Light level emitted by the table. |
| `deployonsit` | true/false | Whether sitting deploys your party. |
| `actiondistance` | number | Interaction range for picnic actions. |
| `washfriendship` | int | Friendship gained from [washing](interactions-and-items.md). |
| `washrequirestable` | true/false | Require a nearby table to wash. |
| `slimeballfriendship` | int | Friendship gained from [playing](interactions-and-items.md). |
| `slimeballbreakchance` | 0..1 | Chance the slime ball breaks when playing. |
| `slimeballrequirestable` | true/false | Require a nearby table to play. |
| `spawnappropriatelvltrainer` | true/false | Scale [Battle Seeker](battle-seeker.md) trainers to your level. |
| `trainerlevelgap` | int | Level offset for summoned trainers. |
| `protectshiny` | true/false | Re-roll keeps **shiny** wild Pokémon instead of despawning them. *Default off.* |
| `protectlegendary` | true/false | Re-roll keeps **legendary** wild Pokémon. *Default off.* |
| `protectmythical` | true/false | Re-roll keeps **mythical** wild Pokémon. *Default off.* |
| `protectultrabeast` | true/false | Re-roll keeps **Ultra Beast** wild Pokémon. *Default off.* |
| `disableseatedaggro` | true/false | While someone is seated, hostile mobs **flee** the table. *Default on.* |
| `seatedrepelradius` | 0–128 | How far (blocks) the seated mob-repulsion reaches. *Default 30.* |

!!! tip "Peaceful picnic & rare protection"
    The four `protect…` toggles are **opt-in** (default off) and granular — turn on only the rarities you
    want the re-roll to spare. `disableseatedaggro` is **on by default**: sit at a table and hostile mobs
    within `seatedrepelradius` blocks lose their target and run away, like a creeper fleeing a cat.

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

Statistics persist in `config/cobblemon_picnic_stats.json` (aggregates) and
`config/cobblemon_picnic_events.jsonl` (a granular per-re-roll log).

!!! note
    Seat counts are **not** configurable — they're fixed per tier. On a dedicated server use these
    commands; the [Mod Menu screen](configuration.md) only edits the local client config.

!!! warning "Renamed in 1.27.0"
    `/cobblemonpicnicconfig` and `/cobblemonpicnicstats` are gone, and there is no `set` keyword any
    more: `/cobblemonpicnicconfig set light 12` is now simply `/picnic light 12`.
