# 🏘️ Which structures get roads

Every structure in your world is one of three things to the road network:

| | What it is | What the roads do |
|---|---|---|
| **Settlement** | a town — a village, a city | roads are planned **to** it |
| **Landmark** | somewhere worth seeing — a pyramid, a ruin, a tower | no road is planned **to** it; a road passing near it bends a little to go **by** it, keeps off its footprint, and signs it |
| **Ignored** | underground, at sea, or not in the Overworld | not visited and not signed; a road still goes around one that stands on the surface, as it does around a landmark |

Which is which is **yours to decide**, and there are three ways to say it, from the one almost
everybody wants to the one for pack authors.

## What a road does beside a landmark

- **It goes around it.** The road steers clear of the structure's real footprint, never through the
  middle of a ruin. Where a landmark fills the only way through, the road still gets built.
- **It passes by it.** A landmark close to where a road is heading pulls the road over a few blocks so
  you walk past it. A road visits **at most one**, the one nearest its line, so roads don't zigzag.
- **It signs it.** Where the road passes, a signpost beside it names the landmark. A structure from a
  mod the sign doesn't know is named from its id, so it still reads as a name.

A structure from a resource or data pack that you want roads to pass by, rather than reach, is simply a
**Landmark** in the checklist below. Each of the three behaviours has its own option under
[Towns & Settlements](configuration.md). They apply to worlds created with them and to ground that has
not generated yet.

---

## The list Routes ships

Routes comes with its own answer for the structures of the packs it is tested on — which are towns,
which are landmarks and which to ignore — so a pack like the Cobblemon Official Modpack gets roads to
its gym entrances with no config at all, and the Kanto cities of
[Cobblemon Cities & Structures](https://modrinth.com/mod/cobblemon-cities-structures) are towns. It is three structure tags in the jar, `routes:settlements`,
`routes:landmarks` and `routes:ignored`, so a data pack can extend or replace any of them.

It sits **below** everything you choose: a row you change in the checklist, and every entry of the
lists below, beats it. A structure it does not name is decided by the automatic rule. Turn it off with
**Use Routes' structure list** in [Towns & Settlements](configuration.md#towns-settlements).

---

## The Towns & landmarks checklist

The **ROUTES** tab on the create-world screen carries a checklist built from **the structures your
world actually has** — every mod and datapack you installed, grouped by the mod each one came from.
Every row reads **Settlement**, **Landmark** or **Ignored**; click it to cycle.

!!! tip "It is built from your world, not from a fixed list"
    The checklist is generated when you open the tab, so a settlement from a mod nobody has ever
    heard of appears in it the same as a vanilla village.

Each row starts on the automatic answer (see [the order things are decided in](#the-order-things-are-decided-in)),
so you only touch the ones you disagree with. This is the way to do it. The two below exist for cases
the checklist cannot reach.

---

## The structure lists, by hand

Two lists in the config, one per role, with the same grammar. Both **add to** the automatic rule
rather than replacing it:

- `route_city_structure_tags` — what counts as a **settlement**;
- `route_landmark_structure_tags` — what counts as a **landmark**, among the things that are not
  settlements.

| You write | It means |
|---|---|
| `minecraft:village_plains` | this exact structure is one |
| `#bca:villages` | every structure in that tag is one |
| `-minecraft:village_desert` | this one is **not**, whatever anything else says |
| `-#minecraft:village` | nothing in that tag is |

The `-` prefix is what the checklist writes when you move a row off a role, and it is read **before**
everything else — so an exclusion always wins, including over the built-in rule that says a village
is a settlement. A structure excluded from both lists is **Ignored**.

---

## The allowlist, for total control

`gen2_settlement_allowlist` is different from everything above: **the moment it holds a single id, it
is the whole truth about settlements.** Only the ids in it are settlements, the automatic rule stops
applying, and `route_city_structure_tags` is not consulted at all.

!!! warning "It is all-or-nothing, and that is the point"
    Put one gym in it and your world's villages stop getting roads. Leave it empty — the default —
    unless you want to hand-author the complete list yourself.

---

## Connect all structures

`connect_all_structures` is the opposite extreme: every **surface** structure becomes a settlement,
not just towns. Underground ones are still skipped, so roads do not dive for a mineshaft.

It makes for a very dense network. It is there for map makers and for seeing what a pack contains.

---

## The order things are decided in

Routes first asks "is this a settlement?", and stops at the first rule that answers:

1. **The allowlist**, if it has anything in it — that is the whole answer.
2. **Connect all structures**, if it is on — every surface structure is one.
3. **Your settlement exclusions** — anything you wrote with a `-`, or moved off Settlement.
4. **The village rule** — anything in the `#minecraft:village` tag.
5. **Your settlement inclusions** — the ids and tags you added.
6. **[The list Routes ships](#the-list-routes-ships)** — a settlement it names is one, and a landmark
   or an ignored structure it names is not, whatever its id says.
7. **The name rule** — an id that calls itself a village, a town or a city.

Anything that is not a settlement then gets the second question — landmark or ignored:

1. **Your landmark exclusions** — Ignored.
2. **Your landmark inclusions** — Landmark.
3. Otherwise it is a **Landmark**, unless it is not in the Overworld, every biome it can generate
   in is ocean, or its name says it is built underground — a mineshaft, a stronghold, a dungeon, a
   buried or sunken thing, an ancient city, trial chambers. Those are **Ignored**.

The reason exclusions sit above the village rule is so moving **Villages** off Settlement actually
works: without that, the village rule would answer first and the change would do nothing.

To see what these rules decided for your world, open the checklist on the create-world screen, or run
`/routes debug towns` and `/routes debug settlements` in game.

---

## A note for pack authors

A road is planned to a settlement's **street layout**, not to a point — the connector walks the road
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
