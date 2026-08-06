# Getting Started

## Obtaining HM Discs

```mermaid
sequenceDiagram
    actor You
    participant P as Wild Pokémon
    You->>You: Hold the trigger item
    You->>P: Sneak + right-click
    P-->>You: 💿 HM Disc (trigger item consumed)
    You->>You: Right-click the disc → ability learned!
```

Each ability is locked behind a **Pokémon interaction**. To unlock one:

1. Locate the required Pokémon in the world (or spawn it with `/pokespawn <species>`).
2. Hold the **trigger item** in your main hand.
3. **Sneak + right-click** the Pokémon.
4. The trigger item is consumed and the Pokémon gives you the **HM Disc**.

!!! tip
    Operators can get HM Discs directly with `/dittohm give <ability_id> <player>` without interacting with a Pokémon.

---

## Learning an ability

Once you have an HM Disc:

- **Right-click** the disc → the ability is **permanently learned** and the disc stays in your inventory as a reusable badge.
- **Left-click** with a learned disc to **use** the ability (or toggle a passive on/off).
- Learned abilities persist across deaths and world reloads (stored server-side).

---

## Crafting the HM Case

The **HM Case** lets you manage all learned abilities from a single hotbar slot.

**Recipe (shapeless)** — drop the ingredients anywhere in the crafting grid:

<div class="cr-craft" title="Shapeless: Chest + Diamond + all 7 Apricorns → HM Case">
  <div class="cr-grid">
    <div class="cr-slot"><img src="../../assets/items/chest.png" alt="Chest"></div>
    <div class="cr-slot"><img src="../../assets/items/diamond.png" alt="Diamond"></div>
    <div class="cr-slot"><img src="../../assets/items/red_apricorn.png" alt="Red Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/yellow_apricorn.png" alt="Yellow Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/green_apricorn.png" alt="Green Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/blue_apricorn.png" alt="Blue Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/black_apricorn.png" alt="Black Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/white_apricorn.png" alt="White Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/pink_apricorn.png" alt="Pink Apricorn"></div>
  </div>
  <div class="cr-arrow">➜</div>
  <div class="cr-result"><img src="../../assets/items/hm_case.png" alt="HM Case"></div>
</div>

| Ingredient | Quantity |
|---|---|
| <img class="cr-inline" src="../../assets/items/chest.png" alt=""> Chest | 1 |
| <img class="cr-inline" src="../../assets/items/diamond.png" alt=""> Diamond | 1 |
| <img class="cr-inline" src="../../assets/items/red_apricorn.png" alt=""> Red Apricorn | 1 |
| <img class="cr-inline" src="../../assets/items/yellow_apricorn.png" alt=""> Yellow Apricorn | 1 |
| <img class="cr-inline" src="../../assets/items/green_apricorn.png" alt=""> Green Apricorn | 1 |
| <img class="cr-inline" src="../../assets/items/blue_apricorn.png" alt=""> Blue Apricorn | 1 |
| <img class="cr-inline" src="../../assets/items/black_apricorn.png" alt=""> Black Apricorn | 1 |
| <img class="cr-inline" src="../../assets/items/white_apricorn.png" alt=""> White Apricorn | 1 |
| <img class="cr-inline" src="../../assets/items/pink_apricorn.png" alt=""> Pink Apricorn | 1 |
| **→ <img class="cr-inline" src="../../assets/items/hm_case.png" alt=""> HM Case** | **1** |

---

## Using the HM Case

| Action | Result |
|---|---|
| **Left-click** | Uses the currently selected (active) HM |
| **Right-click** | Opens the HM Case GUI |

In the GUI you can:

- See all 35 HMs (grey glass = not yet learned, disc icon = learned)
- **Right-click** an **Active HM** to set it as the quick-use ability
- **Right-click** a **Toggle HM** to enable or disable it
- **Left-click + drag** an HM onto another slot in the same section to reorder them

See the [HM Case guide](hm-case.md) for full details.

---

## The hunger system

- **Active HMs** cost hunger on use (configurable per ability).
- **Toggle HMs** block your maximum hunger while enabled — most reduce your max food bar by **2 points** (Harden by **3**, Burning Bulwark by **4**). You still regenerate health at the cap via a slow Regeneration effect. The cap never drops below 2.

| Food points blocked | Max hunger |
|---|---|
| 0 | 20 / 20 |
| 2 | 18 / 20 |
| 4 | 16 / 20 |
| 6 | 14 / 20 |
| 8 | 12 / 20 |
