# Commands & Configuration

Everything is under `/poketrades`. Two commands are for every player; the rest need operator level 2.
A trader id written without a namespace is read as `cobblemon_poketrades:`.

## For every player

| Command | What it does |
| --- | --- |
| `/poketrades info` | the trader you look at: each offer, what it asks, and whether you can still take it |
| `/poketrades history` | your last 20 trades, newest first |

## Managing traders

| Command | What it does |
| --- | --- |
| `/poketrades spawn <trader>` | place an NPC that trades as `<trader>` where you stand |
| `/poketrades remove` | remove the trader you look at; its rolled offers and who took them are forgotten |
| `/poketrades list` | every loaded trader, with clickable coordinates (teleport) and UUID (copy) |
| `/poketrades reset <player> [trader] [offer]` | give a player back the offers they took: all of them, one trader's (by UUID), or one offer |
| `/poketrades reload` | reread every trader, pool, category and item value without a full `/reload` |

A broken definition file is skipped whole, with one line in the server log naming the file and the
field; everything else still loads. `reload` says how many errors and warnings there were.

## Building a trader in game

A trader can live in the **world** instead of a datapack, built one command at a time, with no JSON
to write. Only these traders can be edited by command: a datapack trader belongs to its datapack.

| Command | What it does |
| --- | --- |
| `/poketrades create <trader> [name]` | a new, empty trader |
| `/poketrades rename <trader> <name>` | its name, and the name tag of its loaded NPCs |
| `/poketrades delete <trader>` | remove it from the world; a datapack trader with the same id takes over |
| `/poketrades export <trader>` | write it as a datapack into `datapacks/poketrades_export/` |
| `/poketrades offer add <trader> <offer> <species> <gives>` | a Pokémon-for-Pokémon offer asking for `<species>`; `<gives>` is a Cobblemon Pokémon spec with a level, like `eevee level=15` |
| `/poketrades offer ask <trader> <offer> <condition> [value]` | set one condition of its ask |
| `/poketrades offer unask <trader> <offer> <condition>` | clear one |
| `/poketrades offer tier <trader> <offer> <1-5>` | set its tier |
| `/poketrades offer remove <trader> <offer>` | remove it |
| `/poketrades offer list <trader>` | its offers, buckets and nicknames |
| `/poketrades nickname add\|remove <trader> <name>` | the nicknames it gives |
| `/poketrades bucket add <trader> <pool> [count]` · `bucket remove <trader> <pool>` | draw offers from a pool |

A condition's value is written as in a datapack: a species, form, gender, nature, ability or ball id;
a level as its minimum; IVs as `perfect=N` or `hp=31,speed=20`; `shiny` takes none. An edit that
would break the trader is refused with nothing changed, and the reason in chat.

An exported trader loads from its datapack after `/reload`, but the world copy keeps precedence until
you `delete` it.

## Debug

| Command | What it does |
| --- | --- |
| `/poketrades debug category <species>` | its category, its default tier, and what decided it |
| `/poketrades debug roll <trader> [seed]` | preview the offers a trader would roll, without saving them |
| `/poketrades debug give <trader> <offer>` | hand yourself an offer's Pokémon as a trade would build it |
| `/poketrades debug validate` | check every definition and print each problem, without reloading |
| `/poketrades debug state [npc]` | what the world remembers of the trader you look at, or of one UUID |

## Configuration

Every feature can be switched off or tuned on a live server, and the change is saved at once to
`config/cobblemon_poketrades.json`.

| Command | What it does |
| --- | --- |
| `/poketrades config <feature>` | whether it is on, and its settings |
| `/poketrades config <feature> enabled <true\|false>` | switch it on or off |
| `/poketrades config <feature> <setting> <value>` | tune one setting |
| `/poketrades config <feature> reset` | that feature back to its defaults |
| `/poketrades config reset_all` | every feature back to its defaults |

| Feature | Setting (default, range) | Off means |
| --- | --- | --- |
| `npc_traders` | | no trader opens its screen, shows a marker, answers `info` or accepts a trade |
| `pc_selection` | | an ask is met from the party only; the screen hides the PC |
| `nickname_lock` | | a Pokémon a trader gave can be renamed like any other |
| `marker` | `range` (64, 8–256 blocks) | no marker over any trader |
| `server_wide_tier` | `min_tier` (5, 1–5) | every offer is once per player, none once for the whole server |
| `history` | `cap` (100, 1–1000 trades per player) | no trade is written to anyone's history |
| `reoffer` | `max_held` (6, 1–54) | a trader that offers what it receives keeps nothing new; what it holds stays offered |
| `battle_guard` | | trades, purchases and sales go through during a Cobblemon battle or an Action Combat fight; a Pokémon on your own battle team is still refused as busy |

`max_held` applies to a trader whose own definition sets no limit.

`battle_guard` is on by default, so nothing changes unless an operator runs
`/poketrades config battle_guard enabled false` (`/poketrades config battle_guard reset` brings the block back).
