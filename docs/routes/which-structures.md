# 🏘️ Which structures get roads

Every structure in your world is one of three things to the road network:

| | What it is | What the roads do |
|---|---|---|
| **Settlement** | a town — a village, a city | roads are planned **to** it |
| **Landmark** | somewhere worth seeing — a pyramid, a ruin, a tower | no road is planned to it |
| **Ignored** | underground, at sea, or not in the Overworld | nothing at all |

Which is which is **yours to decide**, and there are three ways to say it, from the one almost
everybody wants to the one for pack authors.

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
6. **The name rule** — an id that calls itself a village, a town or a city.

Anything that is not a settlement then gets the second question — landmark or ignored:

1. **Your landmark exclusions** — Ignored.
2. **Your landmark inclusions** — Landmark.
3. Otherwise it is a **Landmark**, unless it is not in the Overworld, every biome it can generate
   in is ocean, or its name says it is built underground — a mineshaft, a stronghold, a dungeon, a
   buried or sunken thing, an ancient city, trial chambers. Those are **Ignored**.

The reason exclusions sit above the village rule is so moving **Villages** off Settlement actually
works: without that, the village rule would answer first and the change would do nothing.

`/routes structures` writes every structure of your world to `routes_structures.txt`, grouped into
the three roles, so you can see exactly what these rules decided.

---

## A note for pack authors

A road is planned to a settlement's **street layout**, not to a point — the connector walks the road
tip to the nearest real street piece and hands over there. A structure with no streets still gets a
road, it just meets it at the edge.

Structures that only exist in the Nether or the End are never connected: roads are an Overworld
thing.
