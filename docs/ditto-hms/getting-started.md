# Getting Started

Cobblemon HMs has nothing to learn, craft or carry. **Your Pokémon do the work.** If a Pokémon of
yours has a move in its movepool, it can share it with you while it is out.

## Your Pokémon's wheel

Send out a Pokémon, open Cobblemon's **interaction wheel** on it and pick **Field moves**. The wheel
that opens lists everything that Pokémon can do for you, and nothing it cannot:

| Kind | What a pick does | Page |
|---|---|---|
| **Partner HM** | That Pokémon lends the move to your **empty fist** | [Partner HMs](abilities/active.md) |
| **Aura** | Switches a passive effect on you, on or off | [Auras](abilities/toggles.md) |
| **Field move** | The Pokémon does it itself, once | [Your Pokémon](pokemon.md#field-moves) |
| **Mount toggle** | Helps that Pokémon when you ride it | [Your Pokémon](pokemon.md#mount-toggles) |

A Pokémon can share a move when the move is **in its movepool** (equipped or not), or when its
species is one listed on those pages. It has to be yours, sent out, and within 24 blocks.

## Using a partner HM

Once a Pokémon is lending you an HM, **click with an empty hand** to fire it. Anything else in your
hand keeps its normal click, so tools, weapons and blocks behave exactly as they always did.

One Pokémon lends one HM at a time. Walk away from it and the HM pauses until you are back. **Put it
back in its ball and it stops lending**, and its auras switch off too (weather auras excepted): send
it out and switch them on again.

!!! tip "Getting your fist back"
    While an HM is lent, a bare-handed click fires it instead of punching. Open the Pokémon's wheel
    and pick the lent move again to hand it back, or simply recall the Pokémon.

## Cost

There is **no hunger cost** and nothing to pay. Each HM has a **cooldown**, kept per Pokémon, so a
second Pokémon with the same move is ready straight away. Auras cost nothing at all.

---

## The Trainer Ditto

A rare wandering **Trainer Ditto** turns up now and then and **sells three random Cobblemon TMs**
for **relic coins**. Right-click it to open its stall. Prices follow the power of the move, from 4
coins for a status move up to 32 for the strongest ones. Each TM is sold once per visit.

Keep what you buy in the [HM Case](tm-bag.md), which holds any number of TMs.

**It is a Ditto in a coat.** Throw a Poké Ball and you catch it like any other, but every trader
after that keeps its distance and **will not open its stall for you again**, so weigh the shop
against the Ditto. How good that Ditto is is the server's call, and **out of the box it rolls its
IVs like any other**: guaranteed perfect stats are an option an operator turns on, not something the
trader comes with. See [Configuration](configuration.md#trainer-ditto).

**One in 8192 is shiny**, at Cobblemon's own odds, and wears a shiny costume. Once caught it is an
**ordinary, non-shiny Ditto**: the shine was the costume, not the prize.

Each trader wears a random player skin, and keeps it for as long as it stands there.

??? note "For resource pack makers: adding faces"
    Every PNG under `assets/cobblemon_ditto_hms/textures/entity/trainer_ditto/` is in the pool, so a
    resource pack adds a face by dropping a file in. A file whose name contains `shiny` is kept for
    the shiny trader.
