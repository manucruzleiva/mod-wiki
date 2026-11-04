# Pokémon Center & Poké Mart

Every settlement has a Pokémon Center in its plaza. Every Town and City also has a Poké Mart across
the square, with a stadium behind it.

## The Pokémon Center

| What | How it works |
| --- | --- |
| Healing machines | heal your team for **free**, as Cobblemon's healing machine always does |
| PC | Cobblemon's PC, to reach your boxes |
| Waystone | a Waystones village waystone, its own in every Center. The first time someone activates it, it gets a generated name; with [Routes](../routes/index.md) installed, it takes the settlement's name |
| Nurse Joy | stands behind the counter between the healing machines. She can't be hurt, never despawns and has nothing to trade: she is there for the look |
| Champions Trainer | with [Champions Training](../champions/champions-trainer.md) installed, a trainer stands beside the counter. Talk to it to change your Pokémon's stat points, nature, ability and moves |
| Berry garden | thirteen beds under the apricorn tree out back, each with a grown Cobblemon berry tree you can pick. It grows back like any planted tree |
| Loot | the Center's chests, barrels and pots hold Poké Balls, apricorns, food and medicine |

The Center sells nothing.

## The Poké Mart

The Poké Mart sells everyday supplies for **CobbleDollars**. Prices are in CobbleDollars; Poké Ball
prices match CobbleDollars' own default shop.

A **Poké Mart Clerk** stands behind the counter. Right-click the clerk to open the Mart's shop;
sneak and right-click to sell emeralds at CobbleDollars' usual rate. The clerk is CobbleDollars' own
merchant: it never moves, takes no damage and stays through restarts.

=== "Poké Balls"

    | Item | Price |
    | --- | ---: |
    | Poké Ball | 2,000 |
    | Citrine, Verdant, Azure, Roseate and Slate Ball | 2,000 each |
    | Premier Ball | 2,000 |
    | Great Ball | 6,000 |
    | Ultra Ball | 8,000 |

=== "Medicine"

    | Item | Price |
    | --- | ---: |
    | Potion | 2,000 |
    | Super Potion | 7,000 |
    | Antidote | 2,000 |
    | Paralyze Heal | 3,000 |
    | Burn Heal | 3,000 |
    | Ice Heal | 1,000 |
    | Awakening | 1,000 |

=== "Battle Items"

    | Item | Price |
    | --- | ---: |
    | X Attack, X Defense, X Sp. Atk, X Sp. Def, X Speed, X Accuracy | 10,000 each |
    | Dire Hit | 10,000 |
    | Guard Spec. | 15,000 |

Stronger medicine and held items are left to specialised shops.

A datapack can replace the whole shop by overriding its id, `cobblemon_poketowns:poke_mart` (see
[For Pack Authors](pack-authors.md)).

## The stadium

Every Town and City has a stadium on the grass west of the Poké Mart, level with the plaza: an
open-air arena for battles between players. You walk in through the middle aisle between its
stands. It is decoration only, with nothing to run it.
