# Configuration

<div class="flow" markdown>

1. <span class="flow__tag">Starts as</span> the built-in defaults
2. <span class="flow__tag">Saved in</span> `config/cobblemon_hms.json`
3. <span class="flow__tag">Changed with</span> the Cloth Config screen (through Mod Menu) or `/hms config`
4. <span class="flow__tag flow__tag--result">Result</span> the per-ability values the game uses

</div>

## Activation

A partner HM fires from your **empty hand**: there is nothing to hold and nothing to select. The one
choice left is the button:

| Setting | Options | Notes |
|---|---|---|
| **Activator button** | Left-click · Right-click · **either** *(default)* | Left never opens chests or doors; right is answered by interactable blocks first |

```
/hms config activator button left|right|either
```

---

## Trainer Ditto

| Setting | Default | What it does |
|---|---|---|
| **Visits** | on | Whether new traders appear. Switching it off leaves any trader already out to finish its visit |
| **Appears every** | 36000 ticks (30 min) | How long the whole server waits between appearances |
| **Stays for** | 6000 ticks (5 min) | How long it waits before wandering off. It is never despawned earlier, and never in the middle of a battle or a catch |
| **Guaranteed perfect IVs** | 0 | Rolled like any wild Ditto · 1 gives it one best stat · 6 is flawless |
| **Level** | 15–45 | The band its level is rolled from, inclusive |
| **TM price** | 4–32 relic coins | The cheapest and dearest a TM can cost |

```
/hms config trader enabled <true|false>
/hms config trader every <1200-1728000>
/hms config trader stay <200-72000>
/hms config trader ivs <0-6>
/hms config trader levels <min> <max>
/hms config trader coins <min> <max>
```

One appearance is **one trader for the whole server**, not one per player, and everybody is told in
chat when it arrives and when it leaves. The clock runs while the server is empty and survives a
restart; an appearance that lands with nobody eligible is missed rather than saved up. It turns up
24 to 48 blocks from a player who has never caught one, on solid ground, in whatever dimension that
player is in (under the Nether's roof, near the player's own height). A trader left in a chunk that
nobody visits leaves quietly the next time someone comes close.

It offers **three random Cobblemon TMs**, rolled once and kept for as long as that trader is
standing there, one of each. A TM's price follows the power of its move: a status move costs the
minimum, and the strongest moves cost the maximum.

It stops visiting a player for good once they catch it, and it keeps its distance from anyone who
has caught one **or beaten one in battle**, so bring a friend who has done neither.

---

## Per-ability values

Every HM has these tunable values:

| Parameter | Description |
|---|---|
| **Cooldown** | Ticks between uses (20 ticks = 1 second; 0 = no cooldown), counted **per Pokémon** |
| **Power** | Ability-specific: radius, duration, damage, count, level, etc. |
| **Required level** | Experience level needed before the HM will fire (every HM ships at 0) |
| **Enabled** | Off hides the HM from every Pokémon |

Nothing costs hunger any more. The cooldown belongs to the Pokémon that lent the move, so a second
Pokémon with the same move is ready straight away.

### Required level

A **requirement, not a price**: nothing is deducted when the HM fires, you simply cannot reach for
it until you have got there. Every HM ships at **0**, so nothing is gated unless a pack says so.
Switching an aura **off** is never gated, so raising a requirement can never strand someone inside
an effect they cannot end.

---

## Cloth Config GUI (Fabric)

Open **Mod Menu → Cobblemon HMs → ⚙** to see sliders for every ability's values.  
Changes save automatically.

---

## In-game commands

Operator-only (`permission level 2`):

```
/hms config <ability> cooldown <0–24000>
/hms config <ability> power <0–512>
/hms config <ability> minlevel <0–100>
/hms config <ability> enabled <true|false>
/hms config <ability> reset
/hms config reset_all
/hms config activator button <left|right|either>
```

---

## Config file

The file is saved at:

- **Fabric:** `config/cobblemon_hms.json`
- **NeoForge:** `config/cobblemon_hms.json`

You can edit it directly — changes take effect on next server start. Settings from before 4.0 that
no longer do anything (hunger, activator item) are left in the file and ignored; the old trader
weight is dropped from it.

---

## Default values — Partner HMs

Durations in the **Power** column are in **ticks** (20 ticks = 1 second), because that is
what the config takes.

| Ability | Cooldown | Power |
|---|---|---|
| Leafage | 2s | 5 |
| Cut | none | 128 |
| Rock Smash | none | 32 |
| Camouflage | 15 min | duration — **18000** |
| Strength | none | 1 |
| Teleport | 30s | 30 |
| Stockpile | 1s | lava self-damage — **7** |
| Charge | 3s | ticks between sparks — **10** |
| Tail Whip | 2s | — |
| Growth | 1 min | how long you stay big — **6000** |
| Minimize | 1 min | how long you stay small — **6000** |
| Outrage | 5 min | — |
| Calm Mind | 2 min | — |
| Celebrate | 10 min | how many rockets — **8** |

## Default values — Auras

| Ability | Power |
|---|---|
| Magnet Rise | 25 |
| Jump | Jump Boost level — **4** |
| Dive | — |
| Flash | — |
| Rock Climb | — |
| Lava Plume | tenths of the lava-stride multiplier — **17** |
| Snowscape | trail radius — **3** |
| Absorb | magnet radius — **6** |
| Lucky Chant | Luck amplifier — **1** |
| Shadow Sneak | percent of your speed you keep — **55** |
| Sweet Scent | — · cooldown **60s** between arrivals (minimum 5s) |
| Sandstorm | how many times faster loose ground breaks — **4** |
| Fog | blocks away a hunter loses you — **8** |
| Rain Dance | — |
| Sunny Day | — |
| Blizzard | radius of the snowfall around you — **24** |

## Default values — Your Pokémon

[Mount toggles](pokemon.md#mount-toggles) belong to the Pokémon you ride.

| Ability | Power |
|---|---|
| Surf | tenths of the multiplier on the mount's swim-speed stat — **15** |
| Agility | tenths of the mount's land-speed multiplier — **15** |
| U-turn | tenths of the mount's turn multiplier — **18** |
| Helping Hand | tenths of the stamina SPEND — **2** |
| Tailwind | tenths of the multiplier on the mount's flight-speed stat — **15** |
| Swift | tenths of how much quicker the mount gets up to speed — **20** (half the time) |

!!! note "Old config files"
    A config written before 4.0 is brought up to date on load, and only where the meaning of a value
    changed. Retired HMs (Fly, Glide, Headbutt, Thief and the combat HMs) drop out of the file.
