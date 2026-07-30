# Shiny Aura

Picnics are better with friends — and **more friends means more shinies**.

**Sit on a table's benches** and each occupied seat raises the **shiny odds** for everyone seated —
for the table's next **re-roll** *and* for **wild Pokémon that spawn naturally around you while you
sit**. The more people seated, the stronger the **Shiny Aura**.

## How it shows

- A **ring of particles** hovers **above the table** while the aura is active.
- Anyone in range gets a **"Shiny Aura" buff** in their HUD, with a numeric **level** that scales
  with how many people are seated (it reads at least **1** at one seat).

## How to sit

Right-click a **bench cell** (a side seat) with an **empty hand** to sit. Sneak or move to stand up.
Seats are invisible mounts — you'll snap neatly onto the bench.

## Tuning

The aura is fully configurable (see **[Configuration](configuration.md)**):

| Setting | Meaning |
|---------|---------|
| `shinyaura <true\|false>` | Master on/off switch for the whole feature. |
| `aurabase <0..1>` | Base shiny boost contributed per occupied seat. |
| `auramax <0..1>` | Cap on the total boost, no matter how many are seated. |

!!! note "When the boost applies"
    The Shiny Aura is a per-player **odds floor** that stays live **the whole time you're seated** at a
    table (it clears about a second after you stand up). While it's live it improves the odds of **any**
    shiny roll Cobblemon attributes to you — that means the table's **re-roll** *and* the **natural wild
    spawns** that appear around you as you sit. Triggering a re-roll also grants the floor to the player
    who triggered it for that roll. It only ever **raises** your odds — it never lowers a boost already
    coming from a Shiny Charm or a higher server shiny rate.
