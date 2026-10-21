# Settlements

PokeTowns adds three kinds of settlement. Each one grows from a plaza with a Pokémon Center, and the
bigger ones add a Poké Mart and a gym.

| Settlement | Share of settlements | In the plaza | Size |
| --- | --- | --- | --- |
| **Village** | about 2 in 3 | Pokémon Center | streets reach up to 80 blocks from the plaza |
| **Town** | about 1 in 4 | Pokémon Center and Poké Mart, facing each other | two to three times the streets and houses of a Village, up to 96 blocks out |
| **Gym Town** | about 1 in 10 | a Town's plaza, plus a [gym](gyms.md) behind the Center | like a Town |

## Where they appear

Settlements appear in the biomes vanilla villages use: plains and meadows, desert, savanna, snowy
plains and taiga. They are placed on a world-wide grid, about as often as vanilla villages by
default; the [Configuration](configuration.md) page shows how to change that.

The ground under each piece is smoothed as the settlement generates, so buildings sit on the land
rather than float over it.

## What is inside

**Streets.** A crossing at the plaza sends two or three cobbled streets out, and they keep
branching. Lamp posts stand along a Village's streets. A Town's streets leave the plaza both north and south.

**Houses and farms.** Each street has a house on one side and a farm on the other. The houses have
kitchens, bedrooms, attics and workshops, with loot to find in their chests. The farms are vanilla's.

**Villagers.** Vanilla villagers live in the houses, and you trade with them as in any village.

**The plaza.** The [Pokémon Center](center-and-mart.md) is always there; in a Town the
[Poké Mart](center-and-mart.md#the-poke-mart) faces it across the square.

## Finding them

All three count as villages, so anything that looks for villages finds them, Routes included.

| Command | Finds |
| --- | --- |
| `/locate structure #minecraft:village` | the nearest village of any kind, PokeTowns' included |
| `/locate structure cobblemon_poketowns:village` | the nearest PokeTowns Village |
| `/locate structure cobblemon_poketowns:town` | the nearest Town without a gym |
| `/locate structure cobblemon_poketowns:town_gym` | the nearest gym Town |
| `/locate structure #cobblemon_poketowns:has_gym` | the nearest settlement with a gym |

## Known limitations

- On steep ground, streets follow the slope while buildings stay level, so a settlement on a
  hillside can end up with buildings at very different heights.
- The houses, streets, Pokémon Center and Poké Mart are stand-ins from Cobblemon Additions (see
  [Community Credits](credits.md)) until PokeTowns' own buildings replace them.
