# ⌨️ Commands & Config

Everything under the **`/nuzlocke`** root, and every switch the ruleset has. Routes' road commands
live under [`/routes`](../routes/commands.md) — the two never mix.

👤 = every player · 🛡️ = operator (permission level 2)

## Quick reference

| Command | Who | One-liner |
| --- | :---: | --- |
| `/nuzlocke status [player]` | 👤 / 🛡️ | Zone records + party deaths (`[player]` is op-only). |
| `/nuzlocke log` · key **I** | 👤 | Opens your party's summary on the **Log** tab — the link's log while you are in a Soul Link. |
| `/nuzlocke map` | 👤 | Dump your capture zones as map waypoints. |
| `/nuzlocke reset [player]` | 🛡️ | Clear a player's zone records, lift their game-over and ask for a new Gym Leader Challenge type. They keep their team. |
| `/nuzlocke revive [player] [zone <zone>]` | 🛡️ | Revive a party's dead Pokémon — all of them, or only the one caught in that zone (by the name the log shows). The mercy switch: it also lifts a game-over, and under [Soul Link](soul-link.md) it revives each one's soulmates with it. |
| `/nuzlocke enable` · `disable` | 🛡️ | Master switch for this world, saved per world. |
| `/nuzlocke config list` | 👤 | Every setting for this world with its current value, by section. |
| `/nuzlocke config get <setting>` | 👤 | Read one setting back. |
| `/nuzlocke config set <setting> <value>` | 🛡️ | Change one, live. Offers the names and refuses a value out of range, or a choice it does not know: it answers in red, lists the choices that exist, and leaves the setting as it was. |
| `/nuzlocke config reset <setting>` | 🛡️ | Put one back to its default. |
| `/nuzlocke config reload` | 🛡️ | Re-read `config/cobblemon_nuzlocke.json`, no restart needed. A world with its own settings keeps them. |
| `/nuzlocke config unoverride` | 🛡️ | Drop this world's own settings, so it follows the config files again. |
| `/nuzlocke set <option> <value>` | 🛡️ | The older spelling of `config set`, kept working, with the same checks. |
| `/nuzlocke debug exp` | 🛡️ | Log what the level cap decides for each EXP gain. |
| `/nuzlocke soullink …` | 👤 | The co-op suite — see [Soul Link](soul-link.md). |
| `/pokemonrestart` | 👤 | Wipe your own run and start over. Its own command, not a `/nuzlocke` one — it belongs to the player whose run it is. Type it twice to confirm. It also takes you out of any Soul Link, forgets a trainer battle you walked away from, and offers the Gym Leader Challenge again when you pick your new starter. |

### `/nuzlocke soullink`

| Command | What it does |
| --- | --- |
| `link <player2> [player3] [player4]` | Offers a contract. Nothing binds until **everyone** accepts. |
| `accept` · `decline` | Answer an offer. The prompt also appears as a dialogue box you cannot dismiss, with a countdown. |
| `unlink` | Dissolves **your** binds. |
| `status` | Lists your binds in chat, with ✝ marking the dead. |
| `summary` | Opens your party's summary on the [Soul Link tab](soul-link.md#the-soul-link-tab). |
| `parties` | The linked-teams screen: every member's full party, offline members included, soulmates marked ⇄. |

Offering a link does not need the command — right-click a player and pick **Soul Link** from
Cobblemon's interaction wheel.

## Configuration

The ruleset is decided **when you create the world**, on a **NUZLOCKE** tab that sits next to
**GAME / WORLD / MORE**. Installing this add-on is what adds that tab; Routes' own generation options
live beside it on its [ROUTES tab](../routes/configuration.md).

<div class="flow" markdown>

1. <span class="flow__tag">Set</span> on the **NUZLOCKE** tab when you create the world
2. <span class="flow__tag flow__tag--or">Or later</span> with `/nuzlocke set <option> <value>`, live, with the same options
3. <span class="flow__tag flow__tag--result">Result</span> your world's rules, saved with that world and never overwritten later

</div>

Choices are stored **per world** and applied to new worlds only, so loading an existing world never
has its rules overwritten. Picking **Hardcore** at world creation turns the full ruleset on.

### The run

| Option | Default | Notes |
| --- | :---: | --- |
| Nuzlocke | on | master switch — off = a normal Cobblemon world |
| First-encounter lock | on | only the first wild per zone is catchable |
| Site encounters | on | structures grant one encounter per **kind** of site; off = none at all |
| Mandatory nicknames | on | the naming prompt |
| Whiteout | To Respawn Point | what losing a battle does — back to your respawn point, Game Over, or nothing |
| Healing sources | ALL | ALL / MACHINES_ONLY / ITEMS_ONLY / NONE |
| No bag in battle | on | closes the battle bag |
| Battle bag blocks | Everything | Everything, or **Healing only** — X items stay legal either way |
| Over cap to PC | on | over-cap catches are boxed (the cap itself comes from RCT) |
| File the dead to the PC | on | a Pokémon that dies is moved out of your party. Your last one always stays |
| Capture zones are | Geography | what counts as one place — the world Routes draws, the **biome** underfoot, or **both** as a pair |
| Require nicknames | on | the naming prompt after every acquisition |
| No trading | on | trades are refused |
| No forfeit | on | battles cannot be surrendered |
| Revival Blessing | off | whether that move may revive mid-battle |
| Healers set your respawn | on | the last healer you used is where you come back |
| Dupes match · Dupes count | evolution line · ever caught | the two halves of the duplicates clause |
| Allow Mega · Gigantamax · Z-Moves · Tera | on | switch off any battle gimmick for a stricter run |
| Duplicates clause | evolution line | what counts as "already owned" |
| Egg clause | Encounter | the hatchling takes the zone it hatches in — or ban eggs, or exempt them |
| Defeated-catch window | 60 s | how long a beaten wild stays catchable — or off |
| Aggressive wilds | on | some species start a battle instead of meleeing you |
| Shared EXP | on | whole team gains EXP |
| EXP boost | x1 | x1 … x50, applies to the shared EXP too |
| PC at block only | on | no remote PC access |

### Starters

| Option | Default | Notes |
| --- | :---: | --- |
| Starter selection | Mix | Normal / Random / Mix — Mix is a Grass, a Fire and a Water from three different generations, drawn from the real main-series starters |
| Starter level | 5 | 1–25 |
| No Legendaries · No Paradox · No Ultra Beasts | on | filters for the Random roll |
| No typical starters | off | excludes the pack's usual starters from Random |
| Shiny starter | Yes | No / Yes (normal odds) / Always |

### Gym Leader Challenge

| Option | Default | Notes |
| --- | :---: | --- |
| Gym Leader Challenge | on | offer every player a monotype run when they go to pick a starter; off = never offered |
| Mega / Tera OK | on | a Pokémon also counts as your type when its Tera type or a Mega form of its species carries it |

How the challenge plays is on the [ruleset page](nuzlocke.md#gym-leader-challenge).

### Roads, towns and trainers

| Option | Default | Notes |
| --- | :---: | --- |
| Route trainers | on | this mod's rules for the trainers Routes places; off = they behave as the trainer mod alone makes them. Needs a trainer mod |
| Trainer entity ID | `rctmod:trainer` | which NPC the rules apply to |
| Trainer sight range | 15 | 0–64 blocks |
| Trainer field of view | 180° | the cone you must stand in to be challenged, 30–360; 360 = they see behind them |
| One challenge gate | on | every challenge goes through this mod's guards; off = the trainer mod also challenges on its own, ignoring them |
| Always-aggressive trainers | `ltsurge` | ids that challenge on sight even though leaders normally wait |
| Challenge delay | 20 | ticks of "!" wind-up before the battle |
| Trainer skirmishes | on | trainers duel each other nearby |
| Trainers challenge on sight | on | off = they stay on the roads and never start a fight; you still battle them by right-clicking |
| Trainers holding post | 70% | share that stay put instead of wandering, 0–100 |
| Fair-fight guard | on | a trainer too far above your strongest Pokémon never picks the fight |
| Max level gap | 5 | how many levels above your strongest Pokémon a trainer may be and still challenge you, 0–50 |

Trainer density, water-crossing trainers and the Route Pokémon settings moved to Routes in 1.5.65,
along with the trainers and Pokémon themselves.

[Soul Link](soul-link.md#settings) has its own settings.
