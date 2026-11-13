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

Two rows of **presets** open the tab, then the options sit in six sections, in the order you meet
them: where roads go, how they look, how they get past hills and water, what they do near landmarks,
where you start, and an **Advanced** section at the end. Advanced starts closed; once you open or
close it, it stays that way for the rest of the session. The Mod Menu config screen shows the same
sections.

### Presets

| Row | Choices | What it sets |
| --- | --- | --- |
| Road network | Sparse · **Balanced** · Dense | Roads per town, longest road and ring roads. Sparse: 2 roads per town, none longer than 1000 blocks, no ring roads. Balanced: 4, up to 1600, with ring roads. Dense: 5, up to 2400, with ring roads |
| Road style | Trails · **Roads** · Highways | Road width, winding, lamp posts, tunnel size and wear. Trails: 3 wide, winding, worn, no lamp posts, small tunnels. Roads: 5 wide, lamp posts on some roads. Highways: 7 wide, nearly straight, lamp posts on every road, big tunnels |

Balanced and Roads are the defaults. Change one of those options by hand and its row shows **Custom**.

### Where roads go

| Option | Default | Notes |
| --- | --- | --- |
| Build roads between towns | on | master switch. Off: no roads planned, and the spawn stays where the game puts it |
| Roads per town | 4 | 1–5, a **ceiling**, not a count: each town rolls its own up to this, inside the band its size puts it in (a village low, a city high), so the network has hamlets and crossroads |
| Longest road (blocks) | 1600 | the farthest two towns can be and still get a direct road |
| Ring roads | on | keep closing loops between towns that are close on the map but far apart by road. Loops are what enclose named **areas** |
| Bigger towns get more roads | on | settlements come as village, town or city by their real footprint, and a bigger one carries more roads. Needs **Check towns before building roads** |
| Towns & landmarks | automatic | every structure your world has, each set to **Town**, **Landmark**, **Ignored** or **Underground town**, with a **Reset to Routes' list** button on top. See [Which structures get roads](which-structures.md) |

### How roads look

| Option | Default | Notes |
| --- | --- | --- |
| Road surface | Random (by biome) | Random paves each stretch from the palette of the biome it crosses, so a road changes material where the land changes. Pick one material, or press **+ Add material** to mix several: each row has a *Share* slider (70 and 30 pave about 70% and 30%), laid in rounded patches. *Random (by biome)* can be one entry of the mix. See [Road materials](#road-materials) |
| Road wear | 0% | 0–30: that share of a road's flat blocks is laid as a worn version of its material: cracked or mossy stone bricks, gravel in cobblestone, grass through a dirt path. Stairs never wear |
| Road width | 5 | 3–9, odd numbers; the brush is symmetric around the centreline |
| How much roads wind | 5 | 0 = ruler-straight, 10 = follows every fold of the land |
| Bridge deck | Random (by biome) | Random builds each bridge from the timber of its biome. Pick one plank or a mix: each bridge takes one of them for its whole span, and its stairs follow the same wood |
| Handrail | Random (per route) | Random gives each route one of twelve fences and walls. Pick one or a mix: each route takes one for its whole length |
| Lamp posts | Random | Random / On / Off. Random decides per route |
| Tunnel lanterns | Random | Random keeps some tunnels as dark caves |
| Lights along water crossings | Random | a sea lantern in the pillar under each water-crossing marker. Random decides per route |
| Road names | on | *Route 3: Steep Pass* on signposts, waypoints and zone banners; off keeps the plain *Route 3*. Roads already numbered keep their name |
| Picnic stops | 3 | with [Cobblemon Picnic](../picnic/index.md) installed, the percent of rest stops that are a picnic table instead of a camp. 0 = never, 100 = every stop |
| Route Pokémon | on | with Cobblemon 1.8 installed, wild Pokémon appear along the roads (see [Dynamic Routes](routes.md)). Off adds no new spots; the ones already there stay |

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

### Hills, rivers and tunnels

| Option | Default | Notes |
| --- | --- | --- |
| Steepest climb | 8 | 1–10, tenths of a block per block. Higher lets roads climb steeper hills; lower makes them cut through or tunnel instead |
| Dig tunnels | on | off, a planned tunnel is built as a steep surface road over the top |
| Tunnel width | 9 | a tunnel's own width, twice the road's. Only the bore widens; the ramp down to it stays road-width. Odd numbers, like the road |
| Tunnel height | 8 | floor to ceiling. Taller tunnels leave a thinner roof in low hills |
| Build bridges | on | off, a river becomes an open water lane and a dry gap is followed on the ground |
| Bridges run straight across | on | a bridge over water runs straight from bank to bank however much the road winds; off, the crossing weaves with the road. A bridge over a dry gap weaves either way |
| Water crossing width | 10 | the marked lane across a lake or sea. Its own number, not a multiple of the road: open water reads much wider than it is |
| Steps at tunnel mouths | on | the ramp out of a tunnel starts with a stair off the tunnel floor, never a step of a block and a half |
| Tunnels surface before a town | on | a road that would reach a town inside a tunnel comes up before the first building and enters on the surface, by the street, with its welcome sign. The ground under a town is never dug. Roads that already arrive on the surface keep their shape. **Fixed per world** |
| Smooth diagonal road steps | on | a road climbing on the diagonal gets no step of a block and a half at its corners: that column is lifted half a block, unless it would leave a step of more than a block on its other side |
| Smooth fork edges | on | a road leaves a fork's levelled ground without a wall at its edge, and no paving or slab is left hanging over air beside it |
| Roads sharing ground agree on its height | on | where roads run together into a fork, over the same strip or side by side, that ground is laid at the lowest of their heights and a road beside another comes down to meet it by half a block per block, so there are no walls between them. Off, each road keeps its own height and the last one drawn wins |
| No road scraps inside towns | on | a road starts after the last building or street of the town it leaves, however far apart two of them are. Off, only gaps of up to ten blocks are left to the town, so a longer one can keep a short piece of road ending in a wall |
| Enter CCS towns by their streets | on | a road into a town of [Cobblemon Cities & Structures](https://modrinth.com/mod/cobblemon-cities-structures) joins the end of a street the town left open, the one facing the road, and not the side of a street or an empty house lot. Does nothing in vanilla villages, in other town packs, or without that mod |

The six look-and-fit options in that list (everything from **Steps at tunnel mouths** down, except
**Tunnels surface before a town**) only change **chunks generated from now on**: roads already in your world
keep their blocks, and the planned routes do not move. **Tunnels surface before a town** reshapes the
planned road, so it follows the rule below for settings that shape the network.

### Landmarks

| Option | Default | Notes |
| --- | --- | --- |
| Roads go around landmarks | on | a road steers around a landmark's (or an ignored structure's) real footprint instead of cutting through it; where one fills the only way through, the road is still built |
| Roads pass by one landmark | 3 | 0–10: how strongly a road bends to pass beside the one landmark it visits, a few blocks and never a detour. 0 = off |
| How far a road detours (blocks) | 96 | how far off a road's straight line a landmark can be and still pull it |
| Sign the landmark a road passes | on | a signpost beside the road names the landmark it passes |
| Landmark waypoints | on | the first time you walk past the landmark a road signs, it gets a waypoint on your map, in its own *Landmarks* set. See [Map Integration](map-integration.md) |

### Your first steps

| Option | Default | Notes |
| --- | --- | --- |
| Start in a town | on | move a new world's spawn into the nearest town; off leaves the vanilla wilderness spawn. Only a world being created does this: a world you already had keeps its spawn when Routes arrives (`/routes debug spawn` moves it by hand) |
| Prepare the land around spawn | 512 | chunks built in the background the first time you enter, so the roads and towns around spawn are already built when you walk out. The default reaches the spawn town and its first road, about 200 blocks. 0 = off |

### Advanced

Ten options a first world rarely needs. The section starts closed.

| Option | Default | Notes |
| --- | --- | --- |
| Every surface structure gets roads | off | also connect surface structures that are not towns, never one whose id names a ruin, an ancient thing or a mineshaft |
| Routes' structure list | on | the hand-reviewed list of towns, landmarks and structures to ignore that ships with Routes (gym entrances included). Your own choices in **Towns & landmarks** always beat it. See [Which structures get roads](which-structures.md#the-list-routes-ships) |
| Town ids only | empty | exact structure ids that count as towns. Empty = the automatic rule |
| Never start in | RS ocean village | towns that may never be the world's **first** town. They stay ordinary towns otherwise |
| Check towns before building roads | on | check the town really generates before the network sends a road to it, so no road ends at an empty field |
| Town size (blocks) | 64 | blocks across from which a settlement is a town rather than a village |
| City size (blocks) | 128 | blocks across from which it is a city. `/routes debug settlements` shows how your world's towns fall into the three |
| Shape the land with the road | on | the ground is road-shaped **before** anything is planted on it, instead of cut and filled afterwards. Decided once, when the world is created |
| Build road chunks early | on | generate a road's chunks a little before you reach them, so the cost lands while you walk |
| Area names | on | *A3-Frostpine* on an area's waypoint and banner; off keeps the plain *Area 3* |

### Map & Notifications (not on the tab)

**Zone notifications** (Off / **Toast** / Announcement / Chat: how entering a route or an area is
announced) and **Map chunk paint** (on: tint chunks on [Xaero's maps and JourneyMap](map-integration.md)
by category) are your own preferences, not world rules, so they are not on the create-world tab. Set
them in Routes' config screen (Mod Menu on Fabric, the **Config** button on NeoForge), under **Map &
Notifications**; the chunk paint, the tint
intensity, the colours and the waypoints are also changed in play with
[`/routesmap`](map-integration.md#changing-how-it-looks-routesmap), with the map in front of you.

Routes builds the towns and the roads between them, and with
[Radical Cobblemon Trainers](https://modrinth.com/mod/radical-cobblemon-trainers) installed it also
places the **route trainers** beside the roads (see [Dynamic Routes](routes.md)). The **gyms next to
towns**, the **league** and the Nuzlocke rules belong to
[Cobblemon Nuzlocke & Soul Link](../nuzlocke/commands.md), on its NUZLOCKE tab.

!!! info "Saved per world, and some fixed for good"
    Choices made in these tabs are stored **per world** and only applied to a brand-new world:
    loading an existing world never gets its rules clobbered. Confirming them says *World rules set: …*.

    The settings that **shape the road network** stay at the value the world was created with: roads
    per town, longest road, ring roads, bigger towns get more roads, the towns & landmarks list, road
    width, how much roads wind, picnic stops, steepest climb, bridges run straight across, tunnels
    surface before a town, the three
    landmark-path settings (go around, pass by, how far), and in Advanced every surface structure gets
    roads, Routes' structure list, town ids only, check towns and the town and city sizes.
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
