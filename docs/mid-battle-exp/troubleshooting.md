# Troubleshooting

Common surprises, what causes them, and what to do. If yours is not here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k): it files the ticket for you.

## Players on my server do not see the move screen

The server pays the EXP; the move screen is drawn by the player's own game. A player who joins without
the mod still earns EXP at each knockout, but a move that does not fit stays in the move pool, as it
does in Cobblemon. Install it **on the server and on every player's game**.

## I cannot find `/midbattleexp` or the Summary button

They arrived in 2.1.0. Update the mod on the server and on every player's game: 2.0.0 has no command,
no config file and no Summary button. The extra sources of EXP (Trainer XP, captures, victory
bonus, Pokédex, pasture, gyms, edible candies) and their commands arrived in 2.2.0 and 2.3.0. See
[Commands & Config](commands.md).

## A battle pays more or less EXP than I expected

The amounts are Cobblemon's own, set in Cobblemon's config (`experienceMultiplier`,
`experienceShareMultiplier`, `luckyEggMultiplier`), and any mod that changes how much a battle gives
is respected: its numbers are the ones paid. On top of that, a gym battle pays ×1.5 with PokeGyms
installed, and a won battle against an NPC trainer pays a victory bonus; check
`/midbattleexp` for the server's own settings. See
[The settings that matter](getting-started.md#the-settings-that-matter) and
[More ways to earn](how-it-works.md#more-ways-to-earn).

## I get vanilla XP from battles

That is the Trainer's share (a tenth of your Pokémon's EXP). An operator turns it off with
`/midbattleexp trainerexpshare 0`. With Cobblemon: PlayerXP installed, this mod pays no player XP
from battles.

## A battle against another player pays nothing

That is Cobblemon's `allowExperienceFromPvP` setting.
