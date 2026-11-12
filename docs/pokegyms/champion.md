# The Champion

Once you carry enough badges, the world has one more trainer to beat: its **Champion**, a Radical Cobblemon
Trainers (RCT) trainer of RCT's own `champion` type. The Champion stands behind a **Champion's Lectern**.
Beat it and you get a trophy; lose and you pay for it.

## The Champion's Lectern

The lectern is a block you craft and place, and it is the only way to get a Champion. It is in the creative tab
too.

Shaped recipe (3 gold blocks, 1 diamond block, 1 lectern):

| | | |
| --- | --- | --- |
| Gold block | Diamond block | Gold block |
| | Lectern | |
| | Gold block | |

- **One Champion per world.** The lectern you placed last is this world's; the Champion stands behind it, facing
  the side you read it from. Placing another retires the older lectern and its Champion goes. Clicking a retired
  lectern says so.
- **Breaking this world's lectern sends the Champion away,** and there is none until a lectern is placed again.
  The lectern drops itself.
- **The Champion is picked once.** It is one of RCT's `champion` trainers, the same one for the same world.
  Without a `champion` trainer in RCT there is no Champion, and the lectern says it is not ready.
- **Click the lectern, or the Champion,** to challenge. Both do the same.

## Who may challenge

PokeGyms refuses the challenge and says why unless all of this holds:

- **Eight badges from different gyms.** A badge is a [signed medal](gyms.md#medals) (or Badge It badge) in
  your inventory, or a City gym whose [leader you beat](gyms.md#fighting-a-city-leader) (or whose
  [mainline badge](gyms.md#mainline-badges) you got). A gym counts once, however many medals you carry from it.
  Medals in a chest do not count: carry them.
- **The penalty in hand.** You need at least the penalty (5000 CobbleDollars by default), because that is
  what losing costs.
- **No cooldown running.** See [Rematch](#rematch-and-the-trophy).
- **Nobody else fighting the Champion.** There is one Champion, so one fight at a time.
- **The Champion is open.** An operator can [close it](commands.md#configuration).

## The battle

- **Level 70 at least.** The Champion's team is [scaled to your best Pokémon](gyms.md#level-scaling) like every
  RCT trainer's, but never under level 70, however low your party is. It never goes over the server's maximum level.
- **Outside RCT's progression,** like a City leader: beating it does not advance your RCT trainer progress.
- **It is a gym battle** for other mods, and counts [with Cobblemon Action Combat](gyms.md#with-cobblemon-action-combat)
  when that mod runs the fight in real time.

## Rematch and the trophy

- **Win: a trophy.** The **Champion's Trophy** names the Champion you beat and the date you won it, in its
  tooltip. You get one per win, and it drops at your feet when your inventory is full.
- **Lose: the penalty is destroyed.** Forfeiting or running away is a loss. The CobbleDollars are taken from you
  and paid to nobody. A fight the server stops with no winner costs nothing.
- **Either result starts a cooldown,** the same [rematch cooldown](gyms.md#rematch-cooldown) setting as the
  player leaders (`rematch.cooldown_minutes`, 60 minutes by default). It is yours alone, and survives a restart.
  With `rematch` switched off there is no wait.

## Settings

An operator tunes the Champion with [`/pokegyms config champion`](commands.md#configuration):

| Setting | Default | What it does |
| --- | --- | --- |
| `champion.enabled` | `true` | Off: the Champion takes no challenges. Trophies already won stay, and a battle already running finishes, a loss still costing the penalty. |
| `champion.badges` | `8` | Medals and badges from different gyms a challenger must carry. |
| `champion.level_floor` | `70` | The lowest level the Champion's team fights at. `1` lets it scale freely. |
| `champion.penalty` | `5000` | What losing costs, in CobbleDollars, and the least a challenger must have to start. |
