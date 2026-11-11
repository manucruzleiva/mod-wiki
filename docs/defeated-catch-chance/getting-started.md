# Getting Started

Defeated Catch Chance targets **Minecraft 1.21.1** on **Fabric** and **NeoForge**, with
**Cobblemon 1.8**. Cobblemon 1.7.x is not supported: the mod refuses to load on it.

## Requirements

| Dependency | Notes |
| --- | --- |
| Minecraft 1.21.1 | |
| Fabric Loader 0.17.2 or newer, **or** NeoForge 21.1 or newer | the jar for your loader |
| Fabric Language Kotlin **or** Kotlin for Forge | the one for your loader (Kotlin for Forge 5 or newer) |
| Architectury API | both loaders |
| [Cobblemon](https://modrinth.com/mod/cobblemon) 1.8 or newer | |

There are no optional mods to add.

## Steps

1. Install Cobblemon and the libraries for your loader.
2. Drop the Defeated Catch Chance jar for **your** loader into `mods/`. Never put both loaders' jars in.
3. On a server, install it **on the server and on every player's game**: the fade-out of a fleeing
   Pokémon is drawn by the player's own game.
4. Win a battle against a wild Pokémon. It lies down instead of vanishing: throw a ball.

That is the whole setup. The mod writes `config/cobblemon_defeated_catch_chance.json` the first time it
runs; you only touch it to [change the defaults](commands.md).

## With Cobblemon Nuzlocke

[Cobblemon Nuzlocke](../nuzlocke/index.md) carries its own copy of this feature. While that copy is
present, this mod stands down and logs that it did, so the two never run together and never
double a body.
