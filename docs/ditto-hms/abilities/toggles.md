# Toggle HMs

Toggle HMs are **passive abilities** that stay active until you turn them off.
Switch them on from the inner ring of the [HM wheel](../hm-wheel.md), or with `/dittohm use <id>`.

There are **14 toggle HMs**.

!!! tip "HUD icons"
    Every enabled toggle shows its **own HM status-effect icon** in your HUD (top-right), so
    it's obvious at a glance which toggles are on. Wherever the game has an equivalent attribute,
    the toggle uses that instead of a status effect, so the HM entry is the only one in your
    inventory rather than a hidden duplicate sitting next to it.

---

## Hunger cost

```mermaid
flowchart LR
    A[🔄 Toggle ON] --> B[🍗 Blocks part of your\nmax food bar]
    A --> C[🖼️ Own HM icon\nshows in the HUD]
    A --> D[✨ Passive effect\nruns every tick]
    E[🔄 Toggle OFF] --> F[Effects removed\nimmediately + hunger\ncap restored]
```

Each enabled toggle **blocks food points** from your maximum food bar (most block 2; **Harden blocks 3**, **Burning Bulwark blocks 4**).
At your effective cap a slow **Regeneration I** effect keeps you healing normally.
The cap never drops below **2**.

| Food points blocked | Max hunger |
|---|---|
| 0 | 20 / 20 |
| 2 | 18 / 20 |
| 4 | 16 / 20 |
| 6 | 14 / 20 |
| 8 | 12 / 20 |
| … | … |
| 18+ | 2 / 20 (floor) |

When a toggle is turned **off**, its effects are removed **immediately**.

---

## Acquisition

| HM | Pokémon (any of) | Trigger item |
|---|---|---|
| Jump | Magikarp, Buneary, Spoink | Cod |
| Surf | Lapras, Kyogre, Suicune | Kelp |
| Rollout | Graveler, Golem, Spheal | Cobblestone |
| Dive | Vaporeon, Lapras, Wailord | Nautilus Shell |
| Flash | Ampharos, Jolteon, Lanturn | Glowstone Dust |
| Rock Climb | Rhydon, Rhyperior, Sneasel | Chain |
| Mean Look | Mimikyu, Gengar, Noctowl | Ominous Bottle |
| Harden | Metapod, Kakuna, Silcoon, Cascoon | Shield |
| Glide | Dragonite, Togekiss, Aerodactyl | Feather |
| Burning Bulwark | Gouging Fire | Blaze Rod |
| Helping Hand | Plusle, Minun, Audino | Saddle |
| Lava Plume | Magcargo, Slugma, Turtonator | Magma Cream |
| Tailwind | Talonflame, Noivern, Staraptor | Breeze Rod |
| Swift | Ninjask, Accelgor, Electrode | Sugar |
| Absorb | Gulpin, Swalot, Victreebel | Hopper |
| Bounce | Spoink, Aipom, Hoppip | Slime Ball |
| Snowscape | Froslass, Mamoswine | Blue Ice |
| Vine Whip | Bulbasaur, Tangela | Vine |

---

## Ability details

### Jump
**Blocks:** 2 · **Power:** Jump Boost level (default **IV**)

Applies continuous **Jump Boost**. The `power` value equals the buff level, so `power = 4` gives Jump Boost IV. Shows in your HUD.

### Surf
**Blocks:** 2 · **Power:** tenths of the multiplier (default 15)

Whatever you are **riding** cuts through water half again as fast. Your own swimming, on foot, is
untouched. Surf's twin in the air is **Tailwind**.

### Rollout
**Blocks:** 2 · **Power:** speed amount

Increases your **movement speed** while active.

### Dive
**Blocks:** 2

Lets you **live and work underwater**. Water stops getting in your way:

- **Breathe underwater** — never run out of air.
- **Walk the seabed as if it were dry land** — no wading, no drag on every step.
- **Mine at full speed** — a block underwater breaks as fast as the same block in open air, and
  the weight a guardian temple puts on your arms lifts while you're under.

Dive takes penalties away; it never hands out a bonus. Push off the bottom and you swim at exactly
the speed you always did — if you want to be *fast* in the water, that's [Surf](#surf).

### Flash
**Blocks:** 2

Lets you **see clearly in the dark**, even in caves and at night. Toggle off to remove instantly.

### Rock Climb
**Blocks:** 2

Lets you **climb any wall you're facing** — while airborne, look at a wall to climb up; hold
**sneak** to climb down. No vanilla movement buffs are applied.

### Mean Look
**Blocks:** 2 · **Power:** detect radius (default 30)

Nearby **hostile mobs flee from you**, running away with real pathfinding — exactly like creepers
running from a cat (they even sprint when you get close). It **never** affects Pokémon, friendly
mobs, or other players.

### Harden
**Blocks:** 3

Hardens your body to **greatly reduce the damage you take** (+20 armour, +8 toughness applied via
attributes, plus damage resistance). Costs more hunger than other toggles.

### Glide
**Blocks:** 2

Lets you **glide like an Elytra without needing the item**. While airborne the real Elytra gliding
kicks in — dive to gain speed, level off to glide far. (Fly auto-enables this.)

### Swift
**Blocks:** 2 · **Power:** tenths of the multiplier (default 20)

Whatever you are riding **gets up to speed twice as quickly** — off the mark, out of a turn, after
every stop. The only one of the three mount toggles that is not about top speed: **Surf** is faster
in water and **Tailwind** faster in the air, while Swift is quicker to get there in all three.

---

### Tailwind
**Blocks:** 2 · **Power:** tenths of the multiplier (default 15)

A following wind for whatever you are **flying** on: it moves half again as fast through the air.
Tailwind's twin in water is **Surf**.

---

### Lava Plume
**Blocks:** 2 · **Power:** tenths of the movement multiplier (default 17)

Dive's twin for lava. It lets you **live and work down there**: move through lava and walk its floor
without the fluid dragging on every step, and breathe while you are under. Swimming out is exactly
as it always was — like Dive, it takes a penalty away rather than handing out a bonus.

**It gives you no fire protection of its own.** That is [Burning Bulwark](#burning-bulwark)'s job,
and two HMs handing out the same immunity would make one of them pointless — so Lava Plume asks for
it instead: you must have learned Burning Bulwark to switch Lava Plume on, and switching Lava Plume
on switches Burning Bulwark on with it. Between them they block 6 food from your maximum.

For the ride to the surface of a **water** pool, that is still **Waterfall**.

---

### Helping Hand
**Blocks:** 2 · **Power:** tenths of the stamina multiplier (default 20 = double)

Whatever you are riding keeps going **about twice as long** before it tires. Nothing else about the
mount changes — it is not faster, it does not recover any quicker, it simply has more in the tank.

```
/dittohm config helping_hand power <0-512>
```

---

### Burning Bulwark
**Blocks:** 4 · **Power:** thorns damage (default 2)

Makes you **immune to fire** and **scorches hostile mobs that get too close** — any hostile within
~1.6 blocks is set alight and takes thorns damage twice a second. Pokémon and friendly mobs are
never harmed.

---

### Absorb
**HungerBlock:** 2 · **Power:** magnet radius 6

Loose items on the ground drift toward you while it is on, so a scattered drop or a mined vein
gathers itself. Items are nudged rather than yanked, so they keep their normal pickup delay.

---

### Bounce
**HungerBlock:** 2

Every block you land on answers like a slime block. The harder you come down the higher you go, up
to a ceiling — and the bounce carries the impact away, so the landing doesn't hurt.

A short step doesn't bounce; you'd never get anywhere.

---

### Snowscape
**HungerBlock:** 2 · **Power:** trail radius 3

Winter follows you on foot: snow settles around you as you walk, and **still water freezes over** as
you cross it. Flowing water is left alone, so a river keeps running instead of being paved.

---

### Vine Whip
**HungerBlock:** 2 · **Power:** 3 extra blocks of reach

Reach further — blocks and creatures several paces away come within arm's length. Mining, placing
and hitting all get the extra range.
