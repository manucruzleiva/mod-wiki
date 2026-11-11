# Troubleshooting

Common surprises, what causes them, and what to do. If yours is not here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k): it files the ticket for you.

## The mod does not load

Defeated Catch Chance needs **Cobblemon 1.8 or newer**. On 1.7.x it refuses to load with a dependency
error. Check too that you put in the jar for **your** loader, and its Kotlin and Architectury
libraries. See [Getting Started](getting-started.md#requirements).

## A beaten Pokémon still vanishes

- **Did a player win?** The window opens only for a wild Pokémon beaten in a battle a player won.
- **Is it switched on?** Check `/dcc config window`: with `enabled` off, beaten Pokémon vanish as in plain
  Cobblemon.
- **Is Cobblemon Nuzlocke installed?** While Nuzlocke has its own copy of this feature this mod stands
  down, and the server log says so. The window you see is then Nuzlocke's, with Nuzlocke's rules.

## The window is shorter or longer than 60 seconds

It follows `window.window_seconds`, and the message above the hotbar says the exact number. The countdown
starts when the Pokémon lies down, after the battle, not at the knockout. See
[Commands & Config](commands.md).

## My ball did nothing on a Pokémon that was running

That is the rule: a missed ball wakes the Pokémon, and from then on balls thrown at it catch nothing.
Switch the flee off with `/dcc config flee enabled false` if you would rather it just vanish.

## My config changes do not stick

If the config file is not valid JSON the mod keeps it untouched and runs on the defaults, so nothing is
saved. The log has a warning with the file's path. Fix the file and restart.

## I want a Pokémon to stay down longer

Raise `window.window_seconds` (up to 3,600). Anything longer is not supported.
