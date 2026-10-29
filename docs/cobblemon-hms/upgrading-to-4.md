# Upgrading to 4.0

4.0 renames the mod to **Cobblemon HMs** and turns it around: **you no longer learn HMs, your
Pokémon lend them to you.** A Pokémon that has learned the move can share it while it is out and
near you, and working costs it fullness. Everything that fights lives in **Cobblemon Action Combat**.

## The new name

Up to 3.x the mod was **Ditto HMs**. 4.0 renames everything, including the mod id
(`cobblemon_ditto_hms` is now `cobblemon_hms`):

- The jars are `cobblemon-hms-fabric-…` and `cobblemon-hms-neoforge-…`. **Delete the old
  `cobblemon-ditto-hms-…` jar** from `mods/` when you update: the loader sees two different mods
  and would load both.
- Your world carries over. HM Cases and discs in chests and inventories, everyone's HM save and the
  config file are read under the old name and saved under the new one.
- The command is **`/hms`** (it was `/dittohm`).
- The key binding for the HM wheel goes back to its default once.
- A new mod icon: the HM Case in the Cobblemon frame, in the mod list of both loaders.

## Your save

Nothing to do, and nothing you paid for is lost. The first time each player joins after the update:

- Every HM you had learned is cleared, and **its trigger item is handed back**, or dropped at your
  feet if your inventory is full.
- An old HM disc found in a chest **trades for its trigger item** when you right-click with it.
- A chat message explains what happened.

The config file is updated too, and only where a value changed meaning; see
[Configuration](configuration.md).

## What changed

- **Nothing to learn.** Open Cobblemon's interaction wheel on your Pokémon, pick **Field moves**,
  and it lists every HM whose move that Pokémon has learned, sorted by kind. See
  [Getting Started](getting-started.md).
- **Partner HMs** go to your empty fist, one at a time. See [Partner HMs](abilities/active.md).
- **Auras** run while the Pokémon is out and within 24 blocks; **weather auras** run one at a time.
  See [Auras](abilities/toggles.md).
- **Mount toggles** belong to the Pokémon you ride. Sneak + right-click while riding opens them. See
  [Your Pokémon](pokemon.md#mount-toggles).
- **Your Pokémon get hungry, not you.** Each use and each minute an aura stays on costs the Pokémon
  fullness; feed it any berry. Working on an empty stomach costs it friendship, and at 0 friendship
  it refuses. See [Keeping it fed](pokemon.md#keeping-it-fed).
- **No HM wheel and no H key.** Everything is in the Pokémon's own wheel.
- **A HUD list** in the top-left corner shows every HM in effect. Auras are no longer potion effects.
- **The Trainer Ditto sells six TMs a visit** for relic coins, pouches and sacks instead of teaching
  HMs, and gives you an HM Case the first time you meet it.
- **The HM Case is a TM bag** with a search box, and is no longer crafted. See [HM Case](tm-bag.md).
- **NeoForge has a config screen**, the same one as Fabric's (it needs Cloth Config).

## What went where

| | HMs |
|---|---|
| **Partner HMs** | [Cut](abilities/active.md#cut) · [Rock Smash](abilities/active.md#rock-smash) · [Dig](abilities/active.md#dig) · [Stockpile](abilities/active.md#stockpile) · [Leafage](abilities/active.md#leafage) · [Strength](abilities/active.md#strength) · [Teleport](abilities/active.md#teleport) · [Camouflage](abilities/active.md#camouflage) · [Charge](abilities/active.md#charge) · [Tail Whip](abilities/active.md#tail-whip) · [Growth](abilities/active.md#growth) · [Minimize](abilities/active.md#minimize) · [Outrage](abilities/active.md#outrage) · [Calm Mind](abilities/active.md#calm-mind) · [Celebrate](abilities/active.md#celebrate) · [Decorate](abilities/active.md#decorate) |
| **Auras** | [Magnet Rise](abilities/toggles.md#magnet-rise) · [Rock Climb](abilities/toggles.md#rock-climb) · [Dive](abilities/toggles.md#dive) · [Jump](abilities/toggles.md#jump) (from Splash) · [Flash](abilities/toggles.md#flash) · [Lava Plume](abilities/toggles.md#lava-plume) · [Absorb](abilities/toggles.md#absorb) · [Lucky Chant](abilities/toggles.md#lucky-chant) · [Shadow Sneak](abilities/toggles.md#shadow-sneak) · [Snowscape](abilities/toggles.md#snowscape) · [Sweet Scent](abilities/toggles.md#sweet-scent) |
| **Weather auras** | [Rain Dance](abilities/toggles.md#rain-dance) · [Thunder](abilities/toggles.md#thunder) · [Sunny Day](abilities/toggles.md#sunny-day) · [Blizzard](abilities/toggles.md#blizzard) · new: [Sandstorm](abilities/toggles.md#sandstorm) · [Mist](abilities/toggles.md#mist) |
| **Merged** | X-Scissor → **Cut** · Rototiller → **Leafage** (crouch) · Water Gun and Eruption → **Stockpile** |
| **Your mount's [toggles](pokemon.md#mount-toggles)** | Surf · Tailwind · Swift · U-turn · Helping Hand, now **Endure** · Agility |
| **Moved to Cobblemon Action Combat** | Bullet Seed · Explosion · String Shot · Crabhammer · Mean Look · Harden · Burning Bulwark · Substitute · Destiny Bond · Egg Bomb · Protect · Whirlwind · Barrier · Acid Armor · Rock Throw · Boomerang · Powder Snow · Confusion |
| **Retired** | Fly · Glide · Headbutt · Thief · Present · Miracle Eye · Rest · Defog · Revival Blessing · Charm · Bounce · Obstruct · Ember · Earthquake · Vine Whip · Waterfall |

**Fly** is gone because travelling by air is what your flying Pokémon are for: ride one, with
[Tailwind](pokemon.md#mount-toggles) on to make it faster. Magnet Rise stays as a slow hover for
building.
