# 🏘️ Which structures get roads

Routes connects **settlements**. Everything else in your world — pyramids, mineshafts, monuments,
ruins — is left alone, and no road is planned to it.

What counts as a settlement is **yours to decide**, and there are three ways to say it, from the one
almost everybody wants to the one for pack authors.

---

## The Cities include checklist

The **ROUTES** tab on the create-world screen carries a checklist built from **the structures your
world actually has** — every mod and datapack you installed, grouped by the mod each one came from.
Tick a structure and roads will run to it; untick it and they will not.

!!! tip "It is built from your world, not from a fixed list"
    The checklist is generated when you open the tab, so a settlement from a mod nobody has ever
    heard of appears in it the same as a vanilla village.

This is the way to do it. The two below exist for cases the checklist cannot reach.

---

## The structure list, by hand

`route_city_structure_tags` in the config takes structure **ids** and structure **tags**, and it
**adds to** the automatic rule rather than replacing it:

| You write | It means |
|---|---|
| `minecraft:village_plains` | this exact structure counts as a settlement |
| `#bca:villages` | every structure in that tag counts |
| `-minecraft:village_desert` | this one does **not** count, whatever anything else says |
| `-#minecraft:village` | nothing in that tag counts |

The `-` prefix is what the checklist writes when you untick a row, and it is read **before**
everything else — so an exclusion always wins, including over the built-in rule that says a village
is a settlement.

---

## The allowlist, for total control

`gen2_settlement_allowlist` is different from everything above: **the moment it holds a single id, it
is the whole truth.** Only the ids in it count as settlements, the automatic rule stops applying, and
`route_city_structure_tags` is not consulted at all.

!!! warning "It is all-or-nothing, and that is the point"
    Put one gym in it and your world's villages stop getting roads. Leave it empty — the default —
    unless you want to hand-author the complete list yourself.

---

## Connect all structures

`connect_all_structures` is the opposite extreme: every **surface** structure becomes a road node,
not just settlements. Underground landmarks are still skipped, so roads do not dive for a mineshaft.

It makes for a very dense network. It is there for map makers and for seeing what a pack contains.

---

## The order things are decided in

When Routes asks "is this a settlement?", it stops at the first rule that answers:

1. **The allowlist**, if it has anything in it — that is the whole answer.
2. **Connect all structures**, if it is on — every surface structure is a node.
3. **Your exclusions** — anything you wrote with a `-`, or unticked on the checklist.
4. **The village rule** — anything in the `#minecraft:village` tag.
5. **Your inclusions** — the ids and tags you added.
6. Otherwise it is **not** a settlement.

The reason exclusions sit above the village rule is so unticking **Villages** actually works: without
that, the village rule would answer first and the tick would do nothing.

---

## A note for pack authors

A road is planned to a settlement's **street layout**, not to a point — the connector walks the road
tip to the nearest real street piece and hands over there. A structure with no streets still gets a
road, it just meets it at the edge.

Structures that only exist in the Nether or the End are never connected: roads are an Overworld
thing.
