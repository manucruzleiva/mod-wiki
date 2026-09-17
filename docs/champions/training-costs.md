# Training Costs

Training is something the **trainer** pays for. Every change is paid out of your own experience bar,
not the Pokémon's, so rebuilding a team is an investment and a mistake is a real one.

## The price list

These are the defaults. A server can change every one of them, and a price of **0** makes that step
free.

| Change | Price (experience points) |
|---|---|
| One stat point, **up or down** | 10 |
| A nature | 1,000 |
| An ability | 2,000 |
| The hidden ability | 6,000 |
| A move | 500, only when the server charges for moves |
| An egg move | 1,500, only when the server charges for moves |

The ratios come from the Pokémon Champions standard, where a move costs 50 stat points, a nature 100
and an ability 200. The hidden ability and egg moves cost three times more, because those are what
players breed for, and breeding should stay the cheaper road.

- **Stat points** are charged per point moved, in both directions: taking one off costs the same as
  putting one on. The whole draft on the SP tab is paid once, on **Save**.
- **Moves** are free by default. The server's "Moves come from" setting decides; see
  [Nature, Ability & Moves](nature-ability-moves.md#moves). Putting moves in a different order is
  never charged.
- **Loading a set** costs what its parts cost together (the stat points that change, plus a nature,
  ability or moves that differ), and is paid once.

Prices are quoted in **experience points**, not levels: `Costs 640 experience`. A level is worth more
experience the higher you are, so the same purchase takes more of a low-level bar than a high one.

## Currency

By default everything is paid in experience. A server with
[CobbleDollars](https://modrinth.com/mod/cobbledollars)
([CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobbledollars)) can bill in its money
instead.

| "Paid in" | What happens |
|---|---|
| **Experience only** (default) | Always experience |
| **Experience, then CobbleDollars** | Experience if you have enough, otherwise CobbleDollars |
| **CobbleDollars, then experience** | CobbleDollars if you have enough, otherwise experience |
| **CobbleDollars only** | Always CobbleDollars |

- **A price is never split** between the two: one currency pays the whole of it.
- **Prices stay written in experience** and are converted at the server's rate, 10 experience per
  CobbleDollar by default, rounded up. A 500-experience move costs 50 CobbleDollars.
- **Without CobbleDollars installed**, everything is paid in experience, whatever the setting says.

Whenever CobbleDollars can pay, the page cannot see your balance, so the buttons stay live and the
server is the one that decides whether you can afford it.

## Where the experience comes from

Vanilla Minecraft only pays experience for defeating mobs, and a Cobblemon world has little of that.
[Cobblemon: PlayerXP](https://modrinth.com/mod/cobblemon-playerxp)
([CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemon-playerxp)) pays you experience
for the battles your Pokémon win, so what training spends refills from what you are already doing.
It is recommended, not required.

Changing a price is on [Commands & Config](commands.md).
