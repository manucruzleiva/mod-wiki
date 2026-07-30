# Configuration

Cobblemon Picnic can be tuned three ways: a **config file**, **in-game commands**, and an optional
**Mod Menu screen**.

## Config file

Runtime settings live in:

```
config/cobblemon_picnic.json
```

Edit it with a text editor, then apply your changes with `/cobblemonpicnicconfig reload` (no restart
needed). Statistics are stored separately in `config/cobblemon_picnic_stats.json` and
`config/cobblemon_picnic_events.jsonl`.

## In-game commands

The fastest way to change a single value is the [`/cobblemonpicnicconfig`](commands.md) command —
see the [Commands](commands.md#settings-you-can-set) page for the full parameter list. Highlights:

- **Spawns:** `spawncap <tier>`, `fuelcost <tier>`, `rerollcooldown <seconds>`
- **Shiny aura:** `shinyaura`, `aurabase`, `auramax`
- **Care:** `washfriendship`, `slimeballfriendship`, `slimeballbreakchance`
- **Party fun:** `tmteachchance` (rare TM cross-teaching on re-roll)
- **Battle Seeker:** `spawnappropriatelvltrainer`, `trainerlevelgap`
- **Re-roll protection:** `protectshiny`, `protectlegendary`, `protectmythical`, `protectultrabeast`
- **Peaceful picnic:** `disableseatedaggro` (on by default), `seatedrepelradius`
- **Misc:** `light`, `actiondistance`, `deployonsit`

## Mod Menu screen

With **[Mod Menu](https://modrinth.com/mod/modmenu)** + **[Cloth Config](https://modrinth.com/mod/cloth-config)**
installed, open **Mods → Cobblemon Picnic → Settings** (the gear button) to edit the same values in a
GUI.

!!! warning "Mod Menu edits the *local* config"
    On a **dedicated server**, the Mod Menu screen only changes your client's file — use
    `/cobblemonpicnicconfig set ...` to change the server's settings for everyone.

## Defaults reference

| Tier | Spawn cap | Fuel/re-roll | Radius | Seats |
|------|:---------:|:------------:|:------:|:-----:|
| Basic | 5 | 7 | 32 | 2 |
| Camping | 8 | 5 | 48 | 3 |
| Glamping | 12 | 3 | 64 | 4 |
| Diving | 12 | 3 | 64 | 4 |

Other notable defaults: **re-roll cooldown** `5` s (per-table + per-player), **party TM cross-teach
chance** `0.05` (5%).
