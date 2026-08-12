# Spawn Re-rolling

The headline feature. **Left-click the center (table) cells** and the table will:

1. **Despawn nearby wild Pokémon** within the tier's [radius](picnic-tables.md#tiers) — but **never
   owned/tethered Pokémon** (yours and other players' stay safe).
2. **Force a fresh "maximized" natural respawn** around the table, using Cobblemon's own spawner at a
   boosted density so you get a full batch immediately.

This lets you **re-roll the local spawns on demand** — ideal for shiny hunting or fishing for a
specific species without wandering the world.

## How many spawn?

Open the table's GUI and use the **slider** to choose how many Pokémon a re-roll spawns, up to the
tier's **spawn cap** (Basic 5 → everything above 12). The re-roll runs several spawner passes and
stops early once it has placed enough.

## Where they appear

Spawns land **inside the table's own radius**, 6 blocks out to the tier's limit, and the search
follows the **ground** at whatever spot it picks. That is what makes a re-roll work on a mountain
top, a ledge or a slope, where the terrain a few blocks away sits well below your feet.

It also **prefers ground near your own altitude**. Stand on a summit and the re-roll fills the summit,
not the valley below it — it only settles for lower ground when there's nothing else within reach, so
a bare peak still gets its Pokémon.

Underground and underwater the search keeps your own altitude instead, so caves and Diving tables
behave the way you'd expect.

A single unlucky spot doesn't end the attempt — the table keeps picking new ones until it fills your
order or runs out of tries. If a place genuinely has nowhere to put a Pokémon, it says so plainly
rather than reporting a silent zero. The bread is still spent: the area was cleared either way, and
that can't be undone.

## Pokémon that fly, spawn flying

A re-rolled Pokémon whose species can fly is lifted **3 to 12 blocks** off the ground it appeared on,
as far as clear air allows. Set the ceiling with `flyingspawnlift` (0 keeps everything on the ground).

And a flier that spawned on ground **below you climbs to your own altitude**. On a peak that's the
difference between watching them circle your table and never seeing them at all, because the only
ground for a hundred blocks was somewhere down the mountainside. Clear air still has the final say, so
none of them end up inside the mountain.

**It doesn't change your odds.** Lifting happens *after* the spawn is decided. Which Pokémon appear,
and how often, is Cobblemon's call alone — its spawn pool, the biome, the light, and any `poke_snack`
influence in range. Nothing is added, removed or re-rolled, so a shiny hunt runs at exactly the rate
it always did.

## Fuel

Each re-roll costs **bread**, depending on tier:

| Tier | Bread per re-roll |
|------|:-----------------:|
| Basic | 7 |
| Camping | 5 |
| Glamping · Diving · Hot · Strange | 3 |

Fuel gets cheaper as tiers improve, and everything above Camping costs the same. Bread can come from the table's
**fuel slot** or from a nearby placed
**[Picnic Basket](interactions-and-items.md#picnic-baskets)** — the table will pull from baskets
automatically. Out of bread? The table tells you and the re-roll is cancelled. Each per-tier cost is
configurable via `fuelcost <tier>` (see **[Commands & Config](commands.md)**).

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

**Owned Pokémon are always safe.** The despawn step skips anything with an owner, so you can leave
your party out — or a pasture nearby — and re-roll freely.
