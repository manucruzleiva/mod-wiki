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
[Getting Started](getting-started.md). To join two towns in land you have already explored, use
[`/routes road`](commands.md#road-a-road-through-land-already-explored).

A world made with the classic generator (Routes 0.77.0 or 1.0.0, or one where the old `use_gen2`
setting was turned off by hand) is no longer supported: the roads already built stay in the world, but
it loses its old map paint, zone banners and town and route names, and new chunks get today's roads
like any other world. Its old towns don't count when you stand in them, because they have no paint; towns in newly
generated land do. Until one does, *Nothing discovered yet* says so in such a world (the **Hint for old
worlds** setting, `route_legacy_hint`, on by default, turns that wording off).

## A town I expected is not connected

Routes only connects the structures it finds in your world, and it decides that per kind of
structure. See [Which Structures Get Roads](which-structures.md). If one still looks wrong, the next
section says what to send.

## `/routes status` says nothing discovered, or my map shows no roads

Nothing in Routes "starts" or runs in the background: roads are built as chunks generate, and a
route is counted the moment its first chunk is drawn. The only progress you see is the spawn
pregeneration, `Loading chunks… x / 512` on the action bar the first time you join. In a new world
with roads on, you spawn inside a town, so `/routes status` is not empty after a few seconds. If it
stays empty, read the line under it, `Roads: … · Spawn town: …`, then check in this order:

1. **Are roads on for this world?** `/routes config get enable_route_generation`. It is chosen in the
   ROUTES tab when the world is created and stored with it; see
   [Configuration](configuration.md#routes-tab).
2. **Are you in the Overworld?** Routes builds roads only there.
3. **Are there towns to connect?** A world generator with no villages, every structure set to
   Ignored, or an allowlist that matches nothing leaves nothing to join. See
   [Which Structures Get Roads](which-structures.md). An operator can list the planned towns with
   `/routes debug towns` (in singleplayer this needs cheats on).
4. **Did you spawn in a town?** If no town near spawn was usable, you start in the wilderness, and
   the nearest road can be outside the area generated so far. Explore, or ask an operator for
   `/routes debug towns`.

On the map, the paint is faint and only covers chunks your map has already seen; see
[Map Integration](map-integration.md#xaeros-minimap). If none of this explains it, these lines of
`latest.log` settle it: `[Routes gen2] ARMED`, `spawn-in-city check: … route generation=`,
`spawn-in-city: exit=`, `feature ALIVE`, `supercell […]: S settlements -> N nodes, E edges` and
`Xaero chunk-paint highlighter registered`. `Common init complete — route generation:` shows the
global setting, not this world's.

## What to paste into a report

For a road that looks wrong: `/routes debug gaps` and, if a bridge or a tunnel is involved,
`/routes debug bridge` or `/routes debug bore`. For a town that should be connected and is not:
`/routes debug towns` and `/routes debug settlements`. For anything slow: `/routes debug chunks` and
`/routes debug workers`. See
[Commands](commands.md).
