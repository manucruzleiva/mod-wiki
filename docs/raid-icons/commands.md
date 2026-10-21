# Commands

One command, and it runs entirely on your client — it is never sent to the server, so it works
everywhere, including on servers where you have no permissions at all. It works the same on Fabric
and NeoForge.

| Command | What it does |
|---|---|
| `/raidicons` | Opens the [settings screen](configuration.md#the-settings-screen). |
| `/raidicons report` | Prints what the mod can currently see — the first thing to run when a den is not showing up. |
| `/raidicons config` | Lists every setting with its current value. |
| `/raidicons config <setting>` | Shows one setting, with its range and its default. |
| `/raidicons config <setting> <value>` | Changes a setting. |
| `/raidicons config reset [<setting>]` | Restores one setting to its default, or all of them. |
| `/raidicons config teraTypes add <type>` · `remove <type>` | Shows or hides one tera type without retyping the whole list. |

## `/raidicons`

Opens the settings screen, in any world, with no trip back to the mod list. The screen needs
[Cloth Config](https://modrinth.com/mod/cloth-config): without it the command says so and points
you to `/raidicons config`, which changes every setting from chat.

The same screen has a key. Under **Controls**, the *Cobblemon Raid Icons* heading has an **Open
settings** key. It starts unbound, so it never collides with Xaero's keys; bind it once and it opens
the screen from anywhere in game.

## `/raidicons config`

Every setting in [Configuration](configuration.md) can be read and changed from chat, with no Cloth
Config needed. A change is saved to the file and shows on the map straight away, with no restart.

```
/raidicons config                      → lists every setting and its value
/raidicons config minTier              → minTier = 0 (0-7, default 0)
/raidicons config minTier 5            → minTier = 5
/raidicons config reset minTier        → minTier = 0
/raidicons config reset                → every setting restored to its default
```

The tera filter takes the whole list at once, or one type at a time — and the command suggests the
type names as you type:

```
/raidicons config teraTypes fire,dragon
/raidicons config teraTypes add water
/raidicons config teraTypes remove fire
/raidicons config teraTypes all
```

`all` clears the filter, so every type is shown again. The filter can never hide every type: removing
the last one left is refused.

## `/raidicons report`

Reports what the mod can currently see. Run it **while aiming at a raid den crystal**: the most
useful line it prints is what the game says that block actually is.

```
Raid Icons
  den block: cobblemonraiddens:raid_crystal_block
  layers: minimap=true worldmap=true
  scan: 4096 chunks examined, 3 den(s) known
  clock: 0 den(s) reading exactly, 2 reset span(s) measured
  nearest den: fighting tier 5 at 214, 71, -388 (36m) boss=klinklang_terafighting feature=NONE
  looking at: cobblemonraiddens:raid_crystal_block [raid_type=fighting, raid_tier=tier_five,
    is_active=true] - MATCHES the den block
```

Every line answers a different question, and together they narrow any "my dens aren't showing up" to
one cause:

| Line | What it tells you |
|---|---|
| `den block` | Whether Raid Dens is installed at all. `NOT in the registry` means nothing can ever be found. |
| `layers` | Whether Xaero's minimap and world map were found. Both `false` means the mod has nowhere to draw. |
| `scan` | How much ground has been covered and how many dens are known. `0 chunks examined` means the scan is not running. |
| `clock` | Where the [den clock](map-icons.md#the-den-clock) gets its numbers. In your own world, the dens reading their exact timer; on a server, how many resets the mod has timed so far — it needs two before it shows a countdown. |
| `nearest den` | The closest den the mod knows, with its type, tier, distance, boss and [feature](map-icons.md#feature-dens) (`NONE` for an ordinary den). |
| `looking at` | The aimed block's registry id and every blockstate property it carries, verbatim — and whether the mod recognises it. |

The report also goes to your log (`logs/latest.log`), so you can read it afterwards, or paste it into
a [bug report](../reporting.md) without having taken a screenshot at the right moment.

!!! tip "The line that matters"

    Everything this mod does rests on one assumption: that the crystal in front of you is the block
    and the properties it expects. `looking at` confirms or destroys that assumption in one step. If
    it says `is NOT the den block` while you are aiming at a den, that is the whole bug report.

## What the log shows

Without running anything, the mod writes three kinds of line to `logs/latest.log`, all starting with
`[Raid Icons]`:

| Line | When | What it rules out |
|---|---|---|
| `scan: N chunks examined, N den(s) known, player at …` | Every 10 seconds, **only while no den is known**. | If the chunk count grows, the scan is running and simply has not met a den yet. |
| `den at … - <type> tier N active=… boss=… feature=…` | Once per den, the first time it is found. | That den was found and read — if it is not on the map, a [filter](configuration.md#the-filters) is hiding it. |
| `first draw: <layer> (N den(s) known)` | The first time each Xaero map asks the mod to draw. | The layer is hooked into that map. No line for a map means Xaero never asked. |
