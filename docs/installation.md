# Installation

Cobblemon Routes targets **Minecraft 1.21.1** on **Fabric**, alongside **Cobblemon** and its deps.

## Requirements

| Dependency | Notes |
| --- | --- |
| Minecraft | 1.21.1 |
| Fabric Loader | 0.16.x+ |
| Fabric API | matched to the pack (e.g. `0.116.10+1.21.1`) |
| Cobblemon | 1.7.3+1.21.1 |
| Cloth Config | bundles AutoConfig (already in the pack) |
| Fabric Language Kotlin | required by Cobblemon (already in the pack) |

The mod does **not** bundle these — they're expected to be present in your Cobblemon installation.

## Steps

1. Download `cobblemon_routes-<version>.jar` from the releases (Modrinth / CurseForge once published, or
   the GitHub builds).
2. Drop it into your profile's `mods/` folder.
3. Make sure only **one** `cobblemon_routes-*.jar` is present (remove older ones first).
4. Launch. Create a new world to see the **NUZLOCKE** and **ROUTES** tabs on the create-world screen.

!!! warning "New save recommended"
    The Nuzlocke and route rules are chosen at world creation and stored per world. Starting a fresh
    world gives you the intended experience.

## Building from source

```bash
./gradlew build      # jar lands in build/libs/cobblemon_routes-<version>.jar
```

Use the Gradle **wrapper** (it pins the supported Gradle version).
