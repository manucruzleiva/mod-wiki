# Getting Started

PokeTowns targets **Minecraft 1.21.1** on **Fabric** and **NeoForge**.

## Requirements

| Dependency | Version | Notes |
| --- | --- | --- |
| Minecraft | 1.21.1 | |
| Fabric Loader **or** NeoForge | 0.17.3+ / 21.1+ | Waystones needs Fabric Loader 0.17.3 or newer |
| Fabric API | any | Fabric only |
| Fabric Language Kotlin **or** Kotlin for Forge | any / 5.10+ | the one for your loader |
| Architectury API | any | both loaders |
| [Cobblemon](https://modrinth.com/mod/cobblemon) | **1.8.0 or newer** | Cobblemon 1.7.x is not supported |
| [CobbleDollars](https://modrinth.com/mod/cobbledollars) | any | the Poké Mart sells through it |
| [Waystones](https://modrinth.com/mod/waystones) | any | every Pokémon Center holds a waystone. Waystones brings **Balm** as its own requirement |

Optional: **[Routes](../routes/index.md)** connects PokeTowns settlements to its road network.
**COBBLEVERSE**'s datapack gives gym Towns their Kanto gym leaders (see [Gyms](gyms.md)).

PokeTowns does **not** bundle any of these. If one is missing, the game refuses to start and names
it.

## Steps

1. Install Cobblemon, CobbleDollars and Waystones, with their own requirements.
2. Drop the PokeTowns jar for **your** loader into `mods/`. Never put both loaders' jars in.
3. On a server, install it **on the server and on every player's game**.
4. Create a **new world**. The **PokeTowns** tab on the create-world screen sets how far apart
   settlements are (see [Configuration](configuration.md)).
5. Find a settlement with `/locate structure #minecraft:village`, or explore.

!!! warning "New world recommended"
    Settlements only appear in chunks generated after PokeTowns is installed. In an existing world
    they show up only in land you have not explored yet, and the settlement spacing of an existing
    world is always the default (34 and 8 chunks).
