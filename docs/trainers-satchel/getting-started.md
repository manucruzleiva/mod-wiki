# Getting Started

The Trainer's Satchel targets **Minecraft 1.21.1** on **Fabric** and **NeoForge**, with
**Cobblemon 1.8**. It goes on the server **and** on every player's game.

## Requirements

| Dependency | Notes |
| --- | --- |
| Minecraft 1.21.1 | |
| Fabric Loader **or** NeoForge | the jar for your loader |
| Fabric API | Fabric only |
| Fabric Language Kotlin **or** Kotlin for Forge | the one for your loader |
| Architectury API | both loaders |
| [Cobblemon](https://modrinth.com/mod/cobblemon) 1.8.0+ | 1.7.x is not supported |
| [Accessories](https://modrinth.com/mod/accessories) 1.1.0-beta.54+ | the back slot the satchel is worn in |

Optional: [PokeBelt](https://modrinth.com/mod/pokebelt-cobblemon) (Fabric only), so the satchel can
[refill the belt's balls](in-the-field.md#pokebelt-refill), and
[Cobblemon Action Combat](../action-combat/index.md), whose real-time fights the
[battle lock](in-the-field.md#in-a-battle) follows too. With
[Cobblemon Nuzlocke](../nuzlocke/index.md), players in one Soul Link
[share their PC item storage](pc-storage.md#soul-link-one-storage-for-the-team).

With an older version of a required mod the game refuses to start and names the mod and the version
it needs.

## Steps

1. Install Cobblemon, Accessories and the libraries for your loader.
2. Drop the Trainer's Satchel jar for **your** loader into `mods/`, on the server and on every player's
   game. Never put both loaders' jars in.
3. Craft the **Canvas Satchel**: string, wool and leather ([Tiers](tiers.md)).
4. Right-click it to open the seven pockets, or wear it in the Accessories **back** slot.

Nothing is ever picked up into the satchel on its own: you put items in, by shift-clicking them from
your inventory or by dropping them on a pocket's slots ([Pockets & Rules](pockets.md)).
