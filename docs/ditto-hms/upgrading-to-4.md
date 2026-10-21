# Upgrading to 4.0

4.0 brings Ditto HMs back to what it was meant to be: **you are a Ditto, copying what you need to move
through the world and shape it.** Over 75 HMs it had become a little of everything, including a
combat mod. Now there are **20 HMs that are yours**, the moves that belong to a Pokémon are done by
your Pokémon, and everything that fights lives in **Cobblemon Action Combat**.

## Your save

Nothing to do, and nothing you paid for is lost. The first time each player joins after the update:

- An HM **merged** into another one teaches you the one it became. If you had **Glide** switched
  on, **Fly** comes on in its place (unless Magnet Rise is running — the two do not mix).
- Any other HM that is no longer yours is forgotten, and **its trigger item is handed back** — or
  dropped at your feet if your inventory is full.
- A chat message lists exactly what happened.

The config file is updated too, and only where a value changed meaning; see
[Configuration](configuration.md).

## What went where

| | HMs |
|---|---|
| **Still yours — actives** | [Cut](abilities/active.md#cut) · [Rock Smash](abilities/active.md#rock-smash) · [Stockpile](abilities/active.md#stockpile) · [Leafage](abilities/active.md#leafage) · [Strength](abilities/active.md#strength) · [Teleport](abilities/active.md#teleport) · [Camouflage](abilities/active.md#camouflage) · [Charge](abilities/active.md#charge) · [Tail Whip](abilities/active.md#tail-whip) |
| **Still yours — toggles** | [Fly](abilities/toggles.md#fly) · [Magnet Rise](abilities/toggles.md#magnet-rise) · [Rock Climb](abilities/toggles.md#rock-climb) · [Dive](abilities/toggles.md#dive) · [Jump](abilities/toggles.md#jump) · [Flash](abilities/toggles.md#flash) · [Lava Plume](abilities/toggles.md#lava-plume) · [Absorb](abilities/toggles.md#absorb) · [Lucky Chant](abilities/toggles.md#lucky-chant) · [Shadow Sneak](abilities/toggles.md#shadow-sneak) · [Snowscape](abilities/toggles.md#snowscape) |
| **Merged** | X-Scissor → **Cut** · Dig → **Rock Smash** · Rototiller → **Leafage** (crouch) · Water Gun and Eruption → **Stockpile** · Glide → **Fly** |
| **Your Pokémon's [field moves](pokemon.md#field-moves)** | Rain Dance · Sunny Day · Blizzard · Sweet Scent · Headbutt · Thief · Present · Miracle Eye · Celebrate · Growth · Minimize · Outrage · Calm Mind · Decorate |
| **Your mount's [toggles](pokemon.md#mount-toggles)** | Surf · Tailwind · Swift · U-turn · Helping Hand · Agility |
| **Moved to Cobblemon Action Combat** | Bullet Seed · Explosion · Thunder · String Shot · Crabhammer · Mean Look · Harden · Burning Bulwark · Substitute · Destiny Bond · Egg Bomb · Protect · Whirlwind · Barrier · Acid Armor · Rock Throw · Boomerang · Powder Snow · Confusion |
| **Cut** | Rest · Defog · Revival Blessing · Charm · Bounce · Obstruct · Ember · Earthquake · Vine Whip · Waterfall |

## Also changed

- **Fly is a toggle.** Switched on, you glide after any jump or fall; jump again in mid-air to take
  off. It cannot run together with Magnet Rise, which stays as a slow hover for building.
- **Teleport** costs 6 hunger and takes 30 seconds to come back.
- **Lava Plume** keeps you from burning on its own.
- **Rock Climb** works on the Pokémon you ride.
- **Agility** is now a land-speed boost for a mount.
