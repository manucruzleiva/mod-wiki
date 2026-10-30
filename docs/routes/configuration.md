# 🧩 World Creation & Config

Everything is decided **when you create the world** — a dedicated **ROUTES** tab sits next to
**GAME / WORLD / MORE** on the create-world screen. Outside world creation there's a global config
screen for defaults.

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
| Generate routes | on | master switch |
| Native route generation | on | roads are drawn as chunks generate — no walking needed. Off falls back to the classic generator that builds as you explore |
| Connect all structures | off | also connect surface structures that are not towns — never one whose id names a ruin, an ancient thing or a mineshaft |
| Routes per city | 4 | a **ceiling**, not a count: each town rolls its own up to this, inside the band its size puts it in — a village low, a city high — so the network has hamlets and crossroads |
| Longest road | 1600 | the farthest two towns can be and still get a direct road |
| Ring roads | on | keep closing loops between nearby towns — loops are what enclose named **areas** |

### Towns & Settlements

| Option | Default | Notes |
| --- | --- | --- |
| Towns & landmarks | automatic | every structure your world has, each set to Settlement, Landmark or Ignored — see [Which structures get roads](which-structures.md) |
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
| Road surface | Random (per route) | each route picks its own material, or fix one for every road |
| Road lamp posts | Random | Random / On / Off — Random decides per route |
| Tunnel lighting | Random | Random keeps some tunnels as dark caves |
| Underwater lighting | Random | a sea lantern in the pillar under each water-crossing marker — Random decides per route |
| Picnic stops | 3 | with [Cobblemon Picnic](../picnic/index.md) installed, the percent of rest stops that are a picnic table instead of a camp. 0 = never, 100 = every stop. Kept per world |

### World Spawn

| Option | Default | Notes |
| --- | --- | --- |
| Spawn in city | on | move a new world's spawn into the nearest town; off leaves the vanilla wilderness spawn |
| Pregenerate around spawn | 512 | chunks built in the background the first time you enter, so the roads and towns around spawn are already built when you walk out — the default reaches the spawn town and its first road, about 200 blocks. 0 = off |

### Map & Notifications

| Option | Default | Notes |
| --- | --- | --- |
| Zone notifications | Toast | how entering a route or an area is announced: Off / Toast / Announcement / Chat |
| Xaero chunk paint | on | tint chunks on [Xaero's maps](map-integration.md) by category. Needs Xaero's Minimap; inert otherwise |

Who stands on the roads and what gets built beside the towns is the Nuzlocke add-on's: **road
trainers**, the **gyms next to towns** and the **league** are configured on its
[NUZLOCKE tab](../nuzlocke/commands.md). Routes on its own builds the towns and the roads
between them.

The map **tint intensity** and **colours** (City / Route / Area) are not world-creation choices —
set them in play with [`/routesmap`](map-integration.md#changing-how-it-looks-routesmap), with the map
in front of you.

!!! info "Saved per world"
    Choices made in these tabs are stored **per world** and only applied to a brand-new world —
    loading an existing world never gets its rules clobbered. Picking **Hardcore** at world
    creation auto-enables the full [Nuzlocke rule set](../nuzlocke/commands.md).

## Global defaults

The global defaults live in `config/routes.json` (English & Spanish labels) and are used
when a world wasn't configured through the tabs. The map-paint intensity and colours are changed in
play with [`/routesmap`](map-integration.md#changing-how-it-looks-routesmap).

## Commands

The root is `/routes`; `/cobblemonroutes …` is accepted as an alias. The full manual — every
command, argument, permission and behaviour — lives on [the Commands page](commands.md).
