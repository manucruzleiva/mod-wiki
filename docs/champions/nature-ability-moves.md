# Nature, Ability & Moves

Stat points are half of a build. The other half is changed where you already read it: the nature and
the ability on the summary's **Info** page, and the moves on Cobblemon's own move screen.

## The Info page

On a Pokémon in training, the **Nature** and **Ability** rows carry a small **▼** at their right
edge. Click the row to open its picker.

A row only has the marker when it really opens:

- the Pokémon is in training (31 in every IV);
- the server lets training change that thing (see [the settings](commands.md#the-settings));
- for the ability, the Pokémon's form has more than one ability to choose from.

Everywhere else the page is exactly Cobblemon's. Click outside the picker to close it without buying.

## Nature

The nature picker has three parts: the stat to **raise** (**+**), the stat to **lower** (**−**), and
the nature those two make.

| Raise | Lower | Nature |
|---|---|---|
| Attack | Speed | Brave |
| Attack | Sp. Atk | Adamant |
| Speed | Attack | Timid |
| Sp. Atk | Attack | Modest |

HP is not on either side, because no nature touches it. Picking **the same stat on both sides** gives
the neutral nature that sits on that line of the nature table:

| Raise and lower | Neutral nature |
|---|---|
| Attack | Hardy |
| Defence | Docile |
| Sp. Atk | Bashful |
| Sp. Def | Quirky |
| Speed | Serious |

The picker opens on the nature the Pokémon has now. The line under it shows what the chosen nature
does and its price; press **Train** to buy it.

The nature you buy is layered over the one the Pokémon was born with, just as a mint does. Picking
its birth nature again removes that layer.

## Ability

The ability picker lists every ability the Pokémon's form can have, **its hidden ability included**.
The highlighted one's description is shown under the list, and a hidden ability is marked as such.
A hidden ability costs more than a common one, because it is something players breed for.

Pick one and press **Train**.

## Moves

A Pokémon in training can switch to **any move its form can legally learn**: level-up moves, TMs,
tutor moves and egg moves. The switch happens on Cobblemon's own move screen, where the full list
appears; nothing new to learn.

| "Moves come from" | Moves offered | Cost of a switch |
|---|---|---|
| **Every legal move, free** (default) | the whole learnset | nothing |
| **Every legal move, charged** | the whole learnset | the move's price; egg moves cost more |
| **Cobblemon's list, free** | only the moves it already learned | nothing, as in plain Cobblemon |

Putting the same moves in a different order is never charged. Levelling up still teaches moves as
usual, whatever the setting.

!!! note "TMs"

    A Pokémon in training can already switch to every move a TM would teach, so a TM tells you it
    already knows the move and is not used up.

## Mints, Ability Capsules and Ability Patches

They keep working by default. A server can make nature or ability changes **training only**, and
then a mint, a capsule or a patch does nothing and says so; with **mints only** or **capsules and
patches only**, the pickers on the Info page stay closed instead.

Prices are on [Training Costs](training-costs.md); the settings are on
[Commands & Config](commands.md).
