# Shiny Aura

Picnics are better with friends — and **more friends means more shinies**.

**Sit on a table's benches** and everyone seated gets their **shiny odds multiplied**. A **full table
doubles them**. Every seat is worth exactly the same share of that bonus, so the ladder is easy to read:

| Seated | Your shiny odds | At Cobblemon's default 1/8192 |
|:------:|:---------------:|:-----------------------------:|
| 1 | **×1.25** | ≈ 1 in 6554 |
| 2 | **×1.50** | ≈ 1 in 5461 |
| 3 | **×1.75** | ≈ 1 in 4681 |
| 4 | **×2.00** | ≈ 1 in 4096 |

Each person is worth **+0.25×**, and a full table is **×2.00** — that's the one number you can change
(see [Tuning](#tuning) below); the rungs in between are always split evenly.

A **full table means four seats**, which is what Expert, Diving, Hot and Strange provide. A smaller
table simply stops earlier: **Basic** seats 2 and tops out at **×1.50**, **Advanced** seats 3 and tops
out at **×1.75**. Sometimes you need a bigger table, not more friends.

## It multiplies, it never replaces

The aura is applied **last**, on top of whatever your odds already are — your server's shiny rate, a
Shiny Charm, anything else. ×2.00 means "twice as likely as you were a moment ago", whatever that was.
It can only ever **improve** your odds.

## Where you can see it

- A **ring of particles** hovers above the table, denser the fuller the table is.
- The **HUD** (top right) reads your live aura in two lines:

    ```
    Shiny Aura ✦ ×1.50 odds
        2/4 seated · 1 in 5461
    ```

- **Chat** tells you the moment it changes — when you sit down, and again each time someone joins or
  leaves your table.
- A **"Shiny Aura" buff** appears in your inventory; its level (I–IV) is how many of you are seated.

All of those numbers are calculated **on the server**, so on multiplayer you're reading its real
settings, not a guess from your own config file.

## When the boost applies

The aura stays live **the whole time you're seated** (it clears about a second after you stand up), and
while it's live it improves **any** shiny roll Cobblemon attributes to you — the table's **re-roll**
*and* the **natural wild spawns** that appear around you as you sit. Triggering a re-roll also grants
the table's multiplier to whoever pressed it, for that roll.

## How to sit

Right-click a **bench cell** (a side seat) with an **empty hand** to sit. Sneak or move to stand up.
Seats are invisible mounts — you'll snap neatly onto the bench.

## Tuning

See **[Commands & Config](commands.md)**:

| Setting | Meaning |
|---------|---------|
| `/picnic shinyaura <true\|false>` | Master on/off switch for the whole feature. |
| `/picnic auramultiplier <1..100>` | Shiny odds at a **full table**. Default **2** (double). `1` turns the aura off. |

In **Mod Menu** it's the **"Shiny odds at a full table (×)"** field, which prints the resulting ladder
right underneath as you type.
