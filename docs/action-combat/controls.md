# Controls

While you drive a Pokémon the keys go to it, never to your Trainer. Every key below can be rebound
in **Options → Controls → Cobblemon Action Combat**, except the ones that reuse a vanilla key.

| Key | What it does |
| --- | --- |
| **W A S D**, mouse | move and turn, at the Pokémon's own Speed |
| **Space** | jump; a double tap takes off with a species that flies, then Space climbs and sprint dives |
| **1 2 3 4** (the hotbar keys) | ready one of the Pokémon's four moves; another key swaps it, its own key again lets it go |
| **Left click** (attack) | fire the readied move; a close-range one needs an opponent in reach |
| **Shift** (sneak) | dodge: a 4-block dash, with a moment where nothing hits you |
| **Right click** (use) | Protect: a bubble that blocks every hit for a second and a half |
| **Z** | lock onto an opponent; **Tab** moves the lock to the next one; Z again lets go |
| **Q** | the battle gimmick: Mega, Tera, Dynamax or Z-Move ([see here](moves.md#battle-gimmicks)) |
| **H** | in doubles, swap control to your other Pokémon |
| **G** (hold) | the consumable wheel: scroll to pick a potion, berry or X item, let go to throw it |
| **B** | throw PokeBelt's selected Poké Ball at the locked target; the scroll wheel picks the ball |
| **R** (Cobblemon's send-out key) | tap to switch Pokémon (15 s between your own switches), hold 2 s to run away or forfeit |

## Stamina

Moves cost **Stamina** instead of PP, and so do the dodge, Protect and flying. The bar above the XP
bar refills on its own a moment after you stop spending. Run it dry and your Pokémon is **exhausted**
for 3 seconds: it moves at half speed and cannot use moves or take off.

## The fight HUD

Your Pokémon's HP and Stamina sit in one panel, your target's HP in another, and your four moves
show their key, cost and cooldown. Damage numbers rise from each hit. `/cachud layout` picks one of
three layouts.

### The controls list

At the start of each fight a list shows every fight control with the key it is bound to **now**, so
a rebind shows in it: lock on (and the key for the next target), the four move keys, the click that
fires, dodge, Protect, the item wheel, the belt's ball, switching (hold to flee), the doubles swap and
the gimmick. A control whose feature the server has turned off is left out.

It sits half-way down the left edge in the `ticket` layout, half-way down the right edge in `pokemon`
and at the top left in `bottom`, clear of the bars and the moves.

By default it shows for the first 10 seconds of each fight. A switch does not start it again; a new
fight does. Each player picks when it shows with `/cachud controls`:

| Command | When the list shows |
| --- | --- |
| `/cachud controls first_seconds [n]` | the first `n` seconds of each fight (default 10) |
| `/cachud controls always` | the whole fight |
| `/cachud controls never` | not at all |
| `/cachud controls` | says which one is in use |

The choice is saved on your own client, so it stays after a restart. The server can turn the list
off for everyone with `/cac config hud controls false`.

## The camera

The camera sits behind your Pokémon in third person, further back the bigger it is, and F5 is locked
for the fight. Your own camera mode comes back when it ends.
