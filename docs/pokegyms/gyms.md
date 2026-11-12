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

### City disciples

While a City gym is still its own leader's, up to **three Radical Cobblemon Trainers** stand at its disciple spots,
like the disciples of a [player gym](#disciples).

- **They share the leader's type**: the type found most often among the primary and secondary types of the leader's
  team. A tie goes to the type of the leader's last Pokémon.
- **They are ordinary RCT trainers**: never a gym leader, Elite Four member, champion, rival or villain boss.
  The City chooses them once, so a gym always has the same ones. A type with fewer than three such trainers gives
  the ones there are.
- **Fought weakest to strongest**, by the highest level in each one's team.
- **Beat them all before the leader.** The leader takes a challenge only once you have beaten every one. Each fight
  needs the [penalty](#fighting-a-city-leader) in hand. Winning costs nothing; **losing to one takes the penalty**
  (destroyed, as against the leader) and sends you back to the first. A finished leader challenge starts the next
  one from the first again, and your progress survives logouts and restarts.
- **They step aside while a player holds the gym**, which has its own disciples, and stand again when the City leader returns.
- **Operators can switch it off** with [`/pokegyms config city_disciples enabled false`](commands.md#configuration):
  no City disciples stand and the City leader is challenged directly.

## Fighting a City leader

Right-click the leader to challenge them, once you have beaten the leader's [disciples](#city-disciples). PokeGyms starts the battle with the leader's RCT team, but it
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
- **A leader NPC stands for it.** `Gym Leader <player>` stands at the gym's leader spot, wearing the
  holder's skin (default or slim, read from their Minecraft profile) and carrying the copy as its
  party. It cannot be hurt, moved or pushed, and does not despawn. If it is killed, it comes back the next
  time its chunk loads.
- **It leaves when the licence ends.** Renouncing or expiring removes the team, the NPC and the gym's [disciples](#disciples). In a City
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

## Leader dialogue

The leader NPC of a player-held gym talks at five moments of a challenge, in Cobblemon's own dialogue box with
the NPC's name and face.

| Moment | When | Default line |
| --- | --- | --- |
| Before the battle | The challenger right-clicks the leader. The box shows first and the battle starts when it is closed. | "So you have come to challenge this gym. Show me what you have got!" |
| Last Pokémon left | The leader is down to its last Pokémon. It is a line in the battle log. | "My last Pokémon... I am not done yet!" |
| You win | The leader wins. Shown about 2 seconds after the battle ends. | "Not this time. Train harder and come back." |
| You lose | The leader loses. Shown about 2 seconds after the battle ends. | "Well fought. You have earned it." |
| Challenger back too soon | A challenger tries again before their [rematch cooldown](#rematch-cooldown) is over. Also a line in chat. | "Back already? Rest your team and come back later." |

"You win" and "You lose" are from the NPC's side: the first is what the leader says after beating the challenger.

- **The holder writes the lines.** On the Team tab, the leader clicks **Dialogue** (bottom left) and types a line for
  each moment. An empty line uses the default, shown greyed in the field. All five are saved together.
- **Lines belong to the licence.** A new leader, or one who [takes the gym over](#taking-over-a-gym), starts on the
  defaults, and when a licence ends the lines go with it.
- **Limits.** A line is at most `dialogue.max_length` characters (120 by default, up to 256). A longer line, or one
  with a formatting code (`§`) or a control character, is refused and nothing is saved.
- **Disciples** say the same moments with the default lines.
- **Only player gyms.** City leaders and RCT trainers keep their own dialogue.
- **Operators can switch it off** with [`/pokegyms config dialogue enabled false`](commands.md#configuration): nobody
  speaks and the battle starts at once. The saved lines are kept for when it is back on.

## Where the battle happens

A **leader** battle is staged at the gym, in singles and in doubles. It applies to the City leader and to the leader of a player-held gym, not to [disciple battles](#challenging-the-disciples), which are not moved.

- **You are moved.** When the battle starts you are taken to the gym's **challenger spot**, facing the leader.
- **Each side's Pokémon have a spot.** Yours come out at the challenger's Pokémon spot and the leader's at its own, and they come back there after a switch.
- **Doubles spread out.** Two Pokémon of one side stand side by side, across the line toward the other side, `staging.doubles_gap` blocks apart (3 by default, 1 to 8).
- **A gym without those spots battles as before.** Gyms the server recorded before 0.0.43 have none, so Cobblemon places everything as it always did. A gym with only some of the spots uses those it has.
- **Other mods' battle blocks never take it over.** Only PokeGyms' own leader battles are placed, matched by the battle itself, so a battle block of another mod nearby (such as Cobblemon Battle Positions) leaves a gym battle alone, and every other battle is left alone too.
- **Operators can switch it off** with [`/pokegyms config staging enabled false`](commands.md#configuration): nobody is moved and Cobblemon places everything.
- **Not in real-time fights.** A fight [Cobblemon Action Combat runs in real time](#with-cobblemon-action-combat) is not staged.

## With Cobblemon Action Combat

[Cobblemon Action Combat](../action-combat/index.md) is optional, on Fabric and on NeoForge. Without it nothing here applies.

- **Real-time gym fights count.** When its NPC fights are real time, beating a player leader, a disciple or a City leader gives what a turn-based win gives: the medal, the [vault](vault.md#winners-share) share, the City badge and the [licence unlock](#unlocking-a-city-gym). A loss, a forfeit or running away costs the penalty.
- **The trainer takes the next challenger** once the fight is over.
- **PokeGyms has no switch for it.** Whether gym fights are real time follows Cobblemon Action Combat's own `/cac format`.
- **Two things are turn-based only.** In real time there is no [battle staging](#where-the-battle-happens) and no last-Pokémon line from the leader (see [Leader dialogue](#leader-dialogue)); the challenge and after-battle lines still show.
- **Operators can check it** in the log: `Cobblemon Action Combat found: real-time gym fights count like turn-based ones`.

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
- **City leaders have no cooldown.** It applies only to player leaders, not to the City (RCT) leaders; the [Champion](champion.md#rematch-and-the-trophy) is the one RCT trainer that uses it.
- **Operators can change it** with [`/pokegyms config rematch`](commands.md#configuration): `cooldown_minutes`
  sets the wait (`0` means no wait), and `enabled` switches the whole cooldown off.

## Taking over a gym

Beat a player leader, keep the medal they gave you, and you can take their gym.

- **Where.** Open the gym's Gym Manager and go to the **Licence** tab, which a visitor and a disciple of the gym both
  see. It shows the **Fee**, what you have and a **Take over** button. A holder cannot take their own gym.
- **What you need.** The medal, in your **main hand**, and the **takeover fee**, 10,000 CobbleDollars by default.
  The fee is destroyed, never paid to anyone, and the medal is used up. A Badge It badge works too, if it is the signed copy you won.
- **Only the real medal.** It must name this gym and its **current** leader. The server refuses an empty hand, a badge
  crafted by hand (it has no PokeGyms signature), a medal of another gym, a medal of an earlier leader of this gym, your
  own gym, a leader in the middle of a battle, too little money, and a server with takeovers switched off. You are told
  why in chat.
- **It works on any gym a player holds**, a town gym or a City gym.
- **No shield.** The new leader gets the **whole [vault](vault.md)** and keeps the gym's [disciples](#disciples) (if
  they were one of them, they are no longer one). The old leader loses the licence, and the gym's team, penalty,
  registered Badge It medal and rematch waits go with it: register your own team in the Team tab. The old leader is
  told in chat if they are online.
- **Your own gym goes first.** One licence per player: if you already held a gym, you give it up before the takeover
  and it goes vacant (or, in a City gym, back to its leader), its vault paid to you.
- **Operators can switch it off** or change the fee with [`/pokegyms config takeover`](commands.md#configuration).

## Medals

Beating a player leader gives you a **Gym Medal**.

- **One medal, for every gym.** It is a single generic item, a gold-rimmed Poké Ball on a red and white ribbon, with no art of its own per gym. It does not
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

## Battle rules

The server can ban **Terastallization**, **Dynamax**, **Mega Evolution**, **Z-Moves** and **held items** in gym
battles, and a leader can ban more for their own gym. All five are allowed by default.

- **Who is held to them.** Only the gym's side: a player leader, their disciples, a City leader, its disciples and the
  [Champion](champion.md). The challenger battles as always, with every gimmick and item they have. A City gym and the
  Champion follow the server's rules alone; they have no leader to add any.
- **The server's rules.** The `rules` group of the [config](commands.md#configuration) has one switch per ban:
  `allow_tera`, `allow_dynamax`, `allow_mega`, `allow_z` and `allow_held_items`. In the file they are `true` or `false`;
  with `/pokegyms config rules <setting>` a `0` bans and a `1` allows. `rules.enabled false` turns every ban off,
  the leaders' too, and they count again when it is back on. A battle keeps the rules it started under.
- **The leader's rules.** In the Gym Manager's **Team** tab the **Rules** row shows how many bans the gym's battles
  run under, the server's included, or **All allowed**. Click it for a screen with one button per rule, switching
  it between *Allowed* and *Banned*; **Done** saves all five and **Cancel** goes back. A leader can only tighten: what
  the server bans shows *Banned by the server*, greyed out, and cannot be switched. The row sits after Format and Team
  (and after the Badge It medal row when Badge It is installed), and is not there while `rules` is off.
  A new licence or a [takeover](#taking-over-a-gym) starts with none of its own.
- **Items.** A banned held item is taken off the gym's Pokémon in the battle only. The registered team and RCT's
  trainers keep theirs afterwards.
- **Gimmicks.** A banned gimmick is never offered to the gym's side, whatever runs its turns, so the Pokémon keeps its
  Tera type and its stone and still cannot use them. Banning Z-Moves bans Ultra Burst too.

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
  (Canonical) and its **location** (X, Z), and in a City gym the **type** of its leader, with a short line about who runs it. At a City gym whose leader you beat, the line says you may buy
  its licence.
- **The Team tab**, which only the holder sees, [registers the gym's team](#registering-your-team) and has the **Dialogue** button for the [leader's lines](#leader-dialogue) and a **Rules** row for the [battle rules](#battle-rules).
- **The Licence tab** is where a visitor or a disciple of a held gym can [take it over](#taking-over-a-gym).
- **The Disciples tab** is seen by the holder, by a player the holder invited and by the gym's disciples:
  see [Disciples](#disciples).
- **The Roster tab** is seen by a visitor and by a player the holder invited, not by the holder or the gym's disciples:
  see [Challenging a gym](#challenging-a-gym).
- **The gym team** panel on the side has six slots. They show the registered team by name and level,
  and stand empty while the gym has none.

The screen shows the gym as the server saw it when you opened it, and every button asks the server
again before anything happens.

The holder's screen has four tabs: Info, Licence, Team and Disciples. A disciple sees Info, Licence and Disciples. A visitor sees Info, Licence (when there is a licence to buy or a gym to take over) and Roster. The **Licence** tab also holds the gym's
[vault](vault.md): its penalty, Withdraw and Renounce. See [Licences](licences.md#the-licence-tab).

## Disciples

A player leader can have up to **three disciples**: other players who train under them and stand in the gym
as trainers.

- **Invite from the Disciples tab.** The holder opens the **Disciples** tab of the Gym Manager, clicks the
  **Invite** row to pick one of the players online who is not yet anyone's disciple, and presses **Invite**.
  The player is told in chat.
- **The invited player accepts** at that gym's Gym Manager, with the **Accept** button of the same tab, and
  takes the first free `disciple_N` place of the gym. A fourth invitation is refused: the gym has three
  places.
- **A disciple registers a team**, like the leader: press **Register** (or **Update**) and the gym keeps a
  frozen copy of the party they carry, in the gym's [format](#registering-your-team), singles while the leader
  has not registered a team. Singles needs 1 Pokémon in the party, doubles 2. Their own Pokémon stay with them.
- **A trainer NPC stands for it.** `Gym Trainer <player>`, wearing the disciple's skin and carrying the
  copy, stands at their place.
- **One gym at a time.** A player is the disciple of a single gym on the server. It needs no
  [licence](licences.md), so a disciple may hold one at another gym.
- **The leader removes a disciple** with a shift-click on their row in the holder's Disciples tab; the NPC goes.
  When the leader's licence ends, every disciple goes with it.
- **The leader can share the vault with them.** Each disciple's row shows their share of the gym's
  [vault](vault.md#splitting-the-vault) (`Name 25%`), a click on it gives them 5% more, and a **Leader** row shows what
  the leader keeps. A withdrawal, or the end of the licence, pays everyone their share.
- **Colours in the holder's list:** a disciple's name is white once they registered a team, gold until then,
  and a free place reads grey.
- **Operators can switch it off** with [`/pokegyms config disciples enabled false`](commands.md#configuration):
  nobody can be invited or register, and disciples already there stay until the leader removes them.

### Challenging the disciples

Right-clicking a disciple's trainer NPC challenges it, like the leader: a fresh copy of its team at your level,
in the gym's current format.

- **Fight them in order.** The disciples that have registered a team are fought in order, disciple 1, 2, 3,
  and the leader takes your challenge only once you have beaten every one. A gym with no disciples is
  challenged at the leader directly.
- **Progress is kept** when you log out or the server restarts, until you lose.
- **A loss to any disciple** costs you the gym's [penalty](vault.md), starts the rematch cooldown and sends you back to
  disciple 1.
- **Beating a disciple pays nothing**: no [winner's share](vault.md#winners-share), no medal and no cooldown.
  A finished leader challenge, won or lost, starts the next one from disciple 1.
- **Changes start everyone over.** A disciple joining, registering again or leaving, or a new licence,
  resets every challenger's progress.
- **Who cannot challenge.** The holder and the gym's own disciples. Each trainer battles one challenger at a time.

## Challenging a gym

A visitor's Gym Manager has a **Roster** tab, titled **Order**, that lists the gym's trainers in the order you
face them: its disciples one after another, the leader last.

- **Beaten trainers are struck out**, the one you face next is **gold** and the rest wait.
- **Press Challenge** and the next trainer takes you on at their place, the same as right-clicking them. The screen closes for the battle.
- **Only the next trainer can be called out.** A disciple you beat cannot be fought again until you start over, after a
  loss or a finished challenge against the leader. If you try anyway, or the gym takes no challenge from you now, you are told in chat.
- **A trainer who is not at their place yet** asks you to try again in a moment.
- **City gyms work the same way**, with their [RCT disciples](#city-disciples) first and the City leader last.
- **A player the holder invited** sees the tab too, while they decide on the invitation.
- **Operators can switch it off** with [`/pokegyms config roster enabled false`](commands.md#configuration):
  challengers get no Roster tab; right-clicking a trainer still challenges it, in the same order.

## Gym battles

A battle against an NPC trainer who stands **inside a gym**, such as a Cities & Structures gym leader,
is a **gym battle** from its start until it ends. PokeGyms marks it, so other mods can tell it apart, and
the gym's side fights under the [battle rules](#battle-rules). **Mid-Battle EXP** uses this to give more EXP in gyms.

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
