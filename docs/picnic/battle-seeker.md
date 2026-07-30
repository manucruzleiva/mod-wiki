# Battle Seeker

The **Battle Seeker** turns a Glamping table into a **trainer-battle generator**.

## What it does

Place a **Battle Seeker** in a **Glamping** table's **fuel slot**. Now, when you re-roll, instead of
(or alongside) wild spawns, the table **summons an RCT trainer** for you to battle. The Battle Seeker
is **not consumed** — it stays in the slot so you can keep challenging trainers.

The summoned trainer's level is **matched to your party**, adjustable in
[configuration](configuration.md):

| Setting | Meaning |
|---------|---------|
| `spawnappropriatelvltrainer <true\|false>` | Scale the trainer to your party's level. |
| `trainerlevelgap <int>` | Level offset applied on top of the match (e.g. make them a bit tougher). |

## How to get one

The Battle Seeker has **no crafting recipe**. It's a **rare loot item found in world chests** —
keep exploring structures and you may find one.

## Requirements

!!! warning "Needs RCT"
    The trainer spawn uses **Radical Cobblemon Trainers (RCT)**. If RCT isn't installed, the Battle
    Seeker simply does nothing — the rest of the table works normally.

!!! tip "Glamping only"
    Only the **Glamping** tier exposes the Battle Seeker slot. Lower tiers use that slot for bread
    fuel instead.
