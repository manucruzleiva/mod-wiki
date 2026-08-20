<!-- Copiado a mano de cobblemon-ditto-hms/CHANGELOG.md. El workflow de ese repo lo copiaba en
     cada build; al mudarse los docs aca ese paso desaparecio. Actualizar al publicar una version. -->

# Changelog

All notable changes are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) + SemVer.

## [2.1.20] - 2026-08-20

### ✨ Changed
- **Blizzard makes it snow.** Actual snowfall where you cast it — flakes in the air and snow
  settling on the ground, a layer at a time — **whatever the biome**. A desert gets a blizzard if
  that is where you called one down, and the biome is never touched to do it. The snow then obeys
  the world's own rules: it stays in a taiga and it is gone from a desert by morning, because
  leaving that to vanilla is what keeps this from being a landscaping tool. Learned with a
  **Snowball** now.

### ✨ New
- **Powder Snow** *(toggle)* — the freezing cold Blizzard used to leave behind, except now you
  **carry** it. Anything that comes near frosts over and starts to freeze; step out and it thaws.
  Its edge is drawn on the ground at exactly the radius that bites, which matters more than ever
  now that the edge walks around with you. You are exempt from your own cold.

## [2.1.19] - 2026-08-20

### ✨ Changed
- **Rock Climb is steered by the movement keys.** **W** climbs, **S** descends, and holding nothing
  holds your place on the wall — which is the one thing the old version could not express, because
  you are always looking somewhere. It used to read your pitch, so "look up to go up" was the only
  way, and glancing down mid-climb dropped you.
- **Decorate carpets the whole floor, and hangs the painting where you point.** Both were scattered
  at random before, and random decoration is not decoration: you cannot aim a sprinkle, and a room
  you cannot aim is a room you cannot finish. Its **power is now the shiny chance**, a plain
  percentage from 1 to 100, for a server to set as generous or as cruel as it likes.

## [2.1.18] - 2026-08-20

### 🐛 Fixed
- **Mean Look stopped playing tug of war.** Frightened Pokémon ran a few steps, turned round and
  came straight back, over and over. They were still hunting you the whole time — the flee path was
  being set and their own AI was undoing it every tick. They now **let go of you** first, which
  ends the chase properly: the Pokémon runs off, calms down, and you can walk up to it afterwards.

### ✨ Changed
- **String Shot does something different standing still.** On the move it still spits a web behind
  you that is gone in a second — an escape, left in a doorway. **Standing still**, it plants one
  where you are **aiming**, and that one **stays**: a trap you set on purpose, or something to break
  a fall at the bottom of a shaft. What you were already doing decides which you meant.
- **Teleport is learned with an Ender Pearl** instead of an Eye of Ender. It also fixes a real
  clash: Teleport and Miracle Eye shared the Eye, and anything looking an HM up by its item alone
  could only ever find the first of the two.

### ✨ New
- **Your real food bar shows what the toggles have taken.** The red the HM wheel draws is now
  painted over the vanilla bar too — which is where you are actually looking when you wonder why it
  will not fill.

## [2.1.17] - 2026-08-20

### 🐛 Fixed
- **Half your HMs had no name.** Nine toggle effects, eighteen keybinds and sixteen discs were
  missing their text entirely, so the game fell back to showing the raw key —
  `effect.cobblemon_ditto_hms.hm_swift` sitting in your status bar where a name should be. Every one
  of those is now generated from the ability list itself, so an HM added later cannot arrive
  nameless.
- **The thrown projectile is not called "Seed".** It is shared by Bullet Seed, Egg Bomb, Rock Throw
  and Boomerang, and it renders as whatever it was loaded with.
- **A two-line HM description no longer falls off the bottom of the screen.** The text is measured
  and lifted until it fits.

### ✨ Changed
- **The selected active HM gets a light of its own**, amber where a running toggle is green. "This
  is what fires" and "this is running" are now the same mark in different colours, instead of one
  being a light and the other a ring you had to know to look for.

## [2.1.16] - 2026-08-20

**The first two fixes that came from actually playing the mod.**

### 🐛 Fixed
- **Magnet Rise flew at full creative speed, and the dash still worked.** Halving the flight speed
  was only half the job: the game **doubles it again while you sprint**, and it does that on your
  own machine as it works out where you moved to — so holding Ctrl handed the whole reduction back.
  The doubling is now cancelled where it happens, which means the speed is the same whether or not
  the key is down. That is what "no dash" was always supposed to mean.
- **Tail Whip swept nothing, and said it had.** It also charged you for the privilege. It now
  re-reads the block between strokes — the last one replaces it, and holding on to the old one is
  how the sweep quietly stopped short — and if it does not finish, it refuses and costs nothing
  instead of playing a happy sound over an untouched block.

## [2.1.15] - 2026-08-20

### ✨ New
- **HMs can be paid for with experience.** A new setting picks the currency — experience then
  hunger (the new default), hunger then experience, or strictly one or the other. Every HM keeps a
  single price, quoted in food, and it is converted at the till, so switching your server to XP
  does not re-balance anything: the relative cost of everything stays exactly where it was.
  `/dittohm config cost order <mode>` and `/dittohm config cost xp <n>`.
- **[Cobblemon: PlayerXP](https://modrinth.com/mod/cobblemon-playerxp)
  ([CurseForge](https://www.curseforge.com/minecraft/mc-mods/cobblemon-playerxp)) is now a declared
  optional dependency.** Vanilla only pays experience for killing things, so on a Cobblemon server
  with mob spawning turned down the XP modes would be a slow starvation. PlayerXP pays you for the
  battles your Pokémon win — install it and the currency refills from the thing you were already
  doing.

### ✨ Changed
- **U-turn is a toggle, and it is about turning.** Whatever you are riding corners far more
  sharply, on land, in water and in the air. It used to be a backwards hop.
- **Your double does what you were doing.** Cast Substitute at a run and it keeps running your way
  at your pace; cast it standing still and it **stands still**. It used to wander off on a random
  bearing when you were still, which gave it away just as badly as freezing would have.

## [2.1.14] - 2026-08-20

### ✨ New
- **Present** — point it at an empty container and it fills itself, out of the tables the game uses
  for the chests nobody placed on purpose: a mineshaft's, a dungeon's, a bonus chest. **One in ten
  is a lump of coal**, which is the whole joke and the reason the cooldown is a full day. It refuses
  a container with anything already in it — a present does not go on top of your things.
- **Blizzard** — leaves a circle of standing cold where you cast it. Anything that walks in freezes
  the way powder snow freezes it, and thaws on the way out. **Its edge is drawn on the ground**, at
  exactly the radius that bites: an area effect that punishes you for entering without showing you
  where it starts is a trap, not a mechanic. The caster is exempt — it is their storm.
- **Boomerang** — throws a bone that turns around and comes back to your hand. Hit something and it
  stops there instead, on the ground beside it, which makes a clean miss the cheap outcome and a hit
  cost you the walk over.
- **Decorate** — carpets the ground around you, all one colour, rolled fresh each time, and hangs
  whatever art fits on the walls in reach. Aimed at a **Pokémon** instead, it takes a single long
  shot at making it shiny — permanently, at the game's own odds, and quietly when it misses.

## [2.1.13] - 2026-08-19

### ✨ New
- **X-Scissor** — clears the ground around you, and it clears it in an order. Weeds first: grass,
  ferns, dead bushes, the things nobody planted. Only when there is not a single weed left in range
  does it start on flowers and crops — so standing in your own wheat field and casting by accident
  costs you the weeds, not the field. And if nothing is growing at all, it strips the grass down to
  dirt.
- **Earthquake** — shakes the ground out of true around you. Some of it rises a block, some of it is
  simply gone, most of it stays: what you get is ground nobody can trust, which is worse to be
  chased across than a crater. It will not move anything with something inside it, and it will not
  move anything tougher than stone, so nobody's floor goes with it.
- **Rock Throw** — throws a stone out of your pockets. It hurts what it hits, and if it hits nothing
  it **lands as a stone**, including somewhere you could never have reached to place one. Ammunition
  you can pick back up is ammunition you can afford to miss with.

## [2.1.12] - 2026-08-19

### ✨ New
- **Barrier** — a three-by-three wall you cannot see, straight in front of you, for a while. An
  arrow stops in mid-air; a creeper walks into nothing. It fills empty space only and takes away
  only what it put down, so it can never eat a piece of anybody's house.
- **Acid Armor** *(toggle)* — a caustic coat worth a quarter of a full diamond set, and whatever
  lands a blow on you gets poisoned for its trouble. One dose per hit, from whatever actually
  reached you: an archer three blocks back never touched the acid.

### 🗑️ Removed
- **Aura Sphere** is gone. It was an early draft of what became Whirlwind, and keeping both meant
  shipping the sketch alongside the drawing.

## [2.1.11] - 2026-08-19

### ✨ New
- **Whirlwind** — takes whatever you aim at and puts it ten blocks away, without hurting it at all.
  It ends an encounter without ending a creature, which makes it the answer to the things you would
  rather not kill and the things you could not.

## [2.1.10] - 2026-08-19

**The mod can hold as many HMs as it likes now.**

### 🐛 Fixed
- **The sixty-four HM ceiling is gone.** What you have learned was stored as one number with one bit
  per HM, and a number of that kind holds exactly sixty-four of them. The mod was at fifty-six with
  more on the way, and going past the line would not have thrown an error — the sixty-fifth HM would
  have quietly shared a bit with the first, so learning one would have taught you the other. It is
  stored as a growing set of numbers instead, with no limit. **Existing worlds are read as they
  are** and convert themselves the next time they save; nothing has to be done by hand.

### ✨ New
- **Tail Whip** — sweeps a suspicious block clean in one motion instead of a dozen slow ones, and
  finds exactly what a brush would have. Rooted dirt gives up its hanging roots to it too.
- **Aura Sphere** — a punch that lands harder the worse off you are: nothing at all while you are
  healthy, five hearts and halfway across the clearing on your last one. A weapon that only becomes
  worth having at the moment you would rather be running.

## [2.1.9] - 2026-08-19

### ✨ New
- **Protect** — nothing can touch you for a single second, and then not again for ten. It is not a
  shield you stand behind; it is a read. Spend it on the creeper you heard, the arrow you saw leave
  the bow, the lava you are about to land in — and spend it a moment early and you have nothing left
  when the blow lands. It blocks **everything**, falls and drowning and the void included.
- **Lucky Chant** *(toggle)* — fortune leans your way while it is on. What you break and what you
  fish give up a little more.
- **Celebrate** — a firework show over your head, for absolutely no reason. Costs almost nothing and
  comes back almost never, which is the only way a party stays a party.
- **A running toggle can be seen from outside.** Each one breathes out its own type's particle on a
  slow loop, so a player with four going no longer looks exactly like a player with none. Sparse on
  purpose — it is a sign, not a firework.

### ✨ Changed
- **The HM Case shows the cooldown.** Fire an active and the Case in your hotbar sweeps around with
  Minecraft's own cooldown shadow, the one every player can already read without being taught.

### 🐛 Fixed
- **Mean Look stopped quietly clearing your luck.** It had not granted any since it became a repel,
  but it was still switching Luck off every tick — which would have fought Lucky Chant for it.

## [2.1.8] - 2026-08-19

**The wheel tells you what things cost before you pay for them.**

### ✨ New
- **A food bar down the side of the wheel.** Twenty pips, and it answers three questions at once:
  how much of your maximum the running toggles have taken (in red — that capacity is not yours
  again until one goes off), how much you have left, and **what the HM under the cursor would
  cost**, flashing, before you commit to it. Hover an active and it flashes what it would eat;
  hover a toggle and it flashes the slice it would claim, or hand back if it is already on.
- **Toggles wear a little green light.** Only toggles have one, so at a glance you can tell what
  fires from what stays on — and lit means that one is running right now. The glow could never say
  that on its own, because a selected active glows too.
- **Scroll on the wheel to resize the discs.** They start twice as big as they used to and go
  twice as far again, and where you leave them is remembered between worlds — the right size
  depends on your monitor and how many HMs you know, which is not something a server can guess.

### ✨ Changed
- **The two ways out of the middle look like buttons now.** A red ✖ for cancel and brushes around
  the ring for clear-everything, visible before you hover them rather than after.

## [2.1.7] - 2026-08-19

**Two HMs turned out to be the wrong move under the right effect.**

### ✨ Changed
- **Rollout is now Agility.** The effect is the same — you move faster while it is on — but it is a
  Psychic move now, learned from different Pokémon, obtained with a different item and wearing a
  different disc. Rolling downhill was never what the speed felt like.
- **Seed Bomb is now Egg Bomb.** Same lob, same small deliberate blast; it throws an **egg**, from
  your own supply, and it flies as one. Learned from the Pokémon you would expect to be carrying
  eggs.

> **Both keep your progress.** If you had learned Rollout or Seed Bomb, you know Agility or Egg Bomb
> — it is the same slot, wearing a different name. Their old discs are gone from the game, and the
> settings for them go back to defaults; run `/dittohm config reset_all` after updating.

### 🐛 Fixed
- **No more counting HMs at people.** The store page and the README stated exactly how many HMs
  there were, in three places, and all three were already wrong. Numbers that go stale the moment
  an HM is added do not belong in a description.

## [2.1.6] - 2026-08-19

**HMs are taught to you now. They are not handed over.**

### ✨ Changed
- **You learn an HM from the Pokémon itself.** Sneak-click one holding the right item and it shows
  you the move — there is no disc in the middle any more, and the Trainer Ditto teaches across the
  counter rather than selling you a badge. The reason is simple: a disc is an item, an item goes in
  a chest, and an HM that can be posted to a friend who never went looking for the Pokémon is not
  something anyone had to earn. What you know cannot be traded away.
- **HM Discs are an operator's tool.** They are still registered, still in the creative tab, still
  work exactly as they did — nothing in survival hands one out.
- **The Trainer Ditto will not deal with you if it is afraid of you.** Catch one, or knock one out,
  and every trader after it backs away instead of opening the stall. It used to only run, which
  meant cornering one against a wall got you a shop as though nothing had happened.

### ✨ New
- **Every HM can be switched off, one at a time.** `/dittohm config <hm> enabled false` closes all
  three doors in at once — nobody can learn it, no Pokémon will teach it, and the Trainer Ditto
  stops offering it. Players who already know it keep it: closing the door is not the same decision
  as taking something back.

## [2.1.5] - 2026-08-19

**Magnet Rise finally does the thing its name says, and Headbutt learned what lives in a tree.**

### ✨ Changed
- **Magnet Rise is a toggle, and it is flight.** Not five seconds of floating — switch it on and you
  are off the ground for as long as you like, drifting at half your walking pace with no dash. The
  price is the steepest of any toggle and it is paid once: fifteen food points off your maximum,
  out of a budget of eighteen. Flying is nearly everything you have.
- **Destiny Bond picks its victim.** Aim at a creature to tie yourself to it, and then **however**
  you die — a mob, a fall, lava, your own Explosion — it dies with you, wherever it happens to be
  standing. It used to only avenge you against whatever landed the last blow, which asked nothing
  of you. Now you choose who you are taking, and then you have to be right.
- **Headbutt knows which trees bear fruit.** Apples — and the Applin that grew inside one — only
  come out of apple trees. Every tree still gives up sticks and its own sapling.

### ✨ New
- **There is sometimes a Greedent in the tree**, and it does not enjoy being woken up.
- **Bees notice.** Headbutt a tree with a hive in it and the whole hive comes out after you, exactly
  as it would if you had broken into it.

## [2.1.4] - 2026-08-19

**Six of the older HMs were not quite the thing their name promised.**

### ✨ Changed
- **Charge is permanent, and it shows.** A charged block stays charged until you charge another one
  or leave — no timer — and it throws off sparks the whole time it is live. A power source that
  switches itself off after a minute is not a power source, it is a fault to go and find.
- **Explosion is what it sounds like.** Nine times in ten it kills you outright. The tenth leaves you
  standing on a single heart. It is not a tool with a downside; it is the last thing you do.
- **Rock Climb stops gluing you to the wall.** You can travel along a face now, and step off it,
  instead of being cut to a fifth speed the moment you touch one. Up, down and holding on are
  unchanged.
- **Mean Look holds off Pokémon that are hunting you**, not only the mobs the game calls hostile.
  Anything else in the field is left where it is.
- **Cut cuts plants.** Grass, ferns, crops and ground cover come away as if you had used shears —
  the right drop, every time, including for plants added by a datapack — and it costs hunger, so it
  is a tool and not an infinite harvester.
- **Sweet Scent takes three times as long to come back.** It was far too quick.

## [2.1.3] - 2026-08-19

**Substitute goes back to doing the one thing a substitute is for: taking the hit.**

### 🐛 Fixed
- **The decoy takes damage now, and pops when it has taken enough.** It could not be hurt at all —
  not because it was set invulnerable, but because it was set *invisible*, and the game refuses every
  blow aimed at an invisible armour stand before it checks anything else. It soaks up a quarter of
  your own maximum health and then goes off in a puff. Nothing drops when it does.
- **The decoy wears your name.** A disguise drawn in a player skin was skipping the nametag
  altogether, so your double stood there anonymous — the one detail that gives a double away. The
  **Trainer Ditto** gets its label back for the same reason.

## [2.1.2] - 2026-08-19

**Camouflage finally copies the thing you are looking at.**

### 🐛 Fixed
- **The disguise is the creature you aimed at.** It had been turning you into a random Pokémon at
  zero health, and it was not random at all: the costume was packed the way a *world save* is written
  and unpacked the way the *client* expects, the read failed every single time, and the game quietly
  handed out a blank Pokémon instead. It is packed the client's way now — right species, right form,
  right shiny, right everything — and with a real creature underneath, the animations follow.
- **The disguise wears the target's nametag.** Whatever hangs over the thing you copied now hangs
  over you, word for word, and nothing hangs over you if nothing hung over it. Trainers, traders and
  named mobs included — it is no longer only Pokémon that carry their label across.

### ✨ Changed
- **Camouflage lasts a quarter of an hour, and you can take it off.** Fifteen minutes instead of
  five, and firing it again while it is running sheds the costume on the spot and frees the HM
  immediately — so swapping from one disguise to another is two presses, not a wait.

## [2.1.1] - 2026-08-19

**A round of things that fired twice, said too much, or quietly took your dinner.**

### 🐛 Fixed
- **One click, one HM.** Firing an HM with an empty hand could set it off twice. The vanilla client
  re-sends a held left-click every few ticks, and every re-send was a fresh cast — which is why the
  HMs with no cooldown of their own (Cut, Rock Smash, Rototiller, Strength, Dig) were the ones you
  saw double. A press now pays out once, however long you hold it.
- **The weather HMs give the sky back properly.** Sunny Day ended with a thunderstorm arriving the
  instant the sun ran out, and Rain Dance ended with the rain stopping and lightning starting in the
  same breath. Both handed rain and thunder the same countdown, so both went off together. Each is
  now rolled separately, the way the game rolls them, and the sky is quiet in between.
- **Leafage stopped wrecking the flowerbed.** Tall flowers were being planted as half a flower, so
  the next cast in the same field knocked every one of them over. They are planted whole now, only
  where there is room, and never on a spot that already has something growing on it. A biome with no
  flowers of its own gets grass rather than a dandelion that does not belong there — and bone-mealing
  a sunflower no longer showers you with free sunflowers.
- **Rest keeps quiet.** It no longer writes a line into the chat log for every person it heals.
- **Your food is not thrown away any more.** With toggles running, your hunger bar is capped below
  full — and the game read that as "still hungry", so you could always eat, and the meal was clipped
  straight back off. Food you cannot use is now refused, and it says so.

### ✨ Changed
- **Miracle Eye throws an eye.** No more line of text telling you the name, the distance and the
  bearing: it flies off towards the monument and you follow it, exactly the way you find a
  stronghold. It does not leave anything behind when it lands.

## [2.1.0] - 2026-08-13

**Six new HMs, and three of the old ones became something else.** Everything below has been in
development since 2.0.1.

### ✨ New
- **Seed Bomb** — lob a heavy seed that bursts where it lands. Small on purpose, and the blast is a
  dial (#52).
- **Eruption** — open a pool of lava on the face of the block you aim at, never underfoot. Respects
  claims and spawn protection, exactly as a bucket does (#56).
- **Miracle Eye** — find the nearest legendary monument: what it is, how far, and which way. Not
  where. Which monuments count is a datapack tag (#11).
- **Helping Hand** *(toggle)* — your mount spends half the effort on everything, so it lasts about
  twice as long (#43).
- **Tailwind** *(toggle)* — whatever you fly on moves half again as fast (#42).
- **Swift** *(toggle)* — and gets up to speed twice as quickly, on land, in water and in the air.

### 🌊 Three HMs found out what they were for
- **Dive** stopped being a way to swim fast and became the ability to **work** underwater: mine at
  full speed, walk the seabed as if it were dry land, breathe. It takes penalties away rather than
  handing out a bonus (#44, #45).
- **Lava Plume** is now Dive's twin for lava — move through it, walk its floor, see and breathe down
  there, and sprint into a proper swim. It grants no fire protection of its own: it asks Burning
  Bulwark for that (#65).
- **Surf** now speeds up **the thing you are riding**, not you (#41).

### 👤 The Trainer Ditto is an event the whole server shares
One turns up every half hour, once, for everybody, announced in chat when it arrives and when it
leaves — neither message says where. Its stall is rolled once and stays put, a disc you bought stays
sold, and scarce HMs turn up scarcely. Beat one in battle and every one after it keeps its distance
(#62, #55, #61, #58, #59).

### 🎡 The wheel
Open it, look, and back out — the bullseye cancels and changes nothing. The ring around it clears
everything, selection and toggles alike. Star your favourites and the **HM Case** opens a short
wheel holding only those. Whatever is live radiates, and the one HM that fires is marked apart from
the ones merely running. Every HM can carry a required experience level, all shipping at zero
(#66, #49, #60, #57, #63).

### 🐛 Fixes
- **Bullet Seed hits things.** It was firing dropped items, which cannot touch a creature (#53).
- **Rock Smash takes the whole vein of netherite and quartz**, and of any ore a mod adds.
- **Rest counts the room the way Minecraft does**, instead of demanding a unanimous yes from every
  connected player (#54).
- **Destiny Bond takes an armoured player down with you** (#51).
- **Camouflage holds its shape and moves with you**, instead of cycling through creatures.
- **Substitute wears your name and walks away with it**, and hides you for two seconds as you go.
- **Headbutt** works from standing, only shakes what you actually reached, and shakes giant
  mushrooms (#68).
- Leafage leaves a meadow (#64); Rock Climb works from standing; the HM Case reports the real
  reason it refused; a disguise holds its shape (#69); sky-clicks reach the server (#46); Headbutt
  drops the right sapling (#50); a toggle you cannot pay for is refused (#48); and one shake in a
  hundred knocks an Applin loose (#67).

## [2.0.28] - 2026-08-13

### ⛏️ Rock Smash takes the whole vein of netherite and quartz
It knew about eight kinds of ore, and the two you actually go to the Nether for were not among
them: **ancient debris belongs to no ore tag at all**, and **nether quartz ore has no tag of its
own**. Both were being treated as ordinary rock and broken one block at a time. Any ore a mod adds
now counts too — by the shared tag every modern one uses, and failing that, by simply being called
an ore.

### 🧿 Substitute lets you actually slip away
You left a copy of yourself standing there and then stood next to it in plain sight, which fools
nobody. Casting it now turns you **invisible for two seconds**: long enough to get behind
something and let whatever was chasing you commit to the wrong target, short enough that it stays
an escape rather than a cloak.

## [2.0.27] - 2026-08-13

### ⚡ New toggle — Swift
Whatever you are riding gets up to speed **twice as quickly** — off the mark, out of a turn, after
every stop. It is the third of the mount toggles and the only one that is not about top speed:
Surf is faster in water, Tailwind faster in the air, Swift is quicker to get there in all three.

Learned from a **Ninjask**, **Accelgor** or **Electrode** with **Sugar**.

```
/dittohm config swift power <0-512>
```

### 🐛 Headbutt only shakes what you actually reached
Charging a tree with something in the way counted as a hit on the tree: it read the block two paces
ahead and never checked whether you got there, so a wall with a trunk behind it dropped sticks while
you bounced off the wall. It now looks for the **first** thing in the way, which is the only thing
your head can have met.

## [2.0.26] - 2026-08-13

### 🍄 Headbutt shakes giant mushrooms
The huge caps of the swamps and the Nether answer a headbutt the way a tree does, and give up
mushrooms instead of saplings. They were never covered before because, for all they look like
trees, the game does not count them as wood.

## [2.0.25] - 2026-08-13

### 🧿 Camouflage holds the shape you picked, and moves with you
Two separate faults, both of them in how the costume was kept.

- **It stopped being a slideshow.** The server re-sends your disguise every couple of seconds so
  anyone who walks into view can see it, and every one of those resends was rebuilding the
  stand-in — which is created as a *random* creature and then filled in from what the message
  carries. The guard that was supposed to stop this compared the whole message, and the message is
  re-read off the live target each time: health, timers, animation state, all of it moving on its
  own, all of it different on every resend. What you are disguised as is **which creature**, so
  that is what is compared now.
- **The disguise walks when you walk.** A Pokémon's animations come from its own movement, not
  from the walk cycle vanilla mobs use, so a stand-in placed frame by frame read as standing
  perfectly still however fast you ran. It is handed your velocity and footing now.

## [2.0.24] - 2026-08-13

### 🌋 Sprinting in lava looks like swimming
Setting the swim flag was not enough and the tick order is why: the game decides whether you are
swimming — refusing outright unless the fluid is water — and then picks your pose from that answer,
both before a mod gets a word in. So the flag was being set after the pose had already been chosen
and cleared again before the next one, every tick, forever. The pose is now set directly, on your
own game and on the server, so you see it and so does everyone else.

## [2.0.23] - 2026-08-13

### 🎡 The selected HM is marked on its slot
Every attempt so far drew the marker around the **disc**, and an item picture is the one place on
this screen that is hard to draw next to — it renders in its own pass, at its own depth, and
whatever you put beside it is at the mercy of where that pass leaves things. So the mark moved to
the **segment**: the selected HM's wedge is flooded white and edged top and bottom, through the
same code that draws every slot on the wheel. Only one active can ever be selected, so there is
never a second white wedge to mistake it for.

### 🐛 The HM Case tells you the real reason again
Firing from the Case reported **"No HM selected"** for every refusal there is — on cooldown, too
hungry, not experienced enough. Each of those had already said exactly what was wrong, and the Case
then talked over it with something untrue. It now only says that when nothing actually is selected.

## [2.0.22] - 2026-08-13

### 🎡 The glow sits around the disc, not behind it
Both the radiance and the selected HM's white ring were sized as if a disc ended eight pixels from
its middle. It does at the edges — but its **corners** reach a good deal further, so the ring was
being drawn underneath them and came out as four disconnected arcs, and the glow only escaped at
the top, bottom and sides. Both now start outside the picture, and both keep those proportions at
any wheel size.

## [2.0.21] - 2026-08-13

### 🎡 You can tell what is selected again
The glow said "this is running", and a dozen toggles can be running at once — so the one HM that
actually fires when you click was lost among them. The **selected** one now carries a hard white
ring of its own, which nothing else on the wheel has and only one thing can ever have. The
type-coloured radiance goes on meaning "on".

## [2.0.20] - 2026-08-13

### 🐴 Surf, Tailwind and Helping Hand actually reach your mount
They were being applied on the server — and **the rider is what simulates the ride**. Like a horse,
a mounted Pokémon is moved by the game of whoever is sitting on it, and the server takes the result;
a speed changed on the server alone was a number nobody was reading. The boost is now written on
both sides, so the one that decides how fast you go has it too.

## [2.0.19] - 2026-08-13

### 🌋 Lava Plume has a second gear
Hold sprint under lava and you **swim** — properly, in the pose and at the pace, not a slightly
brisker wade. Vanilla's swim is hardcoded to water and can never happen in lava no matter what you
do, so Lava Plume brings its own.

### 🎡 Clear means clear
The centre of the wheel switches off **every toggle** along with your selection, instead of only
unsetting the active. One gesture puts you back to a bare fist — and switching a toggle back on is
one click, which the old split never was.

## [2.0.18] - 2026-08-13

### ✨ A live HM glows
The disc that is running now **radiates** — light coming off it in its own type colour, breathing
slowly. It used to carry an enchantment glint, which was the wrong signal twice over: a sheen that
sweeps across a picture is not the same as a picture giving off light, and at a glance it just read
as "this item is enchanted".

### 🔦 You can see in lava
Lava is not dark, it is **foggy** — vanilla draws it at one block, three if you are fire resistant,
which is why brightening it did nothing at all. With Lava Plume on you now see two dozen blocks
down there.

### 🐴 Helping Hand spends half instead of holding twice
It was reaching for the wrong end of the same number and doubling what a mount **spends** rather
than what it has, so it was quietly making mounts tire *faster*. Everything it does now costs half
the effort, which is the same "lasts about twice as long" asked the right way round.

## [2.0.17] - 2026-08-13

### 🐛 Fixes
- **Lava Plume no longer sends you skating.** Letting go of the controls left you sliding across the
  pool like it was ice: lava's only brake is that it halves your momentum every tick, and taking the
  drag off had taken the brake with it. Let go now and you come to rest the way you would on land.
- **You can see something in there.** Lava is pitch black from the inside; Lava Plume lights it up
  while you are under. The dense fog is drawn by your own game rather than the server, so this is
  only half the answer — but it is the difference between the block in front of your face and
  nothing at all.
- **Surf and Tailwind find your mount however you are sitting on it.** They only looked at what you
  were *directly* riding, so anything sat between you and the Pokémon hid it from them.

### 🔧 For working out what is going on
```
/dittohm mount
```
Reports what the mount boosts can actually see — which Pokémon, whether each toggle is on, and the
raw speed stat it is reading.

## [2.0.16] - 2026-08-13

### 👁️ New HM — Miracle Eye
Reach out and find the nearest **legendary monument**. It tells you what it is, roughly how far, and
which way — and deliberately **not** where. Knowing that Lake Verity is nine hundred blocks
north-east is what makes it a journey; a pair of numbers is what ends one (#11).

Five food and a thirty-second wait, because searching the world for one is genuinely hard work.

Learned from a **Xatu**, **Sigilyph** or **Unown** with an **Eye of Ender**.

**Which monuments it knows about is a datapack tag**, `cobblemon_ditto_hms:miracle_eye`. It ships
pointing at the thirteen from **Legendary Monuments** — the three lakes, Turnback Cave, Stark
Mountain, Giratina's island, Eternatus' cocoon, the distortion portal and the shrines — each listed
as optional, so a world without that mod loads fine and the HM simply says there is nothing out
there. Override the tag to point it at anything you like.

## [2.0.15] - 2026-08-13

### 🏄 Surf is for the thing you are riding
Surf made **you** a better swimmer. It now makes your **mount** one: get on something in water with
Surf on and it cuts through at half again its usual pace. Your own swimming on foot is untouched by
it — that was never what an HM called Surf was supposed to mean (#41).

### 💨 New toggle — Tailwind
A following wind for whatever you are **flying** on: the same half-again, in the air instead of the
water. Learned from a **Talonflame**, **Noivern** or **Staraptor** with a **Breeze Rod** (#42).

```
/dittohm config surf power <0-512>
/dittohm config tailwind power <0-512>
```

Both boosts are put on the creature you are riding and taken straight off again the moment you get
down or switch the toggle off — nothing about your Pokémon is changed for good.

## [2.0.14] - 2026-08-13

### 🌋 Lava Plume becomes the ability to work in lava
Lava Plume was a one-shot ride to the surface of a pool. It is now what **Dive** is underwater: the
ability to **live and work down there**. It is a toggle, so it lives in the wheel's inner ring now.

- **Move through lava, and walk its floor, without the fluid dragging on you.** Lava normally cuts
  you to about a third of a walking pace; it no longer does.
- **Breathe while you are under.**
- **Swimming out is exactly as it always was.** Like Dive, it takes a penalty away rather than
  handing out a bonus.
- **It gives you no fire protection of its own** — that is Burning Bulwark's job, and two HMs
  handing out the same immunity makes one of them pointless. Lava Plume **asks for it** instead:
  you need Burning Bulwark learned to switch it on, and switching it on switches Burning Bulwark on
  with it. The same arrangement Fly already has with Glide (#65).

For the ride to the surface of a **water** pool, that is still Waterfall.

## [2.0.13] - 2026-08-13

### ⭐ Favourites, and a short wheel to hold them
Fifty HMs is a lot to read at a glance when you use six of them.

- **Right-click a slot in the wheel to star it.** The wheel stays open, so you can set your whole
  list up in one visit, and a starred slot carries a gold star from then on. Right-click again to
  take it off.
- **Hold the HM Case and open the wheel, and only your favourites are on it.** No new gesture to
  learn: the Case is already in your hand as the activator, and now it is the short way in too.
  It still fires your selection exactly as before.
- Starred nothing yet? The Case shows the full wheel and tells you how to star something, rather
  than opening an empty ring.

Your list is saved with your world (#49).

## [2.0.12] - 2026-08-13

### 🐴 New toggle — Helping Hand
Whatever you are riding keeps going **about twice as long** before it tires. Nothing else changes:
it is not faster and it does not recover any quicker, it simply has more in the tank. Costs 2 food
off your maximum while it is on, like most toggles (#43).

```
/dittohm config helping_hand power <0-512>
```

Learned from a **Plusle**, **Minun** or **Audino** with a **Saddle**.

### 🌋 New HM — Eruption
Opens a pool of lava **on the face of the block you are aiming at** — the same square a bucket
would fill, and never underfoot. It refuses outright if you are standing close enough to end up in
it, and it has to pass the same permission check a lava bucket does, so claims, spawn protection
and the world border all hold: a plot you cannot build in is a plot you cannot erupt in.

Five food and a ten-second wait, so it stays a deliberate act rather than something you pave with
(#56).

Learned from a **Camerupt**, **Magcargo** or **Heatran** with a **Magma Block**.

## [2.0.11] - 2026-08-13

### 💣 New HM — Seed Bomb
Lob a single heavy seed and it bursts where it lands. It is Bullet Seed's ammunition with a fuse:
same flight, same "it renders as the seed you actually threw", one of them instead of a dozen.

The blast is **small on purpose** — a strength of 1, against a creeper's 3 and TNT's 4. It scatters
what is standing there and takes a bite out of soft ground; it will not open a hole in your base.
If you want a bigger bang, that is exactly what the dial is for (#52).

```
/dittohm config seed_bomb power <0-512>
```

It follows your world's mob-griefing rule, so a server with block damage off gets the bang and the
knock without the crater. For moving terrain on purpose, **Explosion** is still the HM.

Learned from a **Breloom**, **Torterra** or **Chesnaught** with **Melon Seeds**.

### 🐛 Fixes
- **Headbutt needs both feet on the ground.** You could fire it mid-air, which quietly turned it
  into a flight tool: charge, hop, charge again before landing, and it carried you across anything.
  It is a shoulder-charge — you have to push off something.

## [2.0.10] - 2026-08-13

### 🌱 Bullet Seed hits things
It never has. The barrage was firing **dropped items** — seeds on the ground, thrown hard — and a
dropped item cannot touch a creature, so every burst passed clean through whatever you aimed at no
matter what the config said. They are proper projectiles now: they fly flat and fast, they still
render as the exact seed you fired, and they hurt what they land on.

Damage comes off the same **power** dial that decides how many seeds a burst holds, so turning
Bullet Seed up makes it hit harder *and* more often (#53).

### 🐛 Fixes
- **Destiny Bond takes an armoured player down with you.** The blow was struck for the largest
  number a computer can hold, which kills a bare mob and then quietly fails against armour: the
  reduction arithmetic overflows and the victim walks away. It now strikes for enough and not more
  (#51).

## [2.0.9] - 2026-08-13

### 🎡 You can open the wheel, look, and back out
The middle of the wheel holds **two** things now, and they are not the same:

- The **bullseye is Cancel.** It closes the wheel and changes nothing — not your selection, not a
  single toggle. Until now every release did something, so there was no way to check what you had
  without committing to it (#66).
- The **ring around it clears your selection**, exactly as the centre used to, and your toggles go
  right on running.

A band of nothing separates both of them from the toggle ring, so a release that drifts a few
pixels off centre can no longer flip a toggle on its way past. Letting go anywhere else that is not
a slot — between the rings, off the wheel entirely — cancels as well.

### 😴 Rest counts the room the way Minecraft does
Rest asked for a **unanimous yes from every single connected player** — spectators, someone AFK in
the Nether, everybody — so one person not joining in meant nothing happened at all, no matter how
many of you were stood there resting.

It now runs the same vote a bed does, `playersSleepingPercentage` and all: spectators are left out,
anyone already asleep counts towards the tally, and the threshold is whatever your server set. The
clock also moves **once** for the whole vote — it used to be pushed to the next boundary again for
every player who agreed, which sent an odd number of you a full night too far (#54).

## [2.0.8] - 2026-08-13

### 🎚️ An HM can ask for an experience level
Every HM carries a **required experience level**, and every one of them ships at **zero** — so
nothing is gated and nothing about your game changes today. What it buys is that gating one
tomorrow is a config line in a pack, not a new version of the mod.

Where a pack does set one, it is a **requirement, not a price**: nothing is deducted when you use
the HM, you simply cannot reach for it until you have got there. The wheel greys out a slot you
have not qualified for and says which level it wants, and it lights back up the moment you level
up (#57).

```
/dittohm config <ability> minlevel <0-100>
```

## [2.0.7] - 2026-08-13

### 👤 The Trainer Ditto is an event the whole server shares
One turns up **every half hour, once, for everybody** — and everyone is told in chat when it
arrives, and again when it moves on. Neither message says where: finding it is the point. It stays
five minutes as it always has, so there is a trader standing somewhere about a sixth of the time.

It used to be a private dice roll per player, which made a rare visitor *commoner the busier the
server was* — four players meant one turning up every ninety seconds, several at a time, each of
them somebody else's. The wait survives a restart, and it runs while the server is empty: an
appearance nobody was around for is missed rather than banked (#62).

```
/dittohm config trader every <ticks>
```

### 🛒 Its stall holds still
- **What it lays out stays laid out.** The offers were worked out afresh every time the screen
  opened, so learning anything — a disc bought from that very trader included — reshuffled the
  whole table behind your back (#55).
- **A disc you bought is sold out.** It used to go straight back on the shelf, and the same trader
  would happily sell you the same disc twice (#55).
- **The scarce HMs turn up scarcely.** Every HM carries a weight the stock is rolled against:
  flight, blinking, a free heal and a suit of armour are the rare ones, the everyday tools are
  common, and a pack can retune any of it — down to never offering something at all (#61).

```
/dittohm config <ability> weight <0-100>
```

### 🥊 It remembers being beaten
Knock one out and word gets around: every trader after that keeps its distance from you, the same
way they already do from someone who caught one. Your friends are unaffected, and it does not
forget over a reload (#58).

## [2.0.6] - 2026-08-12

### 🌼 Leafage leaves a meadow, not a lawn
Bare ground now answers a burst in **flowers**, with the odd blade of grass among them — the other
way round from before. The blooms are ones the **biome you are standing in** would grow, read from
its own worldgen, so a burst in a plains looks nothing like one in a flower forest, and no two
patches come out the same (#64).

Crops, saplings and berry trees still leap to full growth exactly as they did.

## [2.0.5] - 2026-08-12

### 🐛 Fixes
- **Rock Climb works from standing.** It used to require you to already be off the ground, so the
  only way to start a climb was to jump into the wall and catch it mid-air. Walk up to a wall,
  look up, and you go up (#68).
- **A disguise holds its shape.** Camouflage was re-rolling what you looked like every couple of
  seconds, cycling through creatures instead of staying as the one you targeted (#69).

### 🖥️ Small
- **The "learned it!" message names your actual wheel key**, and stays right if you rebind it. It
  also goes to chat now instead of flashing past on the action bar — it is the one line telling
  you how to use what you just earned (#63).

## [2.0.4] - 2026-08-12

### 👤 No two Trainer Dittos are the same any more
- **Its level is rolled**, from a band you can set, instead of every visitor arriving identical.
- **Its IVs are rolled like any wild Ditto's.** Every trader used to be flawless, which turned a
  rare visitor into a stat vending machine with nothing left to hope for. A pack that wants the
  old behaviour can ask for it back (#59).

```
/dittohm config trader levels <min> <max>
```

## [2.0.3] - 2026-08-12

### 🎡 The wheel tells you what it is doing
- **The disc under your cursor grows.** No more guessing which slot a release will commit (#60).
- **Whatever is live now pulses.** The selected HM and every toggle that is on carry a much
  stronger halo, a bright rim and a slow breath of light — readable in a dark cave and at noon
  alike. Size always means "about to be picked", light always means "running", so the two never
  get confused for each other (#60).

### 🐛 Fixes
- **The HM Case fires at open sky again.** Left-clicking at nothing with the Case in hand did
  nothing at all, which killed **Teleport** and **Explosion** — the two you use without aiming at a
  block (#46).
- **Headbutt drops the right sapling.** Shake a birch and you get a birch sapling; the same for
  every other tree, modded ones included. Woods with nothing to plant drop none (#50).
- **A toggle you cannot pay for is refused**, and says how much is spare, instead of switching on
  into a state it cannot sustain (#48).

### 🍎 And one for the tree-shakers
- One shake in a hundred knocks an **Applin** loose. It lands at the foot of the trunk (#67).

## [2.0.2] - 2026-08-12

### 🌊 Dive becomes the ability to work underwater
Dive was a way to swim faster. It is now the ability to **live and work** down there — it takes the
water's penalties away rather than handing out a bonus.

- **Mine underwater at full speed.** A block below the surface breaks as fast as the same block in
  open air, and the weight a guardian temple puts on your arms lifts while you are under (#45).
- **Walk the seabed as if it were dry land**, with no drag on every step.
- **Breathe freely**, as before.
- **Swimming is exactly as fast as it always was.** Push off the bottom and you move like anyone
  else — if you want speed in the water, that is Surf's job (#44).

## [2.0.1] - 2026-08-07

**Everything here since 1.1.0.** 34 abilities became **47**, HMs moved off an item and onto a
wheel, and a wandering Ditto turned up selling discs.

### ✨ Nine new HMs
- **Thief** — take whatever the creature you're aiming at is holding (#36).
- **U-turn** — leap backwards and spin to face what you were running from (#35).
- **Charge** — turn the block you aim at into a redstone power source for a while. Timed, not
  permanent: the original block comes back exactly as it was (#33).
- **Destiny Bond** — for a short window, whatever kills you does not outlive you (#34).
- **Sweet Scent** — draw a horde of wild Pokémon out of hiding around you (#8).
- **Headbutt** — hurl yourself forward head-first. Shakes trees loose, hurts what you hit, and
  hurts you (#9).
- **Bounce** *(toggle)* — every block you land on answers like a slime block (#37).
- **Snowscape** *(toggle)* — winter follows you: snow underfoot, still water freezing as you cross (#6).
- **Vine Whip** *(toggle)* — reach several paces further, for blocks and creatures alike (#7).

### 🎡 The HM Wheel
- Press **H** for a radial selector holding every HM you know, tinted by the type of the move it is
  named after. Only what you have learned appears, so a handful of HMs get wide, easy segments (#14).
- **Whatever is live glows** — the selected HM and every toggle that is on get a halo and a glint,
  so one look tells you what is running.
- **The HM Case is no longer required.** It survives as one of two activators; a bare hand is the
  other, and both are configurable. HMs fire on **left-click** by default — it never opens a chest
  or a door out from under you — with right-click and either as options.
- **A keybind for every HM**, unbound by default, in *Options → Controls*.
- Discs, HUD icons and wheel slots all wear the same art: the Scarlet/Violet TM disc for the move's
  type, with the trigger item set into it.

### 🧬 The Trainer Ditto
- A rare wanderer with **perfect IVs** that lays out five random HM Discs, each costing only that
  HM's own trigger item. If you have learned nothing yet, your first disc is **free** (#15).
- It really is a Ditto — throw a Poké Ball and catch it. Do that and it never seeks you out again,
  and actively keeps its distance if it meets you.

### 🔧 Also
- **Camouflage really turns you into the creature**, hitbox included, instead of spawning a copy and
  hiding you under it (#30, #4).
- **Stockpile** (#16), **Lava Plume** (#38) and **Absorb** (#32) joined earlier on.
- **Same-move teachers** *(optional)* — any Pokémon knowing an HM's namesake move can teach it (#12).
- **Strength** pushes in six directions and moves double chests as one unit, contents intact (#5).
- Big fix-and-feel pass: Dive (#26), Rock Climb (#27), Waterfall (#18), Glide (#29), Explosion (#24),
  Charm (#25), Magnet Rise (#19), Dig (#23), and free single-block Cut/Rock Smash (#3).
- **Bullet Seed no longer crashes** (#21). Ember lights campfires (#20), Rain Dance actually rains
  (#22), Burning Bulwark scorches nearby blocks (#28), and right-clicking a chest opens it instead
  of firing your HM (#17).
- **HMs tell you why they didn't fire** — cooldown, hunger, wrong target — instead of doing nothing.
- **Toggles no longer double up.** Jump, Rollout, Dive and Harden work through attributes rather
  than status effects, so the HM entry is the only one you see. Hiding the icon was never enough —
  the inventory lists every effect regardless.
- **The Trainer Ditto's IVs are a setting** — from rolled like any wild Ditto, through one
  guaranteed best stat, up to flawless.
### 🐛 Fixed
- **Rock Climb climbs again.** It only ever clung to walls like a web: it watched the forward
  movement key, which a server never receives unless you are riding something, so the climb branch
  could not fire. **Look up to climb, sneak or look down to descend, look level to hold on.**
- **Waterfall stops at the surface** instead of launching you out of the water and into the sky.
- **Charge powers the block instead of replacing it.** It used to swap in a redstone block and put
  the original back — so charging a furnace briefly deleted it, and anything with contents was
  refused. Now the block stays exactly what it is and simply answers as a power source.
- **Substitute no longer duplicates your gear.** The decoy copied your armour and held item onto an
  armour stand, which could then be broken for a second set — backpacks included. It now wears
  **your skin** and carries nothing.
- **The Trainer Ditto is finally the right height to talk to.** Entity ray-tracing is done by the
  client, and the client never got the disguise hitbox, so its head was not clickable.
- **Strength moves containers properly again.** A moved block entity kept the coordinates of where
  it used to be, which broke it and every later push of the same chest.
- **Sweet Scent actually spawns a crowd**, beside you and made of what lives around you. It used the
  world heightmap to place them, so underground or indoors the horde appeared far off at the surface.
- **Stockpile's lava gulp hurts properly** — 3.5 hearts, up from half a heart.

### 🔧 Changed
- Kotlin incremental compilation is off. It failed repeatedly while Gradle still reported success,
  shipping jars missing synthetic classes that crashed the server and looked exactly like code bugs.

## [1.2.9] - 2026-08-07

### Fixed
- **A disguise now has the shape it looks like.** The Trainer Ditto stood at head height but kept a
  Ditto's knee-high hitbox, so you had to aim at its feet to trade with it. Camouflage got the same
  treatment: wear a Wailord and you take up a Wailord's room (#15).
- **Throwing a Poké Ball at the Trainer Ditto drops the costume**, so it is a Ditto being sucked
  into the ball rather than a trainer standing there unbothered while the ball wobbles.

## [1.2.8] - 2026-08-07

### Added
- **The Trainer Ditto wears a player skin.** Four faces ship with it and each trader picks one from
  its own identity, so it keeps the same face while it stands there. Drop more PNGs into
  `textures/entity/trainer_ditto/` and they join the rotation on their own — masculine and feminine
  share one pool, because a Ditto has no gender (#15).
- **A shiny trader is a genuinely shiny Ditto**, rolled at Cobblemon's own odds, and it wears the
  shiny skin. The sparkle does not survive capture: what lands in your party looks like any other
  Ditto.
- `/dittohm trader spawn shiny [player]` forces one, the only sane way to see that skin without
  waiting out 1-in-8192.

## [1.2.7] - 2026-08-07

### Added
- **The HM wheel's disc size is adjustable** in the config screen, 50%–200%. A wheel holding three
  HMs wants bigger discs than one holding twenty.

### Fixed
- **HM Discs could not be learned.** Right-clicking one did nothing at all: the activator was
  swallowing the click before the disc ever saw it, so the disc was never consumed and the HM never
  learned. Right-click learns again; left-click still fires a learned disc.
- **The Trainer Ditto's stall was empty** for anyone who already knew an HM. Opening the trade
  screen never sent the offers themselves, so it came up blank — the free starter disc worked only
  because it is handed over directly rather than sold.
- **The Trainer Ditto looks like a trader**, not like a plain Ditto standing in a field.
- The free starter disc no longer also sits on the table with a price on it.

## [1.2.6] - 2026-08-07

### Fixed
- **`/dittohm trader spawn` took the server down.** Summoning a Trainer Ditto threw
  `NoSuchMethodError` and killed the server tick loop. Five more of the same fault were waiting
  behind it — the trader despawning, fleeing, being looked up, and being named would each have
  crashed in turn (#15).

## [1.2.5] - 2026-08-07

### Added
- **Trainer Ditto keeps its distance from anyone who has already caught one.** Word gets around: it
  runs from you the way a creeper runs from a cat, on foot, so a friend can still walk up and trade
  while you hang back (#15).
- `/dittohm trader spawn [player]` summons one on demand, and `/dittohm trader forget [player]`
  undoes a catch so it will visit again.
- `/dittohm learn <ability> [player]` teaches an HM outright, no disc needed.

### Changed
- **Every player-facing command now takes an optional `[player]`** — `give`, `learn`, `select`,
  `forget`, `forget_all` and both `trader` actions. An operator can run the whole set on someone
  else without logging in as them.

## [1.2.4] - 2026-08-07

### ✨ Added
- **The Trainer Ditto visits.** A rare wanderer that lays out **five random HM Discs**, each priced
  at nothing but that HM's own trigger item — no emeralds, no haggling. Right-click it to see the
  stall. Its IVs are perfect, and if you have **not learned a single HM yet it hands you your first
  disc for free**, once ever, so the trigger items stop being a chicken-and-egg problem.
- It really is a Ditto: throw a **Poké Ball** and you catch it like any other. Do that and it never
  seeks you out again — you already have yours. Rarity, how long it stays and whether it comes at
  all are configurable in the config screen and under `/dittohm config trader` (#15).

## [1.2.3] - 2026-08-07

### 🔧 Changed
- **Camouflage really turns you into the creature now.** You *are* the mob: your model is replaced
  by it, matching its variant and its gear. Before, an inert copy was spawned on top of you and you
  were made invisible underneath — which meant a second real creature stood in the world, could be
  hit, blocked doorways, and trailed a tick behind you. Nothing is spawned any more, and the
  disguise cannot be killed off you (#30).

## [1.2.2] - 2026-08-07

### ✨ Added
- **Lava Plume** — 27th active HM. Waterfall's twin for lava: ride a rising current to the surface
  of a pool, without burning on the way up or as you climb out. Learned from a **Magcargo**,
  **Slugma** or **Turtonator** with a **Magma Cream** (#38).
- **Absorb** — 11th toggle HM. Loose items on the ground drift toward you while it is on. Learned
  from a **Gulpin**, **Swalot** or **Victreebel** with a **Hopper** (#32).
- **A keybind for every HM**, in *Options → Controls → Cobblemon Ditto HMs*. All unbound by
  default — bind the two or three you reach for constantly and leave the rest to the wheel. A
  keybind always works, whatever is in your hand and wherever you are looking.

### 🔧 Changed
- **Your HMs now tell you why they didn't fire.** Cooldown left, hunger short, aiming at nothing,
  not in water, not off the ground — each says so on the action bar with a short thud, instead of
  silently doing nothing.
- **Toggle HMs no longer double up in the HUD.** The HM icon is the only badge a toggle shows; the
  vanilla effect behind it (Dolphin's Grace, Night Vision, Resistance…) stays hidden, and a visible
  instance left over from an earlier session is replaced rather than kept.

## [1.2.1] - 2026-08-07

### ✨ Added
- **Substitute** — 26th active HM. Leaves a decoy of you standing where you were, wearing your head
  and your armour, and hostile creatures already hunting you go for it instead. Learned from a
  **Wobbuffet**, **Mew** or **Smeargle** with an **Armor Stand** (#31).
- **You choose how HMs fire.** Two settings in the config screen (Mod Menu on Fabric) and under
  `/dittohm config activator`:
  - **Activator item** — an **empty hand**, the **HM Case**, or either. The empty hand costs you
    punching and hand-mining while an HM is selected; the Case costs a hotbar slot and leaves your
    fist alone.
  - **Activator button** — **left-click**, **right-click**, or either.
- **The HM Case is back**, now purely as an activator: it holds nothing and manages nothing, so any
  Case is every Case and one is all you will ever need. Craftable as before.

### 🔧 Changed
- **The wheel only shows HMs you have learned.** No more hunting for your three abilities among 35
  slivers — with a handful learned, each one gets a wide, easy segment.

### 🐛 Fixed
- **Fly and Magnet Rise did nothing.** Both are used looking at open sky, and the vanilla client
  only tells the server about a click when a block or entity is in reach — so the HM was never
  reaching the server at all. Aiming at nothing now works, with either button.
- **Strength duplicated a container's contents.** Pushing a chest spilled its inventory onto the
  floor *and* carried the same items along inside the block. The chest now arrives with its
  contents and nothing is left behind.

## [1.2.0] - 2026-08-07

A big pass over how you reach your HMs, plus a fix-and-feel sweep across most of them.

### ✨ Added
- **The HM Wheel** — press **H** (rebindable) for a radial selector holding every HM you know: the
  25 actives on the outer ring, the 10 toggles on the inner one, each tinted by the **type of the
  move it is named after**. Hold the key and release on a slot, or tap to pin the wheel open and
  click. Picking a toggle switches it on or off; the centre clears your selection (#14).
- **Stockpile** — 25th active HM. Drinks up the water or lava you aim at, though lava burns going
  down. Learned from a **Gulpin** or **Swalot** with a **Sponge** (#16).
- **Same-move teachers** *(optional, off by default)* — any Pokémon whose moveset holds an HM's
  namesake move can teach it, on top of the curated species (#12).

### 🔧 Changed
- **The HM Case is gone.** Nothing to craft, nothing to carry — learn an HM and it is in your
  wheel. Your selection is per player, so it survives death and relogging.
- **Active HMs fire on a left-click with an empty main hand.** Anything in your hand keeps its
  normal left-click, so tools mine and weapons swing as before — and right-clicking a chest or door
  opens it instead of firing your HM (#17). While an HM is selected a bare-handed click fires it
  rather than punching; clear the selection from the wheel's centre to get your fist back.
- **New disc art** — every HM Disc is the Scarlet/Violet TM disc for its move's type, with the
  trigger item set into the bottom of the face. Toggle **HUD icons are the same disc**, so wheel,
  inventory and hotbar all match.
- **Strength** pushes in any of the six directions you look, and moves double chests as one unit —
  both halves travel together, or the push fails. Contents are preserved (#5).
- **Dive** is a proper scuba suit: water breathing, Dolphin's Grace and full underwater stride
  speed. The forced sinking is gone (#26).
- **Rock Climb** is ladder-like — hold forward to climb, sneak to descend, idle to cling (#27).
- **Waterfall** raises a soul-sand-style bubble column that carries you to the surface (#18).
- **Cut** slices bamboo and wood blocks in one swing, keeping the whole-tree cascade for trees.
  **Leafage** bonemeals everything in range and sprouts grass and flowers.
- A single-block **Cut** or **Rock Smash** is free; you only pay hunger when the whole-tree or
  whole-vein effect fires (#3).
- **Explosion** now has a 1-in-10 chance of being fatal instead of always leaving you at 1 HP (#24).
- **Charm** reaches about a block and plays a sweet chime (#25).
- **Magnet Rise** cooldown drops to 5s so it chains with its own effect (#19).
- **Dig** no longer grants Haste — it breaks the block you aim at and nothing more (#23).
- `/dittohm select <ability>` needs no item in your hotbar; `/dittohm select none` clears it.

### 🐛 Fixed
- **Bullet Seed** crashed on first use, then fired arrows. It fires seeds now (#21).
- **Camouflage** actually disguises you as a creature: aim at a mob in clear view and an inert copy
  of it, matching its variant and gear, mirrors your every move. Before, it only turned you
  invisible. It is **creature-only** — a block, a wall or empty air does nothing (#4).
- **Glide** only engages after you have been dropping a couple of blocks, so a normal jump is no
  longer hijacked (#29).
- **Ember** lights campfires and soul campfires, like flint and steel (#20).
- **Rain Dance** sets the weather in your own dimension, so it actually rains (#22).
- **Burning Bulwark** also scorches the odd block beside you while it is up (#28).
- **Charm**, **Leafage**, **Stockpile** and **Thunder** discs showed the missing-texture checker
  instead of their trigger item.
- Learned and enabled HMs used 32-bit masks, so past 32 abilities the newest collided with the
  oldest — Glide and Burning Bulwark shared bits with Water Gun and Leafage.

## [1.1.0] - 2026-06-21

### ✨ Added
- **Burning Bulwark** — 10th toggle HM (learn from a **Gouging Fire** with a **Blaze Rod**).
  Grants fire immunity and a thorns aura that scorches hostile mobs that get close. Blocks 4 hunger.
- **Per-toggle HUD icons** — each enabled toggle shows its own HM status-effect icon, so it's
  obvious which toggles are on. Underlying vanilla effects have their icons hidden.
- **Particles & sounds** for every HM use and toggle on/off.
- HM Discs now use **custom TM-style disc art** (gold "HM" rim + type-coloured ring) with the
  trigger item as the centre symbol.

### 🔧 Changed
- **Fly** no longer equips an Elytra — it requires **Glide** to be learned, auto-enables Glide,
  and launches you skyward (re-use mid-air for a firework-style boost).
- **Glide** now uses real Elytra gliding (no more Slow Falling).
- **Mean Look** now makes hostile mobs **flee with pathfinding** (like creepers from a cat);
  it never affects Pokémon, friendly mobs, or players.
- **Rock Climb** reworked — look at a wall to climb, sneak to descend.
- **Cut** now also fells vines.
- **Dive** sink tuned so it no longer fights swimming.
- **HM Case** — disc icons, drag-and-drop reordering, sections separated without spacer panes,
  and ability descriptions shown in tooltips.
- Rewrote all ability descriptions to say what each HM does (no Minecraft buff names).

### 🐛 Fixed
- Corrected several wrong ability descriptions (Leafage, Rock Smash, Rototiller, Waterfall,
  Dig, Defog, Revival Blessing, Strength).
- Fixed missing disc overlay textures for block/shield trigger items (Sunny Day, Harden, etc.).

## [1.0.0] - 2026-06-20

Initial release. **33 Pokopia-inspired HM abilities** (24 active + 9 toggles) for Cobblemon,
multiloader (Fabric + NeoForge).

### 🧬 Core systems
- **HM Discs** — learn an ability by right-clicking its disc; the disc remains as a reusable badge.
- **Acquisition** — obtain a disc by holding an ability's trigger item and **sneak + right-clicking**
  one of its unlock Pokémon. Which Pokémon/item unlocks each HM is intentionally **not shown
  in-game** — it's documented only in the wiki.
- **HM Case** — craftable hotbar item; right-click uses the active HM, shift-right-click opens a
  management GUI. Slots use each ability's trigger item as an icon; **shift+click reorders** HMs
  within a section.
- **Hunger** — active HMs cost hunger on use; toggles block food points from your max while enabled.
- **Per-ability config** — hunger / cooldown / power / hungerBlock via `/dittohm config` and the
  Cloth Config screen (Fabric, through Mod Menu).

### ⚡ Active HMs (24)
Water Gun, Leafage, Cut, Rock Smash, Rototiller, Camouflage, Strength, Waterfall, Magnet Rise,
Ember, Bullet Seed, Teleport, Fly, Rain Dance, Sunny Day, Rest, Dig, Explosion, Thunder,
String Shot, Defog, Crabhammer, Revival Blessing, Charm.

- **Camouflage** morphs you into the block or entity in your crosshair (5 min).
- **Magnet Rise** is airborne-only and grants Levitation II + Slow Falling for 5s.
- **Charm** makes a targeted mob follow you for 2 minutes.

### 🔄 Toggle HMs (9)
Jump (Jump Boost IV), Surf (Dolphin's Grace), Rollout (Speed), Dive (Water Breathing + sink),
Flash (Night Vision), Rock Climb (all blocks act as ladders), Mean Look (repel mobs),
Harden (full diamond armour, blocks 3 hunger), Glide (elytra-like glide physics, no item).

### ⌨️ Commands
`/dittohm use|list|select`, plus operator `give|config|reset_all|learn_all|forget|forget_all`.

### 🧩 Multiloader
Fabric and NeoForge shipped as one Modrinth version.
