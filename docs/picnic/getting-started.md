# Getting Started

## Installation

Cobblemon Picnic runs on **Fabric** *and* **NeoForge** for Minecraft **1.21.1**.

1. Install your loader for Minecraft **1.21.1**: **[Fabric Loader](https://fabricmc.net/use/)** *or*
   **[NeoForge](https://neoforged.net/) 21.1.x**.
2. Put these mods in your `mods/` folder:
    - **Cobblemon Picnic** ([Modrinth](https://modrinth.com/mod/cobblemon-picnic) /
      [CurseForge](https://www.curseforge.com/projects/1581251))
    - **[Cobblemon](https://modrinth.com/mod/cobblemon) 1.7.x**
    - **Fabric:** [Fabric API](https://modrinth.com/mod/fabric-api) +
      [Fabric Language Kotlin](https://modrinth.com/mod/fabric-language-kotlin)
    - **NeoForge:** [Architectury API](https://modrinth.com/mod/architectury-api) +
      [Kotlin for Forge](https://modrinth.com/mod/kotlin-for-forge)
3. *(Optional)* **[Cloth Config](https://modrinth.com/mod/cloth-config)** for the in-game settings screen
   (plus **[Mod Menu](https://modrinth.com/mod/modmenu)** on Fabric — on NeoForge the screen opens from the
   mods list's **Config** button).

!!! tip "Server vs. client"
    The mod runs on both. On a dedicated server, use the [commands](commands.md) to configure it
    (the Mod Menu screen only edits the local client config).

## Your first table

1. **Craft a Picnic Table.** First the components — a **Table** (wool + planks, one per dye color), a
   **Dining Bench** (slabs + planks, one per wood) and a **Picnic Basket** (apricorns + apricorn
   planks) — then combine them with a **Nether Star**, a **Campfire Pot** and a **Campfire** into the
   Basic Picnic Table. The Table and Bench you use set its color and wood. Full grids in
   **[Picnic Tables → Crafting](picnic-tables.md#crafting)**.
2. **Place it** on open, flat ground. The table is a **3×2 multiblock** that deploys **in front of
   you**, with the table column centered — so face the direction you want it and place.
3. **Add fuel.** **Right-click** a **center (table) cell** to open the GUI and drop **bread** into
   the fuel slot, or place a **[Picnic Basket](interactions-and-items.md#picnic-baskets)** with bread
   nearby.
4. **Re-roll!** **Left-click** a **center (table) cell** to despawn the surrounding wild Pokémon and
   roll a fresh batch. The slider in the GUI sets how many spawn (capped by tier).

!!! tip "One button each"
    **Right-click** a table cell to open its GUI, **left-click** to re-roll, and **right-click a
    bench** to sit. Table cells take no mining damage, so a re-roll can never break the table —
    **hit a bench** when you want to pick the structure back up.

!!! note "Placement needs room"
    The footprint is **3 wide × 2 deep**. If the cells are blocked, the table won't place. Leave a
    clear area so spawns have room to appear.

## What next?

- Bring friends and **[sit on the benches](shiny-aura.md)** to boost shiny odds.
- Upgrade toward **Glamping** for the biggest radius and the **[Battle Seeker](battle-seeker.md)** slot.
- Going underwater? Build a **[Diving table](picnic-tables.md#tiers)**.
