# World creation & configuration

## World-creation tabs

When you create a new world, Cobblemon Routes adds two tabs next to **GAME / WORLD / MORE**:

### NUZLOCKE tab

The four gamemode toggles inline (Nuzlocke, first-encounter lock, permadeath, spectator-on-loss) plus
an **"All Nuzlocke options…"** button opening the full screen with every option:

| Option | Default | Notes |
| --- | --- | --- |
| Nuzlocke / encounter lock / permadeath / spectator | on | the core rule set |
| Healing sources | ALL | ALL / MACHINES_ONLY / ITEMS_ONLY / NONE |
| Starter selection | DEFAULT_PLUS_RANDOM | DEFAULT / DEFAULT_PLUS_RANDOM / THREE_RANDOM |
| Starter level | 5 | 1–25 |
| Shared EXP | on | whole team gains EXP |
| EXP during battle (per KO) | on | |
| EXP boost | 1× | 1–16× |
| Capture zones | By route/city | Biome / Route / Route+Biome |
| Share same-structure zones | off | one zone per structure type vs. per instance |
| Hunger | on | off keeps players fed |
| PC only at the PC block | on | blocks remote PC access in Nuzlocke worlds |

### ROUTES tab

Customise dynamic route generation for the world:

| Option | Default | Notes |
| --- | --- | --- |
| Generate routes | on | master switch |
| Routes per city | 3 | 1–6 roads out of each city |
| Connect all structures | on | also connect non-city surface structures |
| Route trainers | on | spawn trainers along finished roads |
| Water crossings | Aquatic channel | Aquatic channel vs. Causeway bridge |

!!! info "Saved per world"
    Choices made in these tabs are stored **per world** and only applied to a brand-new world — loading
    an existing world never gets its rules clobbered. Picking **Hardcore** at world creation auto-enables
    the full Nuzlocke rule set.

## In-game config screen

Outside world creation, open the global config any time with the **K** key or `/cobblemon_routes config`
(Cloth Config). It writes `config/cobblemon_routes.json` and provides the defaults used when a world
wasn't configured through the tabs.

## Commands

| Command | Permission | Description |
| --- | --- | --- |
| `/cobblemon_routes config` | — | Open the config screen (client). |
| `/cobblemonroutes nuzlocke status` | — | Your Nuzlocke zones and party deaths. |
| `/cobblemonroutes nuzlocke reset/revive [player]` | OP 2 | Admin / testing. |
| `/cobblemonroutes routes status/scan/connect/reset` | OP 2 | Route diagnostics (routes generate on their own). |
