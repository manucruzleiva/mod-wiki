# 🧩 World Creation & Config

Everything is decided **when you create the world** — a dedicated **ROUTES** tab sits next to
**GAME / WORLD / MORE** on the create-world screen. Outside world creation there's a global config
screen for defaults, opened from the mod list (Mod Menu on Fabric, the **Config** button on NeoForge).

!!! tip "Looking for the NUZLOCKE tab?"
    The Nuzlocke ruleset, its starter options and the Soul Link toggles belong to
    **[Cobblemon Nuzlocke & Soul Link](../nuzlocke/commands.md)** — install that add-on and its
    tab appears next to this one.

<div class="flow" markdown>

1. <span class="flow__tag">Set</span> on the **ROUTES** tab when you create the world
2. <span class="flow__tag flow__tag--or">Defaults</span> from the global config (key **K**, `config/routes.json`) for a world that was not configured
3. <span class="flow__tag flow__tag--result">Result</span> your world's rules, saved with that world and never overwritten later

</div>

## ROUTES tab

The tab is split into six sections, in the order you meet them: what the network is, what it
connects, how a road is shaped, what it is made of, where you start, and what you are shown.

### Route Generation

| Option | Default | Notes |
| --- | --- | --- |
| Generate routes | on | master switch. Off: no roads planned, and the spawn stays where the game puts it |
| Connect all structures | off | also connect surface structures that are not towns — never one whose id names a ruin, an ancient thing or a mineshaft |
| Routes per city | 4 | a **ceiling**, not a count: each town rolls its own up to this, inside the band its size puts it in — a village low, a city high — so the network has hamlets and crossroads |
| Longest road | 1600 | the farthest two towns can be and still get a direct road |
| Ring roads | on | keep closing loops between nearby towns — loops are what enclose named **areas** |

### Towns & Settlements

| Option | Default | Notes |
| --- | --- | --- |
| Towns & landmarks | automatic | every structure your world has, each set to Settlement, Landmark or Ignored — see [Which structures get roads](which-structures.md) |
| Use Routes' structure list | on | the hand-reviewed list of towns, landmarks and structures to ignore that ships with Routes (gym entrances included). Your own choices above always beat it — see [Which structures get roads](which-structures.md#the-list-routes-ships) |
| Settlement allowlist (advanced) | empty | exact structure ids that count as towns. Empty = the automatic rule |
| Never spawn here | RS ocean village | towns that may never be the world's **first** town. They stay ordinary towns otherwise |
| Confirm towns exist | on | check the jigsaw really assembles before the network treats a candidate as a town — no towns on the map with an empty field under them |
| Bigger towns, more roads | on | settlements come as village, town or city by their real footprint, and a bigger one carries more roads. Needs **Confirm towns exist** |
| Town size | 64 | blocks across from which a settlement is a town rather than a village |
| City size | 128 | blocks across from which it is a city. `/routes debug settlements` shows how your world's towns fall into the three |
| Roads go around landmarks | on | a road steers around a landmark's real footprint instead of cutting through it; where one fills the only way through, the road is still built |
| Landmark pull | 3 | 0–10: how strongly a road bends to pass beside the one landmark it visits — a few blocks, never a detour. 0 = off |
| Landmark reach | 96 | how far off a road's straight line, in blocks, a landmark can be and still pull it |
| Landmark signs | on | a signpost beside the road names the landmark it passes |

### Road Shape

| Option | Default | Notes |
| --- | --- | --- |
| Road width | 5 | odd numbers; the brush is symmetric around the centreline |
| Water crossing width | 10 | its own number, not a multiple of the road — open water reads much wider than it is |
| Road curviness | 5 | 0 = ruler-straight, 10 = maximum seeded wander |
| Straight bridges | on | a bridge over water runs straight from bank to bank however much the roads wander; off, the crossing weaves with the road. A bridge over a dry gap weaves either way |
| Steepest climb | 8 | tenths of a block per block, before a road cuts or bores instead of hugging the ground |
| Dig tunnels | on | off, a planned tunnel is built as a steep surface road over the top |
| Tunnel width | 9 | a tunnel's own width, twice the road's — only the bore, the ramp down to it stays road-width. Odd numbers, like the road |
| Tunnel height | 8 | floor to ceiling. Taller tunnels leave a thinner roof in low hills |
| Build bridges | on | off, a river becomes an open water lane and a dry gap is followed on the ground |
| Shape terrain around roads | on | the ground is road-shaped **before** anything is planted on it, instead of demolished afterwards. Decided once, when the world is created |
| Warm road chunks ahead | on | generate a road's chunks a little before you reach them, so the cost lands while you walk |

### Surface & Lighting

| Option | Default | Notes |
| --- | --- | --- |
| Road surface | Random (by biome) | Random paves each stretch from the palette of the biome it crosses, so a road changes material where the land changes. Pick one material, or press **+ Add material** to mix several: each row has a *Share* slider (70 and 30 pave about 70% and 30%), laid in rounded patches. *Random (by biome)* can be one entry of the mix |
| Road wear | 0% | 0–30: that share of a road's flat blocks is laid as a worn version of its material — cracked or mossy stone bricks, gravel in cobblestone, grass through a dirt path. Stairs never wear |
| Bridge deck | Random | Random builds each bridge from the timber of its biome. Pick one plank or a mix: each bridge takes one of them for its whole span, and its stairs follow the same wood |
| Handrail | Random | Random gives each route one of twelve fences and walls. Pick one or a mix: each route takes one for its whole length |
| Road lamp posts | Random | Random / On / Off — Random decides per route |
| Tunnel lighting | Random | Random keeps some tunnels as dark caves |
| Underwater lighting | Random | a sea lantern in the pillar under each water-crossing marker — Random decides per route |
| Descriptive route names | on | *Route 3: Steep Pass* on signposts, waypoints and zone banners; off keeps the plain *Route 3*. Roads already numbered keep their name |
| Descriptive area names | on | *A3-Frostpine* on an area's waypoint and banner; off keeps the plain *Area 3* |
| Picnic stops | 3 | with [Cobblemon Picnic](../picnic/index.md) installed, the percent of rest stops that are a picnic table instead of a camp. 0 = never, 100 = every stop. Kept per world |

#### Road materials

The **Road surface** picker offers these materials. Each one paves every road in that block; *Random (by
biome)* is the default.

| Choice | Block |
| --- | --- |
| Random (by biome) | `random` — the biome palette below |
| Dirt Path | `minecraft:dirt_path` |
| Cobblestone | `minecraft:cobblestone` |
| Mossy Cobblestone | `minecraft:mossy_cobblestone` |
| Gravel | `minecraft:gravel` |
| Stone Bricks | `minecraft:stone_bricks` |
| Mossy Stone Bricks | `minecraft:mossy_stone_bricks` |
| Cracked Stone Bricks | `minecraft:cracked_stone_bricks` |
| Andesite | `minecraft:andesite` |
| Polished Andesite | `minecraft:polished_andesite` |
| Sandstone | `minecraft:sandstone` |
| Cut Sandstone | `minecraft:cut_sandstone` |
| Cut Red Sandstone | `minecraft:cut_red_sandstone` |
| Packed Mud | `minecraft:packed_mud` |
| Mud Bricks | `minecraft:mud_bricks` |
| Coarse Dirt | `minecraft:coarse_dirt` |

A mix holds up to six of them. In the config file or with [`/routes config set path_block_material`](commands.md#config-read-and-change-this-worlds-settings), the setting also takes any other
block id, modded ones included, as `minecraft:cobblestone=70,minecraft:gravel=30`. An id the game does not
know is dropped from the mix, and if nothing is left the road falls back to Random.

**What Random lays.** Each stretch takes its block from the biome it crosses, in patches a few blocks across.
The biome's name is checked first, then its temperature:

| Biome | Random draws from |
| --- | --- |
| Badlands | cobblestone, cut red sandstone, gravel, stone bricks |
| Swamp, mangrove swamp | packed mud, mud bricks, mossy cobblestone, coarse dirt |
| Jungle | mossy cobblestone, mossy stone bricks, dirt path, gravel |
| Desert, beach, very hot biomes | cobblestone, cut sandstone, gravel, stone bricks |
| Frozen | stone bricks, cobblestone, cracked stone bricks, gravel |
| Cold | cobblestone, stone bricks, andesite, gravel |
| Temperate | dirt path, cobblestone, mossy cobblestone, stone bricks, gravel |
| Warm | dirt path, packed mud, sandstone, gravel |

**Bridge deck** offers oak, spruce, birch, jungle, acacia, dark oak, mangrove, cherry, bamboo, crimson and
warped planks; the config file takes any planks block. Random uses the biome's timber: cherry in a cherry
grove, mangrove in a mangrove swamp, bamboo in a bamboo jungle, dark oak in a dark forest or badlands, birch
in a birch forest, jungle in a jungle, acacia in a savanna, spruce in taiga, mountains and the cold, oak
everywhere else.

**Handrail** offers oak, spruce, birch, jungle, acacia, dark oak, mangrove and cherry fences, and cobblestone,
mossy cobblestone, stone brick, mossy stone brick, andesite and diorite walls; the config file takes any fence
or wall. Random rolls one of twelve per route: every fence but mangrove and cherry, and the six walls.

### World Spawn

| Option | Default | Notes |
| --- | --- | --- |
| Spawn in city | on | move a new world's spawn into the nearest town; off leaves the vanilla wilderness spawn |
| Pregenerate around spawn | 512 | chunks built in the background the first time you enter, so the roads and towns around spawn are already built when you walk out — the default reaches the spawn town and its first road, about 200 blocks. 0 = off |

### Map & Notifications

| Option | Default | Notes |
| --- | --- | --- |
| Zone notifications | Toast | how entering a route or an area is announced: Off / Toast / Announcement / Chat |
| Map chunk paint | on | tint chunks on [Xaero's maps and JourneyMap](map-integration.md) by category; inert without either |

Who stands on the roads and what gets built beside the towns is the Nuzlocke add-on's: **road
trainers**, the **gyms next to towns** and the **league** are configured on its
[NUZLOCKE tab](../nuzlocke/commands.md). Routes on its own builds the towns and the roads
between them.

The map **tint intensity** and **colours** (City / Route / Area) are not world-creation choices —
set them in play with [`/routesmap`](map-integration.md#changing-how-it-looks-routesmap), with the map
in front of you.

!!! info "Saved per world, and some fixed for good"
    Choices made in these tabs are stored **per world** and only applied to a brand-new world —
    loading an existing world never gets its rules clobbered. Confirming them says *World rules set: …*.

    The settings that **shape the road network** stay at the value the world was created with: connect
    all structures, routes per city, longest road, ring roads, the towns & landmarks list and Routes'
    structure list, the allowlist, confirm towns, bigger towns and the town and city sizes, the four
    landmark settings, road width, curviness, straight bridges, steepest climb and picnic stops.
    Changing one mid-world would give the land generated afterwards a second network whose roads stop
    short of the old ones. `/routes config set` on one of them saves the value for the worlds you create
    next and says so; `/routes config list` marks them.

## Global defaults

The global defaults live in `config/routes.json` (English & Spanish labels) and are used
when a world wasn't configured through the tabs. The map-paint intensity and colours are changed in
play with [`/routesmap`](map-integration.md#changing-how-it-looks-routesmap).

## Commands

The root is `/routes` (the old `/cobblemonroutes` alias is gone). The full manual — every
command, argument, permission and behaviour — lives on [the Commands page](commands.md).
