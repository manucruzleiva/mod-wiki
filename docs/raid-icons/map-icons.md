# The Icons

Every raid den the mod has seen is drawn where it stands, as the icon of its **tera type** — or, in a
Dynamax, Gigantamax or Mega raid, as the icon of its [feature](#feature-dens). A den is found the
moment its chunk reaches your client, and the marker disappears the moment the crystal does — mine
one and it is gone from the map on the same tick.

The markers are not waypoints. They are drawn by the mod straight onto Xaero's maps, so they never
enter your waypoint list, cannot be dragged out of place, and leave nothing behind when you uninstall.

## Tera icons

A den is drawn as its boss' tera type, one icon for each of the eighteen types and one for Stellar.

<div class="den-icon-grid" markdown>
<figure markdown="span">![Normal](assets/icons/tera/normal.png){ .den-icon }<figcaption>Normal</figcaption></figure>
<figure markdown="span">![Fire](assets/icons/tera/fire.png){ .den-icon }<figcaption>Fire</figcaption></figure>
<figure markdown="span">![Water](assets/icons/tera/water.png){ .den-icon }<figcaption>Water</figcaption></figure>
<figure markdown="span">![Electric](assets/icons/tera/electric.png){ .den-icon }<figcaption>Electric</figcaption></figure>
<figure markdown="span">![Grass](assets/icons/tera/grass.png){ .den-icon }<figcaption>Grass</figcaption></figure>
<figure markdown="span">![Ice](assets/icons/tera/ice.png){ .den-icon }<figcaption>Ice</figcaption></figure>
<figure markdown="span">![Fighting](assets/icons/tera/fighting.png){ .den-icon }<figcaption>Fighting</figcaption></figure>
<figure markdown="span">![Poison](assets/icons/tera/poison.png){ .den-icon }<figcaption>Poison</figcaption></figure>
<figure markdown="span">![Ground](assets/icons/tera/ground.png){ .den-icon }<figcaption>Ground</figcaption></figure>
<figure markdown="span">![Flying](assets/icons/tera/flying.png){ .den-icon }<figcaption>Flying</figcaption></figure>
<figure markdown="span">![Psychic](assets/icons/tera/psychic.png){ .den-icon }<figcaption>Psychic</figcaption></figure>
<figure markdown="span">![Bug](assets/icons/tera/bug.png){ .den-icon }<figcaption>Bug</figcaption></figure>
<figure markdown="span">![Rock](assets/icons/tera/rock.png){ .den-icon }<figcaption>Rock</figcaption></figure>
<figure markdown="span">![Ghost](assets/icons/tera/ghost.png){ .den-icon }<figcaption>Ghost</figcaption></figure>
<figure markdown="span">![Dragon](assets/icons/tera/dragon.png){ .den-icon }<figcaption>Dragon</figcaption></figure>
<figure markdown="span">![Dark](assets/icons/tera/dark.png){ .den-icon }<figcaption>Dark</figcaption></figure>
<figure markdown="span">![Steel](assets/icons/tera/steel.png){ .den-icon }<figcaption>Steel</figcaption></figure>
<figure markdown="span">![Fairy](assets/icons/tera/fairy.png){ .den-icon }<figcaption>Fairy</figcaption></figure>
<figure markdown="span">![Stellar](assets/icons/tera/stellar.png){ .den-icon }<figcaption>Stellar</figcaption></figure>
</div>

## Feature dens

In a Dynamax, Gigantamax or Mega raid, the tera type is not what you are choosing — the raid itself
is. A marker that showed the type would be showing the wrong fact, so those dens are drawn as their
**feature** instead:

| Icon | Drawn for | Tooltip colour |
|---|---|---|
| ![Dynamax](assets/icons/feature/dynamax.png){ .den-icon } | Dynamax, Eternamax | Red for Dynamax, purple for Eternamax |
| ![Gigantamax](assets/icons/feature/gigantamax.png){ .den-icon } | Gigantamax | Magenta |
| ![Mega](assets/icons/feature/mega.png){ .den-icon } | Mega, Mega X, Mega Y | Blue |

Eternamax shares the Dynamax icon: it is the same raid dressed differently, and rare enough that a
third icon would mostly go unseen.

Every other den keeps its tera icon, and that includes Tera, Shadow, Primal and Stellar raids — in
those, the type genuinely is the point.

A den's star tier says nothing about whether it is featured. Every featured den is 7-star, but so
are many plain ones, so the mod reads the feature from the boss itself.

## On the minimap

The icon sits over the minimap at 36×36 pixels — big enough to read at a glance in the corner of the
screen, small enough that a cluster of dens does not bury the terrain.

A den that is outside the minimap's view is **not drawn at all**. Xaero pins an off-view marker to
the rim of the minimap, which is the right behaviour for a waypoint you chose to watch and the wrong
one for every den in the world: the border would fill up with icons for dens hundreds of blocks away.

## On the world map

The same icon, at 48×48 — the world map is a whole screen, and an icon sized for the minimap reads
as a speck on it.

### The tooltip

Hover a den on the world map and it names itself in two lines:

```
Klinklang
★★★★★ Fighting
```

The Pokémon waiting in the den comes first, because that is what you are deciding on. Below it, the
star tier and the tera type, written in that type's own colour.

A [feature den](#feature-dens) names its feature in that line instead, in the feature's colour:

```
Alcremie
Gigantamax
```

The feature replaces both the stars and the type rather than joining them: the type is not what the
raid is about, and every featured den is 7-star anyway.

If your client has not yet received the den's contents, the species line is **left out** rather than
filled with a placeholder. A tooltip that said "Unknown" would be claiming the den has no boss, which
is a different fact from not knowing yet.

### The right-click menu

Right-click a den on either map and Xaero's menu is titled by the same rule as the icon:
**`Fighting Raid Den`** for an ordinary den, **`Gigantamax Raid Den`** for a featured one.

## What gets an icon

Everything the scan finds, until you say otherwise. Three [filters](configuration.md) narrow it down:

- **Star tier** — hide everything below the tier you are hunting.
- **Tera type** — list the types you care about and the rest stop being drawn. A feature den is
  never hidden by it, because its marker does not show a type.
- **Active only** — hide the dens that are not currently live.

A den whose tera type the mod does not recognise still gets a marker. A den you cannot classify is
worth more on the map than no den at all.

## Why icons appear as you walk

The mod reads dens out of the chunks your game has already been sent — it asks the server for
nothing and adds no network traffic. Chunks you have never loaded hold no dens as far as it is
concerned, so the map fills in behind you as you explore rather than all at once.

That also means a den someone else builds far away appears the next time you are near it, and the
scan re-checks what it knows continuously, so a den that changes is never remembered wrong.
