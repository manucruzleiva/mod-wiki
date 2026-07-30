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

!!! tip "Upgrading"
    You can upgrade a table to a higher tier via crafting — the recipe **keeps the cloth color and
    bench wood** you originally used, so your table stays the same style.

## Crafting

Tables are crafted from a **cloth** on top of a **bench**:

- **Cloth** — any of the **16 dye colors** sets the tablecloth color.
- **Bench** — any of the supported **wood types** sets the frame wood.

The result renders in that exact **color × wood** combination, using the mod's **own models and
textures** (no other furniture mod required). Every color/wood variant is available in the Creative
inventory.

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
