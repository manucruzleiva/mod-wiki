# Datapack Format

Traders, their offers and the numbers behind tiers are JSON files in a datapack. Each kind lives in
its own folder under `data/<namespace>/poketrades/`:

| Folder | What a file holds |
| --- | --- |
| `traders/` | one trader |
| `pools/` | one pool of offers that traders draw from |
| `categories/` | which category some species fall in |
| `item_values/` | what items are worth, for the tier of item offers |

A file's id is its namespace and path without `.json`:
`data/mypack/poketrades/traders/fisherman.json` is the trader `mypack:fisherman`. The mod's own
files use the `cobblemon_poketrades` namespace; a pack replaces one by shipping a file at the same
path. `/reload` or `/poketrades reload` picks up changes.

!!! tip "A broken file is skipped whole"
    A file loads whole or not at all. Its first bad field is one error line in the server log, naming
    the file and the field (`offers[2].asks[0].min`), and every other file still loads. A field the
    format does not have is only a warning, usually a typo. `/poketrades debug validate` prints every
    problem without reloading.

    Changing a file never changes the offers a trader **already rolled**: those are kept for good.

## Traders

```json
{
  "name": "Trader Wilma",
  "nicknames": ["Abby", "Pip", "Clover"],
  "destination": "discard",
  "offers": ["cobblemon_poketrades:o03"],
  "buckets": [
    { "pool": "common_pfp_t1", "count": 2 },
    { "pool": "uncommon_pfp_t2", "count": 1 }
  ]
}
```

| Field | Required | What it is |
| --- | --- | --- |
| `name` | yes | the name shown on the screen and in chat |
| `nicknames` | no | the names a Pokémon it gives can get, one at random; empty or missing, it keeps its species name |
| `destination` | no | where a Pokémon it receives goes: `discard` (default), `reoffer` or `team` ([Where your Pokémon goes](traders.md#where-your-pokemon-goes)) |
| `reoffer_limit` | no | how many received Pokémon a `reoffer` trader holds at once (1 or more); missing, the server's `reoffer max_held` (6) |
| `offers` | no | fixed offers, each written in full ([Offers](#offers)) or as the id of an offer some pool defines |
| `buckets` | no | each `{ "pool": <pool id>, "count": <1 or more> }`: draw that many offers from that pool |

- A trader needs at least one fixed offer or bucket.
- A pool id without a namespace is a pool of the trader's own namespace.
- A trader never draws the same offer twice, and never draws one it already holds as fixed. Its
  buckets cannot ask a pool for more offers than it has left once the trader's fixed offers and
  earlier buckets are taken out.
- A trader whose bucket names a pool that did not load is skipped too, with its own error line.

To make an NPC trade as this trader, see [Cobblemon NPCs](traders.md#cobblemon-npcs). An RCT trainer
uses the trader `rct/<trainer id>` ([RCT trainers](traders.md#rct-trainers)), and the village trader
is `cobblemon_poketrades:villager`.

## Pools

A pool is a list of offers that share one trade type and one tier, so a trader can say "two common
swaps" without naming them.

```json
{
  "category": "common",
  "type": "pokemon_for_pokemon",
  "tier": 1,
  "offers": [
    {
      "id": "mypack:wooper_for_psyduck",
      "gives": "wooper level=12",
      "asks": [{ "condition": "species", "species": "psyduck" }]
    }
  ]
}
```

| Field | Required | What it is |
| --- | --- | --- |
| `type` | yes | the [offer type](#offer-types) of every offer in it |
| `category` | no | the [category](#categories) its offers trade: `common`, `uncommon`, `rare`, `baby`, `fossil`, `starter`, `paradox`, `ultra_beast`, `legendary`, `mythical` |
| `tier` | no | 1 to 5; missing, the category's tier. One of the two must be there |
| `offers` | yes | at least one [offer](#offers) |

An offer in a pool takes the pool's type and tier. It may write them again, but only with the same
values.

## Offers

| Field | Required | What it is |
| --- | --- | --- |
| `id` | yes | unique across everything loaded, like `mypack:wooper_for_psyduck` |
| `type` | outside a pool | the [offer type](#offer-types) |
| `tier` | no | 1 to 5; see [How an offer gets its tier](#how-an-offer-gets-its-tier) |
| `gives` | yes | what the trader hands over |
| `asks` | yes | what it takes |

### Offer types

| `type` | `gives` | `asks` |
| --- | --- | --- |
| `pokemon_for_pokemon` | a Pokémon | a Pokémon ask |
| `pokemon_for_items` | a Pokémon | items |
| `pokemon_for_money` | a Pokémon | money |
| `buy_with_items` | items | a Pokémon ask |
| `buy_with_money` | money | a Pokémon ask |

- **A Pokémon** is a Cobblemon Pokémon properties string, as in `/pokegive`, and it **must set a
  level**: `"eevee level=15"`, `"vulpix form=alola level=20 nature=timid"`. Whatever it leaves out
  rolls like a wild Pokémon of that level, except that it is never shiny and comes in a Poké Ball
  unless the string says so (`shiny=yes`, `pokeball=ultra_ball`).
- **Items** is a list of `{ "item": "minecraft:emerald", "count": 8 }`, at least one; `count` is 1 when
  missing. An item counts by id alone.
- **Money** is a whole number, 1 or more, in units of the currency (CobbleDollars): `"gives": 400`.
- **A Pokémon ask** is a list of [conditions](#conditions), at least one.

### Conditions

Each condition is an object with a `condition` field and the fields of that condition. An ask lists
each condition at most once, and a Pokémon must meet all of them. An id without a namespace is
Cobblemon's.

| `condition` | Fields | Example |
| --- | --- | --- |
| `species` | `species` | `{ "condition": "species", "species": "psyduck" }` |
| `form` | `form`, any case | `{ "condition": "form", "form": "alola" }` |
| `gender` | `gender`: `male`, `female` or `genderless` | `{ "condition": "gender", "gender": "female" }` |
| `nature` | `nature`; a mint counts | `{ "condition": "nature", "nature": "timid" }` |
| `ability` | `ability` | `{ "condition": "ability", "ability": "drizzle" }` |
| `ivs` | `min`: the least IV per stat (0 to 31), **or** `perfect`: how many stats at 31 (1 to 6) | `{ "condition": "ivs", "min": { "hp": 31, "speed": 20 } }` |
| `level` | `min`, 1 or more | `{ "condition": "level", "min": 30 }` |
| `shiny` | none | `{ "condition": "shiny" }` |
| `ball` | `ball` | `{ "condition": "ball", "ball": "ultra_ball" }` |

The stats of `ivs` are `hp`, `attack`, `defence`, `special_attack`, `special_defence` and `speed`. A
Bottle Cap counts. Other mods add conditions under their own namespace
([For Mod Authors](api.md#ask-conditions)).

### How an offer gets its tier

The first of these that applies:

1. the offer's own `tier`;
2. its pool's `tier` (or its pool's category's);
3. for an item offer, what its items are worth ([Item values](#item-values)); if one of them has no
   value, the offer must set its tier, or it fails;
4. for a money offer, its price ([the price bands](traders.md#tiers));
5. for a fixed Pokémon-for-Pokémon offer, the category of the species it gives, worked out when the
   trader rolls.

The [tier tables](traders.md#tiers) guide balance; they do not bind it. A Pokémon-for-Pokémon ask
that does not fit its tier, items worth another tier's band, or a price in another band, is a
warning, and the offer loads anyway.

## Categories

Every species already has a category, from its Cobblemon labels or its catch rate
([Tiers](traders.md#tiers)). A file in `categories/` sets it by hand:

```json
{
  "species": {
    "eevee": "rare",
    "othermod:fluffle": "legendary"
  }
}
```

A species without a namespace is Cobblemon's. Files are read in id order, and when two set the same
species, the first one keeps it and the second gets a warning.

## Item values

What items are worth, in emeralds, for the tier of item offers:

```json
{
  "values": {
    "minecraft:emerald": 1,
    "cobblemon:fire_stone": 12,
    "cobblemon:master_ball": 250
  }
}
```

An item without a namespace is Minecraft's, and a value is a whole number, 0 or more. The mod ships
values for 37 items (Poké Balls, evolution stones, held items, the Master Ball…) in
`cobblemon_poketrades:default`. Any other pack's value for the same item replaces the mod's.
