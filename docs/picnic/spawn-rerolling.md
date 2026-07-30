# Spawn Re-rolling

The headline feature. **Right-click the center (table) cells** and the table will:

1. **Despawn nearby wild Pokémon** within the tier's [radius](picnic-tables.md#tiers) — but **never
   owned/tethered Pokémon** (yours and other players' stay safe).
2. **Force a fresh "maximized" natural respawn** around the table, using Cobblemon's own spawner at a
   boosted density so you get a full batch immediately.

This lets you **re-roll the local spawns on demand** — ideal for shiny hunting or fishing for a
specific species without wandering the world.

## How many spawn?

Open the table's GUI and use the **slider** to choose how many Pokémon a re-roll spawns, up to the
tier's **spawn cap** (Basic 5 → Glamping/Diving 12). The re-roll runs several spawner passes and
stops early once it has placed enough or a pass yields nothing.

## Fuel

Each re-roll costs **bread**, depending on tier:

| Tier | Bread per re-roll |
|------|:-----------------:|
| Basic | 7 |
| Camping | 5 |
| Glamping | 3 |
| Diving | 3 |

The cost follows a **7 / 5 / 3 / 3** curve — cheaper as tiers improve. Bread can come from the table's
**fuel slot** or from a nearby placed
**[Picnic Basket](interactions-and-items.md#picnic-baskets)** — the table will pull from baskets
automatically. Out of bread? The table tells you and the re-roll is cancelled. Each per-tier cost is
configurable via `fuelcost <tier>` (see **[Configuration](configuration.md)**).

## Cooldown

To stop a table being spammed, each re-roll starts a **cooldown** (default **5 seconds**). It's
enforced **both per-table and per-player** — whichever is still counting down blocks the re-roll, so
you can't dodge it by hopping between tables. A blocked attempt shows a short **actionbar countdown**
and costs no bread. Change it with `rerollcooldown <seconds>` (0 disables the wait).

## Party TM teaching

Every re-roll has a small chance (**5%** by default) that one of **your party Pokémon teaches another
party member** one of its moves — a little picnic bonding. A Pokémon only ever learns a move it is
**actually able to learn** (its normal learnset / TM compatibility), so it never gains an illegal move;
if all four slots are full, one move is swapped out. Tune or disable it with `tmteachchance <0..1>`.

## Snack bias

If a **seasoned `poke_snack`** is nearby when you re-roll, the spawn **respects that snack's spawn
influence** (so you can bias toward what the snack attracts) and **consumes one bite** of the closest
snack. See **[Interactions & Items → Snacks](interactions-and-items.md#poke_snack-bias)**.

!!! tip "Owned Pokémon are protected"
    The despawn step explicitly skips Pokémon with an owner. You can leave your party out (or a
    pasture nearby) and re-roll freely.
