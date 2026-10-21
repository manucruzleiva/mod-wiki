# Pokémon Center & Poké Mart

Every settlement has a Pokémon Center in its plaza. Every Town also has a Poké Mart across the square.

## The Pokémon Center

| What | How it works |
| --- | --- |
| Healing machines | heal your team for **free**, as Cobblemon's healing machine always does |
| PC | Cobblemon's PC, to reach your boxes |
| Waystone | a Waystones waystone. The first time someone activates it, it gets a generated name; with [Routes](../routes/index.md) installed, it takes the settlement's name |
| Nurse Joy | stands behind the counter between the healing machines. She can't be hurt, never despawns and has nothing to trade: she is there for the look |
| Loot | the Center's chests, barrels and pots hold Poké Balls, apricorns, food and medicine |

The Center sells nothing.

## The Poké Mart

The Poké Mart sells everyday supplies for **CobbleDollars**. Prices are in CobbleDollars; Poké Ball
prices match CobbleDollars' own default shop.

!!! warning "No clerk yet"
    In this build the Mart's building stands in every Town, but no clerk stands behind its counter,
    so its shop cannot be opened from the Mart yet.

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
