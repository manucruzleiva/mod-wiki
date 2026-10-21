# Getting Started

## Install

Cobblemon Raid Icons is **client-side**. It goes in your own `mods/` folder and nowhere else: the
server does not need it, does not know you have it, and cannot tell the difference. Play on any
server that runs raid dens.

Drop **one** jar — the one for your loader, never both.

=== "Fabric"

    | | |
    |---|---|
    | Minecraft | 1.21.1 |
    | Required | [Fabric API](https://modrinth.com/mod/fabric-api) · [Fabric Language Kotlin](https://modrinth.com/mod/fabric-language-kotlin) |
    | Required | [Cobblemon Raid Dens](https://modrinth.com/mod/cobblemonraiddens) ([CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemonraiddens)) |
    | For the icons | [Xaero's Minimap](https://modrinth.com/mod/xaeros-minimap) and/or [Xaero's World Map](https://modrinth.com/mod/xaeros-world-map) |

=== "NeoForge"

    | | |
    |---|---|
    | Minecraft | 1.21.1 |
    | Required | [Kotlin for Forge](https://modrinth.com/mod/kotlin-for-forge) |
    | Required | [Cobblemon Raid Dens](https://modrinth.com/mod/cobblemonraiddens) ([CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemonraiddens)) |
    | For the icons | [Xaero's Minimap](https://modrinth.com/mod/xaeros-minimap) and/or [Xaero's World Map](https://modrinth.com/mod/xaeros-world-map) |

Optional: [Cloth Config](https://modrinth.com/mod/cloth-config) adds a
[settings screen](configuration.md#the-settings-screen), and on Fabric
[Mod Menu](https://modrinth.com/mod/modmenu) puts its button in the mod list. Without them every
setting still changes with [`/raidicons config`](commands.md#raidicons-config).

Cobblemon Raid Dens brings [Cobblemon](https://modrinth.com/mod/cobblemon) and GeckoLib with it, so
you do not install those separately for this mod's sake.

!!! tip "One Xaero is enough"

    Install the minimap alone and you get icons on the minimap. Install the world map alone and you
    get icons and tooltips on the big map. Install both and you get both. With neither, the mod loads
    and quietly draws nothing.

## What you should see

Walk into a world with raid dens in it. Within a few seconds of a den's chunk arriving, its tera
type icon appears where it stands — a fire den shows the Fire icon, a stellar den the Stellar one.

The mod only knows about dens in chunks the game has already sent you, so **icons fill in as you
walk**. Teleporting across the map and expecting it to be covered in markers is the one thing that
looks broken and is not: there is nothing loaded out there to find.

Open the world map and hover a den to see [what is waiting in it](map-icons.md#the-tooltip) and
[when it next resets](map-icons.md#the-den-clock).

To hide the dens you do not want, run [`/raidicons`](commands.md#raidicons) for the settings screen,
or [`/raidicons config`](commands.md#raidicons-config) to change settings from chat.

## When nothing shows up

Run [`/raidicons report`](commands.md#raidicons-report) while aiming at a den crystal. In one screen it tells you whether
the den block is in the registry, whether Xaero's layers were found, how much the scan has covered,
and what the game says the block in front of you actually is.
