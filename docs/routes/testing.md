# 🧪 Test & Feedback

Routes is built by one person, and almost everything it does happens **while the world generates** —
which means a bug can sit in a feature for months without anyone standing in the right chunk to see
it. This page is the answer to that: for every feature, what it is, **exactly how to prove it works**,
and what to say if it does not.

You do not need to be a modder, and you do not need a GitHub account. Pick one section, follow the
steps, and tell us what you saw.

!!! warning "Every test on this page needs a **new** world"
    Roads are baked in as chunks generate. An existing world keeps whatever it was given, so a fix
    or a setting you change today shows up **only in ground that has not generated yet**. Testing on
    an old save is the single most common reason a test "fails" when nothing is wrong.

## Before you start

Write these down once — every report wants them:

| | Where to find it |
| --- | --- |
| **Routes version** | the file name of the jar in your `mods/` folder |
| **Loader** | Fabric or NeoForge |
| **Minecraft version** | 1.21.1 |
| **Modpack** | its name and version, or "none" |

Then set yourself up so you can actually see what you are testing:

1. Create a new world. On the create-world screen, tick **Allow Cheats**.
2. Once in, `/gamemode creative` and fly. Most of these tests are about ground you have not walked.
3. `/routes zone` tells you what the chunk under your feet is — a town, a route, an area or open
   wilderness. It is the quickest way to know whether you are standing where you think you are.
4. `/routes debug verify 128` and `/routes debug gaps 128` sweep the roads around you and print what
   they find. When something looks wrong, run these **before** writing the report — their output is
   worth more than a paragraph of description.

---

## 1. Roads that generate with the world

**What it is** — Routes finds the towns your world seed places and connects them with real roads,
drawn as the chunks generate. Nothing has to be walked first, and nothing builds while you stand
there. See [Dynamic Routes](routes.md).

**How to test**

1. Create a new world and note the seed.
2. Fly a few thousand blocks in a straight line, somewhere you have never been.
3. Look down.

**Expected** — you cross finished roads running between towns. They are complete when you arrive, not
half-built; they do not stop dead in the middle of a field; and flying back over one later shows the
same road, unchanged.

**Also worth checking** — `/routes status` prints how many towns and completed routes the world knows
about. `/routes list routes` lists them with their endpoints.

**If it looks wrong** — say whether the road was **missing**, **incomplete**, or **wrong**, and paste
the output of `/routes debug graph 128` and `/routes debug edges 128` from where you stood.

---

## 2. Climbing, cutting, tunnelling and bridging

**What it is** — a road answers the land it crosses. Gentle ground it follows; a steep rise it cuts
into or bores a tunnel through; a gap or a river it decks over. How steeply it is willing to climb
before doing any of that is the **Steepest climb** setting.

**How to test**

1. New world. Find a road that crosses hilly ground — mountains, a ravine, a river valley.
2. **Walk it end to end.** Not fly — walk. This is the one test that has to be done on foot.
3. Watch for: a step you cannot walk up, a stretch that drops away under you, a tunnel with no exit,
   a bridge with a hole in the deck.

**Expected** — the road is walkable from one end to the other without jumping and without swimming.
Tunnels are lit or honestly dark, and they come out the other side. Bridges have a solid deck.

**Turn the switches off too**

1. Create another world with **Dig tunnels** off. A road that would have bored through a hill now
   goes over the top — steeper, but continuous.
2. And one with **Build bridges** off. A river becomes an open lane you swim; a dry gap is followed
   down and back up on the ground.

**If it looks wrong** — coordinates, a screenshot, and the output of `/routes debug bridge 128` when
it is a bridge. Say whether the world was made with tunnels and bridges **on or off**.

---

## 3. Water crossings and the shoreline

**What it is** — where a route meets water it does not stop: the road runs to the shore, and an open
lane marked by stones on both sides carries on across the water. Frozen lakes are crossed **under**
the ice, never paved over it.

**How to test**

1. Find a road that reaches a river, a lake or a strait — `/routes debug gaps 128` points at the
   crossings near you.
2. **Stand in the water and look back at the shore.**
3. Swim the crossing to the far side and come out.

**Expected** — the road runs at the ground's own height right up to the shore: **nothing is cut into
the bank or built up on it**. Where the bank stands above the water there is a step down into the
lane. The lane is marked on both sides and you can surface anywhere along it.

**Then check a bridge** — walk onto one from land. The approach must rise to meet the deck in a single
step.

**If it looks wrong** — say which one it was (open water crossing or bridge), give coordinates, and a
screenshot taken **from the water looking at the land**.

---

## 4. Route numbers and signposts

**What it is** — every road gets a number the moment it is built, plus a name drawn from the terrain
it crosses (*Route 3: Steep Forest Pass*). Signs stand at both ends and at junctions, saying which
road this is and which town lies each way.

**How to test**

1. New world. Fly until you find a road you have **never walked**.
2. Land at its end and read the sign.
3. Now walk the road properly, from end to end.
4. Load an older world you already had, and check its roads too.

**Expected** — step 2 already shows **Route N**, not two town names and not a blank. Step 3 does not
change the number: it is the same road it was before you touched it. Step 4 shows every number the
old world had already given out, unchanged.

**Also worth checking** — a short road carries a sign at each end, not three signs within sight of
each other.

**If it looks wrong** — a screenshot of the sign, the coordinates of the road's ends, and whether the
world was new or already existed.

---

## 5. Towns, routes and areas — names and pop-ups

**What it is** — the world is divided into named places: **towns**, the **routes** between them, and
the **areas** those roads enclose once a loop closes. Crossing into one announces itself, in the style
you picked with **Zone notifications**.

**How to test**

1. New world. Walk out of a town onto a road and keep going.
2. Watch for the pop-up as you cross from one to the next.
3. `/routes zone` at each step — it must agree with what the pop-up said.
4. `/routes weave 4` forces ring roads to close now. Every loop that completes encloses a new named
   area; walk into one.
5. Change **Zone notifications** to Chat, then to Announcement, then Off, and cross a boundary each
   time.

**Expected** — a town has a real name, not *(unnamed town)*. A route reads *Route N: Something*. An
area reads *A3-Frostpine* or similar. Each setting changes **how** the announcement appears, and Off
silences it completely without silencing anything else.

**If it looks wrong** — the exact text you saw, the output of `/routes zone` at the same spot, and
`/routes debug areas 16` if it is an area.

---

## 6. Rest stops along the road

**What it is** — roads carry small roadside stops. Normally a campfire camp; with
[Cobblemon Picnic](../picnic/index.md) installed, about a third of them come up as one of its basic
picnic tables with a basket of bread beside it instead.

**How to test — with Cobblemon Picnic installed**

1. New world, with both mods.
2. Follow one long road, passing several stops.
3. **Look at the shape of a table**: three wide, two deep, benches at the front, table down the
   middle, the two back corners empty.
4. Open the basket.

**Expected** — a mix: some stops are picnic tables, some are still campfire camps. The table is a real
one from Cobblemon Picnic, whole and correctly assembled. The basket holds bread.

**How to test — without Cobblemon Picnic**

1. New world, Routes only.
2. Follow a road past several stops, then check `logs/latest.log`.

**Expected** — every stop is a campfire camp, and the log is silent: no warning, no stack trace.
Routes never builds a look-alike table out of ordinary blocks — it is Picnic's table or it is a camp.

**If it looks wrong** — a screenshot of the table from above, your Cobblemon Picnic version, and
whether roads at that spot generated **before or after** you installed Picnic. Stops on roads that
already generated stay as they were.

---

## 7. Xaero's maps — paint and waypoints

**What it is** — with [Xaero's Minimap or World Map](map-integration.md) installed, Routes tints the
map by category and drops a waypoint the first time you reach a town, a route or an area.

**How to test**

1. New world with Xaero's installed. Explore, then open the world map with **M**.
2. Check the colours: magenta over towns, orange over routes, teal over enclosed areas, wilderness
   untinted.
3. Walk into a town you have not visited, then onto a road you have not visited.
4. Quit to title and rejoin, then reopen the map.

**Expected** — step 3 drops one waypoint each, once. Step 4 shows them still there and **not
duplicated**.

**Also worth checking** — the paint shows on the full-screen world map regardless of your Y level and
of the minimap's Cave Mode.

**If it looks wrong** — which Xaero mods you have and their versions, whether it was the minimap or
the world map, and a screenshot of the map itself.

---

## 8. `/routesmap` — how your map looks

**What it is** — every choice about how the chunk paint looks on **your** map is a
[command any player can use](map-integration.md#changing-how-it-looks-routesmap). It never reaches the
server.

**How to test**

1. In a world with Xaero's installed and some roads already on the map, run `/routesmap` and read what
   it prints.
2. Run `/routesmap opacity route 0`, then open the world map with **M**.
3. Run `/routesmap opacity route 100` and `/routesmap colour route blue`.
4. Run `/routesmap paint off`, look at both maps, then `/routesmap paint on`.
5. Quit to title, rejoin, and run `/routesmap` again.
6. On a server, as a player **without** operator rights, repeat step 2.

**Expected** — step 1 lists the paint, the three opacities, the three colours and the waypoint
grouping. Step 2 hides the roads' tint on the minimap and on the world map, with no relog. Step 3
brings it back, blue and at full strength, straight away. Step 4 clears both maps and then restores
them. Step 5 prints what you set, not the defaults. Step 6 behaves exactly like single-player — no
permission message.

**If it looks wrong** — the exact command you typed, the line it printed back, and whether the
minimap and the world map disagreed with each other.

---

## 9. The ROUTES tab at world creation

**What it is** — every rule is chosen up front, on a **ROUTES** tab beside GAME / WORLD / MORE, and
saved with that world. See [World Creation & Config](configuration.md).

**How to test**

1. Start creating a new world and open the **ROUTES** tab.
2. **Read all of it, top to bottom.**
3. Hover a few options and read the tooltips.
4. Change something visible — Road surface, or Steepest climb — create the world, and go look.
5. Open the mod's own settings screen from the mods list too.

**Expected** — six sections in this order: Route Generation, Towns & Settlements, Road Shape, Surface
& Lighting, World Spawn, Map & Notifications. Every heading and every option is readable English, not
a raw key like `screen.routes.category.generation`. Every option has a tooltip. Step 4 shows up in the
world. Step 5 shows the same six groups.

**If it looks wrong** — a screenshot of the tab, and the exact text of anything that rendered as a raw
key. If a setting did not take effect, say which one and what you saw instead.

---

## 10. Where a new world starts

**What it is** — a new world puts you next to the nearest town instead of in the wilderness, and
quietly builds some ground around spawn in the background so the map is not empty on your first look.

**How to test**

1. New world with **Spawn in city** on. Look around the moment you land.
2. Open the map straight away, before exploring.
3. `/routes debug spawn` prints what the spawn finder decided.
4. Make another world with **Pregenerate around spawn** set to 0.

**Expected** — step 1 puts you on dry, solid ground in or beside a town, never in water. Step 2
already shows some towns and roads, and while the ground is still being built a counter on the action
bar says how far it has got, then how many chunks it generated. Step 4 shows an empty map at first,
and no counter, which is correct — that is what 0 means.

**If it looks wrong** — the seed, the coordinates you landed on, and the output of
`/routes debug spawn`.

---

## 11. Waystones

**What it is** — with [Waystones](https://modrinth.com/mod/waystones) installed, activating a
waystone registers it as a named town on the road network.

**How to test**

1. New world with Waystones installed. Find and activate one.
2. `/routes list cities`.
3. Open the map.

**Expected** — the waystone's name appears as a town, and a waypoint drops for it.

**If it looks wrong** — your Waystones version, the waystone's name, and its coordinates.

---

## 12. Commands

**What it is** — `/routes` carries a player-facing set (status, list, nearest, zone) and an
operator-facing one for building, renaming and debugging. The full manual is on
[the Commands page](commands.md).

**How to test**

1. Type `/routes ` and press **Tab**. Walk the suggestions.
2. Run each one and **watch the world**, not just the chat.
3. As a non-operator, try an operator command.

**Expected** — every command either does what it says **in the world** or tells you why it did not. A
command that reports success and changes nothing is the specific failure worth hunting here: if the
chat says it worked, go and look. Operator commands do not appear in tab-completion for a player who
cannot run them.

**If it looks wrong** — the exact command you typed, what it printed, and what you saw (or did not
see) in the world afterwards.

---

## Sending feedback

**One place for all of it: [the Discord](https://discord.gg/SwcwXcCN4k).** Open a post in the
**Routes tickets** thread and pick a tag — a bot files it as a tracked issue within about ten minutes,
replies in your thread with anything it still needs, and posts back there when it is closed. No GitHub
account, no form, no captcha to squint at.

Include the four lines from [Before you start](#before-you-start), plus whatever that feature's **If
it looks wrong** paragraph asked for. [Reporting bugs & ideas](../reporting.md) has the tag guide and
what makes a report get fixed fast.

Testing something and finding **nothing wrong** is worth reporting too — a feature nobody has
confirmed is not the same as a feature that works, and this page exists because too much of Routes is
in the first group.

Everyone who reports gets thanked on the [community credits page](credits.md). 💚
