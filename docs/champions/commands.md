# Commands & Config

Every system this mod replaces can be switched off, and every price can be changed. Do it from the
**config screen**, from **`/champions config`** in game, or in the settings file.

## `/champions sp [slot]`

A read-out of one party Pokémon, for anyone. `slot` is 1 to 6, counted the way your party screen
counts, and defaults to 1.

```
=== Bulbasaur (slot 1, level 30) ===
Gate: open — Champions training is available.
Budget: 66/66
HP sp=32 room=0 ev=0 iv=31 • stat=97
Attack sp=32 room=0 ev=0 iv=31 • stat=81
...
```

| Line | What it tells you |
|---|---|
| `Gate` | Whether the Pokémon is in training. When it is not, which IVs are short of 31, with their values. |
| `Budget` | Points in use, out of 66 |
| one line per stat | Its stat points (`sp`), how many more it can take (`room`), its effort values and IV, and the final stat |

Running it also switches a Pokémon over if it has just reached 31 in every IV, so its numbers are
the ones you will be spending. When stat points are turned off on the server, it says so first.

## `/champions config`

For **operators** (permission level 2). Every change is saved to the settings file and reaches every
connected player at once; nobody has to reconnect.

```
/champions config                               every setting, grouped
/champions config <group>                       one group
/champions config <group> <setting>             one value
/champions config <group> <setting> <value>     change it
/champions config <group> reset [<setting>]     back to the default
/champions config reset_all                     every setting back to its default
```

A value that is not one of the allowed ones is refused, and the message lists the ones that are.
Typing a group name and pressing **Tab** suggests its settings.

## The settings

| Group | Setting | Values | Default | What it controls |
|---|---|---|---|---|
| `statpoints` | `enabled` | `true` / `false` | `true` | The stat-point system. Off: effort values as in plain Cobblemon, points kept for later. |
| `statpoints` | `requireMaxIvs` | `true` / `false` | `true` | Only a Pokémon with 31 in every IV can train. |
| `statpoints` | `hyperTrainingUnlocks` | `true` / `false` | `true` | IVs raised with Bottle Caps count toward the 31s. |
| `statpoints` | `xpPerStatPoint` | 0 or more | `10` | Experience per stat point moved. |
| `nature` | `source` | `MINTS` / `TRAINING` / `BOTH` | `BOTH` | Where a nature can be changed: mints, the Info page, or both. |
| `nature` | `xpPerNatureChange` | 0 or more | `1000` | Experience per nature. |
| `ability` | `source` | `ITEMS` / `TRAINING` / `BOTH` | `BOTH` | Where an ability can be changed: Ability Capsules and Patches, the Info page, or both. |
| `ability` | `xpPerAbilityChange` | 0 or more | `2000` | Experience per ability. |
| `ability` | `xpPerHiddenAbility` | 0 or more | `6000` | Experience per hidden ability. |
| `moves` | `source` | `SWAP` / `TRAINING` / `BOTH` | `BOTH` | `SWAP`: Cobblemon's list, free. `TRAINING`: every legal move, charged. `BOTH`: every legal move, free. |
| `moves` | `xpPerMoveChange` | 0 or more | `500` | Experience per move, when moves are charged. |
| `moves` | `xpPerEggMove` | 0 or more | `1500` | Experience per egg move, when moves are charged. |
| `currency` | `order` | `XP_ONLY` / `XP_THEN_COBBLEDOLLARS` / `COBBLEDOLLARS_THEN_XP` / `COBBLEDOLLARS_ONLY` | `XP_ONLY` | What training is paid in. |
| `currency` | `rate` | 1 or more | `10` | Experience per CobbleDollar, rounded up. |

For example, to charge for moves and make egg moves steeper:

```
/champions config moves source TRAINING
/champions config moves xpPerEggMove 3000
```

[Nature, Ability & Moves](nature-ability-moves.md) and [Training Costs](training-costs.md) explain what
these do in play.

## The config screen

With [Cloth Config](https://modrinth.com/mod/cloth-config) installed, the same settings are on a
screen: on Fabric, open it from [Mod Menu](https://modrinth.com/mod/modmenu); on NeoForge, from the
mods list. Each setting has a tooltip.

!!! note "Whose settings count"

    The server's settings are the rules. While you are connected to a server, your game uses the
    server's values, whatever your own file says, and it goes back to yours when you leave. The
    screen always edits **your own** file, which is what counts in single player and on a server you
    host.

## The settings file

`config/cobblemon_champions_training.json`, created with the defaults the first time the game starts.

```json
{
  "configVersion": 1,
  "statPointsEnabled": true,
  "requireMaxIvs": true,
  "hyperTrainingUnlocks": true,
  "natureSource": "BOTH",
  "abilitySource": "BOTH",
  "moveSource": "BOTH",
  "xpPerStatPoint": 10,
  "xpPerNatureChange": 1000,
  "xpPerAbilityChange": 2000,
  "xpPerHiddenAbility": 6000,
  "xpPerMoveChange": 500,
  "xpPerEggMove": 1500,
  "costOrder": "XP_ONLY",
  "xpPerCobbleDollar": 10
}
```

A missing key takes its default, and a misspelled value falls back to the default with a line in the
log naming the key and the values it accepts. A negative price is read as 0, and a rate under 1 as 1.
