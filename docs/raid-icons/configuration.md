# Configuration

There are three ways to change a setting, and they all edit the same values:

- **The settings screen**, through `/raidicons`, a key you bind, Mod Menu on Fabric or the mod list
  on NeoForge. It needs [Cloth Config](https://modrinth.com/mod/cloth-config).
- **[`/raidicons config`](commands.md#raidicons-config)** in chat, with or without Cloth Config.
- **The settings file**, `config/cobblemon_raid_icons.properties` in your game folder.

A change made on the screen or by command is saved to the file and shows on the map straight away,
with no restart.

## The settings screen

Run `/raidicons`, or bind **Options → Controls → Cobblemon Raid Icons → Open settings**. On Fabric,
Mod Menu's config button opens it too; on NeoForge, the mod list's **Config** button does. Without
Cloth Config the button is not there and the command points you to `/raidicons config` instead.

The screen has three tabs:

| Tab | Settings |
|---|---|
| **Filters** | Only active dens, Lowest star tier, one switch per tera type |
| **Icons** | Minimap icon size, World map icon size |
| **Advanced** | Scan radius (chunks), Chunks scanned per tick |

## The settings file

The file is created with the defaults the first time you load a world. An unreadable or misspelled
value never stops the mod: it falls back to its default and says so in the log.

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

An unrecognised name is dropped from the list rather than silently matching nothing. From chat,
`/raidicons config teraTypes add <type>` and `remove <type>` change one type at a time, and
`/raidicons config teraTypes all` clears the filter. On the screen, each type has its own switch;
turning every switch off shows every type again, because a filter cannot hide all of them.

A [feature den](map-icons.md#feature-dens) is never hidden by this filter. Its marker shows the
feature, not the tera type, so filtering it out by type would hide it for a reason the map does not
show.

### `onlyActiveDens`

`true` hides dens that are not currently live. Default `false`, which draws every den whether it is
ready to fight or resetting.

## Icon size

### `minimapIconScale` and `worldMapIconScale`

The size of the den icons on each map, as a percentage of that map's normal size. Default `100`,
from `50` to `200`. At `100` an icon is 36×36 pixels on the minimap and 48×48 on the world map.

They are separate so you can shrink a crowded minimap without making the world map harder to read.

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

Run [`/raidicons config`](commands.md#raidicons-config) to see every value the mod is using. For the
scan itself, [`/raidicons report`](commands.md#raidicons-report) shows the ground actually being
covered on its `scan` line, and what survived your filters on its `nearest den` line.
