<!-- Copiado a mano de cobblemon-ditto-hms/CHANGELOG.md. El workflow de ese repo lo copiaba en
     cada build; al mudarse los docs aca ese paso desaparecio. Actualizar al publicar una version. -->

# Changelog

All notable changes are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) + SemVer.

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
