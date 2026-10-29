# Commands

The command root is `/hms`.

| Who | Commands |
|---|---|
| 🙂 Every player | `list` · `mount` |
| 🛡️ Operators (level 2) | `list <player>` · `config …` · `trader …` |

There are no commands to learn, select or use an HM any more: your Pokémon lend them, from
Cobblemon's interaction wheel (see [Your Pokémon](pokemon.md)).

## Player commands

```
/hms list
```
Shows what your Pokémon are lending you right now: the HM on your fist and the auras in effect.

```
/hms mount
```
Reports what the mount boosts can see on the Pokémon you are riding. Useful for telling a broken
boost apart from riding something you did not expect.

---

## Operator commands

Require **permission level 2**.

```
/hms list <player>
```
The same report, for another player.

```
/hms trader spawn [player]
/hms trader spawn shiny [player]
/hms trader forget [player]
```
Summons a Trainer Ditto on demand, or undoes a catch so it will visit that player again.

```
/hms config <ability> cooldown <0–24000>
/hms config <ability> power <0–512>
/hms config <ability> minlevel <0–100>
/hms config <ability> enabled <true|false>
/hms config <ability> reset
/hms config reset_all
```

```
/hms config activator button <left|right|either>
/hms config trader enabled <true|false>
/hms config trader every <ticks>
/hms config trader stay <ticks>
/hms config trader ivs <0–6>
/hms config trader levels <min> <max>
/hms config trader coins <min> <max>
```

!!! tip "After updating to 4.0"
    There is nothing to reset. Every save is migrated the first time each player joins — see
    [Upgrading to 4.0](upgrading-to-4.md). Retired HMs no longer answer any command.

---

## Ability IDs

### Partner HMs

| ID | Display name |
|---|---|
| `leafage` | Leafage |
| `cut` | Cut |
| `rock_smash` | Rock Smash |
| `camouflage` | Camouflage |
| `strength` | Strength |
| `teleport` | Teleport |
| `stockpile` | Stockpile |
| `charge` | Charge |
| `tail_whip` | Tail Whip |
| `growth` | Growth |
| `minimize` | Minimize |
| `outrage` | Outrage |
| `calm_mind` | Calm Mind |

### Auras

| ID | Display name |
|---|---|
| `magnet_rise` | Magnet Rise |
| `jump` | Jump |
| `dive` | Dive |
| `flash` | Flash |
| `rock_climb` | Rock Climb |
| `lava_plume` | Lava Plume |
| `snowscape` | Snowscape |
| `absorb` | Absorb |
| `lucky_chant` | Lucky Chant |
| `shadow_sneak` | Shadow Sneak |
| `sweet_scent` | Sweet Scent |
| `sandstorm` | Sandstorm |
| `mist` | Mist |
