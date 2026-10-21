# Troubleshooting

If yours is not here, post it in the [Discord](https://discord.gg/SwcwXcCN4k): it files the ticket
for you.

## My battle opened the normal battle screen

The server has that kind of battle turn-based: check `/cac format`. Triples, multi and free-for-all
battles are always turn-based, and so is a battle with a player morphed with Synchro Machine.

## I was refused at login

The server runs Action Combat and your game does not, or runs another version. Install the same
version as the server.

## Q does nothing

It needs **Cobblemon: Mega Showdown**, the right held item and key item ([Battle
gimmicks](moves.md#battle-gimmicks)), and it works once per fight. The chat line says which.

## B says I need a belt

Throwing a ball mid-fight needs **PokeBelt** ([Catching](fights.md#catching)), and only works in a
wild fight.

## Moves do not break anything

The `mobGriefing` game rule is off, `block_damage` is switched off, you are inside an arena
(`/cac arena list`), or the move is not strong enough for that block ([Block
damage](moves.md#block-damage)).

## An RCT trainer's battle is turn-based

The server log says why at start: RCT's version changed what Action Combat calls. Also check
`/cac format npc`.
