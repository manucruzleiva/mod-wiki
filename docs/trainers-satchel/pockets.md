# Pockets & Rules

Right-click the satchel to open it. It has seven tabs, one per pocket, and each pocket takes only its
own kind of item. Put anything else in and it bounces back, with the slot flashing red.

## The seven pockets

| Tab | Pocket id | What goes in |
| --- | --- | --- |
| Poké Balls | `poke_balls` | Poké Balls |
| Medicine & Restores | `medicine` | potions, restores, revives, remedies, ethers |
| Evo & Held Items | `evo_held` | evolution items and held items |
| Agriculture & Farming | `agriculture` | berries, apricorns, seeds and saplings |
| Architect & Building | `architect` | building blocks |
| Materials & Drops | `materials` | crafting materials and mob drops |
| Key & Utility Items | `key_utility` | key and utility items |

The contents live on the bag itself, so they survive closing it, dropping it and picking it up again.
**Shift-click** an item in your inventory to send it straight to its pocket.

## Which pocket an item goes to

1. An operator's **rule**, if the item has one. A rule sends the item to one pocket, or to `none`, which
   keeps it out of every pocket.
2. Otherwise the **pocket tags** `cobblemon_trainers_satchel:pocket/<pocket id>`, which a datapack can
   edit. This is how items from other mods land in the right place without any setup.

A rule always wins over the tags. Remove the rule and the tags decide again.

## The Rules screen

The **Rules** button on the satchel's title row lists every item with its pocket, filterable by mod
or id. `(tag)` marks an item the tags decide; `▸` marks one a rule decides. A click moves an item to
the next pocket.

Everyone sees the rules; only an **operator** can save. **Save** writes
`config/cobblemon_trainers_satchel/item_rules.json` on the server and updates every player at once.

You can also edit the file by hand:

```json
{"rules": {"minecraft:stick": "materials", "minecraft:bone": "none"}}
```

and run `/satchel rules reload` ([Commands](commands.md#satchel-rules-reload)). A file that is not
valid JSON is never overwritten: the rules already in force stay.

Switch the whole sorting system off with `/satchel config classifier enabled false`: every pocket then
takes any item and the Rules button hides.
