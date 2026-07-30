# Modding Wiki

Every Cobblemon mod by **shiero**, documented in one place.

Every page lives in **this** repository — one site, one build, one source of truth — with a section
per mod. The mod repos themselves are private; the documentation is not. This page is just the front
door.

Each section follows the same shape: **Getting Started**, then the mod's own feature pages, then
**Commands**, **Configuration**, **Reporting Bugs & Ideas**, **Roadmap**, **Community Credits** and
**License**.

## The mods

<div class="grid cards" markdown>

-   ### [Cobblemon Routes](routes/index.md)

    Physical routes generated during worldgen that connect the world's structures, signposted and
    named like the games (`Route 3: Plains Forest`). Turns any Cobblemon world into a classic linear
    RPG.

    **MC 1.21.1 · Cobblemon 1.7.3 · Fabric + NeoForge**

-   ### [Cobblemon Picnic](picnic/index.md)

    Scarlet/Violet-style picnics in Cobblemon.

    **Fabric + NeoForge**

-   ### [Cobblemon Ditto HMs](ditto-hms/index.md)

    Classic-generation HMs for Cobblemon.

-   ### Cobblemon Nuzlocke & Soul Link *(coming)*

    The full Hardcore-Nuzlocke ruleset: per-zone first-encounter capture lock, permadeath, mandatory
    nicknames, a shiny clause, starter randomiser and level caps. All of it works **solo**.

    On top of that, **Soul Link**: the co-op mode where you link parties with friends and share fates
    — when one linked Pokémon dies, so do its soulmates.

    Currently being split out of Routes into its own mod. Until it ships, install **Cobblemon
    Routes** to get everything documented here — progress updates land in
    [the Discord](https://discord.gg/SwcwXcCN4k).

</div>

## Reporting bugs and requesting features

Every mod has its own Discord forum channels, and a bot turns posts into GitHub issues
automatically. You don't need a GitHub account: post in the mod's forum and that's it.

The bots live in [`intake-bots`](https://github.com/manucruzleiva/intake-bots), one per project.

---

!!! info "This wiki replaces the old per-mod wikis"
    Each mod used to have its own wiki at its own URL (`cobblemon-routes-wiki`,
    `cobblemon-picnic-wiki`, `cobblemon-ditto-hms`). There is now a single one:
    **manucruzleiva.github.io/mod-wiki/**. Old links published on Modrinth and CurseForge should be
    updated.

!!! tip "Want to fix or improve a page?"
    Every page here lives in [this repository](https://github.com/manucruzleiva/mod-wiki) — the mod
    repos themselves are private, but the documentation is not. Open a pull request against
    `docs/<mod>/` and it goes live on merge.
