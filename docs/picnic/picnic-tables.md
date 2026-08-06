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

=== "Table"

    The tablecloth piece — **3 wool + 2 oak planks**. The wool's color is the table's color, so
    there is one for each of the **16 dye colors** (*White Table*, *Red Table*, …).

    | Left | Middle | Right |
    |:--:|:--:|:--:|
    | Wool | Wool | Wool |
    | Oak Planks | *(empty)* | Oak Planks |

    **→ 1 Table** of that color.

=== "Dining Bench"

    The seat — **3 slabs + 2 planks of the same wood**. Available in **11 woods**: oak, spruce,
    birch, jungle, acacia, dark oak, mangrove, cherry, bamboo, crimson and warped.

    | Left | Middle | Right |
    |:--:|:--:|:--:|
    | Slab | Slab | Slab |
    | Planks | *(empty)* | Planks |

    **→ 2 Dining Benches** of that wood.

=== "Picnic Basket"

    **2 apricorns + 2 apricorn planks**, in a 2×2 corner of the grid. One per apricorn color —
    white, black, blue, green, pink, red and yellow.

    | Left | Right |
    |:--:|:--:|
    | Apricorn | Apricorn |
    | Apricorn Planks | Apricorn Planks |

    **→ 1 Picnic Basket** of that color. It's also useful on its own as a
    **[bread store](interactions-and-items.md#picnic-baskets)**.

### 2. The Basic Picnic Table

A full **3×3** recipe:

| Left | Middle | Right |
|:--:|:--:|:--:|
| **Picnic Basket** | *(empty)* | **Nether Star** |
| **Table** | **Table** | **Campfire Pot** |
| **Dining Bench** | **Dining Bench** | **Campfire** |

- **Picnic Basket** — any color.
- **Table** — any two of the 16 colors. The **left** one sets the tablecloth color.
- **Dining Bench** — any two of the 11 woods. The **left** one sets the frame wood.
- **Campfire Pot** — any of Cobblemon's colored **Campfire Pots**, or Cobblemon's own **Campfire**.
- **Campfire** — vanilla **Campfire** *or* **Soul Campfire**.

The result renders in that exact **color × wood** combination, using the mod's **own models and
textures** (no other furniture mod required). The basket, pot and campfire are consumed but don't
change how the table looks. Every color/wood variant is also available in the Creative inventory.

### 3. Upgrading

The three higher tiers are **shapeless** recipes — put the ingredients anywhere in the grid:

| Result | Ingredients |
|---|---|
| **Camping Picnic Table** | Basic Picnic Table **+** Diamond **+** any Dining Bench |
| **Glamping Table** | Camping Picnic Table **+** Netherite Ingot **+** any Dining Bench |
| **Diving Picnic Table** | Glamping Table **+** Heart of the Sea |

An upgrade **keeps the color and wood** the table was crafted with, so it stays the same style all
the way up. The bench you add is fuel for the recipe, not a new style — its wood is ignored.

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
