# Features

## 🗺️ Dynamic routes (worldgen)

- **Automatic road network** between cities (vanilla villages, `bca` villages, Gimmighoul towers, gyms —
  configurable tags), built with terrain-aware A\* pathfinding.
- **Pure worldgen**: corridors pre-generate themselves — no commands, no need to walk the area
  (`route_pregen_range`, default 2048 blocks).
- **Flat & inland**: the pathfinder strongly penalises slopes and keeps a buffer away from shorelines,
  while still bridging water when there's no alternative.
- **Mineshaft tunnels**: when connecting to a node would mean climbing a mountain (or there's no surface
  path), the road bores a straight, lit, supported tunnel through it instead of going over.
- **Clean tree clearing**: where a road crosses a tree it removes the whole trunk and canopy (no floating
  leaves, no dropped items).
- **Biome-based names**: each road is named in English after the biomes it crosses, e.g.
  `Route 3: Plains Forest`.
- **Signposting & differentiated junctions**: directional signs at each end; crossings are paved as a
  contrasting plaza so they stand out from the road.
- **Aquatic vs causeway** water crossings, route trainers along finished roads, and route-entry toasts.

## 🎮 Hardcore Nuzlocke

- **First-encounter capture lock** per zone (zone = biome, route, or structure depending on the mode):
  only the first wild you meet in a zone is catchable; a spent zone bounces Poké Balls.
- **Permadeath**: a fainted owned Pokémon is tagged dead — no healing (machines, items, revive, sleep),
  no battling, no trading; only PC storage or release.
- **Defeated Catch**: a defeated wild stays on the ground, catchable, for a window — and stays **inert**
  (can't wander or be re-battled, only re-caught).
- **Mandatory nicknames**: a blocking screen on every Pokémon you obtain.
- **Spectator on loss**: when your whole team is dead, your run ends (configurable).

## 🧩 Modular healing & EXP

- `healing_mode`: **ALL / MACHINES_ONLY / ITEMS_ONLY / NONE**, applied only to player Pokémon.
- Configurable starter level, whole-team shared EXP, EXP-per-KO, and a whole-number EXP boost.

## 🧭 Integrations (optional)

- **Waystones** — activating a waystone registers it as a named city node for the route network.
- **Xaero's Minimap** — auto waypoint + toast when you discover a waystone.

See [World creation & configuration](configuration.md) for how to set all of this per world.
