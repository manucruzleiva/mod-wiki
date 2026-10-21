---
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# Cobblemon mods by shiero

Mods that turn a Cobblemon world into an adventure: roads and towns worth exploring, a Nuzlocke
that enforces itself, every HM in your own hands, and more. The documentation for all of them lives
here.

<div class="hero-actions" markdown>
[Browse the mods](#the-mods){ .md-button }
[Report a bug](#found-a-bug-or-have-an-idea){ .md-button }
[Discord](https://discord.gg/SwcwXcCN4k){ .md-button }
</div>

</div>

## The mods

<div class="mod-filter" role="group" aria-label="Show only some mods" hidden>
<button type="button" data-filter="" aria-pressed="true">All</button>
<button type="button" data-filter="client-only" aria-pressed="false">Client-only</button>
<button type="button" data-filter="no-cobblemon" aria-pressed="false">No Cobblemon</button>
</div>

<div class="mod-list" markdown>

<div class="mod-row" data-mod-color="routes" data-tags="no-cobblemon" markdown>
![](routes/assets/logo.png){ .mod-row__logo }
<div class="mod-row__body" markdown>
[Routes](routes/index.md){ .mod-row__name }
<span class="mod-row__what">Roads between your structures, named routes and map integration.</span>
<span class="mod-row__chips"><span class="badge">No Cobblemon</span></span>
</div>
</div>

<div class="mod-row" data-mod-color="nuzlocke" data-tags="" markdown>
![](nuzlocke/assets/logo.png){ .mod-row__logo }
<div class="mod-row__body" markdown>
[Cobblemon Nuzlocke & Soul Link](nuzlocke/index.md){ .mod-row__name }
<span class="mod-row__what">A Hardcore Nuzlocke the game enforces, plus co-op Soul Link.</span>
<span class="mod-row__chips"><span class="badge">Cobblemon 1.8</span> <span class="badge">Needs Routes</span></span>
</div>
</div>

<div class="mod-row" data-mod-color="picnic" data-tags="" markdown>
![](picnic/assets/logo.png){ .mod-row__logo }
<div class="mod-row__body" markdown>
[Cobblemon Picnic](picnic/index.md){ .mod-row__name }
<span class="mod-row__what">A picnic table that re-rolls the wild spawns around it.</span>
<span class="mod-row__chips"><span class="badge">Cobblemon 1.8+</span></span>
</div>
</div>

<div class="mod-row" data-mod-color="ditto-hms" data-tags="" markdown>
![](ditto-hms/assets/logo.png){ .mod-row__logo }
<div class="mod-row__body" markdown>
[Cobblemon Ditto HMs](ditto-hms/index.md){ .mod-row__name }
<span class="mod-row__what">20 HMs you learn yourself, paid for in hunger.</span>
<span class="mod-row__chips"><span class="badge">Cobblemon 1.8+</span></span>
</div>
</div>

<div class="mod-row" data-mod-color="raid-icons" data-tags="client-only" markdown>
![](raid-icons/assets/logo.png){ .mod-row__logo }
<div class="mod-row__body" markdown>
[Cobblemon Raid Icons](raid-icons/index.md){ .mod-row__name }
<span class="mod-row__what">Every raid den on your minimap and world map.</span>
<span class="mod-row__chips"><span class="badge">Client-only</span> <span class="badge">Needs Raid Dens</span></span>
</div>
</div>

<div class="mod-row" data-mod-color="champions" data-tags="" markdown>
![](champions/assets/logo.png){ .mod-row__logo }
<div class="mod-row__body" markdown>
[Cobblemon Champions Training](champions/index.md){ .mod-row__name }
<span class="mod-row__what">Stat points instead of EVs, spent from the summary.</span>
<span class="mod-row__chips"><span class="badge">Cobblemon 1.8</span></span>
</div>
</div>

<div class="mod-row" data-mod-color="mid-battle-exp" data-tags="" markdown>
![](mid-battle-exp/assets/logo.png){ .mod-row__logo }
<div class="mod-row__body" markdown>
[Cobblemon Mid-Battle EXP](mid-battle-exp/index.md){ .mod-row__name }
<span class="mod-row__what">EXP at every knockout, used in the same battle.</span>
<span class="mod-row__chips"><span class="badge">Cobblemon 1.7–1.8</span></span>
</div>
</div>

<div class="mod-row" data-mod-color="tree-carve" data-tags="no-cobblemon" markdown>
![](tree-carve/assets/logo.png){ .mod-row__logo }
<div class="mod-row__body" markdown>
[Tree Carve](tree-carve/index.md){ .mod-row__name }
<span class="mod-row__what">Carve messages and symbols into logs with a sword.</span>
<span class="mod-row__chips"><span class="badge">No Cobblemon</span> <span class="badge">MC 1.21.1 · 26.x</span></span>
</div>
</div>

<div class="mod-row" data-mod-color="poketowns" data-tags="" markdown>
![](poketowns/assets/logo.png){ .mod-row__logo }
<div class="mod-row__body" markdown>
[Cobblemon PokeTowns](poketowns/index.md){ .mod-row__name }
<span class="mod-row__what">Pokémon Centers, Marts and gyms in your villages.</span>
<span class="mod-row__chips"><span class="badge">Not released yet</span></span>
</div>
</div>

</div>

Every mod runs on **Minecraft 1.21.1**, on **Fabric** and **NeoForge**.

## Start here

<div class="grid cards" markdown>

-   ### :material-download: Installing

    Every mod runs on **Minecraft 1.21.1** on either **Fabric** or **NeoForge**. Drop the jar for your
    loader into `mods/` — never both jars at once.

    The Cobblemon mods also need **Cobblemon**; each one's *Getting Started* page names the version.
    **Routes and Tree Carve do not.** Tree Carve also runs on Minecraft 26.1 to 26.3, with a jar for
    each version.

    Each mod's *Getting Started* page lists its own dependencies.

-   ### :material-tune: Configuring

    Routes and Nuzlocke are set up on the **world-creation screen** and stored with that world.
    Picnic, Ditto HMs and Raid Icons use in-game config: a command, or a settings screen. Tree Carve
    is set by operators with `/treecarve config`. Mid-Battle EXP has nothing to configure.

    See each mod's *Configuration* page.

-   ### :material-map-search: Finding things

    Every section follows the same order: **Getting Started**, the mod's own feature pages,
    **Commands**, **Configuration**, **Community Credits**.

    The search box at the top covers every mod at once.

</div>

## Found a bug, or have an idea?

Post in the mod's **tickets thread on [Discord](https://discord.gg/SwcwXcCN4k)** and tag it —
**Bug**, **Crash**, **Idea** or **Feedback**. A bot files it as an issue, replies in your thread
with what it needs from you, and posts back there when it is closed. **You do not need a GitHub
account.**

For a crash, attach `crash-reports/crash-*.txt` — the stack trace is what turns a hunt into a fix.

Something wrong on a page? Say so in the Discord — same place, same thread, and it gets fixed here.
