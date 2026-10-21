# Commands

Every command runs entirely on your client. None of them is ever sent to the server, so they work
everywhere, including on servers where you have no permissions at all and on servers that have never
heard of this mod.

| Command | What it does |
|---|---|
| `/raidicons` | Opens the [settings screen](configuration.md#the-settings-screen). |
| `/raidicons report` | Prints what the mod can currently see. |
| `/raidicons config` | Lists every setting with its current value. |
| `/raidicons config <setting>` | Shows one setting with its range and default. |
| `/raidicons config <setting> <value>` | Changes one setting. |
| `/raidicons config reset [<setting>]` | Restores one setting, or every setting, to its default. |
| `/raidicons config teraTypes add\|remove <type>` | Shows or hides one tera type. |

## `/raidicons`

Opens the settings screen, the same one Mod Menu (Fabric) or the mod list (NeoForge) opens. The
screen needs [Cloth Config](https://modrinth.com/mod/cloth-config); without it the command says so
and points you to `/raidicons config`, which changes the same settings from chat.

You can also bind a key to it: **Options → Controls → Cobblemon Raid Icons → Open settings**. It
starts unbound, so it never collides with Xaero's keys.

## `/raidicons config`

Reads and changes every setting from chat, with or without Cloth Config. A change is saved to the
settings file straight away and shows on the map on the next frame, with no restart.

```
/raidicons config                      # list every setting and its value
/raidicons config minTier              # minTier = 0 (0-7, default 0)
/raidicons config minTier 5            # hide everything below 5 stars
/raidicons config teraTypes fire,dragon
/raidicons config teraTypes add water  # show one more type
/raidicons config teraTypes remove fire
/raidicons config teraTypes all        # back to every type
/raidicons config reset minTier        # one setting back to its default
/raidicons config reset                # every setting back to its default
```

The setting names and their ranges are on the [Configuration](configuration.md) page. The command
suggests tera type names as you type. A value outside a setting's range is refused rather than
changed to something you did not ask for, and the tera filter refuses to hide its last type: a filter
that hid every type would hide every den.

## `/raidicons report`

Reports what the mod can currently see. Run it **while aiming at a raid den crystal**: the most
useful line it prints is what the game says that block actually is.

```
Raid Icons
  den block: cobblemonraiddens:raid_crystal_block
  layers: minimap=true worldmap=true
  scan: 4096 chunks examined, 3 den(s) known
  clock: 3 den(s) reading exactly, 0 reset span(s) measured
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
| `clock` | Where the [den clock](map-icons.md#the-den-clock) gets its numbers. Dens *reading exactly* have a real countdown, which only happens in singleplayer or as the host of a LAN game. *Reset spans measured* is how many times the mod has watched a den roll a new raid on a server, which is what the estimated clock is built from. |
| `nearest den` | The closest den the mod knows, with its type, tier, distance, boss and feature (`NONE` for an ordinary den). |
| `looking at` | The aimed block's registry id and every blockstate property it carries, verbatim, and whether the mod recognises it. |

The report also goes to your log (`logs/latest.log`), so you can read it afterwards, or paste it into
a [bug report](../reporting.md) without having taken a screenshot at the right moment.

!!! tip "The line that matters"

    Everything this mod does rests on one assumption: that the crystal in front of you is the block
    and the properties it expects. `looking at` confirms or destroys that assumption in one step. If
    it says `is NOT the den block` while you are aiming at a den, that is the whole bug report.

## What the log shows on its own

Without running anything, the mod writes a few lines to `logs/latest.log`, all starting with
`[Raid Icons]`:

| Line | When | What it rules out |
|---|---|---|
| `scan: N chunks examined, N den(s) known, player at …` | Every 10 seconds, **only while no den is known yet** | Whether the scan is running at all. The line stops as soon as the first den is found. |
| `den at … - <type> tier N active=… boss=… feature=…` | Once per den, the first time it is found | Whether a den was found but filtered out, as opposed to never found. |
| `first draw: <layer> (N den(s) known)` | The first time each Xaero map layer asks the mod to draw | Whether Xaero is calling the mod at all. |
