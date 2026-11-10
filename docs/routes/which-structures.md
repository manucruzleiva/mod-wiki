# 🏘️ Which structures get roads

Every structure in your world is one of four things to the road network:

| | What it is | What the roads do |
|---|---|---|
| **Town** | a village, a town, a city | roads are planned **to** it |
| **Landmark** | somewhere worth seeing — a pyramid, a ruin, a tower | no road is planned **to** it; a road passing near it bends a little to go **by** it, keeps off its footprint, and signs it |
| **Ignored** | underground, at sea, or not in the Overworld | not visited and not signed; a road still goes around one that stands on the surface, as it does around a landmark |
| **Underground town** | a town built under the ground | a road runs to the spot above it, and a stone spiral stairway beside the road's end goes down to it |

Routes decides each one for you, and for most worlds its answer is the one you want. When it is not,
the three recipes below change it: one for a new world, one for a world you already play, and one for
pack authors.

---

## Make a structure a town, a landmark or ignored

### When you create a world: the ROUTES tab

1. On the create-world screen, open the **ROUTES** tab.
2. Under **Where roads go**, click **▶ Towns & landmarks** to unfold the structure list. It holds
   every structure your world will have, from every mod and data pack you installed.
3. Find your structure. The list is grouped by the mod it comes from, one bold heading per mod:
   **Minecraft** first, then the others in alphabetical order of their mod id. Inside a group the
   towns come first, then **Other structures**, each in alphabetical order. A row is named from the
   structure's id (`minecraft:village_plains` reads **Village Plains**); hover a row to see the id
   itself.
4. Click the row's button until it reads what you want: **Town** → **Landmark** → **Ignored** →
   **Underground town**, and round again.

That is all: the world is created with your choice. **Reset to Routes' list**, at the top of the
structure list, puts every row back to Routes' own answer.

!!! tip "Finding the id of a structure you have seen in game"
    Type `/locate structure ` in any world with the same mods and let tab-completion list the ids. The
    part before the `:` is the mod id, which is the heading to look under.

### On a world you already play

A structure's role **cannot change in a world that already has roads.** The world records the
structure list the moment its first roads are planned, so that every chunk generated later belongs to
the same network: a change halfway through would leave roads ending at a seam. What you can do in that
world, as an operator:

- **Make one structure a town:** stand in it and run `/routes settlement add [name]`. Roads plan to it
  as if the world had generated a town there.
- **Take one town off the network:** stand near it and run `/routes settlement remove`. Its roads go
  with it; `/routes settlement restore` brings both back.

See [the `settlement` commands](commands.md) for the rest.

To change the list for the worlds you create **next**, `/routes config set` writes it into your own
config, which the ROUTES tab starts from:

```
/routes config set route_city_structure_tags minecraft:village, bca:villages, -minecraft:village_desert
/routes config set route_landmark_structure_tags mymod:old_tower
```

`set` replaces the whole list, so type every entry you want to keep, separated by commas. Run
`/routes config get route_city_structure_tags` first to see what is in it. The grammar is in
[the structure lists](#the-structure-lists).

### For a pack author: a data pack

Routes reads three structure tags, and a data pack can add to any of them:

| Tag | File in your data pack |
|---|---|
| `routes:settlements` | `data/routes/tags/worldgen/structure/settlements.json` |
| `routes:landmarks` | `data/routes/tags/worldgen/structure/landmarks.json` |
| `routes:ignored` | `data/routes/tags/worldgen/structure/ignored.json` |

This one makes a mod's camp a town and its ruined tower a landmark:

```json title="data/routes/tags/worldgen/structure/settlements.json"
{
  "replace": false,
  "values": [
    { "id": "mymod:camp", "required": false }
  ]
}
```

```json title="data/routes/tags/worldgen/structure/landmarks.json"
{
  "replace": false,
  "values": [
    { "id": "mymod:ruined_tower", "required": false }
  ]
}
```

- `"replace": false` adds to what Routes ships. `"replace": true` throws Routes' list for that tag away
  and keeps only yours.
- `"required": false` keeps the tag loading when the mod that owns the structure is not installed.
- A structure belongs in **one** of the three. One listed in two is read in this order:
  `routes:ignored` first, then `routes:settlements`, then `routes:landmarks`.
- There is no tag for **Underground town**: that one is only set from the ROUTES tab or the config.

Add the data pack **before you create the world**. Added to a world that already has roads, it changes
only the ground not generated yet, and the roads there may not meet the ones built before. It is read
below the player's own choices, so a row someone changes on the ROUTES tab beats it, and it is
read only while **Routes' structure list** (under **Advanced**) is on.

### Check that it worked

- **A town**: run `/locate structure <id>`, go there, and run `/routes debug towns` (operator). It lists
  the towns the road network knows around you, nearest first, with their coordinates; yours is the
  one at the coordinates `/locate` gave.
- **A landmark**: follow a road that passes near it — within **How far a road detours**, 96 blocks
  unless you changed it. The road bends to go by
  it, and a signpost beside the road names it.
- **Ignored**: no road goes to it, and none signs it.
- **Underground town**: a road ends near the spot above it, beside a stairway going down.

---

## What a road does beside a landmark

- **It goes around it.** The road steers clear of the structure's real footprint, never through the
  middle of a ruin. Where a landmark fills the only way through, the road still gets built.
- **It passes by it.** A landmark close to where a road is heading pulls the road over a few blocks so
  you walk past it. A road visits **at most one**, the one nearest its line, so roads don't zigzag.
- **It signs it.** Where the road passes, a signpost beside it names the landmark. A structure from a
  mod the sign doesn't know is named from its id, so it still reads as a name.

Each of the three has its own option under **Landmarks** on the ROUTES tab: **Roads go around
landmarks**, **Roads pass by one landmark** and **Sign the landmark a road passes**.

---

## The list Routes ships

Routes comes with its own answer for the structures of the packs it is tested on — which are towns,
which are landmarks and which to ignore — so a pack like the Cobblemon Official Modpack gets roads to
its gym entrances with no config at all, and the Kanto cities of
[Cobblemon Cities & Structures](https://modrinth.com/mod/cobblemon-cities-structures) are towns. It is
the three structure tags of
[the data-pack recipe](#for-a-pack-author-a-data-pack), shipped in the jar.

It sits **below** everything you choose: a row you change on the ROUTES tab, and every entry of the
lists below, beats it. A structure it does not name is decided by the automatic rule. Turn it off with
**Routes' structure list**, under **Advanced** on the ROUTES tab.

---

## The structure lists

The ROUTES tab rows write three lists in the config, and `/routes config` and `config/routes.json`
edit the same lists by hand:

- `route_city_structure_tags` — what counts as a **town**;
- `route_landmark_structure_tags` — what counts as a **landmark**, among the things that are not
  towns;
- `route_underground_structure_tags` — what is an **Underground town**. Inclusions only.

The first two have the same grammar, and both **add to** the automatic rule rather than replacing it:

| You write | It means |
|---|---|
| `minecraft:village_plains` | this exact structure is one |
| `#bca:villages` | every structure in that tag is one |
| `-minecraft:village_desert` | this one is **not**, whatever anything else says |
| `-#minecraft:village` | nothing in that tag is |

The `-` prefix is what a row writes when you move it off a role, and it is read **before** everything
else — so an exclusion always wins, including over the built-in rule that says a village is a town. A
structure excluded from both lists is **Ignored**.

---

## Advanced options

Three options under **Advanced** on the ROUTES tab change how the whole list is decided. A first world
needs none of them.

### Town ids only

**Town ids only** (`gen2_settlement_allowlist`) is different from everything above: **the moment it holds a single id, it
is the whole truth about towns.** Only the ids in it are towns, the automatic rule stops
applying, and `route_city_structure_tags` is not consulted at all.

!!! warning "It is all-or-nothing, and that is the point"
    Put one gym in it and your world's villages stop getting roads. Leave it empty — the default —
    unless you want to hand-author the complete list yourself.

### Every surface structure gets roads

**Every surface structure gets roads** (`connect_all_structures`) is the opposite extreme: every
**surface** structure becomes a town. Underground ones are still skipped, so roads do not dive for a mineshaft.

It makes for a very dense network. It is there for map makers and for seeing what a pack contains.

### Routes' structure list

On by default. Off, Routes ignores [the list it ships](#the-list-routes-ships) and guesses every
structure you have not set yourself from its name.

---

## The order things are decided in

Routes first asks "is this an Underground town?": only a structure you set to one is, and that answer
beats every rule below. Then it asks "is this a town?", and stops at the first rule that answers:

1. **Town ids only**, if it has anything in it — that is the whole answer.
2. **Every surface structure gets roads**, if it is on — every surface structure is one.
3. **Your town exclusions** — anything you wrote with a `-`, or moved off Town.
4. **The village rule** — anything in the `#minecraft:village` tag.
5. **Your town inclusions** — the ids and tags you added.
6. **[The list Routes ships](#the-list-routes-ships)** — a town it names is one, and a landmark
   or an ignored structure it names is not, whatever its id says.
7. **The name rule** — an id that calls itself a village, a town or a city.

Anything that is not a town then gets the second question — landmark or ignored:

1. **Your landmark exclusions** — Ignored.
2. **Your landmark inclusions** — Landmark.
3. **The list Routes ships** — a landmark or an ignored structure it names.
4. Otherwise it is a **Landmark**, unless it is not in the Overworld, every biome it can generate
   in is ocean, or its name says it is built underground — a mineshaft, a stronghold, a dungeon, a
   buried or sunken thing, an ancient city, trial chambers. Those are **Ignored**.

The reason exclusions sit above the village rule is so moving a village off **Town** actually
works: without that, the village rule would answer first and the change would do nothing.

To see which towns these rules gave a world, run `/routes debug towns` in it.

---

## A note for pack authors

A road is planned to a town's **street layout**, not to a point — the connector walks the road
tip to the nearest real street piece and hands over there. A structure with no streets still gets a
road, it just meets it at the edge. A road joins at the **open end of a street**, at the street's own
height, never at a leftover connector behind a building.

- **Choose where roads come in.** Mark a street end with an open jigsaw named `routes:city_exit` and a
  road into the town ends on one of those exits — the one facing it most squarely — so it continues
  your street. Exits no road uses stay ordinary dead-end streets.
- **Say what kind of place it is.** Tag the structure `routes:settlement/village`,
  `routes:settlement/town` or `routes:settlement/city` and its name gets that word: *Pallet* becomes
  *Pallet Town*. A name that already ends in one (*Black City*) is left as it is.

Structures that only exist in the Nether or the End are never connected: roads are an Overworld
thing.
