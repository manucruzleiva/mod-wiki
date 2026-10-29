# Troubleshooting

Common surprises, what causes them, and what to do. If yours is not here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k): it files the ticket for you.

## The game will not start and names Cobblemon

Cobblemon HMs needs **Cobblemon 1.8.0 or newer**. On 1.7.x it refuses to load with a dependency error
rather than crashing mid-session. Update Cobblemon. The rest of what to install is in the table at
the bottom of the [home page](index.md#get-it).

## Two copies of the mod load, or the game crashes on start after updating

The 4.0 jar is `cobblemon-hms-…`; the old one was `cobblemon-ditto-hms-…`. To the loader they are
different mods, so both load. **Delete the old jar** from `mods/`. See
[Upgrading to 4.0](upgrading-to-4.md#the-new-name).

## My punches fire an HM

While a Pokémon is lending you an HM, a bare-handed click fires it instead of punching. Pick the
lent move again in that Pokémon's wheel to hand it back, or recall the Pokémon. See
[Partner HMs](abilities/active.md).

## A Pokémon does not offer an HM

By default it has to have **learned the move**: one of its four, or one it learned and swapped out.
A move it could learn but never did does not count, unless the server turned *Pokémon must have
learned the move* off. It also has to be yours, sent out, and within 24 blocks, and the HM has to
be enabled on the server.

## My Pokémon refuses to do HMs

Its **friendship ran out**. HMs cost a Pokémon fullness, and once it is empty each point it cannot
pay costs it friendship; at 0 friendship it refuses. Feed it berries (right-click it with any berry)
and raise its friendship again. See [Keeping it fed](pokemon.md#keeping-it-fed).

## There is no Config button on NeoForge

The config screen needs **Cloth Config**, an optional dependency on NeoForge. Install it, or use
`/hms config` instead, which works without it.

## An HM I had is gone after updating to 4.0

In 4.0 you no longer learn HMs: your Pokémon lend them. Every trigger item you paid is handed back
the first time you join, so there is nothing to reset. See [Upgrading to 4.0](upgrading-to-4.md).

## My old config file changed

A config written before 4.0 is brought up to date on load, and only where the meaning of a value
changed. Retired HMs drop out of the file. See [Configuration](configuration.md).
