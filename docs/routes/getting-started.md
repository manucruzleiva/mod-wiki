# Getting Started

Routes targets **Minecraft 1.21.1** on **Fabric** and **NeoForge**.

```mermaid
flowchart LR
    A[⬇️ Download the jar<br/>for YOUR loader] --> B[📁 Drop into mods/]
    B --> C[🚀 Launch the game]
    C --> D[🆕 Create a new world<br/>ROUTES tab]
```

## Requirements

| Dependency | Notes |
| --- | --- |
| Minecraft | 1.21.1 |
| Fabric Loader **or** NeoForge | 0.16.x+ / 21.1.x |
| Fabric API | Fabric only |
| Architectury API | both loaders |
| Cloth Config | bundles AutoConfig |

Optional but integrated: **Waystones** and **Xaero's Minimap / World Map** — see
[Map Integration](map-integration.md).

The mod does **not** bundle these — install them alongside it.

## Steps

1. Download the version matching your loader from [Modrinth](https://modrinth.com/mod/routes)
   or [CurseForge](https://www.curseforge.com/projects/1584243) — each release ships
   as `x.y.z+fabric` and `x.y.z+neoforge`.
2. Drop the jar into your profile's `mods/` folder.
3. Make sure only **one** `routes-*.jar` is present (remove older ones first).
4. Launch. Create a new world and look for the **ROUTES** tab on the create-world screen.

!!! warning "New save recommended"
    Route rules are chosen at world creation and stored per world, and the road network is laid out
    as the world generates. Starting a fresh world gives you the intended experience.
