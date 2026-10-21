# Getting Started

## Install

Cobblemon Champions Training goes on **both sides**: the server keeps the rules and the points, and
your game draws the pages you train from. In single player, that is just your own `mods/` folder.

Drop **one** jar, the one for your loader, never both.

=== "Fabric"

    | | |
    |---|---|
    | Minecraft | 1.21.1 |
    | Required | [Cobblemon](https://modrinth.com/mod/cobblemon) 1.8 and what it needs ([Fabric Language Kotlin](https://modrinth.com/mod/fabric-language-kotlin), Architectury API) |
    | Recommended | [Cobblemon: PlayerXP](https://modrinth.com/mod/cobblemon-playerxp) |
    | Optional | [CobbleDollars](https://modrinth.com/mod/cobbledollars) · [Cloth Config](https://modrinth.com/mod/cloth-config) + [Mod Menu](https://modrinth.com/mod/modmenu) for the settings screen |

=== "NeoForge"

    | | |
    |---|---|
    | Minecraft | 1.21.1 |
    | Required | [Cobblemon](https://modrinth.com/mod/cobblemon) 1.8 and what it needs ([Kotlin for Forge](https://modrinth.com/mod/kotlin-for-forge), Architectury API) |
    | Recommended | [Cobblemon: PlayerXP](https://modrinth.com/mod/cobblemon-playerxp) |
    | Optional | [CobbleDollars](https://modrinth.com/mod/cobbledollars) · [Cloth Config](https://modrinth.com/mod/cloth-config) for the settings screen |

!!! tip "Why PlayerXP"

    Training is paid with **your** experience. Vanilla only pays experience for defeating mobs, and a
    Cobblemon world has little of that. PlayerXP pays you for the battles your Pokémon win, so what
    training spends refills from what you are already doing.

## Which Pokémon it touches

Only a Pokémon that is **31 in all six IVs**. It can get there by being bred that way, caught that
way, or raised with Bottle Caps. Everything below that is plain Cobblemon: its stats, its effort
values and its summary screen are exactly the game's own.

The moment a Pokémon crosses that line, it switches over once and for good, and you see:

> This Pokémon trains with stat points now — visit a Champions Trainer to spend them. Effort values
> no longer do anything for it.

Whatever effort values it had become its first stat points, so a Pokémon you trained before is not
set back. [Stat Points](stat-points.md#converting-from-effort-values) explains the exchange.

A server can loosen or tighten this rule, or turn the stat points off entirely; see
[Commands & Config](commands.md).

## Where everything is

Everything is on the Pokémon's summary. There is no new screen and no new item. Since version
1.0.14 the summary only **sells** at a [Champions Trainer](champions-trainer.md): talk to one and
its summary opens with every control live. Opened anywhere else, it shows the same pages read-only.

| Summary page | What changes | Details |
|---|---|---|
| **Stats** | The IV and EV tabs are replaced by **SP** and **Sets** | [Stat Points](stat-points.md#the-sp-tab) · [Saved Sets](sets.md) |
| **Info** | The Nature and Ability rows open a picker, marked with a **▼** | [Nature, Ability & Moves](nature-ability-moves.md) |
| **Moves** | Cobblemon's move screen offers every move the Pokémon can legally learn | [Nature, Ability & Moves](nature-ability-moves.md#moves) |

Every change shows its price before you commit to it, is paid once, and plays a short chime when it
goes through. [Training Costs](training-costs.md) lists the prices.

## Your first build

1. Talk to a [Champions Trainer](champions-trainer.md). Pick a Pokémon with 31 in every IV and go
   to **Stats → SP**.
2. Use **+** and **−** to spread up to 66 points, 32 at most in one stat. **++** fills a stat as far
   as it can go.
3. Read the price under the buttons, then press **Save**.
4. On the **Info** page, click the **Nature** row, pick the stat to raise and the stat to lower, and
   press **Train**.
5. Back on **Stats → Sets**, press **Store** on an empty slot. The whole build is saved, ready to
   load again later.
