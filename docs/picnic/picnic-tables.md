# Picnic Tables

Picnic Tables are the core block of the mod. Each is a **3×2 multiblock**: the **center column**
holds the **table cells** (re-roll + GUI), and the **side cells** are **benches** you can sit on, up
to the tier's seat cap. Leftover side cells stay empty.

## Tiers

| Tier | Spawn cap | Radius | Seats | Fuel / re-roll | Notes |
|------|:---------:|:------:|:-----:|:--------------:|-------|
| **Basic** | 5 | 32 | 2 | 7 bread | Entry tier |
| **Camping** | 8 | 48 | 3 | 5 bread | Cheaper fuel, bigger |
| **Glamping** | 12 | 64 | 4 | 3 bread | Unlocks the **[Battle Seeker](battle-seeker.md)** slot |
| **Diving** | 12 | 64 | 4 | 3 bread | **Placed underwater only** |

- **Spawn cap** — the maximum Pokémon a single re-roll can spawn (and the GUI slider's max).
- **Radius** — how far around the table wild Pokémon are despawned and re-rolled.
- **Seats** — how many benches the footprint provides (seat counts are **fixed per tier**, not
  configurable).
- **Fuel** — bread consumed per re-roll, on a **7 / 5 / 3 / 3** curve (cheaper as tiers improve).
  Bread comes from the table's fuel slot or from a nearby
  **[Picnic Basket](interactions-and-items.md#picnic-baskets)**. The per-tier cost is configurable
  (`fuelcost <tier>`).

## Crafting

A Picnic Table is built in two steps: craft the **three components**, then assemble them into the
**Basic Picnic Table**. Higher tiers are upgrades of that one.

### 1. The components

Each one comes in every color or wood the table can be built from — the grids below show one
example.

=== "Table"

    The tablecloth piece. Any of the **16 dye colors** of wool, over **oak planks**, gives that
    color's Table (*White Table*, *Red Table*, …).

    <div class="cr-scroll">
    <div class="cr-craft" title="3× Red Wool + 2× Oak Planks → 1× Red Table">
      <div class="cr-grid cr-grid--2row">
        <div class="cr-slot"><img src="../../assets/items/white_wool.png" alt="Wool"></div>
        <div class="cr-slot"><img src="../../assets/items/white_wool.png" alt="Wool"></div>
        <div class="cr-slot"><img src="../../assets/items/white_wool.png" alt="Wool"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_planks.png" alt="Oak Planks"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_planks.png" alt="Oak Planks"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/table_red.png" alt="Table"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/white_wool.png" alt=""> Wool — any of the 16 colors | 3 |
    | <img class="cr-inline" src="../../assets/items/oak_planks.png" alt=""> Oak Planks | 2 |
    | **→ <img class="cr-inline" src="../../assets/items/table_red.png" alt=""> Table** in that color | **1** |

=== "Dining Bench"

    The seat. Slabs and planks of the **same wood** — available in **11 woods**: oak, spruce, birch,
    jungle, acacia, dark oak, mangrove, cherry, bamboo, crimson and warped.

    <div class="cr-scroll">
    <div class="cr-craft" title="3× Oak Slab + 2× Oak Planks → 2× Oak Dining Bench">
      <div class="cr-grid cr-grid--2row">
        <div class="cr-slot"><img src="../../assets/items/oak_slab.png" alt="Oak Slab"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_slab.png" alt="Oak Slab"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_slab.png" alt="Oak Slab"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_planks.png" alt="Oak Planks"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_planks.png" alt="Oak Planks"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/dining_bench_oak.png" alt="Oak Dining Bench"><span class="cr-count">2</span></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/oak_slab.png" alt=""> Slab — any of the 11 woods | 3 |
    | <img class="cr-inline" src="../../assets/items/oak_planks.png" alt=""> Planks of the same wood | 2 |
    | **→ <img class="cr-inline" src="../../assets/items/dining_bench_oak.png" alt=""> Dining Bench** in that wood | **2** |

=== "Picnic Basket"

    Apricorns over apricorn planks, in a 2×2 corner of the grid. One per apricorn color — white,
    black, blue, green, pink, red and yellow.

    <div class="cr-scroll">
    <div class="cr-craft" title="2× Red Apricorn + 2× Apricorn Planks → 1× Red Picnic Basket">
      <div class="cr-grid cr-grid--2row">
        <div class="cr-slot"><img src="../../assets/items/red_apricorn.png" alt="Apricorn"></div>
        <div class="cr-slot"><img src="../../assets/items/red_apricorn.png" alt="Apricorn"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"><img src="../../assets/items/apricorn_planks.png" alt="Apricorn Planks"></div>
        <div class="cr-slot"><img src="../../assets/items/apricorn_planks.png" alt="Apricorn Planks"></div>
        <div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/red_picnic_basket.png" alt="Red Picnic Basket"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/red_apricorn.png" alt=""> Apricorn — any of the 7 colors | 2 |
    | <img class="cr-inline" src="../../assets/items/apricorn_planks.png" alt=""> Apricorn Planks | 2 |
    | **→ <img class="cr-inline" src="../../assets/items/red_picnic_basket.png" alt=""> Picnic Basket** in that color | **1** |

    A basket is also useful on its own, as a
    **[bread store](interactions-and-items.md#picnic-baskets)** next to the table.

### 2. The Basic Picnic Table

<div class="cr-scroll">
<div class="cr-craft" title="Picnic Basket + Nether Star + 2× Table + Campfire Pot + 2× Dining Bench + Campfire → Basic Picnic Table">
  <div class="cr-grid">
    <div class="cr-slot"><img src="../../assets/items/red_picnic_basket.png" alt="Picnic Basket"></div>
    <div class="cr-slot"></div>
    <div class="cr-slot"><img src="../../assets/items/nether_star.png" alt="Nether Star"></div>
    <div class="cr-slot"><img src="../../assets/items/table_red.png" alt="Table"></div>
    <div class="cr-slot"><img src="../../assets/items/table_red.png" alt="Table"></div>
    <div class="cr-slot"><img src="../../assets/items/campfire_pot_red.png" alt="Campfire Pot"></div>
    <div class="cr-slot"><img src="../../assets/items/dining_bench_oak.png" alt="Dining Bench"></div>
    <div class="cr-slot"><img src="../../assets/items/dining_bench_oak.png" alt="Dining Bench"></div>
    <div class="cr-slot"><img src="../../assets/items/campfire.png" alt="Campfire"></div>
  </div>
  <div class="cr-arrow">➜</div>
  <div class="cr-result"><img src="../../assets/items/picnic_table.png" alt="Basic Picnic Table"></div>
</div>
</div>

| Ingredient | Amount | Accepts |
| --- | :---: | --- |
| <img class="cr-inline" src="../../assets/items/red_picnic_basket.png" alt=""> Picnic Basket | 1 | any of the 7 colors |
| <img class="cr-inline" src="../../assets/items/nether_star.png" alt=""> Nether Star | 1 | — |
| <img class="cr-inline" src="../../assets/items/table_red.png" alt=""> Table | 2 | any of the 16 colors — **the left one sets the tablecloth color** |
| <img class="cr-inline" src="../../assets/items/campfire_pot_red.png" alt=""> Campfire Pot | 1 | any Cobblemon Campfire Pot, or Cobblemon's own Campfire |
| <img class="cr-inline" src="../../assets/items/dining_bench_oak.png" alt=""> Dining Bench | 2 | any of the 11 woods — **the left one sets the frame wood** |
| <img class="cr-inline" src="../../assets/items/campfire.png" alt=""> Campfire | 1 | Campfire *or* <img class="cr-inline" src="../../assets/items/soul_campfire.png" alt=""> Soul Campfire |
| **→ <img class="cr-inline" src="../../assets/items/picnic_table.png" alt=""> Basic Picnic Table** | **1** | |

The result renders in that exact **color × wood** combination, using the mod's **own models and
textures** (no other furniture mod required). The basket, pot and campfire are consumed but don't
change how the table looks. Every color/wood variant is also available in the Creative inventory.

### 3. Upgrading

The three higher tiers are **shapeless** — the ingredients can sit anywhere in the grid. An upgrade
**keeps the color and wood** the table was crafted with, so it stays the same style all the way up;
the bench you add is fuel for the recipe, not a new style, and its wood is ignored.

=== "Camping"

    <div class="cr-scroll">
    <div class="cr-craft" title="Shapeless: Basic Picnic Table + Diamond + Dining Bench → Camping Picnic Table">
      <div class="cr-grid cr-grid--2row">
        <div class="cr-slot"><img src="../../assets/items/picnic_table.png" alt="Basic Picnic Table"></div>
        <div class="cr-slot"><img src="../../assets/items/diamond.png" alt="Diamond"></div>
        <div class="cr-slot"><img src="../../assets/items/dining_bench_oak.png" alt="Dining Bench"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/camping_picnic_table.png" alt="Camping Picnic Table"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/picnic_table.png" alt=""> Basic Picnic Table | 1 |
    | <img class="cr-inline" src="../../assets/items/diamond.png" alt=""> Diamond | 1 |
    | <img class="cr-inline" src="../../assets/items/dining_bench_oak.png" alt=""> Dining Bench — any wood | 1 |
    | **→ <img class="cr-inline" src="../../assets/items/camping_picnic_table.png" alt=""> Camping Picnic Table** | **1** |

=== "Glamping"

    <div class="cr-scroll">
    <div class="cr-craft" title="Shapeless: Camping Picnic Table + Netherite Ingot + Dining Bench → Glamping Table">
      <div class="cr-grid cr-grid--2row">
        <div class="cr-slot"><img src="../../assets/items/camping_picnic_table.png" alt="Camping Picnic Table"></div>
        <div class="cr-slot"><img src="../../assets/items/netherite_ingot.png" alt="Netherite Ingot"></div>
        <div class="cr-slot"><img src="../../assets/items/dining_bench_oak.png" alt="Dining Bench"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/glamping_table.png" alt="Glamping Table"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/camping_picnic_table.png" alt=""> Camping Picnic Table | 1 |
    | <img class="cr-inline" src="../../assets/items/netherite_ingot.png" alt=""> Netherite Ingot | 1 |
    | <img class="cr-inline" src="../../assets/items/dining_bench_oak.png" alt=""> Dining Bench — any wood | 1 |
    | **→ <img class="cr-inline" src="../../assets/items/glamping_table.png" alt=""> Glamping Table** | **1** |

=== "Diving"

    <div class="cr-scroll">
    <div class="cr-craft" title="Shapeless: Glamping Table + Heart of the Sea → Diving Picnic Table">
      <div class="cr-grid cr-grid--2row">
        <div class="cr-slot"><img src="../../assets/items/glamping_table.png" alt="Glamping Table"></div>
        <div class="cr-slot"><img src="../../assets/items/heart_of_the_sea.png" alt="Heart of the Sea"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/diving_picnic_table.png" alt="Diving Picnic Table"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/glamping_table.png" alt=""> Glamping Table | 1 |
    | <img class="cr-inline" src="../../assets/items/heart_of_the_sea.png" alt=""> Heart of the Sea | 1 |
    | **→ <img class="cr-inline" src="../../assets/items/diving_picnic_table.png" alt=""> Diving Picnic Table** | **1** |

!!! note "Diving table"
    The **Diving** table can **only be placed underwater**. Try to place it in air and it won't
    deploy.

## Placement & orientation

- The table **deploys in front of you** when you place it, with the **table column centered** on
  where you aim. It orients to your facing — the "wide" axis runs left-to-right relative to you.
- The structure is one block tall. Benches sit on the sides; the center is the functional table.
- **Breaking** any cell breaks the whole structure and returns the table item.

!!! warning "Don't place two tables touching"
    Give each table its own footprint. Overlapping structures can interfere with each other's cells.
