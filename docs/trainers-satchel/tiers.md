# Tiers

| Item | Recipe | Slots per pocket | Unlocks |
| --- | --- | --- | --- |
| **Canvas Satchel** | string, wool, leather | 14 | the seven pockets |
| **Leather Explorer Bag** | a Canvas Satchel + 6 hides + 2 copper ingots | 28 | [sorting and slot locks](#sorting-and-slot-locks), the [PokeBelt refill](in-the-field.md#pokebelt-refill) |
| **Ultra Satchel** | an Explorer Bag + 2 diamonds + 2 netherite scrap or shulker shells | 42 | the [cosmetic slot](#on-your-back) |

"Hides" are leather, rabbit hide and anything tagged `#c:leathers`
(`cobblemon_trainers_satchel:hides`); the Ultra materials are tagged
`cobblemon_trainers_satchel:ultra_materials`. A datapack can add to both.

**Upgrading keeps the bag's contents and its name.** The slot counts are settings
([Commands & Configuration](commands.md)). Lowering them never drops items: the ones past the new count
are kept out of sight until it goes back up, and an open bag closes when its slot count changes.

Everything else, the [battle lock](in-the-field.md#in-a-battle) and
[keeping it on death](death.md), is the same at every tier.

## Sorting and slot locks

From the Leather Explorer Bag up, a row under the pocket has:

- **Sort**: sorts this pocket.
- **Sort all**: sorts every pocket.
- **The order**: click to change it between **ID**, **Category** (creative-tab group, then id) and
  **Count**. Right-clicking Sort or Sort all changes it too.

Sorting merges partial stacks first, then orders them. **Shift + right-click** a slot to lock it, shown
with a small padlock: sorting never touches a locked slot. Each player's order is saved with the world.

An operator can turn sorting and locks off for everyone with `/satchel config sort enabled false`.

## On your back

Wear the satchel in the **Accessories back slot** and, in third person and for every other player, each
tier is a different 3D bag: a small canvas pouch, a leather pack with a bedroll, the Ultra pack with
its cyan emblem. It sits over a chestplate and follows sneaking. No GeckoLib needed.

- **Dyeing**: put any tier and dyes in the crafting grid, like leather armour. The cloth takes the
  colour; the pockets keep everything.
- **Cosmetic slot** (Ultra Satchel only): to the right of the pocket grid. Put a banner or a Poké Ball
  there (any item tagged `cobblemon_trainers_satchel:cosmetic`) and that is what your back shows
  instead of the bag, with the same pockets and slots. Take it out and the bag comes back.

`/satchel config cosmetics enabled false` draws no bag on the back and hides the slot; what is in it
stays.
