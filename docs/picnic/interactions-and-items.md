# Items & Care

Beyond re-rolling, the picnic is a place to **care for your Pokémon** and **manage supplies**.

## Pokémon care (Cobblemon interaction wheel)

Point at one of your Pokémon and open Cobblemon's **interaction wheel** — Cobblemon Picnic adds two
options:

=== "Wash 🧽"

    Wash a Pokémon → **+friendship**. Carry either a **wet sponge**, which is used up, or a
    [**Poke-sponge**](#poke-sponge), which never is. Friendship gained is set by `washfriendship`.

=== "Play 🟢"

    Play fetch → **+friendship**. Carry either a **slime ball**, which has a chance to splatter and
    be lost, or a [**Fetchball**](#fetchball), which always comes back. The Pokémon **sprints** after
    the ball, tracking it as it bounces and rolls, then **walks back at a normal pace** with it.
    Tunables: `slimeballfriendship`, `slimeballbreakchance`.

When you carry both, the crafted item wins — you never spend a wet sponge while a Poke-sponge is in
your bag.

### You have to be at a picnic

Both options only appear on the wheel while a **picnic table is in range** (`actiondistance`, 25
blocks by default) — the wheel never offers something that is about to be refused. Turn
`washrequirestable` or `slimeballrequirestable` off and that option shows up anywhere.

### One Pokémon at a time

Each option has a **3-second cooldown, counted per Pokémon** (`washcooldown`, `playcooldown`). Look
after one and you can turn straight to the next; come back to the first and you wait. It's there so a
single Pokémon can't be farmed for friendship, not to slow down caring for a whole team.

## Crafted care items

Two permanent upgrades to the interactions above. Neither is ever consumed, and neither replaces
anything: the plain slime ball and the wet sponge keep working exactly as they always have.

### Fetchball

A slime ball bound in leather and string. Play fetch with it and your Pokémon brings it back
**every time** — it never splatters, and it never leaves your inventory.

<div class="cr-scroll">
<div class="cr-craft" title="4× String + 4× Leather + 1× Slime Ball → 1× Fetchball">
  <div class="cr-grid">
    <div class="cr-slot"><img src="../../assets/items/string.png" alt="String"></div>
    <div class="cr-slot"><img src="../../assets/items/leather.png" alt="Leather"></div>
    <div class="cr-slot"><img src="../../assets/items/string.png" alt="String"></div>
    <div class="cr-slot"><img src="../../assets/items/leather.png" alt="Leather"></div>
    <div class="cr-slot"><img src="../../assets/items/slime_ball.png" alt="Slime Ball"></div>
    <div class="cr-slot"><img src="../../assets/items/leather.png" alt="Leather"></div>
    <div class="cr-slot"><img src="../../assets/items/string.png" alt="String"></div>
    <div class="cr-slot"><img src="../../assets/items/leather.png" alt="Leather"></div>
    <div class="cr-slot"><img src="../../assets/items/string.png" alt="String"></div>
  </div>
  <div class="cr-arrow">➜</div>
  <div class="cr-result"><img src="../../assets/items/fetchball.png" alt="Fetchball"></div>
</div>
</div>

| Ingredient | Amount |
| --- | :---: |
| <img class="cr-inline" src="../../assets/items/string.png" alt=""> String | 4 |
| <img class="cr-inline" src="../../assets/items/leather.png" alt=""> Leather | 4 |
| <img class="cr-inline" src="../../assets/items/slime_ball.png" alt=""> Slime Ball | 1 |
| **→ <img class="cr-inline" src="../../assets/items/fetchball.png" alt=""> Fetchball** | **1** |

### Poke-sponge

A bath sponge that never dries out. One of them washes a whole team, forever.

<div class="cr-scroll">
<div class="cr-craft" title="2× Water Bucket + 2× String + 4× Sponge + 1× Slime Ball → 1× Poke-sponge">
  <div class="cr-grid">
    <div class="cr-slot"><img src="../../assets/items/water_bucket.png" alt="Water Bucket"></div>
    <div class="cr-slot"><img src="../../assets/items/sponge.png" alt="Sponge"></div>
    <div class="cr-slot"><img src="../../assets/items/string.png" alt="String"></div>
    <div class="cr-slot"><img src="../../assets/items/sponge.png" alt="Sponge"></div>
    <div class="cr-slot"><img src="../../assets/items/slime_ball.png" alt="Slime Ball"></div>
    <div class="cr-slot"><img src="../../assets/items/sponge.png" alt="Sponge"></div>
    <div class="cr-slot"><img src="../../assets/items/string.png" alt="String"></div>
    <div class="cr-slot"><img src="../../assets/items/sponge.png" alt="Sponge"></div>
    <div class="cr-slot"><img src="../../assets/items/water_bucket.png" alt="Water Bucket"></div>
  </div>
  <div class="cr-arrow">➜</div>
  <div class="cr-result"><img src="../../assets/items/poke_sponge.png" alt="Poke-sponge"></div>
</div>
</div>

| Ingredient | Amount |
| --- | :---: |
| <img class="cr-inline" src="../../assets/items/water_bucket.png" alt=""> Water Bucket | 2 |
| <img class="cr-inline" src="../../assets/items/string.png" alt=""> String | 2 |
| <img class="cr-inline" src="../../assets/items/sponge.png" alt=""> Sponge **or** <img class="cr-inline" src="../../assets/items/wet_sponge.png" alt=""> Wet Sponge | 4 |
| <img class="cr-inline" src="../../assets/items/slime_ball.png" alt=""> Slime Ball | 1 |
| **→ <img class="cr-inline" src="../../assets/items/poke_sponge.png" alt=""> Poke-sponge** | **1** |

The four sponge slots take **either** a dry Sponge or a Wet Sponge, in any mix — no need to dry them
out first. The two Water Buckets come back as empty buckets, as vanilla always returns them.

## Picnic Baskets

**Picnic Baskets** are placeable furniture available in **every apricorn color**. The apricorn you use
picks the color, and a basket is also an ingredient of the Picnic Table itself.

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

The apricorn and the basket cycle together: **whichever colour you put in is the colour you get out.**

| Ingredient | Amount |
| --- | :---: |
| <img class="cr-inline" src="../../assets/items/red_apricorn.png" alt=""> Apricorn — any of the 7 colors | 2 |
| <img class="cr-inline" src="../../assets/items/apricorn_planks.png" alt=""> Apricorn Planks | 2 |
| **→ <img class="cr-inline" src="../../assets/items/red_picnic_basket.png" alt=""> Picnic Basket** in that color | **1** |

- **Place** one on the ground like a block.
- **Store bread** inside it.
- A nearby **table pulls bread from baskets** to fuel its re-rolls — so you can keep a basket
  stocked next to your setup instead of refilling the fuel slot.

## `poke_snack` bias

If a **seasoned `poke_snack`** (a Cobblemon snack item with spawn influence) is on the ground near a
table when you re-roll:

- The re-roll **respects the snack's spawn influence**, biasing what appears.
- **One bite** is consumed from the closest snack each time.

This lets you steer a re-roll toward the kinds of Pokémon a given snack attracts.

## Battle Seeker

Put a **Battle Seeker** in a **Expert** table's fuel slot and every re-roll also **summons an RCT
trainer** to battle. It is **never consumed** — it stays in the slot, so you can keep challenging
trainers for as long as you like. Only the Expert tier exposes that slot; every other tier uses it
for bread.

It has **no recipe**. It's rare loot from world chests, so keep looting structures.

The trainer's level is matched to your party:

| Setting | Meaning |
|---------|---------|
| `spawnappropriatelvltrainer <true\|false>` | Scale the trainer to your party's level. |
| `trainerlevelgap <int>` | Level offset on top of the match, to make them tougher or softer. |

⚠️ The summon needs **Radical Cobblemon Trainers (RCT)** installed. Without it the Battle Seeker
simply does nothing and the rest of the table works normally.

## Colours, woods and fire

A picnic table is built in **16 cloth colours × 11 frame woods × 11 bench woods**, and the coloured
tables, dining benches and apricorn-coloured baskets it is built from are all in the Creative
inventory. All of them are **flammable** — they burn like wood planks, which is what
the [Nether](picnic-tables.md#where-each-table-can-go) exploits.

Friendship built at the picnic stacks with normal Cobblemon mechanics, so it's a good way to evolve
friendship-based Pokémon while you hunt.
