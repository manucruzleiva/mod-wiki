# Commands & Configuration

Every command is under `/satchel`, for **operators** only.

## /satchel rules reload

Re-reads `config/cobblemon_trainers_satchel/item_rules.json` after a hand edit and updates every
player. A broken file is never overwritten, and the rules in force stay
([Pockets & Rules](pockets.md#the-rules-screen)).

## /satchel config

Shows and changes every setting on a live server. A change applies to **everyone at once**, without a
restart, and is written to `config/cobblemon_trainers_satchel/config.json` so it survives one.

| Command | What it does |
| --- | --- |
| `/satchel config` | Lists every feature with its settings and the allowed values. |
| `/satchel config <feature>` | Lists one feature. |
| `/satchel config <feature> enabled <true\|false>` | Switches the feature on or off. |
| `/satchel config <feature> <setting> <value>` | Sets one of its numbers or choices. |

## Configuration

`config.json` holds an `enabled` switch for every feature, plus these settings. A broken file is
never overwritten, and the settings in force stay.

| Feature | What `enabled false` does | Settings |
| --- | --- | --- |
| `pockets` | The satchel does not open and open screens close. | `canvas_slots` `14`, `explorer_slots` `28`, `ultra_slots` `42` (each 7 to 63) |
| `classifier` | Every pocket takes any item; the Rules button hides. | |
| `sort` | [Sorting and slot locks](tiers.md#sorting-and-slot-locks) off for everyone. | |
| `death` | Deaths are left to the game ([Keeping It on Death](death.md)). | `death_rule`: `PROTECTED` (default), `BOUND_ITEM` or `VANILLA` |
| `battle` | The [battle lock](in-the-field.md#in-a-battle) and both limits off. | `balls_per_battle` `0`, `items_per_battle` `0` (0 = unlimited) |
| `evo_indicator` | No [evolution hints](in-the-field.md#evolution-hints). | |
| `planting` | No [planting from the bag](in-the-field.md#planting-from-the-bag). | |
| `belt_refill` | No [PokeBelt refill](in-the-field.md#pokebelt-refill). | |
| `cosmetics` | No bag drawn on the back, cosmetic slot hidden; what is in it stays. | |
| `pc_storage` | The PC opens straight to Cobblemon's PC; what is stored stays. | |

All features are on by default.
