# Troubleshooting

Common surprises, what causes them, and what to do. If yours is not here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k): it files the ticket for you.

## The game will not start and names Cobblemon

Ditto HMs needs **Cobblemon 1.8.0 or newer**. On 1.7.x it refuses to load with a dependency error
rather than crashing mid-session. Update Cobblemon. The rest of what to install is in the table at
the bottom of the [home page](index.md#get-it).

## My punches fire an HM

While an HM is selected, a bare-handed click fires it instead of punching or hand-mining. Pick the
**centre** of the [HM Wheel](hm-wheel.md) to clear the selection, or set the activator to **HM Case**
so your fist is never involved.

## Turning on Fly turned off Magnet Rise

On purpose: switching one on switches the other off. Fly is for travelling; Magnet Rise is a slow
hover for building. See [Toggle HMs](abilities/toggles.md).

## An HM I had is gone after updating to 4.0

4.0 cut the mod back to 20 HMs; the rest went to your Pokémon or were retired, and retired HMs no
longer answer any command. Every save is migrated the first time each player joins, so there is
nothing to reset. See [Upgrading to 4.0](upgrading-to-4.md).

## My old config file changed

A config written before 4.0 is brought up to date on load, and only where the meaning of a value
changed. Retired HMs drop out of the file. See [Configuration](configuration.md).
