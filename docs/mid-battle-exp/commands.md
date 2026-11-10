# Commands & Config

The server's EXP settings are set by operators with `/midbattleexp`, and each Pokémon's Summary has
a button that pauses its EXP. Every extra source of EXP or XP has its own on/off switch.

## `/midbattleexp`

For **operators** (permission level 2). Every change applies straight away, is saved to the
server's `config/cobblemon_mid_battle_exp.json` and is announced to the other operators, as vanilla
settings are.

### Battle EXP

| Command | What it does | Default |
|---|---|---|
| `/midbattleexp` | Shows the current settings | |
| `/midbattleexp multiplier <0–1000>` | Multiplies **all battle EXP**: knockouts, Exp. Share and whatever the end of the battle still pays | `1` |
| `/midbattleexp expshare <0–1000>` | How much of a knockout a Pokémon **that did not fight** gets through the Exp. Share. `1` is a full share, `0.5` half, `0` nothing | Cobblemon's |
| `/midbattleexp expshare default` | Goes back to Cobblemon's own `experienceShareMultiplier` | |
| `/midbattleexp globalexpshare <true\|false>` | **Global Exp. Share**: the whole team gets that share, whether it holds an Exp. Share or not | `false` |
| `/midbattleexp expsharebonus <1–1000>` | With the global Exp. Share on, a Pokémon that **holds** an Exp. Share and did not fight gets the share times this | `1` |
| `/midbattleexp gymexp <true\|false>` | **Gym battles pay more** (needs [PokeGyms](../pokegyms/index.md) 0.0.17 or later) | `true` |
| `/midbattleexp gymexpmultiplier <0–1000>` | How much more a gym battle pays | `1.5` |

### Capture EXP

| Command | What it does | Default |
|---|---|---|
| `/midbattleexp captureexp <true\|false>` | **Catching a Pokémon pays EXP** | `true` |
| `/midbattleexp captureexpshare <0–1000>` | That EXP, as a share of what knocking the same Pokémon out would pay | `0.5` |
| `/midbattleexp capturetrainerexp <true\|false>` | The player also gets their Trainer EXP share of a capture | `true` |

### Trainer (player) XP

| Command | What it does | Default |
|---|---|---|
| `/midbattleexp trainerexpshare <0–1000>` | The player gets this share of their Pokémon's battle EXP as vanilla XP. `0` turns it off | `0.1` |
| `/midbattleexp ediblecandy <true\|false>` | **Edible candies**: Shift + right-click with an EXP Candy or Rare Candy eats it for XP | `false` |
| `/midbattleexp candyexp <0–1000>` | XP points per point of the candy's Pokémon EXP | `0.1` |
| `/midbattleexp pokedexexp <true\|false>` | **New Pokédex entries pay XP** | `true` |
| `/midbattleexp pokedexseen <0–10000>` | XP for a species seen for the first time | `10` |
| `/midbattleexp pokedexcaught <0–10000>` | XP for a species caught for the first time | `50` |

### Victory bonus and pasture

| Command | What it does | Default |
|---|---|---|
| `/midbattleexp victorybonus <true\|false>` | **Beating an NPC trainer pays a bonus** at the end of the battle | `true` |
| `/midbattleexp victoryexp <0–1000>` | The bonus for each Pokémon still standing, as a share of the EXP it earned in that battle | `0.25` |
| `/midbattleexp victoryxp <0–1000>` | Player XP per level of the trainer's strongest Pokémon | `1` |
| `/midbattleexp pasture <true\|false>` | **Pokémon in a Pasture Block slowly gain EXP** | `true` |
| `/midbattleexp pastureexp <n>` | EXP each pastured Pokémon gains per interval | `10` |
| `/midbattleexp pasturecap <n>` | The most EXP a pastured Pokémon gains in one hour | `300` |
| `/midbattleexp reload` | Rereads the file after you edit it by hand | |

`/midbattleexp` answers with one line. With the defaults:

```
Mid-Battle EXP: EXP ×1 · Exp. Share ×0.5 (Cobblemon's) · global Exp. Share off · Exp. Share holder bonus ×1 · capture EXP ×0.5 · edible candy off (×0.1, Rare Candy 30 XP) · Trainer EXP ×0.1 · pasture EXP on, 10 per 60 s, at most 300 per hour · victory bonus on (EXP ×0.25, 1 XP per level) · Pokédex XP on (seen 10, caught 50) · gym EXP ×1.5
```

### How they combine

- The **multiplier** comes on top of everything Cobblemon already applies (its own
  `experienceMultiplier`, Lucky Egg, traded, friendship…). `2` doubles what you would have earned;
  `0` turns battle EXP off for everyone. It does not touch candies, `/levelup` or the pasture.
- A Pokémon that **fought** the fainted opponent always gets the full amount; the Exp. Share setting
  is only for the ones that did not.
- With **global Exp. Share** on, a teammate that did not fight gets the share even with no Exp. Share
  held, and it gets its EVs too, as a holder would. A Pokémon that has fainted still earns nothing,
  unless Cobblemon's `awardExperienceToFaintedPokemon` says so.
- The **Exp. Share holder bonus** only counts while the global Exp. Share is on, so holding the item
  still matters. With `expshare 0.5` and `expsharebonus 2`, a benched holder earns what a fighter
  does, and the rest of the bench half. The server log marks those payments "(Exp. Share ×2)".
- The **gym multiplier** comes on top of `multiplier`, for every point of EXP a gym battle pays.
- A level-cap mod still has the last word: the multipliers are applied first, then the cap.

### Other mods

Nothing is paid twice when another mod already does the same job:

| Installed | What this mod leaves to it |
|---|---|
| [Cobblemon: PlayerXP](https://modrinth.com/mod/cobblemon-playerxp) | All the player's XP from battles: the Trainer EXP share, capture XP and the victory bonus's XP. The Pokémon's part of the victory bonus is still paid |
| Cobblemon Capture XP | Capture EXP: this mod pays nothing for captures |
| [PokeGyms](../pokegyms/index.md) 0.0.17+ | Nothing: it is what turns the gym bonus on. Without it, the gym settings do nothing |

### The file

```json
{
  "experienceMultiplier": 1.0,
  "expShareMultiplier": null,
  "globalExpShare": false,
  "expShareHolderBonus": 1.0,
  "captureExpShare": 0.5,
  "captureExp": true,
  "captureTrainerExp": true,
  "edibleCandy": false,
  "candyPlayerExpShare": 0.1,
  "rareCandyPlayerExp": 30,
  "trainerExpShare": 0.1,
  "pastureExp": true,
  "pastureExpPerInterval": 10,
  "pastureExpHourlyCap": 300,
  "pastureExpIntervalSeconds": 60,
  "victoryBonus": true,
  "victoryBonusExp": 0.25,
  "victoryXp": 1,
  "pokedexExp": true,
  "pokedexSeenExp": 10,
  "pokedexCaughtExp": 50,
  "gymExp": true,
  "gymExpMultiplier": 1.5
}
```

`expShareMultiplier: null` means "use Cobblemon's". Two settings have no command and live only in
the file: `rareCandyPlayerExp` (XP for an eaten Rare Candy, 0–1400) and `pastureExpIntervalSeconds`
(seconds between two pasture payments, 1–3600).

The file is created with these defaults the first time the server starts, and read again at every
start. A value out of range (or not a number) falls back to its default; a file that cannot be read
keeps all the defaults and says so in the server log.

## Pausing a Pokémon's EXP

Next to the level, at the Summary's top-left corner, there is a small **EXP** button with a green
square: EXP is on. Click it and the square turns red, **EXP: Off**: that Pokémon gains **no battle
EXP** until you click it again. It is the way to hold a Pokémon at a level cap, or to stop it
evolving by level.

- It works per Pokémon, and only on **your own** Pokémon, in the party or in the PC.
- It is saved **with the Pokémon**: it stays off across restarts, in the PC and after a trade.
- A paused Pokémon **still gains EVs**, and still counts as having fought, for the rest of the team.
- A paused Pokémon gets no capture EXP and no pasture EXP either.
- **Candies** and `/levelup` still work, so a candy is never wasted.
- You can change it in the middle of a battle; the next knockout follows it.
- Hover it to read whether EXP is on or off. While the Pokémon has a status (PAR, BRN, FNT…), the
  button covers it.

The button needs the mod **on your game and on the server**. Without it on either side, the Summary
shows no button.
