# PC Item Storage

Behind every Cobblemon PC there is a place to keep items.

## Using it

Right-click a Cobblemon PC and it first asks: **Pokémon** or **Items**.

- **Pokémon** opens Cobblemon's own PC, with your party and boxes, with all of Cobblemon's own checks.
- **Items** opens your item storage.

The storage is **yours**: the same at every PC in the world, and nobody else's. It has the satchel's
seven pockets as tabs and **no limit**: each kind of item is one cell with its total (1.2k, 34k, the
exact number in the tooltip), with pages when a section holds more than 42 kinds.

| Action | Result |
| --- | --- |
| Put an item on a cell | stores the whole stack |
| Right-click with an item | stores one |
| Shift-click an item in your inventory | stores it, in the open section if that takes it, otherwise in its own pocket's |
| Left-click a cell | takes a stack |
| Right-click a cell | takes half a stack |
| Shift-click a cell | takes a stack into your inventory |

It is saved with the world, so it survives a restart, and it closes when you walk away from the PC.
The cells are a view of the storage, never real slots, so no more than a stack leaves at a time.

## Switching it off

`/satchel config pc_storage enabled false` removes the question: the PC opens straight to Cobblemon's
PC. What is stored stays.
