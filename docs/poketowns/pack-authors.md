# For Pack Authors

PokeTowns' settlements are data: structures, template pools, tags and a shop, all in the
`cobblemon_poketowns` namespace. This page lists the ids other datapacks and mods can rely on.

## Structures and tags

| Id | Kind | What it is |
| --- | --- | --- |
| `cobblemon_poketowns:village` | structure | the Village |
| `cobblemon_poketowns:town` | structure | the Town without a gym |
| `cobblemon_poketowns:town_gym` | structure | the gym Town |
| `cobblemon_poketowns:city` | structure | the City |
| `cobblemon_poketowns:settlements` | structure set | all four, at weights 60, 21, 9 and 10 |
| `#minecraft:village` | structure tag | PokeTowns adds its four structures, so anything that looks for villages finds them |
| `#cobblemon_poketowns:has_gym` | structure tag | every settlement with a gym: `town_gym` and `city` |
| `#routes:settlement/village`, `/town`, `/city` | structure tags | which archetype each structure is, for Routes: `village`; `town` and `town_gym`; `city` |
| `#cobblemon_poketowns:has_structure/settlement` | biome tag | where settlements may start. It pulls in vanilla's five `has_structure/village_*` tags; add a biome here to let settlements spawn in it |

## Placement

The `settlements` set uses the placement type `cobblemon_poketowns:world_spread`. It is vanilla's
`random_spread` in every way (`/locate`, explorer maps and Routes treat it as one), except that its
spacing and separation come from the world, as chosen on the PokeTowns tab, and not from the JSON.
A datapack that overrides the set keeps the per-world values as long as it keeps this placement type.

It also takes a `clearance` field, in chunks (5 in PokeTowns' set): a settlement does not start within
that many chunks of a chunk where another surface structure, from any random-spread set, would start
in a biome it accepts. `0` turns the check off.

## Level sites

The four structures use the type `cobblemon_poketowns:level_site`: a vanilla `jigsaw` structure with
two more fields. Before it plans, it samples the surface within `site_radius` blocks of the start
(32 for the Village, 48 for the others) and gives the start up when the ground rises or falls more
than `max_site_rise` blocks (6). Streets, crossings and street ends are `rigid`, and every structure
uses `terrain_adaptation: beard_box`, so the street network stays level with the plaza.

Every street end has an open `routes:city_exit` jigsaw on its outer edge, facing out, with the pool
`minecraft:empty`: nothing docks to it, and Routes reads it as the place where a road enters.

## Gyms

- Every gym piece's template id starts with `cobblemon_poketowns:gym/`. A mod can tell it is inside a
  gym by that prefix.
- Gym Towns and Cities pick from the pool `cobblemon_poketowns:town/gyms`. When none of its gyms can be placed,
  the pool falls back to `cobblemon_poketowns:town/gym_fallback`, the battle pad.
- Every gym piece holds eight named data markers, each with the way its NPC faces, for gym mods to
  read: `pokegyms:manager`, `pokegyms:leader`, `pokegyms:disciple_1` to `pokegyms:disciple_3`,
  `pokegyms:challenger`, `pokegyms:leader_pokemon` and `pokegyms:challenger_pokemon`. The challenger
  and the two Pokémon marks face the leader along the arena.

## Docking another pack's building

`cobblemon_poketowns:docked` is a template pool element that places a building from **another**
datapack without copying it. It is how the COBBLEVERSE gyms get into gym Towns.

```json
{
  "element_type": "cobblemon_poketowns:docked",
  "location": "cobblemon_poketowns:gym/cobbleverse/brock",
  "building": "cobbleverse:brock",
  "processors": "minecraft:empty",
  "projection": "rigid"
}
```

| Field | Meaning |
| --- | --- |
| `location` | the anchor: a template the building's size that holds the jigsaw that docks it and the path out of its door |
| `building` | the other pack's template, read by id. It is placed first, at the same origin and rotation as the anchor |
| `processors`, `projection` | as in a vanilla `single_pool_element` |

If the `building` template is not installed, the element offers no jigsaw, so generation moves on
to the next element and then to the pool's fallback. A missing building is never an error.

## The Poké Mart's shop

The Mart's stock is a CobbleDollars datapack shop with the id `cobblemon_poketowns:poke_mart`, at
`data/cobblemon_poketowns/cobbledollars/shop/poke_mart.json`. A datapack that ships a file at the
same path replaces the whole shop.

## Vanilla villages

The built-in pack **PokeTowns: Replace Vanilla Villages** overrides only `minecraft:villages`, the
vanilla village structure set, and leaves it empty. Villages that other mods add in their own sets
keep generating. See [Configuration](configuration.md#vanilla-villages) to turn it off.
