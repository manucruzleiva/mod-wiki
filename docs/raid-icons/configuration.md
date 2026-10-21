# Configuration

There are three ways to change a setting, and they all edit the same file:

- **The [settings screen](#the-settings-screen)**, with Cloth Config installed.
- **[`/raidicons config`](commands.md#raidicons-config)** from chat, with nothing else installed.
- **The file itself**, described below.

A change made in game shows on the map as soon as it is saved, with no restart.

## The settings screen

With [Cloth Config](https://modrinth.com/mod/cloth-config) installed, the mod gets a settings screen.
Open it with [`/raidicons`](commands.md#raidicons), with the **Open settings** key under Controls
(unbound until you set it), or from the mod list: the config button in
[Mod Menu](https://modrinth.com/mod/modmenu) on Fabric, and in NeoForge's own mod list.

It has three tabs: **Filters** (only active dens, lowest star tier, one switch per tera type),
**Icons** (the two icon sizes) and **Advanced** (the scan). Without Cloth Config the button is simply
not there, and the command and the file work as before.

## The file

The settings live in **`config/cobblemon_raid_icons.properties`**, inside your game folder — the
same `config/` your other mods write to. The file is created with the defaults the first time you
load a world, so start it once and then edit it.

An unreadable or misspelled value never stops the mod: it falls back to its default and says so in
the log.

```properties
scanRadius=12
chunksPerTick=12
onlyActiveDens=false
minTier=0
teraTypes=
minimapIconScale=100
worldMapIconScale=100
```

## The filters

These decide which dens get an icon. They are the settings worth touching.

### `minTier`

The lowest star tier that gets a marker, from `0` to `7`. `0` marks everything; a value outside that
range is clamped to it.

| Value | Effect |
|---|---|
| `0` | Every den, whatever its tier. The default. |
| `5` | Only 5-star dens and above — the endgame view. |
| `7` | Only 7-star dens. Every [feature den](map-icons.md#feature-dens) is 7-star, but so are many plain ones, so this does not single them out. |

A den whose tier the mod could not read is always drawn, at any setting. It might be the one you
want, and hiding it on a technicality is worse than one extra icon.

### `teraTypes`

The tera types that get a marker, comma-separated. **Empty means all of them**, which is the default.

```properties
# Only fire and dragon dens
teraTypes=fire,dragon
```

The names are the eighteen types plus `stellar`, lower-case:

`normal` · `fire` · `water` · `electric` · `grass` · `ice` · `fighting` · `poison` · `ground` ·
`flying` · `psychic` · `bug` · `rock` · `ghost` · `dragon` · `dark` · `steel` · `fairy` · `stellar`

An unrecognised name is dropped from the list rather than silently matching nothing.

A [feature den](map-icons.md#feature-dens) is never hidden by this filter. Its marker shows the
feature, not the tera type, so filtering it out by type would hide it for a reason the map does not
show.

### `onlyActiveDens`

`true` hides dens that are not currently live. Default `false`, which draws every den whether it is
ready to fight or resetting.

## The icon sizes

### `minimapIconScale` and `worldMapIconScale`

How big the den icons are, as a percentage of each map's normal size. Default `100`, clamped to
`50`–`200` — from half to twice the size.

There is one per map so you can shrink a crowded minimap without making the world map harder to read.
At `100` an icon is 36×36 pixels on the minimap and 48×48 on the world map.

## The scan

The two remaining settings control how the mod looks for dens. The defaults are good; change them
only if you have a reason.

### `scanRadius`

How many chunks out from you are examined. Default `12`, clamped to `1`–`32`.

Raising it past your render distance buys nothing: chunks the game has not loaded hold no dens as
far as this mod is concerned.

### `chunksPerTick`

How many chunks are examined each client tick. Default `12`, clamped to `1`–`64`.

The scan cycles continuously over the whole radius, so this sets how quickly a newly placed den
appears — at the default, the full radius comes round in under three seconds. Each chunk is nearly
free to check, so there is little to gain by lowering it.

## Checking a change took effect

Run [`/raidicons report`](commands.md#raidicons-report). The `scan` line shows the ground actually being covered, and the
`nearest den` line shows what survived your filters.
