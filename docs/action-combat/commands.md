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
| `npc switch_seconds` | 10 | the least time between an NPC's switches |
| `gimmicks dynamax_seconds` | 20 | how long a Dynamax lasts |
| `block_damage soft_power` / `stone_power` | 60 / 100 | the power to break soft blocks and stone |
