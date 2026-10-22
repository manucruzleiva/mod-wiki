# Auras

Auras are **passive HMs your Pokémon give you** while they are out and near you (24 blocks). Open
Cobblemon's interaction wheel on one of your sent-out Pokémon, pick **Field moves**, and switch an
aura on; it shows **✔** while it is on. Recall the Pokémon or walk away from it and the aura stops;
it comes back when the Pokémon does.

You can run as many auras as you like, from one Pokémon or several. They cost nothing.

The toggles that make **a mount** better — Surf, Tailwind, Swift, U-turn, Helping Hand and Agility —
belong to the Pokémon you ride: see [Your Pokémon](../pokemon.md#mount-toggles).

!!! tip "HUD icons"
    Every aura in effect shows its **own HM status-effect icon** in your HUD (top-right), so it's
    obvious at a glance which ones are on.

---

## Who can give it

A Pokémon can give an aura when the move is **in its movepool** (equipped or not), or when its
species is one of these:

| Disc | Aura | Pokémon (any of) |
|---|---|---|
| <img class="hm-disc" src="../../../assets/items/hm_absorb.png" alt=""> | Absorb | Gulpin, Swalot, Victreebel |
| <img class="hm-disc" src="../../../assets/items/hm_dive.png" alt=""> | Dive | Vaporeon, Lapras, Wailord |
| <img class="hm-disc" src="../../../assets/items/hm_flash.png" alt=""> | Flash | Ampharos, Jolteon, Lanturn |
| <img class="hm-disc" src="../../../assets/items/hm_jump.png" alt=""> | Jump | Magikarp, Buneary, Spoink |
| <img class="hm-disc" src="../../../assets/items/hm_lava_plume.png" alt=""> | Lava Plume | Magcargo, Slugma, Turtonator |
| <img class="hm-disc" src="../../../assets/items/hm_lucky_chant.png" alt=""> | Lucky Chant | Clefairy, Chimecho, Togetic |
| <img class="hm-disc" src="../../../assets/items/hm_magnet_rise.png" alt=""> | Magnet Rise | Magnemite, Magneton, Magnezone |
| <img class="hm-disc" src="../../../assets/items/hm_rock_climb.png" alt=""> | Rock Climb | Rhydon, Rhyperior, Sneasel |
| <img class="hm-disc" src="../../../assets/items/hm_shadow_sneak.png" alt=""> | Shadow Sneak | Gengar, Banette, Spiritomb |
| <img class="hm-disc" src="../../../assets/items/hm_snowscape.png" alt=""> | Snowscape | Froslass, Mamoswine |
| <img class="hm-disc" src="../../../assets/items/hm_sweet_scent.png" alt=""> | Sweet Scent | Gloom, Bellossom, Vileplume, Aromatisse |

---

## Ability details

### <img class="hm-disc" src="../../../assets/items/hm_absorb.png" alt=""> Absorb
**Power:** magnet radius 6

<img class="hm-disc" src="../../../assets/items/hud_absorb.png" alt=""> — how it shows in your status bar while it runs.

Loose items on the ground drift toward you while it is on, so a scattered drop or a mined vein
gathers itself. Items are nudged rather than yanked, so they keep their normal pickup delay.

---

### <img class="hm-disc" src="../../../assets/items/hm_dive.png" alt=""> Dive

<img class="hm-disc" src="../../../assets/items/hud_dive.png" alt=""> — how it shows in your status bar while it runs.

Lets you **live and work underwater**. Water stops getting in your way:

- **Breathe underwater** — never run out of air.
- **Walk the seabed as if it were dry land** — no wading, no drag on every step.
- **Mine at full speed** — a block underwater breaks as fast as the same block in open air, and
  the weight a guardian temple puts on your arms lifts while you're under.

Dive takes penalties away; it never hands out a bonus. Push off the bottom and you swim at exactly
the speed you always did — if you want to be *fast* in the water, ride a Pokémon with [Surf](../pokemon.md#mount-toggles) switched on.

---

### <img class="hm-disc" src="../../../assets/items/hm_flash.png" alt=""> Flash

<img class="hm-disc" src="../../../assets/items/hud_flash.png" alt=""> — how it shows in your status bar while it runs.

Lets you **see clearly in the dark**, even in caves and at night. Toggle off to remove instantly.

---

### <img class="hm-disc" src="../../../assets/items/hm_jump.png" alt=""> Jump
**Power:** Jump Boost level (default **IV**)

<img class="hm-disc" src="../../../assets/items/hud_jump.png" alt=""> — how it shows in your status bar while it runs.

Applies continuous **Jump Boost**. The `power` value equals the buff level, so `power = 4` gives Jump Boost IV. Shows in your HUD.

---

### <img class="hm-disc" src="../../../assets/items/hm_lava_plume.png" alt=""> Lava Plume
**Power:** tenths of the movement multiplier (default 17)

<img class="hm-disc" src="../../../assets/items/hud_lava_plume.png" alt=""> — how it shows in your status bar while it runs.

Dive's twin for lava. It lets you **live and work down there**: you **do not burn**, you move
through lava and walk its floor without the fluid dragging on every step, and you breathe while you
are under. Swimming out is exactly as it always was — like Dive, it takes a penalty away rather than
handing out a bonus.

It used to need Burning Bulwark for the fire protection. Burning Bulwark went to Cobblemon Action
Combat, so Lava Plume now covers that on its own.

---

### <img class="hm-disc" src="../../../assets/items/hm_lucky_chant.png" alt=""> Lucky Chant

<img class="hm-disc" src="../../../assets/items/hud_lucky_chant.png" alt=""> — how it shows in your status bar while it runs.

Fortune leans your way while it lasts: what you break and what you fish give up a little more.

---

### <img class="hm-disc" src="../../../assets/items/hm_magnet_rise.png" alt=""> Magnet Rise

<img class="hm-disc" src="../../../assets/items/hud_magnet_rise.png" alt=""> — how it shows in your status bar while it runs.

**Flight.** Switch it on and you are off the ground for as long as you like, drifting at half your
walking pace with no dash.

It is a **building** tool, not a way to travel: for that, ride one of your flying Pokémon.

---

### <img class="hm-disc" src="../../../assets/items/hm_rock_climb.png" alt=""> Rock Climb

<img class="hm-disc" src="../../../assets/items/hud_rock_climb.png" alt=""> — how it shows in your status bar while it runs.

Every vertical surface behaves like a ladder, and it is steered by the **movement keys**: **W**
climbs, **S** descends, and holding nothing holds your place on the wall.

Your horizontal movement is left alone, so you can travel along a face and step off it whenever you
like — a wall is something to climb, not something to be stuck to. On the ground it only takes over
when you are actually asking to go up, so walking and jumping near a wall work normally.

**It works on your mount too.** Riding a Pokémon, run into a wall holding **W** and your Pokémon
climbs it with you.

---

### <img class="hm-disc" src="../../../assets/items/hm_shadow_sneak.png" alt=""> Shadow Sneak
**Power:** percent of your speed you keep (default **55**)

<img class="hm-disc" src="../../../assets/items/hud_shadow_sneak.png" alt=""> — how it shows in your status bar while it runs.

Total stealth on foot. No footstep sounds, no name over your head, and **nothing underfoot notices
you** — not pressure plates, not tripwires, not a sculk sensor.

You move slower than a walk for it, though faster than a crouch, so it is something you can actually
travel in rather than a stationary hiding trick.

!!! note "If you are already on a scoreboard team"
    The hidden nametag is done with a vanilla team, so a player who already belongs to one keeps
    their team and simply does not get that part of the effect. Everything else still applies.

---

### <img class="hm-disc" src="../../../assets/items/hm_snowscape.png" alt=""> Snowscape
**Power:** trail radius 3

<img class="hm-disc" src="../../../assets/items/hud_snowscape.png" alt=""> — how it shows in your status bar while it runs.

Winter follows you on foot: snow settles around you as you walk, and **still water freezes over** as
you cross it. Flowing water is left alone, so a river keeps running instead of being paved.

---

---

### <img class="hm-disc" src="../../../assets/items/hm_sweet_scent.png" alt=""> Sweet Scent
**Cooldown:** 60s between arrivals

Works like a **Poké Snack you carry around**. While it is on, a wild Pokémon from the area turns up
near you about once a minute. It uses Cobblemon's own spawner with the Poké Snack's rules, so what
arrives is what lives there, and it never brings a herd.
