# Upgrading to 4.0

4.0 renames the mod to **Cobblemon HMs** and turns it around: **you no longer learn HMs, your
Pokémon lend them to you.** A Pokémon that has a move in its movepool can share it while it is out
and near you. Everything that fights lives in **Cobblemon Action Combat**.

## Your save

Nothing to do, and nothing you paid for is lost. The first time each player joins after the update:

- Every HM you had learned is cleared, and **its trigger item is handed back**, or dropped at your
  feet if your inventory is full.
- Old HM discs stay in chests as inert items, so you can still trade them away.
- A chat message explains what happened.

The config file is updated too, and only where a value changed meaning; see
[Configuration](configuration.md).

## What changed

- **Nothing to learn.** Open Cobblemon's interaction wheel on your Pokémon, pick **Field moves**,
  and it lists every HM that Pokémon can share. See [Getting Started](getting-started.md).
- **Partner HMs** go to your empty fist, one at a time. See [Partner HMs](abilities/active.md).
- **Auras** run while the Pokémon is out and within 24 blocks. See [Auras](abilities/toggles.md).
- **No hunger.** The only cost is a cooldown, kept per Pokémon.
- **No HM wheel and no H key.** Everything is in the Pokémon's own wheel.
- **The Trainer Ditto sells TMs** for relic coins instead of teaching HMs.
- **The HM Case is a TM bag** with a search box. See [HM Case](tm-bag.md).

## What went where

| | HMs |
|---|---|
| **Partner HMs** | [Cut](abilities/active.md#cut) · [Rock Smash](abilities/active.md#rock-smash) · [Stockpile](abilities/active.md#stockpile) · [Leafage](abilities/active.md#leafage) · [Strength](abilities/active.md#strength) · [Teleport](abilities/active.md#teleport) · [Camouflage](abilities/active.md#camouflage) · [Charge](abilities/active.md#charge) · [Tail Whip](abilities/active.md#tail-whip) · [Growth](abilities/active.md#growth) · [Minimize](abilities/active.md#minimize) · [Outrage](abilities/active.md#outrage) · [Calm Mind](abilities/active.md#calm-mind) |
| **Auras** | [Magnet Rise](abilities/toggles.md#magnet-rise) · [Rock Climb](abilities/toggles.md#rock-climb) · [Dive](abilities/toggles.md#dive) · [Jump](abilities/toggles.md#jump) · [Flash](abilities/toggles.md#flash) · [Lava Plume](abilities/toggles.md#lava-plume) · [Absorb](abilities/toggles.md#absorb) · [Lucky Chant](abilities/toggles.md#lucky-chant) · [Shadow Sneak](abilities/toggles.md#shadow-sneak) · [Snowscape](abilities/toggles.md#snowscape) · [Rain Dance](abilities/toggles.md#rain-dance) · [Sunny Day](abilities/toggles.md#sunny-day) · [Sweet Scent](abilities/toggles.md#sweet-scent) · new: [Sandstorm](abilities/toggles.md#sandstorm) · [Fog](abilities/toggles.md#fog) |
| **Merged** | X-Scissor → **Cut** · Dig → **Rock Smash** · Rototiller → **Leafage** (crouch) · Water Gun and Eruption → **Stockpile** |
| **Your Pokémon's [field moves](pokemon.md#field-moves)** | Blizzard · Celebrate |
| **Your mount's [toggles](pokemon.md#mount-toggles)** | Surf · Tailwind · Swift · U-turn · Helping Hand · Agility |
| **Moved to Cobblemon Action Combat** | Bullet Seed · Explosion · Thunder · String Shot · Crabhammer · Mean Look · Harden · Burning Bulwark · Substitute · Destiny Bond · Egg Bomb · Protect · Whirlwind · Barrier · Acid Armor · Rock Throw · Boomerang · Powder Snow · Confusion |
| **Retired** | Fly · Glide · Headbutt · Thief · Present · Miracle Eye · Decorate · Rest · Defog · Revival Blessing · Charm · Bounce · Obstruct · Ember · Earthquake · Vine Whip · Waterfall |

**Fly** is gone because travelling by air is what your flying Pokémon are for: ride one. Magnet Rise
stays as a slow hover for building.
