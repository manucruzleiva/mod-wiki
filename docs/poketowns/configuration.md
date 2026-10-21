# Configuration

PokeTowns has no config file and no commands. There are two settings, both chosen when the world is
created.

| Setting | Where | Default |
| --- | --- | --- |
| Replace vanilla villages | the data pack screen when creating a world | on |
| Settlement spacing | the PokeTowns tab when creating a world | 34 chunks |
| Minimum gap | the PokeTowns tab when creating a world | 8 chunks |

## Vanilla villages

While the built-in data pack **PokeTowns: Replace Vanilla Villages** is on, vanilla villages stop
generating and PokeTowns settlements take their place. It is on in every new world.

To keep vanilla villages alongside PokeTowns, open **Data Packs** on the create-world screen and move
**PokeTowns: Replace Vanilla Villages** to the *Available* side.

While the pack is on:

- only the vanilla village set is emptied; villages that other mods add in their own sets still
  generate;
- pillager outposts no longer keep their distance from villages, because there are no vanilla
  villages for them to avoid.

!!! note "On a dedicated server"
    A server has no create-world screen. To start a server world without the pack, list the data
    packs with `/datapack list` on a test world, then add the pack's id to `initial-disabled-packs` in
    `server.properties` **before** the world is first generated. Turning the pack off in a world that
    already exists only affects chunks generated afterwards.

## Settlement spacing

The **PokeTowns** tab sits next to Game, World and More on the create-world screen.

| Slider | Range | Default | What it does |
| --- | --- | --- | --- |
| Settlement Spacing | 10–80 chunks | 34 | the world is cut into squares this many chunks wide, and each square may hold one settlement. Lower spacing means more settlements |
| Minimum Gap | 1 to one less than the spacing | 8 | two settlements never start closer than this. It always stays below the spacing, and moving the spacing down pulls it down with it |

The defaults are vanilla villages' own. The values are saved with the world and never change after
it is created. `/locate` and Routes use the world's own values.

!!! note "Defaults apply when"
    A dedicated server, a world created without opening the tab, and a world that existed before
    PokeTowns was installed all use 34 and 8.
