# Picnic Tables

Picnic Tables are the core block of the mod. Each is a **3×2 multiblock**: the **center column**
holds the **table cells** (re-roll + GUI), and the **side cells** are **benches** you can sit on, up
to the tier's seat cap. Leftover side cells stay empty.

## Tiers

| Tier | Spawn cap | Radius | Seats | Fuel / re-roll | Notes |
|------|:---------:|:------:|:-----:|:--------------:|-------|
| **Basic** | 5 | 32 | 2 | 7 bread | Entry tier |
| **Advanced** | 8 | 48 | 3 | 5 bread | Cheaper fuel, bigger |
| **Expert** | 12 | 64 | 4 | 3 bread | Unlocks the **[Battle Seeker](interactions-and-items.md#battle-seeker)** slot |
| **Diving** | 12 | 64 | 4 | 3 bread | At home **underwater** — on dry land it floods what is around it |
| **Hot** | 12 | 64 | 4 | 3 bread | At home in the **Nether** — anywhere else it scorches what is around it |
| **Strange** | 12 | 64 | 4 | 3 bread | At home in **the End** — anywhere else it will not stay put |

- **Spawn cap** — the maximum Pokémon a single re-roll can spawn (and the GUI slider's max).
- **Radius** — how far around the table wild Pokémon are despawned and re-rolled.
- **Seats** — how many benches the footprint provides (seat counts are **fixed per tier**, not
  configurable).
- **Fuel** — bread consumed per re-roll, cheaper as tiers improve (7 for Basic, 5 for Advanced, 3 for
  everything above). Bread comes from the table's fuel slot or from a nearby
  **[Picnic Basket](interactions-and-items.md#picnic-baskets)**. The per-tier cost is configurable
  (`fuelcost <tier>`).

**Basic → Advanced → Expert** is the ladder. **Diving**, **Hot** and **Strange** are three steps
sideways off the top of it: identical in what they do, different only in where they can go. See
[Where each table can go](#where-each-table-can-go).

## Crafting

A Picnic Table is built in two steps: craft the **three components**, then assemble them into the
**Basic Picnic Table**. Higher tiers are upgrades of that one.

### 1. The components

Each one comes in every color or wood the table can be built from — the grids below show one
example.

=== "Table"

    The tabletop. Any of the **16 dye colors** of wool over any of the **11 woods** of planks — the
    wool is the cloth and the planks are the frame, so there are **176** of them (*Red Table*,
    *Spruce Red Table*, *Cherry Black Table*, …). Oak's are the ones with no wood in the name.

    <div class="cr-scroll">
    <div class="cr-craft" title="3× Wool + 2× Planks → 1× Table in that colour and wood">
      <div class="cr-grid">
        <div class="cr-slot cr-cycle cr-cycle--16" style="background-image:url(../../assets/items/strips/wool.png)" role="img" aria-label="Wool — any of the 16 colours"></div>
        <div class="cr-slot cr-cycle cr-cycle--16" style="background-image:url(../../assets/items/strips/wool.png)" role="img" aria-label="Wool — any of the 16 colours"></div>
        <div class="cr-slot cr-cycle cr-cycle--16" style="background-image:url(../../assets/items/strips/wool.png)" role="img" aria-label="Wool — any of the 16 colours"></div>
        <div class="cr-slot cr-cycle cr-cycle--11" style="background-image:url(../../assets/items/strips/planks.png)" role="img" aria-label="Planks — any of the 11 woods"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot cr-cycle cr-cycle--11" style="background-image:url(../../assets/items/strips/planks.png)" role="img" aria-label="Planks — any of the 11 woods"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result cr-cycle cr-cycle--16" style="background-image:url(../../assets/items/strips/table.png)" role="img" aria-label="Table in the wool colour you used"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/white_wool.png" alt=""> Wool — any of the 16 colors | 3 |
    | <img class="cr-inline" src="../../assets/items/oak_planks.png" alt=""> Planks — any of the 11 woods | 2 |
    | **→ <img class="cr-inline" src="../../assets/items/table_red.png" alt=""> Table** in that color and wood | **1** |

=== "Dining Bench"

    The seat. Slabs and planks of the **same wood** — available in **11 woods**: oak, spruce, birch,
    jungle, acacia, dark oak, mangrove, cherry, bamboo, crimson and warped.

    <div class="cr-scroll">
    <div class="cr-craft" title="3× Oak Slab + 2× Oak Planks → 2× Oak Dining Bench">
      <div class="cr-grid">
        <div class="cr-slot"><img src="../../assets/items/oak_slab.png" alt="Oak Slab"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_slab.png" alt="Oak Slab"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_slab.png" alt="Oak Slab"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_planks.png" alt="Oak Planks"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"><img src="../../assets/items/oak_planks.png" alt="Oak Planks"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result cr-cycle cr-cycle--11" style="background-image:url(../../assets/items/strips/dining_bench.png)" role="img" aria-label="Dining Bench in the wood you used"><span class="cr-count">2</span></div>
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
    <div class="cr-craft" title="2× Apricorn + 2× Apricorn Planks → 1× Picnic Basket in that colour">
      <div class="cr-grid">
        <div class="cr-slot cr-cycle" style="--n:7; background-image:url(../../assets/items/strips/apricorn.png)" role="img" aria-label="Apricorn — any of the 7 colours"></div>
        <div class="cr-slot cr-cycle" style="--n:7; background-image:url(../../assets/items/strips/apricorn.png)" role="img" aria-label="Apricorn — any of the 7 colours"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"><img src="../../assets/items/apricorn_planks.png" alt="Apricorn Planks"></div>
        <div class="cr-slot"><img src="../../assets/items/apricorn_planks.png" alt="Apricorn Planks"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result cr-cycle" style="--n:7; background-image:url(../../assets/items/strips/basket.png)" role="img" aria-label="Picnic Basket in the apricorn's colour"></div>
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
<div class="cr-craft" title="Picnic Basket + Vivichoke + 2× Table + Campfire Pot + 2× Dining Bench + Campfire → Basic Picnic Table">
  <div class="cr-grid">
    <div class="cr-slot"><img src="../../assets/items/red_picnic_basket.png" alt="Picnic Basket"></div>
    <div class="cr-slot"></div>
    <div class="cr-slot"><img src="../../assets/items/vivichoke.png" alt="Vivichoke"></div>
    <div class="cr-slot"><img src="../../assets/items/table_red.png" alt="Table"></div>
    <div class="cr-slot"><img src="../../assets/items/table_red.png" alt="Table"></div>
    <div class="cr-slot"><img src="../../assets/items/campfire_pot_red.png" alt="Campfire Pot"></div>
    <div class="cr-slot cr-cycle cr-cycle--11" style="background-image:url(../../assets/items/strips/dining_bench.png)" role="img" aria-label="Dining Bench — any of the 11 woods"></div>
    <div class="cr-slot cr-cycle cr-cycle--11" style="background-image:url(../../assets/items/strips/dining_bench.png)" role="img" aria-label="Dining Bench — any of the 11 woods"></div>
    <div class="cr-slot"><img src="../../assets/items/campfire.png" alt="Campfire"></div>
  </div>
  <div class="cr-arrow">➜</div>
  <div class="cr-result"><img src="../../assets/items/basic_picnic_table.png" alt="Basic Picnic Table"></div>
</div>
</div>

| Ingredient | Amount | Accepts |
| --- | :---: | --- |
| <img class="cr-inline" src="../../assets/items/red_picnic_basket.png" alt=""> Picnic Basket | 1 | any of the 7 colors |
| <img class="cr-inline" src="../../assets/items/vivichoke.png" alt=""> Vivichoke | 1 | — |
| <img class="cr-inline" src="../../assets/items/table_red.png" alt=""> Table | 2 | any of the 176 — **the left one sets the cloth colour and the frame wood**. Tables from **CobbleFurnies** and **Handcrafted** work too |
| <img class="cr-inline" src="../../assets/items/campfire_pot_red.png" alt=""> Campfire Pot | 1 | any Cobblemon Campfire Pot, or Cobblemon's own Campfire |
| <img class="cr-inline" src="../../assets/items/dining_bench_oak.png" alt=""> Dining Bench | 2 | any of the 11 woods — **each one becomes a seat, in the order you place them**. Benches from **Handcrafted** work too |
| <img class="cr-inline" src="../../assets/items/campfire.png" alt=""> Campfire | 1 | Campfire *or* <img class="cr-inline" src="../../assets/items/soul_campfire.png" alt=""> Soul Campfire |
| **→ <img class="cr-inline" src="../../assets/items/basic_picnic_table.png" alt=""> Basic Picnic Table** | **1** | |

The result is drawn as **exactly the items you built it from**: the cloth and the wood of the table
you used, and **a separate bench per seat** — two benches of different woods come out as two
different seats. All of it with the mod's **own models and textures**, so no other furniture mod is
required. The basket, pot and campfire are consumed but don't change how the table looks.

Hold **Shift** over a picnic table in your inventory to read back everything it is made of.

### 3. Upgrading

The three higher tiers are **shapeless** — the ingredients can sit anywhere in the grid. An upgrade
**keeps the colour and the woods** the table was crafted with, and it adds a seat: **the bench you
hand over is the bench that seat is made of**. A table can end up with four seats in four woods.

=== "Advanced"

    <div class="cr-scroll">
    <div class="cr-craft" title="Shapeless: Basic Picnic Table + Diamond + Dining Bench → Advanced Picnic Table">
      <div class="cr-grid">
        <div class="cr-slot"><img src="../../assets/items/basic_picnic_table.png" alt="Basic Picnic Table"></div>
        <div class="cr-slot"><img src="../../assets/items/diamond.png" alt="Diamond"></div>
        <div class="cr-slot cr-cycle cr-cycle--11" style="background-image:url(../../assets/items/strips/dining_bench.png)" role="img" aria-label="Dining Bench — any of the 11 woods"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/advanced_picnic_table.png" alt="Advanced Picnic Table"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/basic_picnic_table.png" alt=""> Basic Picnic Table | 1 |
    | <img class="cr-inline" src="../../assets/items/diamond.png" alt=""> Diamond | 1 |
    | <img class="cr-inline" src="../../assets/items/dining_bench_oak.png" alt=""> Dining Bench — any wood | 1 |
    | **→ <img class="cr-inline" src="../../assets/items/advanced_picnic_table.png" alt=""> Advanced Picnic Table** | **1** |

=== "Expert"

    <div class="cr-scroll">
    <div class="cr-craft" title="Shapeless: Advanced Picnic Table + Netherite Ingot + Dining Bench → Expert Picnic Table">
      <div class="cr-grid">
        <div class="cr-slot"><img src="../../assets/items/advanced_picnic_table.png" alt="Advanced Picnic Table"></div>
        <div class="cr-slot"><img src="../../assets/items/netherite_ingot.png" alt="Netherite Ingot"></div>
        <div class="cr-slot cr-cycle cr-cycle--11" style="background-image:url(../../assets/items/strips/dining_bench.png)" role="img" aria-label="Dining Bench — any of the 11 woods"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/expert_picnic_table.png" alt="Expert Picnic Table"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/advanced_picnic_table.png" alt=""> Advanced Picnic Table | 1 |
    | <img class="cr-inline" src="../../assets/items/netherite_ingot.png" alt=""> Netherite Ingot | 1 |
    | <img class="cr-inline" src="../../assets/items/dining_bench_oak.png" alt=""> Dining Bench — any wood | 1 |
    | **→ <img class="cr-inline" src="../../assets/items/expert_picnic_table.png" alt=""> Expert Picnic Table** | **1** |

=== "Diving"

    <div class="cr-scroll">
    <div class="cr-craft" title="Shapeless: Expert Picnic Table + Heart of the Sea → Diving Picnic Table">
      <div class="cr-grid">
        <div class="cr-slot"><img src="../../assets/items/expert_picnic_table.png" alt="Expert Picnic Table"></div>
        <div class="cr-slot"><img src="../../assets/items/heart_of_the_sea.png" alt="Heart of the Sea"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/diving_picnic_table.png" alt="Diving Picnic Table"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/expert_picnic_table.png" alt=""> Expert Picnic Table | 1 |
    | <img class="cr-inline" src="../../assets/items/heart_of_the_sea.png" alt=""> Heart of the Sea | 1 |
    | **→ <img class="cr-inline" src="../../assets/items/diving_picnic_table.png" alt=""> Diving Picnic Table** | **1** |

=== "Hot"

    <div class="cr-scroll">
    <div class="cr-craft" title="Shapeless: Expert Picnic Table + Netherite Ingot → Hot Picnic Table">
      <div class="cr-grid">
        <div class="cr-slot"><img src="../../assets/items/expert_picnic_table.png" alt="Expert Picnic Table"></div>
        <div class="cr-slot"><img src="../../assets/items/netherite_ingot.png" alt="Netherite Ingot"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/hot_picnic_table.png" alt="Hot Picnic Table"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/expert_picnic_table.png" alt=""> Expert Picnic Table | 1 |
    | <img class="cr-inline" src="../../assets/items/netherite_ingot.png" alt=""> Netherite Ingot | 1 |
    | **→ <img class="cr-inline" src="../../assets/items/hot_picnic_table.png" alt=""> Hot Picnic Table** | **1** |

=== "Strange"

    <div class="cr-scroll">
    <div class="cr-craft" title="Shapeless: Expert Picnic Table + Eye of Ender → Strange Picnic Table">
      <div class="cr-grid">
        <div class="cr-slot"><img src="../../assets/items/expert_picnic_table.png" alt="Expert Picnic Table"></div>
        <div class="cr-slot"><img src="../../assets/items/ender_eye.png" alt="Eye of Ender"></div>
        <div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
        <div class="cr-slot"></div><div class="cr-slot"></div><div class="cr-slot"></div>
      </div>
      <div class="cr-arrow">➜</div>
      <div class="cr-result"><img src="../../assets/items/strange_picnic_table.png" alt="Strange Picnic Table"></div>
    </div>
    </div>

    | Ingredient | Amount |
    | --- | :---: |
    | <img class="cr-inline" src="../../assets/items/expert_picnic_table.png" alt=""> Expert Picnic Table | 1 |
    | <img class="cr-inline" src="../../assets/items/ender_eye.png" alt=""> Eye of Ender | 1 |
    | **→ <img class="cr-inline" src="../../assets/items/strange_picnic_table.png" alt=""> Strange Picnic Table** | **1** |

## Where each table can go

**Any table can be placed in any dimension.** Where a table goes is your business — what the place
does to it once it is standing there is the dimension's.

Each themed table belongs somewhere, and **carries that somewhere with it**. At home it is simply a
table. Anywhere else it inflicts on its surroundings exactly what an ordinary table suffers where
that home is native: the Hot table scorches, the Strange one will not sit still, the Diving one
floods.

| Table | Overworld | Nether | The End |
|---|:---:|:---:|:---:|
| **Basic / Advanced / Expert** | ✅ | ⚠️ catches fire | ⚠️ drifts away |
| **Diving** | 🌊 floods around it | 🔥 **burns at once** | 🌊 floods · ⚠️ drifts away |
| **Hot** | 🔥 scorches around it | ✅ **at home** | 🔥 scorches · ⚠️ drifts away |
| **Strange** | ⚠️ drifts away | ⚠️ drifts · catches fire | ✅ **at home** |

🔥 **An ordinary table burns in the Nether.** Leave any table but the **Hot** one down there and it
has a **30% chance every second** of a flame taking hold on it. Nothing is destroyed outright — it
burns from there under the normal fire rules, so you can still put it out. The **Diving** table is
the exception in the other direction: a tableful of water in that heat goes up **the moment it
arrives**. To picnic in the Nether properly, bring the Hot table: nothing sets it alight, anywhere.

🌡️ **The Hot table takes the Nether with it.** Standing anywhere else, once a second it sets a flame
on the ground within **3 blocks** and burns everything in that radius — **including whoever is
sitting at it**. It can also be sunk into lava. It is a table for the Nether, and taking it home is
supposed to be a bad idea.

🌊 **The Diving table takes the water with it.** Placed on dry land it fills the ring of blocks
around itself with water and lets it run downhill from there; put it back underwater and it just
sits there, because there is nothing left to spill.

🌌 **The End will not hold a picnic still, and the Strange table will not sit still anywhere else.**
Sit down at any table but the **Strange** one out there,
or try to re-roll at it, and the whole table is **somewhere else within 24 blocks** before the click
lands — leaving you standing where it used to be. Nothing is lost: the bread in the slot, the cloth
colour and the woods it was crafted with, and your Pokémon-per-re-roll setting all travel with it. A
table with nowhere to go — walled in, or ringed by void — stays put and works normally. To picnic in
the End properly, bring the Strange table: it never drifts.



## Placement & orientation

The table **deploys in front of you**, with the **table column centred** on where you aim, oriented to
your facing — the "wide" axis runs left-to-right relative to you. The structure is one block tall:
benches on the sides, the functional table down the middle. All six cells must be free, and each table
needs its own footprint, since overlapping structures interfere with each other's cells.

**To pick it back up, break a bench.** Table cells take no mining damage — that's what keeps a re-roll
from destroying the table you're clicking. Breaking any bench takes the whole structure and returns
the table item.
