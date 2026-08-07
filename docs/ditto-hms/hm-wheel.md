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
              ╭──── outer ring: the 25 ACTIVE HMs ────╮
           Cut     Fly     Dig    Ember   Teleport   ...
        ╲     ╲      ╲      │      ╱      ╱     ╱
          ╲    ╭────────────────────────╮    ╱
            ╲  │  inner ring: 10 TOGGLES │  ╱
      Water ──┤   Jump  Surf  Dive  ...  ├── Thunder
            ╱  │                         │  ╲
          ╱    ╰────────────────────────╯    ╲
        ╱     ╱      ╱      │      ╲      ╲     ╲
           Rest   Charm  Strength  Waterfall   ...
                    ( centre: clear )
```

| What you see | What it means |
|---|---|
| A disc on a type-coloured segment | Learned, ready to pick |
| A dim pip on a dark segment | Not learned yet. The wheel never hints at which Pokémon unlocks it |
| A glowing, glinting slot | Currently selected (active) or currently switched on (toggle) |

The middle of the wheel names whatever your cursor is over, its type, and its state; the ability's
description sits just below the wheel.

---

## Picking an HM

| Ring | What a pick does |
|---|---|
| **Outer — active HMs** | Selects it. Selecting it again deselects it |
| **Inner — toggle HMs** | Switches it on or off straight away |
| **Centre** | Clears your selection |

Hold **H**, move the cursor onto a slot and let go — the wheel closes on whatever you were pointing
at. A quick tap instead leaves the wheel pinned open, so you can take your time and click.

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
    If you use the empty hand as your activator, picking the **centre** of the wheel clears the
    selection and gives you back punching and hand-mining. Setting the activator to **HM Case**
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
