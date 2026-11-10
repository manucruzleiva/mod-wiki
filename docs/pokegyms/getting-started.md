# Getting Started

PokeGyms targets **Minecraft 1.21.1** on **Fabric** and **NeoForge**, with **Cobblemon 1.8**. It is
made for multiplayer servers, and it goes on the server **and** on every player's game.

## Requirements

| Dependency | Notes |
| --- | --- |
| Minecraft 1.21.1 | |
| Fabric Loader 0.18.0+ **or** NeoForge | the jar for your loader |
| Fabric Language Kotlin **or** Kotlin for Forge | the one for your loader |
| Architectury API | both loaders |
| [Cobblemon](https://modrinth.com/mod/cobblemon) 1.8.0+ | 1.7.x is not supported |
| [CobbleDollars](https://modrinth.com/mod/cobbledollars) 2.0.0+ | the currency licences are paid in |
| [Radical Cobblemon Trainers](https://modrinth.com/mod/radical-cobblemon-trainers) 0.19.2-beta+ | with its **RCT API** 0.16.2-beta+ |
| [Cobblemon Cities & Structures](https://modrinth.com/mod/cobblemon-cities-structures) | the cities whose gyms PokeGyms runs |

PokeGyms starts without Cities & Structures, but then it finds **no gyms** and does nothing. With an
older version of any of the others, the game refuses to start and names the mod and the version it
needs.

## Steps

1. Install Cobblemon, CobbleDollars, Radical Cobblemon Trainers with RCT API, Cobblemon Cities &
   Structures and the libraries for your loader.
2. Drop the PokeGyms jar for **your** loader into `mods/`, on the server and on every player's game.
   Never put both loaders' jars in.
3. Start the server. Existing worlds work: a city generated before PokeGyms was installed has its gym
   found the first time it loads.
4. Walk into the gym of a Cities & Structures Kanto city. The **Gym Manager** lectern stands just
   inside the door; right-click it.

An operator can list every gym the server has found in the current dimension with `/pokegyms gyms`
([Commands](commands.md#pokegyms-gyms)).
