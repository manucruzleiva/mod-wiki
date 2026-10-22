# Commands

The command root is `/dittohm`.

| Who | Commands |
|---|---|
| 🙂 Every player | `list` · `mount` |
| 🛡️ Operators (level 2) | `list <player>` · `config …` · `trader …` |

There are no commands to learn, select or use an HM any more: your Pokémon lend them, from
Cobblemon's interaction wheel (see [Your Pokémon](pokemon.md)).

## Player commands

```
/dittohm list
```
Shows what your Pokémon are lending you right now: the HM on your fist and the auras in effect.

```
/dittohm mount
```
Reports what the mount boosts can see on the Pokémon you are riding. Useful for telling a broken
boost apart from riding something you did not expect.

---

## Operator commands

Require **permission level 2**.

```
/dittohm list <player>
```
The same report, for another player.

```
/dittohm trader spawn [player]
/dittohm trader spawn shiny [player]
/dittohm trader forget [player]
```
Summons a Trainer Ditto on demand, or undoes a catch so it will visit that player again.

```
/dittohm config <ability> cooldown <0–24000>
/dittohm config <ability> power <0–512>
/dittohm config <ability> minlevel <0–100>
/dittohm config <ability> enabled <true|false>
/dittohm config <ability> reset
/dittohm config reset_all
```

```
/dittohm config activator button <left|right|either>
/dittohm config trader enabled <true|false>
/dittohm config trader every <ticks>
/dittohm config trader stay <ticks>
/dittohm config trader ivs <0–6>
/dittohm config trader levels <min> <max>
/dittohm config trader coins <min> <max>
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
