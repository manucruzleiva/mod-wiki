# 🗺️ Dynamic Routes

Routes grows a **road network through your world during worldgen** — no commands, no
walking the area first. Cities are found from the world seed, connected with terrain-aware paths,
and every road is signposted and named.

```mermaid
%%{init: {"flowchart": {"curve": "basis", "nodeSpacing": 28, "rankSpacing": 38, "padding": 16}, "themeVariables": {"fontSize": "15px"}}}%%
flowchart TD
    S[🔍 Locate cities from the seed<br/>villages · modpack towns · gym entrances] --> P[🧠 Terrain-aware pathfinding<br/>prefers flat, inland ground]
    P -->|steep mountain in the way| T[⛏️ Bore a mineshaft tunnel<br/>~⅓ are dark caves — bring a torch!]
    P -->|water in the way| W[🌊 Water crossing<br/>bridge deck or open lane between rock markers]
    P --> B[🛤️ Build the road<br/>natural palette + lamp posts]
    T --> B
    W --> B
    B --> G[🪧 Signs at ends & junctions<br/>name · destination · distance]
    G --> N[✨ Route 3: Steep Forest Pass]
```

## What you get

- **Automatic road network** between cities — vanilla villages, modpack villages, the gym entrances
  of the packs [Routes ships a list for](which-structures.md#the-list-routes-ships), and any structure
  you list. Built incrementally and resumed after a restart.
- **Flat & inland paths** — the pathfinder strongly penalises slopes and keeps a buffer away from
  shorelines, while still crossing water when there's no alternative.
- **Mineshaft tunnels** — when a climb is too steep (or there's no surface path at all), the route
  bores a clean, walkable, oak-framed tunnel — twice the road's width and eight blocks tall —
  instead of an impassable cliff. About a third of tunnels are atmospheric **dark caves** — bring
  torches!
- **Descriptive route names** — every road gets a code plus an auto-generated name from the terrain
  it crosses (*Route 5: Coastal Road*, *Route 8: Marsh Crossing*), always the same for your seed.
- **Clean tree clearing** — a road crossing a tree removes the whole trunk and canopy; no floating
  leaves, no item spam.
- **Water crossings** — always on the surface. A river gets a plank bridge with its pillars dropped to
  the riverbed, in one wood from end to end; a longer stretch stays an open lane of water to swim or
  sail, marked on both edges by natural rock markers, most of them lit, and the road meets it at the
  shore's own height. The seabed is never touched, and a frozen lake keeps its ice. Water the planner
  could not see coming (a river carved later by Streams Reflowing, an aquifer pool) is crossed on a
  timber bridge at the banks' height, not left as a swim gap.
- **Climbs you can walk** — where a road rises one or two blocks it steps up in half blocks (slab, full
  block, slab), in the road's own material, so most climbs need no stairs and no jumping. Three or more
  rises in a row keep their stairs. The ramps into a tunnel and onto a bridge follow the same graded
  profile, and a wall that is still two blocks or more gets a ladder.
- **Roads made of what you choose** — the surface can be one material or a mix laid in rounded
  patches, with an optional share of worn blocks (cracked or mossy bricks, gravel in cobblestone, grass
  through a dirt path). Bridge decks and handrails are chosen the same way, one material per bridge and
  per route. Left on *Random*, each stretch takes the palette of the biome it crosses. See
  [Configuration](configuration.md#surface-lighting).
- **Signs everywhere** — directional signs at each end and at junctions (one per road, even at a fork
  right by a chunk border), with plaza-paved crossings that stand out from the road, and a **welcome
  board** with the town's name where a road arrives.
- **Junctions built for the spot** — where two roads cross, the crossing is either a ringed
  **roundabout** around a lit pillar or an open **signed crossing** with fingerposts naming all four
  destinations. Roads that meet at different heights are an **overpass**: the upper one simply bridges
  over. A fork that lands inside a hill opens into a **chamber** where its tunnels meet.
- **Rest stops** — every few hundred blocks, a small camp just off the road: a campfire with log
  seats, a lantern post and a sign. Now and then one keeps a **supply chest** from the last traveller —
  rarely, so finding one still means something. With [Cobblemon Picnic](../picnic/index.md) installed,
  now and then a stop is one of its picnic tables instead — about 3 in 100, set by **Picnic stops**
  in [Configuration](configuration.md).
- **Landmarks along the way** — a road passing a pyramid, a tower or a ruin bends a little to go by
  it, keeps off its footprint, and puts up a signpost with its name. No road is planned *to* a
  landmark — see [Which structures get roads](which-structures.md).
- **Villages, towns and cities** — a settlement's real size decides how many roads leave it, so the
  network has quiet hamlets and busy hubs. A fork out of a big town stands past its last houses, never
  among them. A structure tagged `routes:settlement/village`, `routes:settlement/town` or
  `routes:settlement/city` (as [PokeTowns](../poketowns/index.md) does) gets that word after its name,
  so Pallet becomes *Pallet Town*.
- **Roads meet the town's own streets** — a road joins a town at the open end of a street, at street
  level, never behind a house or climbing into the air. A pack can mark its street ends with an open
  jigsaw named `routes:city_exit` (PokeTowns does), and the road then continues the street that faces
  it most squarely.
- **Spawn in a city** — new worlds start next to the nearest city, on real ground, never in the
  water — coastal towns and PokeTowns towns included.
- **A loading screen that shows the real wait** — while a new world opens, two towns and the road
  between them are the progress bar. Each step (surveying the towns around your spawn, generating the
  spawn chunks, building your spawn town) gets its share of the road by how long it really takes. The
  road's tip only moves while work actually finishes, the line under it counts tasks done, and it says
  *no progress for N s* when nothing has finished for a while.

!!! tip "Tune it per world"
    Roads per city, road width, materials, lighting and more are all set from the **ROUTES**
    tab at world creation — see [World Creation & Config](configuration.md).
