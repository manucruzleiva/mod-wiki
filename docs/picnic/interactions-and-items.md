# Interactions & Items

Beyond re-rolling, the picnic is a place to **care for your Pokémon** and **manage supplies**.

## Pokémon care (Cobblemon interaction wheel)

Point at one of your Pokémon and open Cobblemon's **interaction wheel** — Cobblemon Picnic adds two
options:

=== "Wash 🧽"

    Use a **wet sponge** to wash a Pokémon → **+friendship**. The sponge is consumed. By default this
    requires being **near a table** (configurable via `washrequirestable`). Friendship gained is set
    by `washfriendship`.

=== "Play 🟢"

    Use a **slime ball** to play fetch → a **throw / fetch / return** animation, **+friendship**, and
    a small chance the ball **breaks**. There's a **0.5 s cooldown** between plays. Tunables:
    `slimeballfriendship`, `slimeballbreakchance`, `slimeballrequirestable`.

## Picnic Baskets

**Picnic Baskets** are placeable furniture available in **every apricorn color**.

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

## Customization & misc

- **Colors & woods** — tables come in **16 cloth colors × wood types**; baskets in every apricorn
  color. All variants are in the Creative inventory.
- **Flammable** — tables burn like wood planks if exposed to fire.

!!! tip
    Friendship-building at the picnic stacks with normal Cobblemon mechanics — a good way to evolve
    friendship-based Pokémon while you hunt.
