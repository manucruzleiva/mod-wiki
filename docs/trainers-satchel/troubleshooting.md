# Troubleshooting

If yours is not here, post it in the [Discord](https://discord.gg/SwcwXcCN4k): it files the ticket
for you.

## The game will not start and names a mod

One of the [requirements](getting-started.md#requirements) is missing or older than the satchel needs,
usually **Accessories**. The message says which and which version; install that one.

## An item bounces back from a pocket

That pocket does not take it. Check where it belongs in the **Rules** button's list: `(tag)` means the
pocket tags decide, `▸` means an operator's rule does. An operator can send the item to another pocket
([Pockets & Rules](pockets.md#the-rules-screen)).

## A pocket is greyed out

You are in a Cobblemon battle (or a Cobblemon Action Combat fight): Agriculture, Architect and
Materials are closed until it ends ([In Battle & in the Field](in-the-field.md#in-a-battle)).

## Something comes back with "past the cap"

An operator set `battle balls_per_battle` or `items_per_battle`. The count starts again with the next
battle.

## Right-clicking the PC does not ask anything

`pc_storage` is switched off on the server, so the PC opens straight to Cobblemon's PC
([PC Item Storage](pc-storage.md#switching-it-off)).

## My Soul Link partner and I do not see the same PC storage

Sharing needs Cobblemon Nuzlocke on the server and `pc_storage soul_link_shared` on (it is by default),
and you must be in the same Soul Link. If you left the link your storage starts empty, and the shared
one stays with the others ([PC Item Storage](pc-storage.md#soul-link-one-storage-for-the-team)).

## The belt is not refilled

The refill needs PokeBelt (Fabric only), the satchel worn on your back and an Explorer Bag or better,
and it only refills with a ball of the **same kind** you just threw
([PokeBelt refill](in-the-field.md#pokebelt-refill)).

## My items disappeared after lowering the slots

They did not: items past the new slot count are hidden, not deleted. Raise the setting again and they
return ([Tiers](tiers.md)).

## The config file did not take my change

Use `/satchel config` on a live server ([Commands & Configuration](commands.md#satchel-config)). A
file that is not valid JSON is left as it is, and the settings in force stay.
