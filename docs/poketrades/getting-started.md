# Getting Started

PokeTrades targets **Minecraft 1.21.1** on **Fabric** and **NeoForge**, with **Cobblemon 1.8**.
Cobblemon 1.7.x is not supported.

## Requirements

| Dependency | Notes |
| --- | --- |
| Minecraft 1.21.1 | |
| Fabric Loader **or** NeoForge | the jar for your loader |
| Fabric Language Kotlin **or** Kotlin for Forge | the one for your loader |
| Architectury API | both loaders |
| [Cobblemon](https://modrinth.com/mod/cobblemon) 1.8 | |

Optional, each adding something when it is there:

- **[CobbleDollars](https://modrinth.com/mod/cobbledollars)**: traders sell Pokémon for
  CobbleDollars and buy yours ([Offer types](traders.md#offer-types)). Without it, money offers stay
  off every trader.
- **[Radical Cobblemon Trainers](https://modrinth.com/mod/radical-cobblemon-trainers)**: a trainer you
  beat trades with you, and what you give it joins its team ([RCT trainers](traders.md#rct-trainers)).
- **[Cobblemon Action Combat](../action-combat/index.md)** 0.1.48 or newer: trades, purchases and
  sales are refused during its real-time fights, as they are during a Cobblemon battle. Without it
  nothing changes.

## Steps

1. Install Cobblemon and the libraries for your loader.
2. Drop the PokeTrades jar for **your** loader into `mods/`. Never put both loaders' jars in.
3. On a server, install it **on the server and on every player's game**. A trader's NPC data is sent
   to each client, and a client without the mod cannot join.
4. Find a trader. Out of the box that is a villager working at a Cobblemon PC in a village, or one
   of the sample traders an operator places with `/poketrades spawn`.
5. Right-click it: the trade screen opens.

!!! danger "Removing the mod"
    Taking PokeTrades out of a world breaks every NPC that still uses its trade interaction:
    Cobblemon cannot read it back. Remove those NPCs first (`/poketrades remove`).

## The sample traders

Four traders ship with the mod. An operator places any of them with `/poketrades spawn <trader>`:

| Trader | Id | Trades |
| --- | --- | --- |
| Trader Wilma | `wilma` | common to rare Pokémon, a money sale and a money purchase |
| Professor Ines | `ines` | starters, fossils, a baby, an item sale and a starter for money; keeps what you give for the next player |
| Keeper Soren | `soren` | legendaries, a mythical, a paradox Pokémon and a legendary for money; tier-5 offers are once for the whole server |
| Trader Bram | `bram` | items and money only, and always buys a shiny Magikarp for a Master Ball; keeps what you give for the next player |

The village trader is a fifth one, `villager`. A modpack replaces or empties any of them with its own
datapack ([Datapack Format](datapacks.md)).
