<div class="hero hero--mod" markdown>

![Cobblemon Nuzlocke & Soul Link](assets/logo.png){ .hero-logo }

<div class="hero-copy" markdown>

# Cobblemon Nuzlocke & Soul Link

A full **Hardcore Nuzlocke** the game enforces for you — one catch per zone, permadeath, mandatory
nicknames, level caps — so you play the run instead of policing yourself. And if you play with
friends, **Soul Link** binds your parties: when one linked Pokémon dies, so do its soulmates.

<span class="badge badge--soon">Not released yet</span> <span class="badge">Requires Routes</span> <span class="badge">MC 1.21.1</span>

<div class="hero-actions" markdown>
[The ruleset](nuzlocke.md){ .md-button }
[Soul Link](soullock.md){ .md-button }
</div>

</div>
</div>

!!! warning "Not released yet"
    This mod is being split out of [Routes](../routes/index.md), where all of these features
    currently ship. Until the split lands, install **Routes** to get everything documented
    here. Progress updates land in [the Discord](https://discord.gg/SwcwXcCN4k).

    It will be published as
    [**Cobblemon Nuzlocke & Soul Link**](https://modrinth.com/project/cobblemon-nuzlocke-soullink/)
    on Modrinth and CurseForge.

!!! note "Not to be confused with the *Cobblemon Nuzlocke* datapack"
    There is an unrelated [datapack by RRULE2001](https://modrinth.com/datapack/cobblemon-nuzlocke)
    with a similar name and goal. This is a different project — a **mod**, not a datapack — which is
    why this one carries *Soul Link* in its name.

## What it does

### [Hardcore Nuzlocke](nuzlocke.md) — works solo

- **First-encounter capture lock** — one catch per zone, and the zone is the route or area you are
  standing in.
- **Permadeath with heal-blocking** — a fainted Pokémon is gone, and you cannot heal your way out.
- **Mandatory nicknames** — every Pokémon you obtain gets named before you can use it.
- **Shiny clause** — a wild shiny is always catchable, no matter the encounter rule.
- **Starter randomiser** with filters for legendaries, paradox forms and Ultra Beasts.
- **Level caps**, EXP tuning, battle restrictions (Mega / Gigantamax / Z-Moves / Tera) and a
  configurable **Defeated-Catch window**.

### [Soul Link](soullock.md) — co-op

Link parties with other players so your runs are bound together: when one linked Pokémon dies, so do
its soulmates. Includes a lone-combat block so nobody grinds ahead alone.

Soul Link is **optional** — it has its own toggle, and the whole Nuzlocke ruleset above works
perfectly well on a single-player world.

## Zones come from Routes

The "one catch per zone" rule needs a definition of *zone*, and it takes it from
[Routes](../routes/index.md): the routes, areas and towns that Routes generates are the
capture zones. That is why this mod **depends on Routes** rather than shipping its own zone model.
