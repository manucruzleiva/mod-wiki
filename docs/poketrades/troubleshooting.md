# Troubleshooting

If yours is not here, post it in the [Discord](https://discord.gg/SwcwXcCN4k): it files the ticket
for you.

## I can't join the server

The server runs PokeTrades and your game does not. Install it on your game too: a trader's NPC data
is sent to every client, and a client without the mod cannot read it.

## Right-clicking a trader does nothing

Its interaction names a trader no datapack loads: the server log says which, once. If the line above
the hotbar says the trader **is not trading on this server**, an operator switched `npc_traders` off.
If it says **it has nothing to trade right now**, you have taken every offer it has for you.

## An RCT trainer battles me instead of trading

You have not beaten that trainer yet, by RCT's own record. Beat it once and its right-click trades
from then on.

## A trader has no money offers

Money offers need a currency: install **CobbleDollars**. Without it they are left off every trader,
and the server log says so once.

## I can't pick a Pokémon from my PC

The server switched `pc_selection` off: asks are met from the party only.

## The trade was refused

The server checks everything again when you press **Trade**. It refuses when you are in a battle (a Cobblemon battle or, with Action Combat 0.1.48 or newer, one of
its real-time fights: trade once it is over; an operator can switch this block off with `battle_guard`,
but a Pokémon on your own battle team is then still refused as busy), the
Pokémon is tethered to a pasture, you walked more than 8 blocks from the trader, or another player
just claimed that once-per-server offer. Nothing changes hands when a trade is refused.

## I can't rename a Pokémon I got in a trade

That is the nickname lock: a Pokémon a trader gave keeps the name the trader gave it. An operator
can switch `nickname_lock` off.

## My datapack trader doesn't show up

Run `/poketrades debug validate`: it prints every problem in every file, naming the file and the
field. A file with an error is skipped whole; an unknown field is only a warning.
