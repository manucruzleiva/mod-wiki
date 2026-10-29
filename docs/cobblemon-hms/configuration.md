# Configuration

<div class="flow" markdown>

1. <span class="flow__tag">Starts as</span> the built-in defaults
2. <span class="flow__tag">Saved in</span> `config/cobblemon_hms.json`
3. <span class="flow__tag">Changed with</span> the Cloth Config screen or `/hms config`
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

Two more switches sit next to it:

| Setting | Default | What it does |
|---|---|---|
| **Pokémon must have learned the move** | on | A Pokémon offers an HM only if it has learned the move, equipped or not. Off: the move in its learnset, or its species, is enough |
| **Show active HMs on the HUD** | on | The list of HMs in effect in the top-left corner. A client setting: each player's own file decides |

```
/hms config requiremove <true|false>
/hms config hud <true|false>
```

---

## Pokémon upkeep

Working costs the Pokémon doing it. Each use of an HM it lends, and every minute an aura, a weather
or a ridden mount toggle of its stays on, takes some of its **fullness**. At 0 fullness it keeps
working, but what it cannot pay comes out of its **friendship**, and below a threshold it refuses
to do HMs until that goes back up. Feed it a berry to top it up.

| Setting | Default | What it does |
|---|---|---|
| **HMs cost the Pokémon fullness** | on | Off: HMs cost the Pokémon nothing |
| **Fullness per use** | 25 hundredths | Four uses to a berry. A Pokémon holds 2 to 7 points, by weight |
| **Fullness per minute kept on** | 20 hundredths | A berry every five minutes, for each HM kept on |
| **Friendship lost per missing fullness** | 5 | 0 = working hungry costs nothing. Friendship goes up to 255 |
| **Friendship needed to do HMs** | 1 | Refuses at 0 friendship · 0 = never refuses |

```
/hms config upkeep enabled <true|false>
/hms config upkeep use <0-700>
/hms config upkeep minute <0-700>
/hms config upkeep friendship <0-255>
/hms config upkeep minfriendship <0-255>
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
| **TM price** | 4–32 relic coins | The cheapest and dearest a TM can cost, used only when `trader_offers.json` is first written |

```
/hms config trader enabled <true|false>
/hms config trader every <1200-1728000>
/hms config trader stay <200-72000>
/hms config trader ivs <0-6>
/hms config trader levels <min> <max>
/hms config trader coins <min> <max>
/hms config trader reload
```

The live prices are in `config/cobblemon_hms/trader_offers.json`. Edit it and run
`/hms config trader reload` to apply it without a restart.

One appearance is **one trader for the whole server**, not one per player, and everybody is told in
chat when it arrives and when it leaves. The clock runs while the server is empty and survives a
restart; an appearance that lands with nobody eligible is missed rather than saved up.

It offers **three random Cobblemon TMs**, rolled once and kept for as long as that trader is
standing there, one of each. A TM's price follows the power of its move: a status move costs the
minimum, and the strongest moves cost the maximum.

It stops visiting a player for good once they catch it, and it keeps its distance from anyone who
has caught one **or beaten one in battle**, so bring a friend who has done neither.

---

## Per-ability values

Each HM has only the values it actually reads:

| Parameter | Which HMs | Description |
|---|---|---|
| **Enabled** | all | Off: no Pokémon lends it, it can't be learned and the Trainer Ditto won't sell it. Whoever already learned it keeps it |
| **Required level** | all | Experience level needed before the HM works for you (every HM ships at 0) |
| **Cooldown** | partner HMs, and Sweet Scent | Ticks between uses (20 ticks = 1 second; 0 = no cooldown), counted **per Pokémon**. For Sweet Scent it is the time between arrivals, at least 100 |
| **Power** | the HMs in the tables below that list a range | What it means depends on the HM: a radius, a duration, a speed in tenths. The menu's tooltip and the command say which |

Auras and mount toggles have no cooldown: they are simply on. Nothing costs the player hunger. The
cooldown belongs to the Pokémon that lent the move, so a second Pokémon with the same move is
ready straight away.

### Required level

A **requirement, not a price**: nothing is deducted when the HM fires, you simply cannot reach for
it until you have got there. Every HM ships at **0**, so nothing is gated unless a pack says so.
Switching an aura **off** is never gated, so raising a requirement can never strand someone inside
an effect they cannot end.

---

## Config screen

The same Cloth Config screen on both loaders (it needs [Cloth Config](https://modrinth.com/mod/cloth-config)):

- **Fabric:** Mod Menu → Cobblemon HMs → ⚙
- **NeoForge:** Mods → Cobblemon HMs → **Config**

Categories: **Activation**, **Pokémon upkeep**, **Trainer Ditto**, then one per HM. Short ranges
are sliders. Cooldowns, long durations and the Trainer Ditto's timers are typed in, with the same
ranges as the command. Each reset arrow goes back to the shipped value. In singleplayer, saving
applies at once.

On a dedicated server the screen edits your own game's file, not the server's. Use `/hms config`
there.

---

## In-game commands

Operator-only (`permission level 2`):

```
/hms config                      lists every HM with the move behind it
/hms config show                 every world-wide setting at once
/hms config <ability>            that HM's values, next to the defaults
/hms config <ability> cooldown <ticks>
/hms config <ability> power <value>
/hms config <ability> minlevel <0–100>
/hms config <ability> enabled <true|false>
/hms config <ability> reset
/hms config reset_all
```

`cooldown` and `power` only exist for an HM that reads them, and each takes the range in the
tables below. The full list is in [Commands](commands.md).

---

## Config file

The file is saved at `config/cobblemon_hms.json` on both loaders.

You can edit it directly. Changes take effect on next server start. It holds only the settings the
mod reads. The ones from before 4.0 (hunger costs, trader weights, cost order, activator item,
wheel icon scale) are dropped the next time it is saved.

---

## Default values — Partner HMs

Durations are in **ticks** (20 ticks = 1 second), because that is what the config takes.

| Ability | Cooldown | Power | Power range |
|---|---|---|---|
| Leafage | 40 (2s) | burst radius — **3** (a 7×7 patch) | 1–16 |
| Cut | none | most blocks felled — **128** | 1–256 |
| Rock Smash | none | most ore from one vein — **32** | 1–128 |
| Camouflage | 18000 (15 min) | ticks in disguise — **18000** | 20–24000 |
| Strength | none | — | |
| Dig | none | — | |
| Teleport | 600 (30s) | blocks of reach — **30** | 5–64 |
| Stockpile | 20 (1s) | lava self-damage, half hearts — **7** | 0–40 |
| Charge | 60 (3s) | ticks between sparks — **10** | 1–200 |
| Tail Whip | none | — | |
| Growth | 1200 (1 min) | ticks you stay big — **6000** | 20–24000 |
| Minimize | 1200 (1 min) | ticks you stay small — **6000** | 20–24000 |
| Outrage | 6000 (5 min) | — | |
| Calm Mind | 2400 (2 min) | — | |
| Celebrate | none | rockets — **8** | 1–32 |
| Decorate | 72000 (1 h) | — | |

Every cooldown takes 0–72000.

## Default values — Auras

| Ability | Power | Power range |
|---|---|---|
| Magnet Rise | flight speed, % of walking — **25** | 10–100 |
| Jump | Jump Boost level — **4** | 1–10 |
| Dive | — | |
| Flash | — | |
| Rock Climb | — | |
| Lava Plume | lava-stride multiplier in tenths — **17** | 10–40 |
| Snowscape | trail radius — **3** | 1–8 |
| Absorb | magnet radius — **6** | 1–24 |
| Lucky Chant | Luck level — **1** | 1–5 |
| Shadow Sneak | percent of your speed you keep — **55** | 10–100 |
| Sweet Scent | — · cooldown **1200** (60s) between arrivals, 100–72000 | |
| Sandstorm | how many times faster loose ground breaks — **4** | 1–32 |
| Mist | blocks away a hunter loses you — **8** | 2–32 |
| Rain Dance | — | |
| Sunny Day | — | |
| Blizzard | radius of the snowfall around you — **24** | 2–256 |

## Default values — Your Pokémon

[Mount toggles](pokemon.md#mount-toggles) belong to the Pokémon you ride.

| Ability | Power | Power range |
|---|---|---|
| Surf | tenths of the mount's swim-speed multiplier — **15** | 10–50 |
| Agility | tenths of the mount's land-speed multiplier — **15** | 10–50 |
| U-turn | tenths of the mount's turn (handling) multiplier, never past the stat's maximum of 100 — **18** | 10–50 |
| Helping Hand | tenths of the stamina SPEND, from 1 (a tenth) to 10 (no help) — **2** | 1–10 |
| Tailwind | tenths of the mount's flight-speed multiplier — **15** | 10–50 |
| Swift | tenths of the mount's acceleration multiplier — **20** | 10–50 |

!!! note "Old config files"
    A config written before 4.0 is brought up to date on load, and only where the meaning of a value
    changed. Retired HMs (Fly, Glide, Headbutt, Thief and the combat HMs) drop out of the file.
