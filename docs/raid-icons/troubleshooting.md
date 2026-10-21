# Troubleshooting

Common surprises, what causes them, and what to do. If yours is not here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k): it files the ticket for you.

## No icons show up

Run [`/raidicons report`](commands.md#raidicons-report) while aiming at a den crystal. In one screen
it tells you whether the den block is in the registry, whether Xaero's layers were found, how much
the scan has covered, and what the game says the block in front of you actually is.

## Icons only on the minimap, or only on the world map

Each Xaero mod carries its own icons. The minimap alone gives icons on the minimap; the world map
alone gives icons and tooltips on the big map; both give both. With neither, the mod loads and quietly draws
nothing.

## Icons appear only as I walk

The mod can only find dens in ground your game has loaded. See
[Why icons appear as you walk](map-icons.md#why-icons-appear-as-you-walk).

## There is no settings screen

The screen comes from [Cloth Config](https://modrinth.com/mod/cloth-config), and on Fabric its button
from [Mod Menu](https://modrinth.com/mod/modmenu). Without them every setting still changes with
[`/raidicons config`](commands.md#raidicons-config).

## Do I install it on the server?

No. Raid Icons is client-side: it goes in your own `mods/` folder and nowhere else.
