# Installation

Cobblemon Routes targets **Minecraft 1.21.1** on **Fabric** and **NeoForge**, alongside
**Cobblemon** and its dependencies.

```mermaid
flowchart LR
    A[⬇️ Download the jar<br/>for YOUR loader] --> B[📁 Drop into mods/]
    B --> C[🚀 Launch the game]
    C --> D[🆕 Create a new world<br/>NUZLOCKE + ROUTES tabs]
```

## Requirements

| Dependency | Notes |
| --- | --- |
| Minecraft | 1.21.1 |
| Fabric Loader **or** NeoForge | 0.16.x+ / 21.1.x |
| Fabric API | Fabric only |
| Cobblemon | 1.7.3+1.21.1 |
| Architectury API | both loaders |
| Cloth Config | bundles AutoConfig |
| Fabric Language Kotlin | required by Cobblemon (Fabric) |

Optional but integrated: **Waystones** and **Xaero's Minimap / World Map** — see
[Map Integration](map-integration.md).

The mod does **not** bundle these — they're expected to be present in your Cobblemon installation.

## Steps

1. Download the version matching your loader from [Modrinth](https://modrinth.com/mod/routes)
   or [CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemon-routes) — each release ships
   as `x.y.z+fabric` and `x.y.z+neoforge`.
2. Drop the jar into your profile's `mods/` folder.
3. Make sure only **one** `cobblemon_routes-*.jar` is present (remove older ones first).
4. Launch. Create a new world and look for the **NUZLOCKE** and **ROUTES** tabs on the
   create-world screen.

!!! warning "New save recommended"
    The Nuzlocke and route rules are chosen at world creation and stored per world. Starting a
    fresh world gives you the intended experience.
