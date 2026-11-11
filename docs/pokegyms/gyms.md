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

## City gyms and their leaders

Every gym starts as a **City gym**, led by one of **Radical Cobblemon Trainers'** own gym leaders (the
`leader_*` trainers, 24 different names in RCT 0.19.2).

- **One leader per City, kept for good.** PokeGyms picks the leader the first time the gym is found and
  remembers it. No leader's name repeats across the world's gyms until every one has been used.
- **The leader stands still and cannot be hurt**, at the gym's leader spot. The Gym Manager names them.
- **Cities & Structures' own leader is removed.** PokeGyms puts RCT's leader in their place, so the gym
  never has two. Worlds made before this version change over by themselves the next time each gym loads.
- A gym that is no longer a City gym loses its RCT leader.

## Fighting a City leader

Right-click the leader to challenge them. PokeGyms starts the battle with the leader's RCT team, but it
**does not count in RCT's progression**: winning does not raise your level cap or add the leader to your
defeat list, and RCT gives no loot or dialogue for it.

- **You need CobbleDollars to start.** You must carry at least the **penalty**, `canonical.penalty`
  (1,000 by default). If you are short, you are told how much you need.
- **Losing costs the penalty.** Losing, forfeiting or running away takes exactly that sum from you. The
  money goes to no one. Winning costs nothing, and [unlocks the gym's licence](#unlocking-a-city-gym) for you.
- **One challenger at a time** per leader. A second challenger is told the leader is busy.
- **A win can also give a badge.** See [Mainline badges](#mainline-badges).
- **Operators can close the fight** or change the penalty with
  [`/pokegyms config canonical`](commands.md#configuration). Closed, leaders take no challenges; battles
  already running finish, and a loss still costs the penalty.

## Unlocking a City gym

A City gym's licence is not for sale to everyone: **only a player who beats its leader** in the fight
above may buy it (see [Licences](licences.md)).

- **A win unlocks it for the winner only.** You are told in chat, the **Info** tab says you may buy
  the licence, and the **Licence** tab appears. Everyone else who opens the Gym Manager is told to beat
  the leader first, and the server refuses their purchase.
- **Nothing else counts.** Losing, running away, a battle that is stopped, or beating the leader
  outside PokeGyms' own fight unlocks nothing.
- **The leader steps aside while the gym is held.** When the winner buys the licence, the RCT leader
  leaves the gym and takes no challenge.
- **When the licence ends, the leader returns.** Renouncing or expiring puts the leader back and locks
  the gym again for everyone, the former holder included: they must beat the leader anew.
- **Your win is remembered** even if licences are switched off, so it still counts when they are
  switched back on.

## Registering your team

A gym's **holder** (the player who holds its licence, in a town gym or in a City gym won from its
leader) can register their party as the gym's team. The gym then has a leader of its own.

- **Open the Team tab** of the Gym Manager, pick **singles** or **doubles**, and press **Register**.
  Singles takes 1 Pokémon from your party, doubles takes 2. Only the holder sees the tab, and the
  server checks it again when you press the button.
- **The gym keeps a frozen copy.** The Pokémon are copied, healed, and the copy does not follow yours:
  you keep your own Pokémon and can train, trade or lose them. Registering again replaces the copy.
- **Everyone sees the team.** The gym team panel on the Gym Manager's side lists the registered
  Pokémon by name and level.
- **A leader NPC stands for it.** **Gym Leader <player>** stands at the gym's leader spot, wearing the
  holder's skin (default or slim, read from their Minecraft profile) and carrying the copy as its
  party. It cannot be hurt, moved or pushed, and does not despawn. If it is killed, it comes back the next
  time its chunk loads.
- **It leaves when the licence ends.** Renouncing or expiring removes the team and the NPC. In a City
  gym, the RCT leader returns at the same time (see [Unlocking a City gym](#unlocking-a-city-gym)).
  An NPC whose chunk was unloaded when the licence ended is removed the next time that chunk loads.
- **Operators can close registration** with
  [`/pokegyms config leader`](commands.md#configuration). Off, nobody can register or replace a team;
  teams already registered stay, with their leader.

Worlds saved before this version load every gym with no team. A saved team that cannot be read is
dropped and the gym is kept.

## Challenging a gym

Right-click the **Gym Leader** NPC of a player-held gym to fight the team its holder registered.

- **The holder picks the format.** It is singles or doubles, whatever the holder registered.
- **Who cannot challenge.** The holder cannot challenge their own gym. A gym with no holder or no
  registered team takes no challenge, and neither does a leader who is already battling someone else
  (you are told it is busy).
- **You need the penalty in hand.** The holder sets a penalty for their gym, and you must carry at
  least that many CobbleDollars to challenge. A loss moves exactly the penalty into the gym's
  [vault](vault.md); a win or a stopped battle costs nothing, and a win takes a
  [share of that vault](vault.md#winners-share). If you are short, you are told how much
  it costs and what you have.
- **The result counts once.** Winning or losing tells you in chat. Forfeiting or running away counts as
  a loss. A battle the server stops counts as nothing.
- **The leader always fields a fresh copy of the team.** Used PP or berries from an earlier battle do
  not carry over, and the gym's registered team is never changed.
- **Nobody's Pokémon are hurt.** The battle uses a copy of your party, so your Pokémon keep their
  health, and it gives **no XP or EVs** for the same reason.
- **In a City gym held by a player,** the fight counts as against the player leader, not the City
  leader: it does not touch the City leader's unlock or penalty, and
  [`/pokegyms battles`](commands.md#pokegyms-battles) lists it as `leader`.
- **A rematch has to wait.** See [Rematch cooldown](#rematch-cooldown).
- **The penalty has its own switch.** [`/pokegyms config vault`](commands.md#configuration) turns it
  off: nobody pays or needs one to challenge.
- **It does not depend on the `leader` switch.** [`/pokegyms config leader`](commands.md#configuration)
  only stops new registrations; challenges keep working.

## Rematch cooldown

After you finish a challenge of a player leader, the same leader will not take you on again right away.

- **It starts when the challenge ends, won or lost.** Forfeiting or running away counts as a loss. A
  battle the server stops, with no winner, starts no wait.
- **It is yours alone, and per gym.** Another challenger can fight the same leader at once, and you can
  still fight other gyms' leaders.
- **Trying early is refused,** and the message tells you the time left, such as "will take your
  challenge again in 45 min". The time is rounded up to whole minutes.
- **It lasts 60 minutes by default,** and survives a server restart. A gym whose licence ends and is
  bought again starts with nobody waiting.
- **City leaders have no cooldown.** It applies only to player leaders, not to the City (RCT) leaders.
- **Operators can change it** with [`/pokegyms config rematch`](commands.md#configuration): `cooldown_minutes`
  sets the wait (`0` means no wait), and `enabled` switches the whole cooldown off.

## Medals

Beating a player leader gives you a **Gym Medal**.

- **One medal, for every gym.** It is a single generic item, with no art of its own per gym. It does not
  show in the creative tab; a medal only comes from a win.
- **It is signed.** Hover it to read the gym ("Pewter City Gym" for a City gym, otherwise "Gym at" its
  coordinates), "Leader:" with the name of the player you beat, and "Won on" with the date of the win.
- **Only a win gives one.** A loss, a forfeit, or a battle the server stops gives none, and so does a win
  against a City (RCT) leader: medals are for player leaders. The leader gets none either.
- **You get one per win.** Winning the same gym again, after the [rematch cooldown](#rematch-cooldown),
  gives another.
- **A full inventory is no loss.** The medal drops at your feet.
- **With Badge It, the medal can be a badge.** [Badge It](https://modrinth.com/mod/badgeit) is optional. When it
  is installed, the holder's Team tab has a third row, **Medal**: hold one of its badges in your main hand and
  click it to register that badge as the gym's medal (you keep the badge). Winners then get a copy of that
  badge signed the same way, with the gym, the leader and the date in its lore. A badge crafted by hand carries
  no signature. Without Badge It, or before a badge is registered, winners get the generic medal. A gym's new
  licence starts without a badge.
- **Operators can switch it off** with [`/pokegyms config medals enabled false`](commands.md#configuration):
  no win gives a medal, and medals already given stay.

## Mainline badges

With [PKGBadges](https://modrinth.com/mod/pkgbadges) installed, beating a **City leader** gives you the badge
that leader gives in the main games: Brock the Boulder Badge, Misty the Cascade Badge, and so on. PKGBadges is
optional.

- **The 16 Kanto and Johto leaders have one.** Radical Cobblemon Trainers' leaders from the main games
  (Brock to Giovanni, Falkner to Clair) give their badge; the other City leaders give none.
- **Once per challenger.** Winning again gives nothing more, and it stays so after the gym's licence ends and
  the City leader is back.
- **A full inventory is no loss.** The badge drops at your feet.
- **Only a win against a City leader gives one.** A loss, a forfeit, a stopped battle, and a win against a
  player leader give none (those give a [medal](#medals)).
- **Datapacks can change the map.** `data/cobblemon_pokegyms/badges.json` maps a leader to an item id. A key is
  an RCT trainer id, or a leader's name, which covers all that leader's variants; a leader with no entry gives
  nothing (the server logs it once). Without PKGBadges no badge is given, and the start-up log says so.
- **Operators can switch it off** with [`/pokegyms config badges enabled false`](commands.md#configuration):
  no win gives a badge, and badges already given stay.

## Level scaling

A gym leader's team fights at **your level**, whatever levels it was registered at. So does the team of
every other Radical Cobblemon Trainers (RCT) trainer, including the ones wandering the world.

- **The level is your best Pokémon's.** It is the highest level in your whole party, fainted Pokémon
  included, so a Pokémon you cannot send out still counts. The team scales up and down alike: a level 20
  team meets a level 50 challenger at 50, and a level 80 team meets a level 30 one at 30.
- **Every Pokémon of the team is set to it, at full HP.** It is capped at the server's maximum Pokémon level.
- **It covers every RCT trainer, in a gym or out of it.** The [City leaders](#fighting-a-city-leader) and the
  trainers you meet in the world are RCT trainers, and so every battle against one is scaled. The
  [player leaders](#challenging-a-gym) are scaled too.
- **Each Pokémon takes the evolution stage of its new level.** A registered Charizard faced at level 12 is a
  Charmander, and a Charmander faced at level 40 is a Charizard. It goes up and down alike, and only level
  evolutions are crossed, so a Vaporeon stays a Vaporeon. A Pokémon holding an Everstone keeps its species
  both ways. Where an evolution branches, the first one that applies is taken.
- **Empty move slots are filled for the new level.** The moves a Pokémon was registered with stay in their
  slots, even one its new stage cannot learn. Each empty slot gets the newest level-up move its stage knows at
  the new level that it does not already have. A Pokémon registered with four moves fights with exactly those four.
- **Only the battle changes.** The Team tab, a holder's registered team and RCT's trainer data keep
  their levels; the scaled Pokémon are copies made for that battle alone, so a trainer's team is the same
  when you meet it again at another level.
- **A format with its own fixed level keeps it.** If the battle format sets a level for everyone, the
  opponent's team is not scaled.
- **Operators can switch it off** with [`/pokegyms config scaling enabled false`](commands.md#configuration):
  teams then fight at their registered levels, RCT trainers' included. Battles already running keep the levels they started with.
  [`/pokegyms config evolution enabled false`](commands.md#configuration) keeps only the evolution stages out: levels still scale, species stay as registered.

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
  (Canonical) and its **location** (X, Z), with a short line about who runs it. At a City gym whose leader you beat, the line says you may buy
  its licence.
- **The Team tab**, which only the holder sees, [registers the gym's team](#registering-your-team).
- **The Vault tab**, which only the holder sees, sets the gym's penalty and withdraws its
  [vault](vault.md).
- **The gym team** panel on the side has six slots. They show the registered team by name and level,
  and stand empty while the gym has none.

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
