# Getting Started

## Install

Cobblemon Picnic runs on **Fabric** *and* **NeoForge** for Minecraft **1.21.1**. Drop these in
`mods/`:

| | |
|---|---|
| **Always** | **Cobblemon Picnic** ([Modrinth](https://modrinth.com/mod/cobblemon-picnic) · [CurseForge](https://www.curseforge.com/projects/1581251)) + [Cobblemon](https://modrinth.com/mod/cobblemon) 1.7.x |
| **Fabric** | [Fabric API](https://modrinth.com/mod/fabric-api) + [Fabric Language Kotlin](https://modrinth.com/mod/fabric-language-kotlin) |
| **NeoForge** | [Architectury API](https://modrinth.com/mod/architectury-api) + [Kotlin for Forge](https://modrinth.com/mod/kotlin-for-forge) |
| **Optional** | [Cloth Config](https://modrinth.com/mod/cloth-config) for the settings screen, plus [Mod Menu](https://modrinth.com/mod/modmenu) on Fabric |

On a dedicated server, configure it with the [commands](commands.md) — the settings screen only
edits your own client's file.

## Your first table

<div class="grid cards" markdown>

- :material-hammer-wrench: **1 · Craft it**

    ---

    Three components — a **Table**, a **Dining Bench** and a **Picnic Basket** — then combine them
    with **Planks**, a **Vivichoke**, a **Campfire Pot** and a **Campfire**. The Table sets its
    cloth colour, the Planks its frame wood and the Bench its bench wood.

    [Full grids](picnic-tables.md#crafting)

- :material-map-marker-plus: **2 · Place it**

    ---

    The table is a **3×2 multiblock** that deploys **in front of you**, table column centred on where
    you aim. Face the way you want it and place. All six cells need to be free.

- :material-bread-slice: **3 · Fuel it**

    ---

    **Right-click** a centre cell to open the GUI and put **bread** in the fuel slot — or leave a
    [Picnic Basket](interactions-and-items.md#picnic-baskets) full of bread nearby and it pulls from
    that.

- :material-dice-multiple: **4 · Re-roll**

    ---

    **Left-click** a centre cell. The wild Pokémon around you are cleared and a fresh batch rolls in.
    The GUI slider sets how many.

</div>

## One button each

| Input | On a **table** cell | On a **bench** cell |
|---|---|---|
| **Right-click** | Opens the GUI | Sit down |
| **Left-click** | Re-roll | Break the structure |

Table cells take **no mining damage**, so a re-roll can never destroy the table by accident. When you
want the structure back in your inventory, hit a **bench**.

## What next?

- Bring friends and **[sit on the benches](shiny-aura.md)** — a full table doubles everyone's shiny odds.
- Upgrade to **[Expert](picnic-tables.md#crafting)** for the biggest radius and the Battle Seeker slot.
- Going somewhere strange? There's a table for **[underwater, the Nether and the End](picnic-tables.md#where-each-table-can-go)**.
