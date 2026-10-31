# Settlements

PokeTowns adds four kinds of settlement. Each one grows from a plaza with a Pokémon Center, and the
bigger ones add a Poké Mart, a stadium and a gym.

| Settlement | Share of settlements | In the plaza | Size |
| --- | --- | --- | --- |
| **Village** | about 6 in 10 | Pokémon Center | streets reach up to 80 blocks from the plaza |
| **Town** | about 2 in 10 | Pokémon Center and Poké Mart, facing each other, with fountains or statues | two to three times the streets and houses of a Village, up to 96 blocks out |
| **Gym Town** | about 1 in 10 | a Town's plaza, plus a [gym](gyms.md) behind the Center | like a Town |
| **City** | about 1 in 10 | a gym Town's plaza: Center, Mart, gym, stadium and decorations, every time | like a Town, but every lot holds a building |

## Where they appear

Settlements appear in the biomes vanilla villages use: plains and meadows, desert, savanna, snowy
plains and taiga. They are placed on a world-wide grid, about as often as vanilla villages by
default; the [Configuration](configuration.md) page shows how to change that.

**Only on level ground.** Before a settlement grows, it looks at the ground around its plaza and
gives the spot up if the land rises or falls more than six blocks, so no settlement is stacked up a
hillside.

**Clear of other structures.** A settlement does not start within five chunks of a spot where
another surface structure would start, so it never cuts through one.

The ground under each piece is filled in and cut back as the settlement generates, so buildings and
streets sit on the land rather than float over it or dig into it.

## What is inside

**Streets.** A crossing at the plaza sends two or three cobbled streets out, and they keep
branching. Streets stay level with the plaza instead of following the slope, and the ground under
them is levelled. Lamp posts stand along a Village's streets. A Town's streets are **five blocks
wide** and leave the plaza both north and south.

**Houses and farms.** Each street has a house on one side and a farm on the other. The houses have
kitchens, bedrooms, attics and workshops, with loot to find in their chests. The farms are vanilla's.
A City grows no farms: every lot along its streets holds a building.

**Berry nurseries.** Most Towns have one or two among their farms: a covered planter by the street
with eight grown Cobblemon berry trees, drawn from Cobblemon's berries and mints, rare ones included.
Right-click a tree to pick its berries; it grows back like any planted tree.

**Villagers.** Vanilla villagers live in the houses, and you trade with them as in any village.

**The plaza.** The [Pokémon Center](center-and-mart.md) is always there; in a Town or City the
[Poké Mart](center-and-mart.md#the-poke-mart) faces it across the square, with a
[stadium](center-and-mart.md#the-stadium) behind the Mart.

**Fountains and statues.** Every Town's square holds two decorations, one in each half of the
square between the Mart and the Center, clear of the path between their doors. Each is a fountain
(a stone basin whose water stays in it), a roofed well or a Poké Ball statue on a pedestal. Now and
then another stands beside a Town street.

## Finding them

All four count as villages, so anything that looks for villages finds them, Routes included.

| Command | Finds |
| --- | --- |
| `/locate structure #minecraft:village` | the nearest village of any kind, PokeTowns' included |
| `/locate structure cobblemon_poketowns:village` | the nearest PokeTowns Village |
| `/locate structure cobblemon_poketowns:town` | the nearest Town without a gym |
| `/locate structure cobblemon_poketowns:town_gym` | the nearest gym Town |
| `/locate structure cobblemon_poketowns:city` | the nearest City |
| `/locate structure #cobblemon_poketowns:has_gym` | the nearest settlement with a gym, gym Town or City |

## Known limitations

- The houses, streets, Pokémon Center, Poké Mart, stadium, wells and berry planters are stand-ins
  from Cobblemon Additions (see [Community Credits](credits.md)) until PokeTowns' own buildings
  replace them.
