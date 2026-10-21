# Server Admin

Everything here needs **operator level 2**.

## Settings

| Command | What it does |
|---|---|
| `/treecarve config` | Lists every setting with its value and range. |
| `/treecarve config <key>` | Shows one setting. |
| `/treecarve config <key> <value>` | Changes one setting. |
| `/treecarve config reset` | Puts every setting back to its default. `reset <key>` does one. |
| `/treecarve reload` | Re-reads the file after you edited it by hand. |

Settings are saved to `config/tree_carve.json`. If the file cannot be read, it is left untouched and
the server runs on the defaults until you fix it and run `/treecarve reload`.

### What can be carved

| Key | Default | Meaning |
|---|---|---|
| `carving` | `true` | Whether a sword carves anything at all. |
| `carveOnStripped` | `false` | Stripped logs can be carved. |
| `carveOnPlanks` | `false` | Planks can be carved. |
| `carveOnAnyWood` | `false` | Anything an axe mines can be carved. |
| `axeStrips` | `true` | Stripping a carved log with an axe takes the message with the bark. |
| `allowEditOthers` | `false` | Anyone may rewrite a carving somebody else cut. Off, only the author and operators can. An axe removes any carving either way. |

!!! warning "Some of these cannot be undone with an axe"

    A message cut into a stripped log, a plank or other wood **comes off only by breaking the
    block**: there is no bark left to strip. The same goes for every carving when `axeStrips` is
    `false`. Turn these on knowing that the only remover left is a pickaxe, an axe swing that
    breaks the block, or [`/treecarve remove`](#moderation).

### Limits and cost

| Key | Default | Range | Meaning |
|---|---|---|---|
| `swordDurability` | `1` | 0–64 | Durability the sword loses per message written. |
| `maxElements` | `16` | 1–64 | Pieces one face may hold. |
| `maxTotalChars` | `240` | 1–240 | Characters across every text piece on a face. |
| `allowDye` | `true` | | A piece can be carved in colour with a dye the player is carrying. |
| `consumeDye` | `true` | | Spend the dye. Off, it only has to be in the inventory. |
| `carveSound` | `true` | | Play a sound at the log when a message is written. |

`maxElements`, `maxTotalChars` and `blockedWords` apply to the next carving; what is already cut is
left alone.

### Look

| Key | Default | Range | Meaning |
|---|---|---|---|
| `letterLighten` | `42` | 0–100 | How far toward white the lettering is pushed, in percent. |
| `grooveDarken` | `25` | 0–100 | How dark the inside of the cut is, in percent. |
| `dyeStrength` | `65` | 0–100 | How far the wood is pulled toward the dye, in percent. |
| `renderDistance` | `48` | 8–128 | How far away a carving is drawn, in blocks. |
| `surfaceOffset` | `3` | 1–50 | How far the lettering sits off the bark, in thousandths of a block. Raise it if a black mesh flickers. |

### Datapack tables

| Key | Default | Meaning |
|---|---|---|
| `datapackSymbols` | `true` | Load symbols from datapacks. |
| `datapackFonts` | `true` | Load fonts from datapacks. |

Both need a `/reload` to take effect. What they switch off is explained in
[Custom Symbols & Fonts](symbols-and-fonts.md#switching-the-tables-off).

## Moderation

| Command | What it does |
|---|---|
| `/treecarve who` | Who cut the face you are looking at, its text and how many symbols it holds. |
| `/treecarve remove` | Clears the face you are looking at. |
| `/treecarve list <player>` | Every carving by that player in every dimension, up to 50. Click a line to get the command that takes you there. |
| `/treecarve removeall <player>` | Clears every carving by that player, online or not. |

Every removal is written to the server log with who did it and what the carving said. A carving made
by a command or another mod has no author, and shows as *nobody*.

### Blocked words

```
/treecarve config blockedWords add "word"
/treecarve config blockedWords remove "word"
```

A blocked word is masked with asterisks wherever it stands as a whole word, in any case. The list
exists because a carving never passes through chat, so a chat-filter mod never sees it. Quote a word
with accents or spaces.
