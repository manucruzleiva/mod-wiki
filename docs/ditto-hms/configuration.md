# Configuration

<div class="flow" markdown>

1. <span class="flow__tag">Starts as</span> the built-in defaults
2. <span class="flow__tag">Saved in</span> `config/cobblemon_ditto_hms.json`
3. <span class="flow__tag">Changed with</span> the Cloth Config screen (through Mod Menu) or `/dittohm config`
4. <span class="flow__tag flow__tag--result">Result</span> the per-ability values the game uses

</div>

## Activation

How an HM fires is two settings, because no single answer suits everyone:

| Setting | Options | Notes |
|---|---|---|
| **Activator item** | Empty hand · HM Case · either *(default)* | The empty hand costs you punching and hand-mining while an HM is selected; the Case costs a hotbar slot |
| **Activator button** | **Left-click** *(default)* · Right-click · either | Left never opens chests or doors; right is answered by interactable blocks first |

There is also **HM wheel disc size** (50%–400%) in the same section, for when the discs read too
big or too small at your GUI scale.

Both activator settings live at the top of the config screen, and as commands:

```
/dittohm config activator item empty_hand|hm_case|either
/dittohm config activator button left|right|either
```

---

## Trainer Ditto

| Setting | Default | What it does |
|---|---|---|
| **Visits** | on | Whether the trader appears at all |
| **Appears every** | 36000 ticks (30 min) | How long the whole server waits between appearances |
| **Stays for** | 6000 ticks (5 min) | How long it waits before wandering off |
| **Guaranteed perfect IVs** | 0 | Rolled like any wild Ditto · 1 gives it one best stat · 6 is flawless |
| **Level** | 15–45 | The band its level is rolled from, inclusive |

```
/dittohm config trader enabled <true|false>
/dittohm config trader every <1200-1728000>
/dittohm config trader stay <200-72000>
/dittohm config trader ivs <0-6>
/dittohm config trader levels <min> <max>
```

One appearance is **one trader for the whole server**, not one per player, and everybody is told in
chat when it arrives and when it leaves. The clock runs while the server is empty and survives a
restart; an appearance that lands with nobody eligible is missed rather than saved up.

It always offers **five** discs, rolled once and kept for as long as that trader is standing there.
Which five is weighted per HM — see [Trader weight](#trader-weight) below.

It stops visiting a player for good once they catch it, and it keeps its distance from anyone who
has caught one **or beaten one in battle**, so bring a friend who has done neither.

---

## Per-ability values

Every ability has these tunable values:

| Parameter | Description |
|---|---|
| **Hunger** | Food levels required and consumed per use (0 = free) |
| **Cooldown** | Ticks between uses (20 ticks = 1 second; 0 = no cooldown) |
| **Power** | Ability-specific: radius, duration, damage, count, level, etc. |
| **HungerBlock** | *(toggles only)* food points blocked from your max while enabled |
| **Trader weight** | How often the Trainer Ditto offers this disc, against the others |
| **Required level** | Experience level needed before the HM will fire (every HM ships at 0) |

### Required level

A **requirement, not a price**: nothing is deducted when the HM fires, you simply cannot reach for
it until you have got there. Every HM ships at **0**, so nothing is gated unless a pack says so.

An HM you have not qualified for is greyed out in the wheel and says which level it wants, and it
comes back to life the moment you level up. Switching a toggle **off** is never gated, so raising a
requirement can never strand someone inside an effect they cannot end.

### Trader weight

A weight, not a percentage: what an HM's share works out to depends on which ones you still have
left to learn. **10** is the common default, **6** covers the ones that reshape how you mine or
fight, and **3** is reserved for flight, blinking, a free heal and a suit of armour. **0** keeps an
HM out of the stall entirely — unless everything you have left is at 0, in which case the roll
falls back to even odds rather than leaving the stall empty.

---

## Cloth Config GUI (Fabric)

Open **Mod Menu → Cobblemon Ditto HMs → ⚙** to see sliders for every ability's values.  
Changes save automatically.

---

## In-game commands

Operator-only (`permission level 2`):

```
/dittohm config <ability> hunger <0–20>
/dittohm config <ability> cooldown <0–24000>
/dittohm config <ability> power <0–512>
/dittohm config <ability> hungerblock <0–20>   (toggles only)
/dittohm config <ability> weight <0–100>
/dittohm config <ability> minlevel <0–100>
/dittohm config <ability> reset
/dittohm config reset_all
/dittohm config activator item <empty_hand|hm_case|either>
/dittohm config activator button <left|right|either>
```

---

## Config file

The file is saved at:

- **Fabric:** `config/cobblemon_ditto_hms.json`
- **NeoForge:** `config/cobblemon_ditto_hms.json`

You can edit it directly — changes take effect on next server start.

---

## Default values — Active HMs

Durations in the **Power** column are in **ticks** (20 ticks = 1 second), because that is
what the config takes.

| Ability | Hunger | Cooldown | Power |
|---|---|---|---|
| Leafage | 1 | 2s | 5 |
| Cut | 2 | none | 128 |
| Rock Smash | 2 | none | 32 |
| Camouflage | 3 | 15 min | duration — **18000** |
| Strength | 2 | none | 1 |
| Teleport | 6 | 30s | 30 |
| Stockpile | 1 | 1s | lava self-damage — **7** |
| Charge | 2 | 3s | ticks between sparks — **10** |
| Tail Whip | 2 | 2s | 1 |

## Default values — Toggle HMs

| Ability | HungerBlock | Power |
|---|---|---|
| Magnet Rise | 15 | 25 |
| Fly | 3 | — · each mid-air take-off costs **3** hunger, cooldown **1s** |
| Jump | 2 | Jump Boost level — **4** |
| Dive | 2 | — |
| Flash | 2 | — |
| Rock Climb | 2 | — |
| Lava Plume | 2 | tenths of the lava-stride multiplier — **17** |
| Snowscape | 2 | trail radius — **3** |
| Absorb | 2 | magnet radius — **6** |
| Lucky Chant | 2 | Luck amplifier — **1** |
| Shadow Sneak | 3 | percent of your speed you keep — **55** |

## Default values — Your Pokémon

[Field moves](pokemon.md#field-moves) never cost you hunger: **Hunger** is ignored, and **Cooldown**
is counted **per Pokémon**. Turning a move's `enabled` off in the file hides it from every wheel.

| Ability | Hunger | Cooldown | Power |
|---|---|---|---|
| Rain Dance | 5 | 10s | 6000 |
| Sunny Day | 5 | 10s | 6000 |
| Thief | 2 | 5s | 1 |
| Sweet Scent | 6 | 90s | how many turn up — **5** |
| Headbutt | 2 | 2s | 14 |
| Miracle Eye | 5 | 30s | search radius in CHUNKS, as /locate counts — **100** |
| Celebrate | 1 | 10 min | how many rockets — **8** |
| Present | 12 | 20 min | — |
| Blizzard | 6 | 30s | radius — **180** |
| Decorate | 4 | 1 min | percent chance of a shiny — **5** |
| Growth | 3 | 1 min | — |
| Minimize | 3 | 1 min | — |
| Outrage | 5 | 5 min | — |
| Calm Mind | 3 | 2 min | — |

[Mount toggles](pokemon.md#mount-toggles) block none of your hunger — they belong to the Pokémon.

| Ability | Power |
|---|---|
| Surf | tenths of the mount's swim-speed multiplier — **15** |
| Agility | tenths of the mount's land-speed multiplier — **15** |
| U-turn | tenths of the mount's turn multiplier — **18** |
| Helping Hand | tenths of the stamina SPEND — **2** |
| Tailwind | tenths of the mount's flight-speed multiplier — **15** |
| Swift | tenths of the mount's acceleration multiplier — **20** |

!!! note "Old config files"
    A config written before 4.0 is brought up to date on load, and only where the meaning of a value
    changed: Fly's glide price, Teleport's price (only if you had left it at the old default) and
    Agility's new mount scale. Retired HMs drop out of the file.
