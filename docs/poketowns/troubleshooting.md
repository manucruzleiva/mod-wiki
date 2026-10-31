# Troubleshooting

Common surprises, what causes them, and what to do. If yours is not here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k): it files the ticket for you.

## The game will not start and names a mod

PokeTowns needs Cobblemon 1.8.0 or newer, CobbleDollars and Waystones, and does not bundle any of
them. If one is missing, the game refuses to start and names it. The full list is in the table at the
bottom of the [home page](index.md#get-it).

## I cannot find any settlement

Settlements only appear in chunks generated after PokeTowns is installed. In an existing world they
show up only in land you have not explored yet. Find one with `/locate structure #minecraft:village`.
See [Getting Started](getting-started.md).

Settlements also only start on level ground and away from other surface structures, so rolling or
crowded land has fewer of them. See [Settlements](settlements.md#where-they-appear).

## My settlement spacing did nothing

The spacing is set on the **PokeTowns** tab when you create a world, saved with it, and never changes
afterwards. A dedicated server, a world created without opening the tab, and a world that existed
before PokeTowns all use the defaults, 34 and 8 chunks. See [Configuration](configuration.md#settlement-spacing).
