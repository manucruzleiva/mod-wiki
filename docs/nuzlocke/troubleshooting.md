# Troubleshooting

Common surprises, what causes them, and what to do. If yours is not here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k): it files the ticket for you.

## The game will not start and names Routes

This is an add-on for [Routes](../routes/index.md), and it needs Routes **1.2.119 or newer**. Older
Routes cannot host it, so the loader stops and names it. Update Routes. The rest of what to install is
in the table at the bottom of the [home page](index.md#get-it).

## There is no NUZLOCKE tab, or my world ignores my rules

The tab is on the create-world screen, next to **GAME / WORLD / MORE**, and the rules are saved with
the world when it is created. Loading an existing world never has its rules overwritten. To change
one in a world that exists, use `/nuzlocke config set <setting> <value>`; see
[Commands & Config](commands.md).

## My Poké Balls bounce

That zone is spent: only the first wild Pokémon you meet in a zone is catchable, and fleeing or
knocking it out spends it just the same. A wild shiny is always catchable, and a duplicate of a line
you already own does not spend the zone. See [The rules](nuzlocke.md#the-rules).

## A Pokémon I caught will not battle

Two causes:

- **Gym Leader Challenge.** Every living Pokémon in your party must carry your type, or the battle
  does not start; the message names the ones to box first. See
  [What the type changes](nuzlocke.md#what-the-type-changes).
- **Soul Link.** A Pokémon you caught where your partner has not caught yet is *pending*, and cannot
  battle until they catch there too. A bound one stays in its ball unless its partners are in their
  owners' active parties, and those owners are online. See [Soul Link](soul-link.md#when-it-goes-wrong).

## No trainers or level caps

Those come from [Radical Cobblemon Trainers](https://modrinth.com/mod/radical-cobblemon-trainers).
Without it, those features stand down and the rest of the ruleset keeps working.

## I want to start over

`/pokemonrestart` wipes your own run; type it twice to confirm. An operator can instead use
`/nuzlocke reset` or `/nuzlocke revive`. See [Commands & Config](commands.md#quick-reference).
