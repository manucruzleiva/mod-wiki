# Troubleshooting

Common surprises, what causes them, and what to do. If yours isn't here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k) — it files the ticket for you.

## The game won't start and names Cobblemon

Picnic needs **Cobblemon 1.8.0 or newer**. With Cobblemon missing, or on 1.7.x, the loader stops at
its dependency screen and says so. Update Cobblemon; nothing else needs changing.

## A re-roll cleared the area but spawned nothing

The table tells you which of two things went wrong:

- **"…nothing spawns on built ground."** You're on a built floor: planks, bricks, quartz,
  concrete, glass, wool. Cobblemon only spawns on natural ground (grass, dirt, stone, sand). Put down
  some natural blocks, or turn on [built platforms](spawn-rerolling.md#built-platforms) with
  `/picnic config platforms enabled true`.
- **"…there was nowhere around here to spawn any."** There's no ground near your altitude inside the table's radius,
  for example a tiny platform over the void. Make the platform bigger, or widen the table's reach with
  `/picnic config reroll radius <tier> <blocks>`.

Over an ocean or a river the message names the biome, because the biome decides which Pokémon can
come at all. The bread is spent either way: the area was cleared, and that can't be undone.

## The table said it spawned Pokémon, but I can't see them

Fliers take off. For 30 seconds after a re-roll a flier that leaves the table's radius turns back, so
look up and around. If you set `flierleash` to `0`, they roam at once. See
[Pokémon that fly](spawn-rerolling.md#pokemon-that-fly-spawn-flying).

## "The table is still resting…"

There's a cooldown (5 seconds by default) **per table and per player**. Swapping tables doesn't skip
it. The blocked attempt costs no bread. An operator can change it with
`/picnic config reroll cooldown <seconds>`.

## "Out of bread!"

Each re-roll costs bread (7 / 5 / 3 by tier). It comes from the table's fuel slot or from a placed
[Picnic Basket](interactions-and-items.md#picnic-baskets) nearby.

## My settings screen changes do nothing on a server

The Mod Menu / Cloth Config screen edits **your own** config file. On someone else's server the
server's settings win, and the screen says so. Ask an operator to use `/picnic config`.

## A Diving, Hot or Strange table wrecks things

They're built for one place: underwater, the Nether, the End. Anywhere else they flood, scorch or
won't stay put. See [where each table can go](picnic-tables.md#where-each-table-can-go). An operator can
turn that off with `/picnic config hazards enabled false`.

## Reporting a bug

Every re-roll is written to `logs/latest.log` (unless `/picnic config reroll log false`): what was
cleared and what spawned, with species, level and position. Attach that part of the log to a report
and it already says what happened.

## Known limitations

- **Re-rolls never guarantee a shiny.** The table only asks Cobblemon to spawn again; the odds are
  Cobblemon's, improved only by the [Shiny Aura](shiny-aura.md).
- **Seat counts are fixed per tier** and can't be configured.
- *Until the next release*, a re-roll also clears a wild Pokémon another player is battling or
  catching inside its radius.
