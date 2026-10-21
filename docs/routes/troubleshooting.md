# Troubleshooting

Common surprises, what causes them, and what to do. If yours is not here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k): it files the ticket for you.

## The game will not start and names a mod

Routes needs Architectury API and Cloth Config on both loaders, and Fabric API on Fabric. The loader
names the one that is missing. The full list is in the table at the bottom of the
[home page](index.md#get-it).

## I changed a setting and the roads did not change

Anything about the shape of the network (how many roads leave a town, how long they may be, how
steep, how wide) decides what gets **built**. It applies to ground that has not generated yet, and
never rebuilds what is already there. Each option says so in [Configuration](configuration.md).

## Routes in a world I already had

Route rules are chosen when the world is created and stored with it, and the road network is laid
out as the world generates. A **new world** gives you the intended experience; see
[Getting Started](getting-started.md).

## A town I expected is not connected

Routes only connects the structures it finds in your world, and it decides that per kind of
structure. See [Which Structures Get Roads](which-structures.md). If one still looks wrong, the next
section says what to send.

## What to paste into a report

For a road that looks wrong: `/routes debug gaps` and, if a bridge is involved, `/routes debug bridge`.
For a town that should be connected and is not: `/routes debug structures` and
`/routes debug settlements`. For anything slow: `/routes debug chunks`. See
[Commands](commands.md).
