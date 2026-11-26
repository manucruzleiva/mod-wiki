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
| Roads enter towns by a street end | on | a road into a town is planned to one of the street ends the town left open, goes around the town's buildings to reach it and stops in front of it. The ends are the ones the town names ([Cobblemon Cities & Structures](https://modrinth.com/mod/cobblemon-cities-structures), or a `routes:city_exit` jigsaw); a town that names none, a vanilla village included, offers the dead ends of its streets. Off, the road is planned to the middle of the town and stops at the first building it meets, as before. A town with no open street end on land keeps that too. **Fixed per world** (`route_street_ends`) |
| Water routes end in a pier at a street | on | a street end that opens on water takes a route too, and the route ends there in a **pier**: a plank deck on the water, level with the street, from the street end out to where the boats arrive. A route whose other end stands in water enters by the nearest open street end, on land or on water; a road that comes by land keeps to the ends on land, and only a town with none it can take gets the pier. Off, a street end on water is passed over: a town standing in the sea gets a water route that stops at its edge. Needs *Roads enter towns by a street end* and *Build bridges* for the deck. **Fixed per world** (`route_piers`) |
| Forks stay outside towns | on | roads that leave a town the same way share one road and part at a fork further out; roads heading the other way leave the town by a road of their own, on their own side, so no fork lands among the town's houses and no road runs back across the town. A fork the ground moves stops short of the town. Off, every long road of a town shares one way out, as before. **Fixed per world** (`route_forks_outside_towns`) |
| Measure the town that is built | on | where a structure pack can build one of several towns on the same spot (the eleven of [Cobblemon Cities & Structures](https://modrinth.com/mod/cobblemon-cities-structures) share one), the town's size, outline and buildings are read from the one the game builds there, not from the first on the pack's list, which can be another town. Vanilla villages read the same either way, except on the border between two biomes. **Fixed per world** (`route_town_as_built`) |
| Roads go around other towns | on | a road keeps off the buildings and streets of every town on its way that it does not end at, not only the town it enters, also when it cannot reach its own town's street end. Only when there is no way around does it cross one, by the shortest way out. Off, a town a road only passes just makes the ground near its centre cost more, and a road can clip the corners of a large town. **Fixed per world** (`route_around_towns`) |
| Roads take the long way around a town | on | before a road is laid over a town on its way, the road planner looks once more for a way around it, however long or steep, with that town's buildings and streets and the 16 blocks around them closed to the road. Only when there is none does the road cross the town. Off, a road crosses a town wherever that costs it less than the way around, as it did up to Routes 2.0.184. Only matters with *Roads go around other towns* on. **Fixed per world** (`route_town_walls`) |
| Roads end on their fork | on | every road of a fork ends on the fork itself, so the roads that part there meet at one point, also where the fork stands over water. Off, each road ends where its own planning grid puts it, up to seven blocks beside the fork, as it did up to Routes 2.0.187: on land the levelled ground of the fork hides that, but over water a bridge could stop beside the others with open water between. **Fixed per world** (`route_fork_ends`) |
| Roads join in front of the street end | on | a road that would head back beside its own town's road, from the fork where that road parts, starts instead in front of the street end the town's road leaves by, at a junction planted there with its fingerposts, so no two roads of a town run side by side. The fork moves to that junction when it stands near it or only one other road leaves it; otherwise it stays, linked to the junction by a road of its own. Where the ground from the street end to the junction is too steep for that short stretch, nothing changes. Off, the fork stays where it is measured from the middle of the town, as it did up to Routes 2.0.189, and a road can run back beside the town's road for a stretch. Only matters with *Roads enter towns by a street end* on. **Fixed per world** (`route_join_at_street_ends`) |
| Bridge ramps meet the road | on | the ramp up to a bridge always reaches the road below at one step, never a wall, even under a high deck: it steepens over its last cells to hand over to the road |
| Ladders on walls at chunk borders | on | a wall of two blocks or more where a road crosses into the next chunk, as on a tunnel ramp, gets a ladder like any other wall. Off, such a wall is laddered only if the planned road already stepped there |
| No slab that leaves a step and a half | on | a slab smooths a one-block rise only where it leaves no step of a block and a half beside it, on the diagonal or into the next chunk; there the rise takes a stair instead |
| No boulders on the road | on | boulders (mossy rocks in old growth taiga) are kept off the road and its edge, as trees already are, so a boulder from the next chunk can no longer land on a road already built or float over it, and the same world builds the same roads whichever chunk generates first |
| Commands clear overhanging trees | on | `/routes road commit` and `/routes debug paint` take the leaves and branches hanging over a road they draw through trees that were already there, on the paving and the column beside it, the way a road in new chunks is cleared. Off: only the space right over the paving is cleared, and the crown of a tree beside the road can stay over its edge. On roads drawn from then on (`route_commit_crowns`) |
| No road hanging under overhangs | on | with terrain mods that build overhangs, like Larion or William Wythers' Overhauled Overworld, a road that cuts down through an overhang, and any road or junction plaza on a thin crust over a cave, has the gap under it filled down to the ground, with the same earth as its embankments, so no road block hangs in the air. Water under the gap is never filled. Off: the cut road is laid at that height with nothing under it. On chunks generated from then on (`route_cut_support`) |
| Roads cut through ore in hills | on | where a road cuts down into a hill, ore buried in the hill is cut away with the rest of it, as a tunnel does, instead of stopping the cut and leaving a wall in the road. Ore showing at the surface is never touched. Off: the cut stops at buried ore. On chunks generated from then on (`route_cut_ores`) |
| Tunnels stay under the roads above them | on | where another road runs over a tunnel, near its mouth or through a low cut, the tunnel is roofed two blocks under that road so the road keeps its ground, instead of the tunnel mouth opening to the sky through it and leaving a wall in that road. A tunnel ramp beside another road also leaves that road's ground alone where it is still only two or three blocks under it, and its steps stop two blocks under the road above (2.0.208). Off: the tunnel clears its full height. On chunks generated from then on (`route_bore_under_roads`, Routes 2.0.207) |
| Roads build the same every time | on | a wild berry tree of Cobblemon standing on a road is cleared like any other plant (Cobblemon spreads the trees of a berry grove differently each time the same world is created, and the road used to stop at each one, so the same spot could be paved in one world and left as grass in the next); a water route that passes under a bridge, or under the platform where roads part (its railing, signposts and piles included), stays open water there, and so does one with a marker stone standing in it, instead of getting loose planks beside them; each of its marker stones is placed once instead of piling up to four high; and a log is told from a wall built of logs without looking at ground two chunks away that may not be generated yet (2.0.205). Off, those four depend on which chunk generates first (`route_same_every_run`) |

The look-and-fit options in that list, from **Steps at tunnel mouths** down, that are not marked
**Fixed per world** only change **chunks generated from now on**: roads already in your world keep their blocks, and the planned routes do not
move. The ones marked **Fixed per world** reshape the planned roads, so they follow the rule
below for settings that shape the network.

### Landmarks

| Option | Default | Notes |
| --- | --- | --- |
| Roads go around landmarks | on | a road steers around a landmark's (or an ignored structure's) real footprint instead of cutting through it; where one fills the only way through, the road is still built |
| Roads pass by one landmark | 3 | 0–10: how strongly a road bends to pass beside the one landmark it visits, a few blocks and never a detour. 0 = off |
| How far a road detours (blocks) | 96 | how far off a road's straight line a landmark can be and still pull it |
| Sign the landmark a road passes | on | a signpost beside the road names the landmark it passes |
| Signposts on grass and snow | on | a signpost can stand where grass, a fern, a flower or a layer of snow lies on the ground: the post takes its place. Leaves, water and anything built are left alone. Off: a spot with a plant or snow on it gets no signpost. It applies to every signpost Routes plants, in chunks drawn from then on (`route_signs_over_plants`) |
| Fork signposts on any bridge deck | on | where a fork's signpost lands on a bridge, the plank under it becomes a cobblestone plinth so the post has ground to stand on, whatever wood the bridge is made of. Off: only oak planks do, and a fork's signpost on a spruce, birch or other bridge is not put up. In chunks drawn from then on (`route_fork_signs_any_deck`) |
| Landmark waypoints | on | the first time you walk past the landmark a road signs, it gets a waypoint on your map, in its own *Landmarks* set. See [Map Integration](map-integration.md) |
| Waystones take the town's name | on | with Waystones or Fabric Waystones installed, a waystone takes the name of its town the first time it is activated or discovered; a name you give it afterwards stays. Off: Routes never renames a waystone. See [Map Integration](map-integration.md#waystones) |
| CCS towns keep their own names | on | a town of [Cobblemon Cities & Structures](https://modrinth.com/mod/cobblemon-cities-structures) is called what that mod calls it (*Pallet Town*, *Viridian City*) instead of a name from Routes' list. Towns that already have a name keep it. Does nothing without that mod (`route_ccs_names`) |
| Repeated town names are numbered by place | on | when several towns share a name (*Cerulean City*, *Cerulean City 2*...), the one nearest the centre of the world (block 0, 0) keeps the bare name and the next nearest is *2*, so every world of the same seed numbers the same town the same. Off: the number follows the order the towns were first named in. Towns that already have a name keep it (`route_stable_town_numbers`) |
| Welcome board beside the road | on | a town's welcome board stands beside the road where it meets the town, off the paving whatever the road's width: on the nearest clear ground of either side, level with the road where there is some. Off: it is tried only two blocks to each side of the road's last block, which on a road five blocks wide is the road itself, so a road that climbs into town in steps gets no board. Affects chunks not generated yet (`route_welcome_beside_road`) |
| Welcome board on piers | on | a town reached by a pier (a town in the sea), or by a bridge that ends at the town, with no ground beside the end of the deck gets its welcome board on top of a post of the railing at the town end, facing out along the deck, so you read it as you walk in from the boat. A town whose board finds ground keeps it there. Off: such a town gets no board. Affects chunks not generated yet (`route_welcome_on_piers`) |
| Blank signs get their text | on | a road sign, welcome board or landmark sign that was left blank (its text is written a moment after the sign is placed, and sometimes never was) gets its text when you come near it, in worlds you already had too. A sign that already reads something, your own words included, is left alone. Landmark signs placed by a version before this one stay as they are. Off: a blank sign stays blank (`route_sign_repair`) |

### Your first steps

| Option | Default | Notes |
| --- | --- | --- |
| Start in a town | on | move a new world's spawn into the nearest town; off leaves the vanilla wilderness spawn. Only a world being created does this: a world you already had keeps its spawn when Routes arrives (`/routes debug spawn` moves it by hand) |
| Prepare the land around spawn | 512 | chunks built in the background the first time you enter, so the roads and towns around spawn are already built when you walk out. The default reaches the spawn town and its first road, about 200 blocks. 0 = off |

### Advanced

Eleven options a first world rarely needs. The section starts closed.

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
| Commands answer from the Overworld | on | Routes builds roads only in the Overworld, so `/routes status` and `/routes list` show the Overworld's towns, routes and areas from the Nether, the End or any other dimension, and `/routes nearest`, `/routes zone` and the zone commands that work where you stand say the roads exist only in the Overworld instead of *Nothing discovered yet*. Off: each command reads the dimension you are in, which outside the Overworld is always empty (`route_commands_overworld`) |
| Status says if roads are on | on | `/routes status`, and every *Nothing discovered yet*, add a line any player can read: `Roads: on for this world · Spawn town: placed`. Roads read **off** when this world was made with roads off; the spawn town reads **none found** when no town near the spawn was usable, and **off** when roads or **Start in a town** are off. Off: the line is left out (`route_status_line`) |

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
    surface before a town, roads enter towns by a street end, measure the town that is built, water
    routes end in a pier, forks stay outside towns, roads go around other towns, roads take the long way
    around a town, roads end on their fork, roads join in front of the street end, the three
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
