# Troubleshooting

Common surprises, what causes them, and what to do. If yours is not here, post it in the
[Discord](https://discord.gg/SwcwXcCN4k): it files the ticket for you.

## My carving disappeared

A carving lives in the block it was cut into. Breaking the log, or building over the spot, takes it
with the block, and an axe that strips the bark takes the message too (unless an operator turned
`axeStrips` off). See [What a carving does not survive](getting-started.md#what-a-carving-does-not-survive).

## I cannot remove a carving with an axe

A message on a stripped log, a plank or other wood has no bark left to strip, and neither does any
carving when `axeStrips` is `false`. Break the block, or an operator can use
[`/treecarve remove`](server-admin.md#moderation).

## My carvings are gone after moving the world to 26.x

A world moved from Minecraft 1.21.1 to 26.x does not bring its carvings along: 26.x keeps them in a
file with a different name and does not read the old one. A world started on 26.x keeps its carvings
like any other.

## The wrong jar

Each Minecraft version has its own jar, and its file name ends in that version
(`tree-carve-fabric-2.0.0+26.3.jar`). Use the one for your Minecraft version and loader, never both
loaders at once.

## My custom symbol sheet looks wrong

The sheet must be white on transparent, or greyscale. See
[Custom Symbols & Fonts](symbols-and-fonts.md).
