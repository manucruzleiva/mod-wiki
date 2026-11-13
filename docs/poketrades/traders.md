# Traders

A trader is someone in the world who swaps Pokémon with you. Right-click one and its trade screen
opens: its offers on the right, your party on the left, and, under the two portraits, every condition
of the offer with a mark for whether your Pokémon meets it.

## Who trades

Three kinds of entity can be a trader. Each one trades as a **trader definition**, which says its
name, its nicknames and where its offers come from. The definitions come from datapacks ([Datapack Format](datapacks.md)), or
are built in game by an operator ([Commands](commands.md#building-a-trader-in-game)).

### Cobblemon NPCs

Any Cobblemon NPC trades when its interaction names a trader. That works on an NPC class, a preset or
a single NPC, however it got into the world: placed with Cobblemon's NPC tools, spawned by a
structure, or placed with `/poketrades spawn <trader>`, which also dresses it in the trader's white
coat.

```json
{
  "names": ["Trader Wilma"],
  "interaction": {
    "type": "cobblemon_poketrades:trade",
    "trader": "wilma"
  }
}
```

A trader id without a namespace is read as `cobblemon_poketrades:`. An id no datapack loads does
nothing on click, and the server log says so once.

### Village traders

An unemployed villager next to a **Cobblemon PC** takes the **Pokémon Trader** profession, with an
open coat over its village's own clothes (and a worn version once zombified). Its right-click always
opens the trade screen, never the vanilla one. It trades as the `villager` trader: by default five
offers from the common, uncommon and item pools. It never levels up, and breaking its PC makes it lose
the profession.

### RCT trainers

With **Radical Cobblemon Trainers** installed, a trainer trades once you have **beaten** it, by RCT's
own record of who beat whom, and from then on for good. Everyone who has not beaten it still gets the
battle. When the battle ends, the trainer tells you its right-click trades now.

A trainer carries offers when a trader named `rct/<trainer id>` is loaded, for example
`data/cobblemon_poketrades/poketrades/traders/rct/leader_brock.json`. Every copy of that trainer
offers the same, and each player takes each offer once.

## Offers

A trader holds **fixed offers**, which it always has, and **buckets**, each drawing a number of offers
at random from an offer pool. The draw happens **once**, the first time anyone uses that trader, and
is kept for good: a reload or a changed datapack never rerolls it. Two NPCs built from the same
structure roll apart.

Each offer can be taken **once per player per trader**. From tier 5 (by default) an offer is **once for
the whole server**: the first player to take it claims it, and everyone else sees it locked as taken by
another player. An operator changes that tier, or switches it off, with
[`server_wide_tier`](commands.md#configuration).

### Offer types

| Type | The trader gives | It asks for |
| --- | --- | --- |
| Pokémon for Pokémon | a Pokémon | a Pokémon that meets its conditions |
| Pokémon for items | a Pokémon | items |
| Pokémon for money | a Pokémon | money |
| Buy with items | items | a Pokémon that meets its conditions |
| Buy with money | money | a Pokémon that meets its conditions |

- **Items** count by id alone: any emerald is an emerald, whatever its name or enchantments. Your
  whole inventory counts, offhand and armour included. The screen shows how many of each you carry.
  Items a trader pays that do not fit in your inventory drop at your feet.
- **Money** needs a currency. With **CobbleDollars** installed the price leaves your balance, or the
  payment lands in it, only when the server confirms the trade. Without a currency, money offers are
  left off every trader and the server log says so once.

### What an ask can require

The Pokémon a trader asks for is a list of conditions, and your Pokémon must meet all of them:

| Condition | Met when your Pokémon… |
| --- | --- |
| species | is that species |
| form | is in that form (`alola`, `galar`…) |
| gender | is male, female or genderless |
| nature | has that nature; a **mint** counts |
| ability | has that ability |
| IVs | has at least the IVs asked per stat, or that many perfect (31) IVs; a **Bottle Cap** counts |
| level | is at least that level |
| shiny | is shiny |
| ball | was caught in that ball |

How each is written: [Conditions](datapacks.md#conditions). Other mods can add conditions of their own
([For Mod Authors](api.md#ask-conditions)).

## Tiers

Every offer has a tier from 1 to 5. In a Pokémon-for-Pokémon offer the tier follows how rare the
Pokémon the trader gives is, and says how much the ask carries:

| Tier | Gives a Pokémon that is… | The ask carries |
| --- | --- | --- |
| 1 | common | the species only |
| 2 | uncommon | + 1 condition |
| 3 | rare, baby or fossil | + 2 conditions |
| 4 | starter or paradox | + 3 conditions, or a minimum IV |
| 5 | legendary, mythical or Ultra Beast | perfect IVs, or shiny |

A species' category comes from its own Cobblemon labels first (mythical, legendary, Ultra Beast,
paradox, starter, fossil, baby); a species with none of them is **common** with a catch rate of 120 or
more, **rare** at 45 or less, and **uncommon** in between. Pokémon from other mods follow the same
rule, and a datapack can set the category of any species. An operator checks one with
`/poketrades debug category <species>`.

For item offers the tier is what the items are worth, counted in emeralds:

| Worth | up to 10 | up to 30 | up to 80 | up to 200 | above 200 |
| --- | --- | --- | --- | --- | --- |
| Tier | 1 | 2 | 3 | 4 | 5 |

For money offers it is the price:

| Price | up to 2,500 | up to 10,000 | up to 40,000 | up to 120,000 | above 120,000 |
| --- | --- | --- | --- | --- | --- |
| Tier | 1 | 2 | 3 | 4 | 5 |

A trader pays about a quarter of what it sells a Pokémon for.

## The trade screen

- The trader's offers fill the right grid, six to a page. An offer you already took, or a
  once-per-server one another player claimed, stays on the grid locked and says why.
- Your party fills the left grid. A Pokémon that misses the ask carries a lock but can still be
  picked, so the marks show what it lacks.
- **PC** opens your boxes one at a time, with how many Pokémon in each box match. A Pokémon in your PC
  can be traded like one in your party (unless the server switched
  [`pc_selection`](commands.md#configuration) off).
- Press **Trade**. The server checks everything again: that the trader is within 8 blocks, the offer is
  still yours to take, and the Pokémon is still yours and meets the ask. A chat line says what you
  traded, and the screen opens again with that offer locked as taken.

A trade happens **whole or not at all**. You cannot trade while in a battle (a Cobblemon battle, or a
[Cobblemon Action Combat](../action-combat/index.md) fight with Action Combat 0.1.48 or newer), nor a
Pokémon tethered to a pasture. An operator can switch the battle block off with
[`battle_guard`](commands.md#configuration): trades then go through mid-battle, but a Pokémon on your
own battle team is still refused as busy. A Pokémon you sent out goes back to its ball first. Leaving the game mid-trade, pressing
twice, or two players confirming the same once-per-server offer at the same moment never moves a
Pokémon that should not move. With a full party the Pokémon you receive goes to your PC, and with a
full party and PC it takes the slot your Pokémon leaves.

## The Pokémon you receive

- It comes out **like a wild Pokémon of its level**, with whatever the offer does not fix (IVs,
  nature, gender, ability, moves…) rolled as a spawn would. It is never shiny and comes in a Poké Ball,
  unless the offer says otherwise.
- The trader is its **original trainer**, and it carries a **nickname** from the trader's list (or its
  species name when the list is empty). That nickname **cannot be changed**: renaming it snaps back,
  and a name tag on it fails without being used up.
- It arrives **as from any Cobblemon trade**: its friendship starts at its species' base value, a
  Pokémon that evolves by trading (Kadabra, Haunter, Machoke…) offers its evolution right away, and the
  trade counts for Cobblemon's trade advancements and statistic.

## Where your Pokémon goes

Each trader decides what happens to the Pokémon you give it:

- **Gone** (the default): only your trade history remembers it.
- **Offered to the next players**: the trader holds it, six at a time by default, the oldest leaving
  first. Other players see it as you gave it, with you as its original trainer and your nickname,
  which they can change. You never see your own Pokémon offered back, and each one can be traded once.
  Its ask is borrowed from the trader pools of its own category and tier.
- **Joins the trainer's team**, for an RCT trainer: it is added to that trainer's battle team, six at
  most. The trainer's own members always stay, the oldest traded one leaves to make room, and every
  player meets the same team.

## The marker

A trader that still holds an offer you can take carries Cobblemon's trade icon over its head, on every
trader within 64 blocks. Once you have taken all its offers the marker goes away for you, while other
players still see theirs. A once-per-server offer another player claims takes the marker away for
everyone it was the last offer for.

## Looking a trader up

- `/poketrades info`, looking at a trader: each offer, what it gives, every condition or item of its
  ask, and whether you can still take it.
- `/poketrades history`: the trades you made, newest first.

Neither says where a trader stands: finding one is part of the game.
