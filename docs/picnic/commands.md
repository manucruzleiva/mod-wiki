# Commands

## `/cobblemonpicnicstats`

Available to **everyone**. Shows a summary of picnic activity:

- Total re-rolls, Pokémon spawned / despawned
- **Shinies** found (with ratio), **legendaries / mythicals**
- Snacks consumed, distinct species
- **Most common** and **rarest** species

```
/cobblemonpicnicstats          # show the summary
/cobblemonpicnicstats reset    # (operator) clear the aggregates
```

Statistics persist in `config/cobblemon_picnic_stats.json` (aggregates) and
`config/cobblemon_picnic_events.jsonl` (a granular per-re-roll log).

## `/cobblemonpicnicconfig`

**Operator only.** Read and change settings live.

```
/cobblemonpicnicconfig get                  # print current settings
/cobblemonpicnicconfig reload               # reload config file from disk
/cobblemonpicnicconfig reset                # restore defaults
/cobblemonpicnicconfig set <param> <value>  # change one setting
```

### Settings you can `set`

| Parameter | Value | What it does |
|-----------|-------|--------------|
| `spawncap <basic\|camping\|glamping\|diving>` | int | Max Pokémon per re-roll for that tier. |
| `fuelcost <tier>` | int | Bread consumed per re-roll for that tier (defaults **7 / 5 / 3 / 3**). |
| `rerollcooldown` | 0–3600 | Seconds between re-rolls (per-table **and** per-player). *Default 5. 0 disables.* |
| `tmteachchance` | 0..1 | Chance per re-roll a party Pokémon teaches another a legal move. *Default 0.05. 0 disables.* |
| `light` | 0–15 | Light level emitted by the table. |
| `aurabase` | 0..1 | Base shiny boost per occupied seat. |
| `auramax` | 0..1 | Cap on the total shiny boost. |
| `shinyaura` | true/false | Master switch for the [Shiny Aura](shiny-aura.md). |
| `deployonsit` | true/false | Whether sitting deploys the seat behavior. |
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

!!! note
    Seat counts are **not** configurable — they're fixed per tier. On a dedicated server use these
    commands; the [Mod Menu screen](configuration.md) only edits the local client config.
