# Getting Started

From an empty `mods/` folder to your first catch. Everything below links to the page that covers it
in full.

## Install

1. Install **[Routes](../routes/index.md)** 1.2.119 or newer, and Cobblemon. The full list for your
   loader is in the table at the bottom of the [home page](index.md#get-it).
2. Drop the jar for **your** loader into `mods/`, never both loaders at once.
3. On a server, install it **on the server and on every player's game**.

## Create the world

The ruleset is decided **when you create the world**, on a **NUZLOCKE** tab next to
**GAME / WORLD / MORE**. Installing this add-on is what adds that tab, and Routes' own options sit
beside it on its ROUTES tab.

- **Hardcore** turns the full ruleset on.
- **Capture zones are** decides what counts as one place: the world Routes draws, the **biome** you
  stand in, or both as a pair. **Biome** is the classic tabletop rule and works from the first minute;
  **Geography** grows with the road network. See [Zones](nuzlocke.md#zones).
- Every rule on the tab is a switch, and all of them can be changed later with
  `/nuzlocke config set`. See [Commands & Config](commands.md).

The choices are saved **with that world**. Loading an existing world never has its rules overwritten.
While the ruleset is on, the world is set to **Hard** every time it starts.

## Your first minutes

1. **The [Gym Leader Challenge](nuzlocke.md#gym-leader-challenge)** is offered to you at character
   creation: one type for the whole run, or decline it with one click.
2. **Pick your starter** from three. By default that is a Grass, a Fire and a Water from three
   different generations.
3. **Name it.** Every Pokémon you obtain gets a naming screen; for the starter, leaving before you
   name it undoes the pick, and you choose again from the same three.
4. **Go find your first encounter.** Only the first wild Pokémon you meet in a zone is catchable.
   Crossing into a new zone puts its name on screen with its state: ○ free, ● in progress,
   ✔ caught, ✘ lost.
5. Press **I** for the run's log: every zone you have found, what you caught there, and whether it
   is still alive.

## Playing with friends

Right-click a player and pick **Soul Link** from Cobblemon's interaction wheel. From then on the
Pokémon you caught in the same place live and die together. See [Soul Link](soul-link.md).

## Starting over

`/pokemonrestart` wipes your own run, typed twice to confirm. If you only want the roads, set
**Enable Nuzlocke** to off on the NUZLOCKE tab, or run `/nuzlocke disable` on a world that already
exists. See [Just want the routes?](nuzlocke.md#just-want-the-routes)
