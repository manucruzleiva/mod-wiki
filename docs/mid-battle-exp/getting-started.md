# Getting Started

Install the jar for your loader and you are done. There is no config file, no command and nothing to
unlock: the next battle you fight already pays at each knockout.

## Installing

1. Install [Cobblemon](https://modrinth.com/mod/cobblemon)
   ([CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemon)) 1.7 or 1.8, with
   **Architectury API** and the Kotlin library for your loader: **Fabric Language Kotlin** on Fabric,
   **Kotlin for Forge** on NeoForge.
2. Drop the Mid-Battle EXP jar for your loader into `mods/`.

On a server, install it **on the server and on every player's game**. The server pays the EXP; the
move screen is drawn by the player's own game. A player who joins without it still earns EXP at each
knockout, but never sees the move screen: a move that does not fit stays in the move pool, as it
does in Cobblemon.

## Your first battle

Fight anything — a wild Pokémon, a trainer or another player. The moment an opponent faints:

- the EXP bar of every Pokémon that fought it fills up, and an Exp. Share holder on the bench gets its
  share;
- a Pokémon that levels up shows its new level and HP on its battle bar;
- the battle log tells you what each of your Pokémon gained.

Everything that happens, and why, is on [How it works](how-it-works.md).

## The settings that matter

In 2.0.0 the mod has none of its own. The ones that shape it are **Cobblemon's**, in Cobblemon's
config, and they work exactly as they always have:

| Cobblemon setting | What it changes here |
|---|---|
| `experienceMultiplier` | how much EXP each knockout pays |
| `experienceShareMultiplier` | the share an Exp. Share holder gets of each knockout |
| `luckyEggMultiplier` | the extra EXP a Lucky Egg holder gets of each knockout |
| `allowExperienceFromPvP` | whether a battle against another player pays at all |
| `awardExperienceToFaintedPokemon` | whether a Pokémon that has fainted still earns (Cobblemon 1.8 only) |

From the next release the server has its own EXP multiplier, Exp. Share portion and global Exp.
Share on top of these, set with `/midbattleexp`, and each Pokémon's Summary has a button that pauses
its EXP: see [Commands & Config](commands.md).
