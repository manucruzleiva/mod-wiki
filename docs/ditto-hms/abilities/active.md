# Partner HMs

Partner HMs are the ones your **empty fist** fires. One of your sent-out Pokémon **lends** you one:
open Cobblemon's interaction wheel on it, pick **Field moves**, then **"Lend me …"**. While that
Pokémon is out and within 24 blocks, a click with an empty hand fires the HM. One Pokémon lends one
HM at a time: picking another replaces it.

The only cost is a **cooldown, kept per Pokémon**: two Pokémon that both know Cut each have their own.

<div class="flow" markdown>

1. <span class="flow__tag">Do</span> Click with an empty hand
2. <span class="flow__tag flow__tag--check">Check</span> A Pokémon of yours, out and near you, is lending the HM
3. <span class="flow__tag flow__tag--check">Check</span> Your experience level is high enough (if the server sets one)
4. <span class="flow__tag flow__tag--check">Check</span> That Pokémon's cooldown has run out
5. <span class="flow__tag flow__tag--result">Result</span> The HM fires and that Pokémon's cooldown starts

</div>

<p class="flow__note">If any check fails, nothing happens.</p>

---

## Who can lend it

A Pokémon can lend an HM when the move is **in its movepool** (equipped or not) — including a move
merged into it, so a Pokémon with Dig can lend Rock Smash — or when its species is one of these:

| Disc | HM | Pokémon (any of) |
|---|---|---|
| <img class="hm-disc" src="../../../assets/items/hm_camouflage.png" alt=""> | Camouflage | Zorua, Kecleon, Ditto |
| <img class="hm-disc" src="../../../assets/items/hm_charge.png" alt=""> | Charge | Elekid, Electabuzz, Electivire |
| <img class="hm-disc" src="../../../assets/items/hm_cut.png" alt=""> | Cut | Scyther, Scizor, Kartana, Kleavor, Vikavolt |
| <img class="hm-disc" src="../../../assets/items/hm_leafage.png" alt=""> | Leafage | Bulbasaur, Chikorita, Treecko, Snivy, Drilbur, Excadrill |
| <img class="hm-disc" src="../../../assets/items/hm_rock_smash.png" alt=""> | Rock Smash | Hitmonchan, Machop, Geodude, Diglett, Dugtrio, Trapinch |
| <img class="hm-disc" src="../../../assets/items/hm_stockpile.png" alt=""> | Stockpile | Gulpin, Swalot, Squirtle, Totodile, Mudkip, Camerupt, Magcargo, Heatran |
| <img class="hm-disc" src="../../../assets/items/hm_strength.png" alt=""> | Strength | Machoke, Machamp, Conkeldurr |
| <img class="hm-disc" src="../../../assets/items/hm_tail_whip.png" alt=""> | Tail Whip | Rattata, Sentret, Buneary |
| <img class="hm-disc" src="../../../assets/items/hm_teleport.png" alt=""> | Teleport | Abra, Kadabra, Alakazam, Ralts |

---

## Ability details

### <img class="hm-disc" src="../../../assets/items/hm_camouflage.png" alt=""> Camouflage
**Cooldown:** 15 min · **Power:** 18000t (**15 minutes**)

Become the **living creature** you're looking at. Your model is replaced by theirs — species, form,
variant, gear and its nametag — for everyone who can see you.

- Aim at a **creature** in clear view → you look exactly like it for 15 minutes.
- **Fire it again while you are wearing one** → the costume comes off and the HM is ready
  immediately, so changing disguise is two presses.
- A block, a wall between you and it, or empty air → nothing happens. You can only copy something
  you can actually see.
- Other **players** can't be copied.

The disguise is a costume, not a creature: nothing extra exists in the world, so there is nothing
to hit, nothing in your way, and nothing that can be killed off you.

---

### <img class="hm-disc" src="../../../assets/items/hm_charge.png" alt=""> Charge
**Cooldown:** 3s · **Power:** 200t (**10 seconds**)

Turns the block you aim at into a redstone power source — enough to throw a door, a piston or a
lamp from across a room. **It does not run out.** The charge ends when you charge something else or
leave, and never on a timer: a power source that switches itself off after a minute is not a power
source, it is a fault to go and find.

The block is never replaced — it stays exactly what it is and simply *answers* as a power source —
so you can charge a chest, a furnace, a statue or a wall without losing anything. While it is live
it throws off **electric sparks**, so a charged block is one you can find again.

---

### <img class="hm-disc" src="../../../assets/items/hm_cut.png" alt=""> Cut
**Power:** max 128 blocks

Aim at a **log** and the whole tree comes down — every connected log, with the leaves and vines
tangled in it. Aim at a **leaf** or a **vine** and just that tangle goes.

It also **cuts plants**: grass, ferns, crops, ground cover. Those come away as if you had used
shears, so the drops are the careful ones — the grass itself rather than a couple of seeds — and
that holds for plants added by a datapack too, because it is the game's own loot tables answering.

**With nothing to cut in front of you, it clears the ground around you** (this is what X-Scissor
used to do), in two passes of decreasing politeness:

1. **Weeds first** — grass, ferns, dead bushes. If there are any, that is all it touches.
2. **Then what somebody planted** — flowers and crops, and *only* once there is not a single weed
   left in range (radius 5). Casting by accident in your own wheat field costs you the weeds, not
   the field.

It never strips grass down to dirt: as a fallback, that would go off every time you missed a tree.

---

### <img class="hm-disc" src="../../../assets/items/hm_leafage.png" alt=""> Leafage
**Cooldown:** 2s · **Power:** radius 5

Instantly grows **every crop around you** to full maturity — handy for fast harvests — and does
the same for saplings and berry trees.

The bare ground answers too, and it answers in **flowers**: a burst leaves a meadow rather than a
lawn, with the odd blade of grass among it. The blooms are ones that belong to the biome you are
standing in, so a burst in a plains looks nothing like one in a flower forest — and a biome with no
flowers of its own gets grass rather than a dandelion that does not belong there.

It only ever plants on **bare ground**. A spot that already has something growing on it is left
exactly as it stands, so casting twice in the same meadow thickens it instead of disturbing it, and
tall flowers are planted whole rather than as a half that topples.

**Crouch while you use it to till instead** (this is what Rototiller used to do): the dirt-type
block you aim at — Dirt, Grass Block, Coarse Dirt, Dirt Path — turns into Farmland.

---

### <img class="hm-disc" src="../../../assets/items/hm_rock_smash.png" alt=""> Rock Smash
**Power:** max 32 ores

Instantly breaks the block you aim at. If it's an **ore**, vein-mines all connected ore of that
type; otherwise breaks the single pickaxe-minable block (Netherite Pickaxe drops).

It **digs** too (this is what Dig used to do): dirt, sand, gravel and anything else a shovel takes
come out in one hit, free, with a Netherite Shovel's drops.

---

### <img class="hm-disc" src="../../../assets/items/hm_stockpile.png" alt=""> Stockpile
**Cooldown:** 1s · **Power:** lava self-damage 7 (3.5 hearts)

Stockpile is a mouthful you keep. It took over **Water Gun** and **Eruption**.

- **Aim at water or lava** (source or flowing) and you **drink it**. The pool is drained, and that
  fluid is now what you carry. Water is free; **lava is spicy** and burns going down.
- **Aim anywhere else** and you **spit it back out** on the face you are aiming at — the same square
  a bucket would fill. You can spit **as often as you like**: what you carry only changes when you
  drink the other fluid.
- Spitting water at a **sponge** soaks it.

It passes the same permission check a bucket does, so claims, spawn protection and the world border
all hold. Lava is never placed at your own feet, and water boils away in the Nether, as it would
from a bucket.

---

### <img class="hm-disc" src="../../../assets/items/hm_strength.png" alt=""> Strength


Pushes the aimed block one block in whichever of the six directions you're looking — up and down
included. Containers travel with their contents, and a **double chest moves as one unit**: both
halves go together, or the push fails if either has nowhere to go. Won't move fluids.

---

### <img class="hm-disc" src="../../../assets/items/hm_tail_whip.png" alt=""> Tail Whip
**Cooldown:** 2s

Sweeps a **suspicious sand or gravel** block clean in a single motion instead of a dozen slow ones,
and finds exactly what a brush would have found. **Rooted dirt** counts too: it is not brushable in
vanilla, but it is the same gesture on the same kind of thing, so it gives up its hanging roots.

---

### <img class="hm-disc" src="../../../assets/items/hm_teleport.png" alt=""> Teleport
**Cooldown:** 30s · **Power:** max 30 blocks

Blinks you to the block you're looking at (≤ 30 blocks), finding the nearest safe landing. Plays
the Enderman teleport sound.

It is the strongest way to travel the mod has, so it is priced like it: dearer than anything else
you fire, and slow to come back.

---
