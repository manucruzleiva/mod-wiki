# Keeping It on Death

Dying never costs you the satchel by default. The setting `death death_rule` picks what a death does,
for every tier alike, and is read at each death, so a change applies to the next one:

| Rule | What a death does |
| --- | --- |
| `PROTECTED` (default) | Every satchel the death would drop is handed back on respawn, into your inventory, with everything in it. It is saved with the world, so quitting on the death screen or a server restart loses nothing. |
| `BOUND_ITEM` | A single bag is left still at the spot where you died. Lava, fire, explosions and time never destroy it; only the void takes it. |
| `VANILLA` | The vanilla rule: the bag drops **and spills its contents** with the rest of your items, and the cosmetic slot goes with them. |

This works for a bag in the inventory, the offhand or the Accessories back slot. A grave mod that keeps
items without dropping them keeps the bag too.

`/satchel config death enabled false` leaves deaths entirely to the game: the bag drops whole.
