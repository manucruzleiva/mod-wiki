# How it works

## The window

A wild Pokémon that a **player beats in battle** does not vanish when the battle ends. Instead:

1. The moment it faints it is kept alive at **1 HP** so the end of the battle cannot remove it.
2. When the battle is over, it is put back on its feet at 1 HP, frozen in place, silent, and laid down
   **asleep**. Smoke rises from it.
3. Everyone within 48 blocks sees a message above their hotbar: *"Pikachu is down — 60s to catch it!"*
   (with the Pokémon's name and the window's length). It is also in Spanish for players on `es_es`.
4. The countdown starts **at that moment**, when the body appears, not when the Pokémon fainted.

While the window is open the Pokémon does not move, make a sound or wake up. You can walk up to it and
throw a ball.

The Pokémon stays at **1 HP for the whole window**. Cobblemon can still write 0 HP to a beaten wild
after the battle is won, so the mod puts it back to 1 HP the moment that happens and checks the
Pokémon's HP (not only its body's) every second. The countdown is not touched by this.

!!! note "Only a player's win counts"
    The window opens for wild Pokémon beaten in a battle that a player won. A Pokémon that was never
    in a battle with a player is left to Cobblemon as usual.

## Why it is easy to catch

The window puts the Pokémon to **sleep** (the status, not just the pose) and pins it at **1 HP**.
Cobblemon's capture formula reads exactly those two things, so a downed Pokémon is as easy to catch as
the formula allows. Your ball, your Pokémon's level and the Pokémon's catch rate still count as always.

## Catching it

Throw any Poké Ball. A successful catch ends the window and the Pokémon goes to your party or PC through
Cobblemon's normal capture flow.

## A missed ball

With the flee on (it is by default), a ball that fails changes what happens next:

1. The Pokémon breaks free of the ball.
2. It wakes up, cries, and **sprints away from the thrower**.
3. It fades out over `flee_ticks` (60 ticks, about 3 seconds by default) and is gone.
4. Balls thrown at it while it runs **catch nothing**. The chance is over.

With the flee off, a failed ball just lets the Pokémon go: it vanishes in a puff within a few seconds,
after the ball's break-free animation.

## When time runs out

If the window ends with no catch, the Pokémon vanishes in a puff of cloud and a short sound.

## No rematch

A downed Pokémon cannot enter a battle again, and neither can one that is running away. It can only be
caught.

## A save and reload

The end of the window is stored on the Pokémon as an absolute world time, so the window keeps counting
through a server restart or a chunk unload, and picks up again when the Pokémon loads.

A Pokémon that was running away when the server stopped is removed rather than saved mid-flee.

## What it does not do

- It does not give a second battle, extra experience or any reward: only the chance to catch.
- It does not touch Pokémon that were not wild, or battles between players.
- It does not change Cobblemon's capture formula.

Every part can be switched off in [Commands & Config](commands.md).
