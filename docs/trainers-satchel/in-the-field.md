# In Battle & in the Field

## In a battle

While you are in a Cobblemon battle (wild, trainer or PvP) the satchel keeps to battle things.
**Agriculture, Architect and Materials close**: their tabs grey out ("Closed during a battle"), they
cannot be opened or filled, and the server refuses to open them. **Poké Balls, Medicine, Evo & Held and
Key & Utility** stay open. The pockets open again as soon as the battle ends, however it ends.

[Cobblemon Action Combat](../action-combat/index.md)'s real-time fights count as battles too, when
that mod is installed.

Operators can also cap what **one battle** may take out of the satchel:

| Setting | Pocket | Default |
| --- | --- | --- |
| `battle balls_per_battle` | Poké Balls | `0` (unlimited) |
| `battle items_per_battle` | Medicine | `0` (unlimited) |

Past the cap the item snaps back with an action-bar line, and the count starts again with each battle.
It counts items **taken out of the satchel**, not items used, through every way out: pickup,
shift-click, number keys, cursor swaps, throwing and double-click collect.

`/satchel config battle enabled false` turns the lock and both limits off.

## Evolution hints

In the **Evo & Held** pocket, an item one of your party Pokémon can use right now glows green. Its
tooltip names who and how:

- "Eevee can evolve with it": a stone, used on the Pokémon.
- "Happiny evolves holding it": an Oval Stone.
- "Pikachu gets its held-item effect": Light Ball, Metal and Quick Powder, Leek, Deep Sea Tooth and
  Scale, Eviolite for anything that can still evolve.

The glow shows even when another requirement is not met yet, and the tooltip then says what is
missing ("needs level 25", "needs friendship 160"). It follows your party live while the bag is open.

`/satchel config evo_indicator enabled false` turns it off.

## Planting from the bag

With the satchel in your **offhand** and your main hand **empty**, right-click farmland, dirt or grass:
it plants the first seed, sapling, berry or apricorn seed from the Agriculture pocket that grows
there, one at a time. Right-click on air still opens the bag; bone meal and hoes stay in your hands.

Wearing the bag on your back instead, press **,** (comma; rebindable under Controls) while looking at the
soil. **Sneak + ,** picks which plant goes first.

Nothing plants during a battle, when Agriculture is closed. `/satchel config planting enabled false`
turns it off.

## PokeBelt refill

*From the Leather Explorer Bag up, Fabric only.* Wear PokeBelt and the satchel, and when you throw the
belt's last ball of a kind, a stack of that same kind moves from the Poké Balls pocket into the belt
slot. It never puts a different ball there; with none of that kind left, the slot stays empty. It
works for Cobblemon Action Combat's throws too, and in a battle the refilled balls count against
`battle balls_per_battle`.

PokeBelt is Fabric only. Without it the log says once that the refill is off.
`/satchel config belt_refill enabled false` turns it off.
