<div class="hero hero--mod" markdown>

![Cobblemon Nuzlocke & Soul Link](assets/logo.png){ .hero-logo }

<div class="hero-copy" markdown>

# Cobblemon Nuzlocke & Soul Link

A full **Hardcore Nuzlocke** the game enforces for you — one catch per zone, permadeath, mandatory
nicknames, level caps — so you play the run instead of policing yourself. And if you play with
friends, **Soul Link** ties your catches together: the Pokémon you caught in the same place live and
die as one.

<span class="badge">MC 1.21.1</span> <span class="badge">Cobblemon 1.7.x</span> <span class="badge">Fabric</span> <span class="badge">NeoForge</span> <span class="badge">Requires Routes</span>

<div class="hero-actions" markdown>
[The ruleset](nuzlocke.md){ .md-button }
[Soul Link](soul-link.md){ .md-button }
</div>

</div>
</div>

## What it does

<div class="grid cards" markdown>

-   ### 🎮 [Hardcore Nuzlocke](nuzlocke.md)

    One catch per zone, permadeath you cannot heal your way out of, mandatory nicknames, level caps
    and a shiny clause. Works on a single-player world.

-   ### ❤️‍🔥 [Soul Link](soul-link.md)

    Catch in the same place as your partner and those two Pokémon are bound: one dies, both die.
    Two to four players. Optional.

-   ### 🎓 [Gym Leader Challenge](nuzlocke.md#gym-leader-challenge)

    One elemental type for the whole run — your starters are drawn from it, and your team may only
    carry it. Offered to each player at character creation.

-   ### 🗺️ [Trainers, gyms and a league](nuzlocke.md#what-it-builds-into-the-world)

    Trainers along the roads, a gym beside every town, and the Elite Four out on a road as a place
    of its own.

</div>

## Installing

It is an **add-on for [Routes](../routes/index.md)**: the zones it locks onto *are* the routes,
areas and towns Routes generates, so you need both. Get it from
[**Modrinth**](https://modrinth.com/mod/cobblemon-nuzlocke-soullink) or
[**CurseForge**](https://www.curseforge.com/projects/1630816), for **Fabric** or **NeoForge** on
Minecraft **1.21.1**.

| Also needs | |
| --- | --- |
| [Cobblemon](https://modrinth.com/mod/cobblemon) 1.7.x ([CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemon)) | the Pokémon |
| [Architectury API](https://modrinth.com/mod/architectury-api) ([CurseForge](https://www.curseforge.com/minecraft/mc-mods/architectury-api)) | both loaders |
| [Cloth Config](https://modrinth.com/mod/cloth-config) ([CurseForge](https://www.curseforge.com/minecraft/mc-mods/cloth-config)) | the settings screen |
| [Fabric API](https://modrinth.com/mod/fabric-api) ([CurseForge](https://www.curseforge.com/minecraft/mc-mods/fabric-api)) | Fabric only |

Trainers and level caps come from
[Radical Cobblemon Trainers](https://modrinth.com/mod/radical-cobblemon-trainers)
([CurseForge](https://www.curseforge.com/minecraft/mc-mods/radical-cobblemon-trainers)) when it is
installed; without it those features simply stand down.

## Zones come from Routes

The "one catch per zone" rule needs a definition of *zone*, and it takes it from
[Routes](../routes/index.md): the routes, areas and towns Routes generates are the capture zones.
That is why this is an add-on rather than a mod with its own map model.

!!! note "Not the *Cobblemon Nuzlocke* datapack"
    There is an unrelated [datapack by RRULE2001](https://modrinth.com/datapack/cobblemon-nuzlocke)
    with a similar name. This is a different project — a **mod** — which is why this one carries
    *Soul Link* in its name.
