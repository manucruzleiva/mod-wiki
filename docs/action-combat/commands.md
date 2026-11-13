# Commands & Configuration

Every command is under `/cac` and needs operator level 2. Each level of the command answers on its
own with what it holds, so the tree can be walked with Tab.

| Command | What it does |
| --- | --- |
| `/cac format [wild\|npc\|pvp] [singles\|doubles] [on\|off]` | which battles play in real time |
| `/cac config [feature] [setting] [value]` | switch off and tune each feature |
| `/cac reset` | every setting back to its default |
| `/cac reload` | reread the config file |
| `/cac move <move>` | one move's real-time numbers |
| `/cac hit <move>` | the Pokémon you drive hits its opponent once, with the numbers in chat |
| `/cac arena add <name> <from> <to>` | mark a box where no move breaks a block |
| `/cac arena remove <name>` · `/cac arena list` | manage the arenas of your dimension |
| `/cac debug events` | print Action Combat's events in your chat (for mod authors) |
| `/cachud layout` | (any player) pick one of three HUD layouts |
| `/cachud controls [always\|never\|first_seconds [n]]` | (any player) when the [controls list](controls.md#the-controls-list) shows on the HUD |

## Features

Every feature has `enabled` plus its own settings, saved to the config file as soon as they change:

`possession` · `camera` · `movement` · `leash` · `disconnect` · `damage` · `moves` · `stamina` ·
`defense` · `hud` · `wild_ai` · `switch` · `aggro` · `bag` · `lock_on` · `capture` · `intrusion` ·
`breath` · `effects` · `status` · `field` · `abilities` · `held_items` · `npc` · `pvp` · `gimmicks` ·
`block_damage`

`/cac config <feature>` lists a feature's settings with their values, and
`/cac config <feature> <setting>` shows the range. A few worth knowing:

| Setting | Default | What it is |
| --- | --- | --- |
| `leash radius` | 32 | blocks your Pokémon may go from your Trainer |
| `damage scale` | 25 | how hard hits land, in percent of the games' damage |
| `pvp time_limit_seconds` | 0 (off) | the PvP clock |
| `hud controls` | on | the controls list on the HUD (each player still picks when it shows) |
| `camera shoulder_offset` | 60 (0 = centred) | how far the camera moves to a shoulder with a lock on, in percent of the Pokémon's width |
| `camera shoulder_side` | `auto` | `right`, `left` or `auto` (the target's side) |
| `switch cooldown_seconds` | 15 (0 = off) | the wait between your own switches |
| `npc switch_seconds` | 10 | the least time between an NPC's switches |
| `npc rct_win_commands` | on | run a Radical Cobblemon Trainers trainer's `winCommands` when a real-time fight against it ends (needs tbcs) |
| `moves accuracy_stages` | on | accuracy and evasion stages change fumbles and dodges |
| `wild_ai protect_percent` | 30 (0 = off) | how often a wild Pokémon raises Protect against a strong move |
| `wild_ai protect_min_power` | 80 | the least power that makes it raise Protect |
| `wild_ai dodge_npc_casts` | on | wild and NPC Pokémon dodge each other's casts, not only a player's |
| `wild_ai type_aware` | on | a wild Pokémon weighs its moves' power by type effectiveness |
| `wild_ai status_weight` | 30 (0 = no Status moves) | how likely a wild Pokémon is to use a Status move that would do something |
| `gimmicks dynamax_seconds` | 20 | how long a Dynamax lasts |
| `block_damage soft_power` / `stone_power` | 60 / 100 | the power to break soft blocks and stone |
