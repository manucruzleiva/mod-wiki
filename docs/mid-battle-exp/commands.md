# Commands & settings

!!! note "Next release"

    Everything on this page arrives in the version after 2.0.0. In 2.0.0 the mod has no command, no
    config file and no Summary button.

Out of the box the mod changes **when** EXP is paid, never how much. Two things can change that: the
server's settings, which operators set with `/midbattleexp`, and a button on each Pokémon's Summary.

## `/midbattleexp`

For **operators** (permission level 2). Every change applies to the next knockout, is saved to the
server's `config/cobblemon_mid_battle_exp.json` straight away, and is announced to the other
operators, as vanilla settings are.

| Command | What it does | Default |
|---|---|---|
| `/midbattleexp` | Shows the current settings | |
| `/midbattleexp multiplier <0–1000>` | Multiplies **all battle EXP**: knockouts, Exp. Share and whatever the end of the battle still pays | `1` |
| `/midbattleexp expshare <0–1000>` | How much of a knockout a Pokémon **that did not fight** gets through the Exp. Share. `1` is a full share, `0.5` half | Cobblemon's |
| `/midbattleexp expshare default` | Goes back to Cobblemon's own `experienceShareMultiplier` | |
| `/midbattleexp globalexpshare <true\|false>` | **Global Exp. Share**: the whole team gets that share, whether it holds an Exp. Share or not | `false` |
| `/midbattleexp reload` | Rereads the file after you edit it by hand | |

`/midbattleexp` answers with one line:

```
Mid-Battle EXP: EXP ×1.5 · Exp. Share ×0.5 (Cobblemon's) · global Exp. Share off
```

### How they combine

- The **multiplier** comes on top of everything Cobblemon already applies (its own
  `experienceMultiplier`, Lucky Egg, traded, friendship…). `2` doubles what you would have earned;
  `0` turns battle EXP off for everyone. It does not touch candies or `/levelup`.
- A Pokémon that **fought** the fainted opponent always gets the full amount; the Exp. Share setting
  is only for the ones that did not.
- With **global Exp. Share** on, a teammate that did not fight gets the share even with no Exp. Share
  held, and it gets its EVs too, as a holder would. A Pokémon that has fainted still earns nothing,
  unless Cobblemon's `awardExperienceToFaintedPokemon` says so.
- A level-cap mod still has the last word: the multiplier is applied first, then the cap.

### The file

```json
{
  "experienceMultiplier": 1.0,
  "expShareMultiplier": null,
  "globalExpShare": false
}
```

`expShareMultiplier: null` means "use Cobblemon's". The file is created with these defaults the first
time the server starts, and read again at every start. A value out of range (below 0, above 1000, or
not a number) falls back to its default; a file that cannot be read keeps all the defaults and says
so in the server log.

## Pausing a Pokémon's EXP

Under the Summary's bottom-left corner there is a button, **EXP: On**. Click it and it turns to
**EXP: Off**: that Pokémon gains **no battle EXP** until you click it again. It is the way to hold a
Pokémon at a level cap, or to stop it evolving by level.

- It works per Pokémon, and only on **your own** Pokémon, in the party or in the PC.
- It is saved **with the Pokémon**: it stays off across restarts, in the PC and after a trade.
- A paused Pokémon **still gains EVs**, and still counts as having fought, for the rest of the team.
- Only battle EXP stops. **Candies** and `/levelup` still work, so a candy is never wasted.
- You can change it in the middle of a battle; the next knockout follows it.

The button needs the mod **on your game and on the server**. Without it on either side, the Summary
shows no button.
