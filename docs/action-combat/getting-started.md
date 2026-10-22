# Getting Started

Action Combat targets **Minecraft 1.21.1** on **Fabric** and **NeoForge**, with **Cobblemon 1.8**.

## Requirements

| Dependency | Notes |
| --- | --- |
| Minecraft 1.21.1 | |
| Fabric Loader **or** NeoForge | the jar for your loader |
| Fabric Language Kotlin **or** Kotlin for Forge | the one for your loader |
| Architectury API | both loaders |
| [Cobblemon](https://modrinth.com/mod/cobblemon) 1.8 | |

Optional, each adding something when it is there:

- **[Cobblemon: Mega Showdown](https://modrinth.com/mod/cobblemon-mega-showdown)**: Mega Evolution,
  Terastallization, Dynamax and Z-Moves in a real-time fight ([Battle gimmicks](moves.md#battle-gimmicks)).
- **[PokeBelt](https://modrinth.com/mod/pokebelt-cobblemon)**: the only way to throw a Poké Ball in
  the middle of a fight ([Catching](fights.md#catching)).
- **[Radical Cobblemon Trainers](https://modrinth.com/mod/radical-cobblemon-trainers)**: its trainers
  fight in real time and a win still counts there ([RCT trainers](fights.md#rct-trainers)).
- **Synchro Machine**: a player morphed into a Pokémon keeps the turn-based battle.

## Steps

1. Install Cobblemon and the libraries for your loader.
2. Drop the Action Combat jar for **your** loader into `mods/`. Never put both loaders' jars in.
3. On a server, install it **on the server and on every player's game**. A client without it, or on
   another version, is refused at login with a message saying so.
4. Start a battle the way you always do: throw your Pokémon at a wild one, talk to a trainer, or
   challenge a player. A gold **"Real-time fight!"** line says it is yours to drive.

## Which battles play in real time

The server decides, per kind of battle and per size, with `/cac format`:

```
/cac format wild singles on
/cac format npc doubles off
/cac format pvp singles on
```

A battle the server leaves turn-based opens Cobblemon's normal battle screen. Triples, multi and
free-for-all battles are always turn-based. See [Commands & Configuration](commands.md).
