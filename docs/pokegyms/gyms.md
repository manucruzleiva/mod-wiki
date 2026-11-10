# Gyms & the Gym Manager

## Which gyms

PokeGyms runs the gym buildings of **Cobblemon Cities & Structures**. Eight of its Kanto cities can
have one:

Pewter · Cerulean · Vermilion · Celadon · Fuchsia · Saffron · Cinnabar · Viridian

Lavender and Pallet have no gym, and a city does not always build its gym, so not every city you
find has one. That is Cities & Structures' choice; PokeGyms records the gyms that are there.

A gym is found **the first time its city loads**, new or generated long before PokeGyms was
installed, and it is remembered for that world from then on, across restarts. Each dimension keeps
its own list.

## City gyms

Every gym starts as a **City gym**, held by Cities & Structures' own leader, who stays where that mod
puts them. PokeGyms does not move or replace them.

## The Gym Manager

Every gym has a **Gym Manager**: a lectern just inside the gym's door. It is put there as soon as the
gym is found and the spot is loaded.

- **It cannot be broken in survival** and drops nothing. A Gym Manager removed in creative comes back
  the next time its chunk loads.
- **It comes in three looks**, wood, tech and Poké Ball. They behave the same; a City gym's is the
  Poké Ball one. All three are in the **PokeGyms** creative tab, for builders.
- A Gym Manager placed by hand somewhere that is not a gym's spot belongs to no gym, and says so when
  right-clicked.

### The screen

Right-clicking a Gym Manager opens its screen, built on Cobblemon's summary screen:

- **The header** names the gym by its city, such as **Pewter City Gym**, with a **CITY** tag, and
  who runs it: the **City leader**.
- **The Info tab**, which everyone sees, gives the gym's **kind** (City gym), its **status**
  (Canonical) and its **location** (X, Z), with a short line about who runs it.
- **The gym team** panel on the side has six slots. They stand empty in this build.

The screen shows the gym as the server saw it when you opened it, and every button asks the server
again before anything happens.

More tabs join the screen as features arrive. The **Licence** tab is already built; see
[Licences](licences.md).

## Gym battles

A battle against an NPC trainer who stands **inside a gym**, such as a Cities & Structures gym leader,
is a **gym battle** from its start until it ends. PokeGyms does not change the battle itself; it only
marks it, so other mods can tell it apart. **Mid-Battle EXP** uses this to give more EXP in gyms.

Each gym battle knows its gym and who the challenger faces: the gym's **leader**, a **disciple**, or the
City gym's **canonical leader**. Operators can list the gym battles running now with
[`/pokegyms battles`](commands.md#pokegyms-battles).

### For mod authors

Ask through `com.shier.pokegyms.api.GymBattleApi`. Every method is a JVM static, so a mod that does not
depend on PokeGyms can call it by reflection:

| Method | Returns |
| --- | --- |
| `isGymBattle(battleId: UUID)` | Whether the Cobblemon battle is a gym battle. |
| `opponent(battleId: UUID)` | `leader`, `disciple` or `canonical_leader`; `null` when it is not a gym battle. |
| `marker(battleId: UUID)` | The whole marker (dimension, gym origin, opponent), for a mod compiled against PokeGyms; `null` when it is not a gym battle. |

```kotlin
val gym = runCatching {
    Class.forName("com.shier.pokegyms.api.GymBattleApi")
        .getMethod("isGymBattle", UUID::class.java)
        .invoke(null, battle.battleId) as Boolean
}.getOrDefault(false) // PokeGyms not installed
```
