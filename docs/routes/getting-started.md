# Getting Started

Routes runs on **Minecraft 1.21.1 to 1.21.11 and 26.1 to 26.3**, on **Fabric** and **NeoForge**.

<div class="flow" markdown>

1. <span class="flow__tag">1</span> Download the jar for **your** loader and Minecraft version
2. <span class="flow__tag">2</span> Drop it into `mods/`
3. <span class="flow__tag">3</span> Launch the game
4. <span class="flow__tag flow__tag--result">4</span> Create a new world and open the **ROUTES** tab

</div>

## Requirements

| Dependency | Notes |
| --- | --- |
| Minecraft | 1.21.1–1.21.11 or 26.1–26.3, each with its own jar |
| Java | 21 for 1.21.x, 25 for 26.x |
| Fabric Loader **or** NeoForge | the one your Minecraft version uses |
| Fabric API | Fabric only |
| Architectury API | both loaders |
| Cloth Config | bundles AutoConfig |

Optional but integrated: **Waystones**, **Fabric Waystones**, **Xaero's Minimap / World Map**,
**JourneyMap**, **[Cobblemon PokeTowns](../poketowns/index.md)** and
**[Cobblemon Picnic](../picnic/index.md)** — see [Map Integration](map-integration.md).

The mod does **not** bundle these — install them alongside it.

## Steps

1. Download the version matching your loader **and your Minecraft version** from
   [Modrinth](https://modrinth.com/mod/routes) or [CurseForge](https://www.curseforge.com/projects/1584243).
   The file names say both: `routes-fabric-2.0.85+1.21.1.jar` is the Fabric jar for 1.21.1. One jar
   covers a group of versions and is named after the newest of them: `+1.21.3` runs on 1.21.2 and
   1.21.3, `+1.21.8` on 1.21.6 to 1.21.8, `+1.21.10` on 1.21.9 and 1.21.10, `+26.1.2` on 26.1 to 26.1.2.
2. Drop the jar into your profile's `mods/` folder.
3. Make sure only **one** `routes-*.jar` is present (remove older ones first).
4. Launch. Create a new world and look for the **ROUTES** tab on the create-world screen.

!!! warning "New save recommended"
    Route rules are chosen at world creation and stored per world, and the road network is laid out
    as the world generates. Starting a fresh world gives you the intended experience.

!!! info "Updating a world from Minecraft 1.21.x to 26.1 or newer"
    Minecraft 26.1 moves a world's saved data into a new folder. Routes picks up its own files from the
    old place on the first start, so the roads, the map paint, the zones and the world's rules come
    along.
