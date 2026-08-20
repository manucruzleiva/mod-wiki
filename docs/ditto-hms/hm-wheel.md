# HM Wheel

Every HM you have learned lives in the **HM wheel** — a radial selector you open with a keypress.
There is nothing to craft and nothing to carry: learn an ability and it is in the wheel.

Press **H** (rebindable under *Options → Controls → Cobblemon Ditto HMs*) to open it.

---

## Reading the wheel

The wheel has two rings. Each slot shows that HM's disc, and the segment behind it is tinted with
the **type of the move the HM is named after** — so Water HMs sit in blue, Fire in orange, and a
familiar HM is easy to find by colour before you can read the label.

```
   ▓                ╭──── outer ring: ACTIVE HMs ────╮
   ▓ f           Cut     Fly     Dig    Ember   Teleport   ...
   ▓ o        ╲     ╲      ╲      │      ╱      ╱     ╱
   ▓ o          ╲    ╭───────────────────────╮    ╱
   ░ d            ╲  │  inner ring: TOGGLES  │  ╱
   ░              ──┤   Jump  Surf  Dive ●   ├──
   ░ b            ╱  │                       │  ╲
   █ a          ╱    ╰───────────────────────╯    ╲
   █ r        ╱     ╱      ╱      │      ╲      ╲     ╲
   █             Rest   Charm  Strength  Waterfall   ...
   █                  ( ✖ cancel · 🧹 clear all )
```

| What you see | What it means |
|---|---|
| A disc on a type-coloured segment | Learned, ready to pick |
| A dim pip on a dark segment | Not learned yet. The wheel never hints at which Pokémon unlocks it |
| **A disc that has grown** | The slot under your cursor — release now and this is what you get |
| **A slot pulsing with light, ringed and glinting** | Currently selected (active) or currently switched on (toggle) |
| **A small light in the corner of a disc** | This is a **toggle**. Green means it is running right now; dark means it is not |

The two cues never collide: **size** always means "the one I am about to pick", and **light** always
means "this one is live". Hover a live HM and you see both at once.

Only **toggles** carry the little corner light, so its presence tells you what kind of HM you are
looking at and its colour tells you whether that one is on. The glow cannot answer the second
question on its own, because a selected active glows too.

The middle of the wheel names whatever your cursor is over, its type, and its state; the ability's
description sits just below the wheel.

---

## The food bar

A column of twenty pips stands down the left of the wheel, and it answers three questions at once:

| Colour | What it is |
|---|---|
| **Red, at the top** | Maximum your running toggles have taken. Not yours again until one goes off |
| **Full** | What you have left |
| **Empty** | Room to eat |
| **Flashing** | What the HM under your cursor would cost, before you commit to it |

Hover an **active** and it flashes what that use would eat off the top of what you are carrying.
Hover a **toggle** and it flashes the slice of maximum it would claim — or, if it is already on, the
slice it would hand back.

!!! tip "Your food is not wasted"
    At the cap the game would normally still let you eat, because your bar is not full. It is
    refused instead, so a steak is never spent on nothing.

---

## Picking an HM

| Ring | What a pick does |
|---|---|
| **Outer — active HMs** | Selects it. Selecting it again deselects it |
| **Inner — toggle HMs** | Switches it on or off straight away |
| **Centre ring (🧹 brushes)** | Clears everything — your selection *and* every toggle |
| **Bullseye (✖)** | Cancel — closes the wheel and changes nothing |
| **Right-click a slot** | Stars it as a favourite. The wheel stays open |
| **Scroll** | Resizes the discs, and remembers it |

Hold **H**, move the cursor onto a slot and let go — the wheel closes on whatever you were pointing
at. A quick tap instead leaves the wheel pinned open, so you can take your time and click.

### The short wheel

**Hold the HM Case and open the wheel, and only your favourites are on it.** With fifty HMs the full
wheel is a lot to read when you use six of them, and the Case is already in your hand as the
activator — so it doubles as the quick way in. It still fires your selection exactly as before.

Star a slot by **right-clicking** it in the normal wheel; a starred slot carries a gold star, and
right-clicking again takes it off. The list is saved with your world.

If you have not starred anything yet, the Case opens the full wheel and says so rather than showing
you an empty ring.

Letting go anywhere that is not a slot cancels too: the gap between the rings, the band between the
centre and the toggles, and everywhere outside the wheel. A release that is not clearly aimed at
something changes nothing, so you can open the wheel, look, and back out.

---

## Using an active HM

Selecting an active HM does not fire it — a click does. **Which** click is up to you, in
[Configuration](configuration.md):

| Activator item | What it costs you |
|---|---|
| **Empty hand** | While an HM is selected, a bare-handed click fires it instead of punching or hand-mining |
| **HM Case** | A hotbar slot. Your fist keeps working |
| **Either** *(default)* | Nothing — both work |

| Activator button | Notes |
|---|---|
| **Left-click** *(default)* | Never opens a chest or a door |
| **Right-click** | Interactable blocks answer first, so a chest still opens instead of firing your HM |
| **Either** | Both work |

Left-click is the default. Whatever you pick, anything else in your hand keeps its normal click: tools mine, weapons swing and
blocks place exactly as they always did.

!!! tip "Getting your fist back"
    If you use the empty hand as your activator, picking the **centre ring** of the wheel clears
    the selection and gives you back punching and hand-mining. Setting the activator to **HM Case**
    avoids the trade entirely.

Toggle HMs need none of this — they are on the moment you switch them on in the wheel, and stay on
until you switch them off.

### The HM Case

A single craftable item whose only job is to be something to click with. It stores nothing, so any
Case behaves like any other and there is no reason to carry two.

<div class="cr-craft" title="Shapeless: Chest + Diamond + all 7 Apricorns → HM Case">
  <div class="cr-grid">
    <div class="cr-slot"><img src="../../assets/items/chest.png" alt="Chest"></div>
    <div class="cr-slot"><img src="../../assets/items/diamond.png" alt="Diamond"></div>
    <div class="cr-slot"><img src="../../assets/items/red_apricorn.png" alt="Red Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/yellow_apricorn.png" alt="Yellow Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/green_apricorn.png" alt="Green Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/blue_apricorn.png" alt="Blue Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/black_apricorn.png" alt="Black Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/white_apricorn.png" alt="White Apricorn"></div>
    <div class="cr-slot"><img src="../../assets/items/pink_apricorn.png" alt="Pink Apricorn"></div>
  </div>
  <div class="cr-arrow">➜</div>
  <div class="cr-result"><img src="../../assets/items/hm_case.png" alt="HM Case"></div>
</div>

---

## Without opening the wheel

### A key per HM

Every HM has its own keybind under *Options → Controls → Cobblemon Ditto HMs*. They are all
**unbound by default** — binding 38 keys for you would collide with half the game — so pick the two
or three you reach for constantly and leave the rest to the wheel.

A keybind ignores the activator entirely: it works whatever is in your hand and wherever you are
looking, which makes it the surest way to use sky-facing HMs like Fly and Magnet Rise.

### Commands

`/dittohm select <ability>` picks an active HM, and `/dittohm select none` clears the selection.
`/dittohm use <ability>` fires an active HM or flips a toggle directly. See
[Commands](commands.md).

---

## When an HM doesn't fire

It will tell you why, on the action bar, with a short thud — still recharging, too hungry, not in
water, not off the ground, or nothing in front of you to use it on. An HM that does nothing and
says nothing is a bug; please [report it](../reporting.md).

---

## HMs belong to you, not to an item

Learning is tracked **per player**, server-side, and survives death and world reloads. The HM Disc
is only the teacher: right-click it once and it has done its job.

---

## Disc size

**Scroll on the wheel** to make the discs bigger or smaller. Where you leave it is remembered on
your own machine and carried between worlds — the right size depends on your monitor, your GUI
scale and how many HMs you happen to know, none of which a server can see.

A server can set the size everyone *starts* at, in the config; scrolling is your answer to it.
