# Custom Symbols & Fonts

The symbol picker and the font picker are not lists baked into the mod. Each is a **table loaded from
datapacks**, and the built-in hearts, stars and typefaces are ordinary entries in it. A pack can add
its own symbol, its own artwork or its own typeface, override a built-in, or hide one behind another
mod, with no code change.

This page is for pack authors and server owners. Players only need [Getting Started](getting-started.md).

## Two kinds of pack

| Pack | Ships | Needed for |
|---|---|---|
| **Datapack** | `data/<pack>/tree_carve/symbol/<name>.json` and `data/<pack>/tree_carve/font/<name>.json` | every entry — this is what puts it in the picker |
| **Resource pack** | a bitmap font and its PNG, plus a language file | only when the entry draws artwork of its own, or when it needs a readable name |

The datapack lives on the server and the tables are sent to every player on join and again after each
`/reload`. The resource pack lives on each **client**: on a server, every player needs it (a server
resource pack is the usual way), or they see the entry without its artwork.

## A symbol from a datapack alone

A symbol is **one character of a font**, not a picture. Minecraft already carries Unifont, which
covers a great deal of Unicode — suits, weather, chess pieces, tools — so a datapack alone can offer
any of those characters:

`data/mypack/tree_carve/symbol/swords.json`

```json
{
  "glyph": "\u2694",
  "order": 25
}
```

That is a complete symbol: crossed swords, placed in the picker between the umbrellas and the skull.
With no `font`, the glyph is drawn in the player's default font.

## A symbol with artwork of its own

When Unicode has no character for what you want, ship a bitmap font in a resource pack and point a
symbol at one of its glyphs. `tree_carve:pokeball` is built exactly this way and is in the mod's jar
if you want a working copy to start from.

### Draw it white

!!! warning "The sheet must be white on transparent, or greyscale"
    A carving is tinted with the wood it is cut into. The mod draws every glyph in one colour taken
    from that species' stripped wood, and that colour **multiplies** every pixel of the glyph. A
    full-colour sheet comes out as your art times the timber, which reads as mud.

    That is the feature, not a limitation: one white sheet comes out oak on an oak, birch on a birch
    and warped-green on a warped stem. Use grey for shading inside the shape.

### The resource pack: a bitmap font

`assets/mypack/font/symbols.json`

```json
{
  "providers": [
    {
      "type": "bitmap",
      "file": "mypack:font/symbols.png",
      "ascent": 8,
      "height": 10,
      "chars": ["\ue000\ue001"]
    }
  ]
}
```

The PNG goes in `assets/mypack/textures/font/symbols.png`, one equal-sized cell per character in
`chars`. Use code points from the Private Use Area (`\ue000` onwards) so they never collide with real
text. Draw the cells large — a symbol can be stretched across a whole trunk, and a bigger cell keeps
its edges clean.

### The datapack: the symbol entry

`data/mypack/tree_carve/symbol/lantern.json`

```json
{
  "glyph": "\ue000",
  "font": "mypack:symbols",
  "order": 75
}
```

## Symbol fields

| Field | Required | Meaning |
|---|---|---|
| `glyph` | yes | What is drawn. Usually one character; a short string is allowed. |
| `font` | no | The font the glyph is looked up in, as `<namespace>:<name>`. Left out, the player's default font. |
| `order` | no | Position in the picker, lowest first. Ties break on the symbol's id. Defaults to `0`. |
| `requires_mod` | no | A mod id. The symbol is **offered** only when that mod is loaded. |

`requires_mod` gates the picker and nothing else. A trunk already carrying the symbol keeps showing
it after that mod is removed — a carving is something a player made, and a changed mod list is not a
reason to erase it. This is how the pokeball appears only with Cobblemon installed.

## Fonts

A font entry offers a typeface a message can be cut in. It names a font the client already has,
vanilla's or one shipped in a resource pack:

`data/mypack/tree_carve/font/runes.json`

```json
{
  "font": "mypack:runes",
  "order": 50
}
```

| Field | Required | Meaning |
|---|---|---|
| `font` | yes | The font, as `<namespace>:<name>` — a font JSON under `assets/<namespace>/font/`. |
| `order` | no | Position in the picker, lowest first. Ties break on the id. Defaults to `0`. |

The same white-or-greyscale rule applies to a bitmap typeface: letters are tinted with the wood
exactly as symbols are.

## Names in the picker

The picker shows a translated name for every entry, built from its id:

| Entry | Language key |
|---|---|
| symbol `mypack:lantern` | `tree_carve.symbol.mypack.lantern` |
| font `mypack:runes` | `tree_carve.font.mypack.runes` |

Put them in your resource pack's `assets/mypack/lang/en_us.json`. Without one, the picker shows the
raw key.

## Overriding and ordering

An entry with the **same id** as a built-in replaces it. To change the heart, ship
`data/tree_carve/tree_carve/symbol/heart.json` in your datapack; a higher-priority datapack wins, as
with any other datapack file.

To slot a new entry between two built-ins, pick an `order` between theirs.

| Symbol | Id | Order |
|---|---|---|
| Pokeball (Cobblemon only) | `tree_carve:pokeball` | 5 |
| Heart | `tree_carve:heart` | 10 |
| Hollow heart | `tree_carve:heart_outline` | 11 |
| Umbrella | `tree_carve:umbrella` | 20 |
| Aiaigasa | `tree_carve:aiaigasa` | 21 |
| Skull | `tree_carve:skull` | 30 |
| Star | `tree_carve:star` | 40 |
| Hollow star | `tree_carve:star_outline` | 41 |
| Flower | `tree_carve:flower` | 50 |
| Music note | `tree_carve:note` | 60 |
| Sun | `tree_carve:sun` | 70 |
| Cloud | `tree_carve:cloud` | 71 |
| Snowflake | `tree_carve:snowflake` | 72 |
| Anchor | `tree_carve:anchor` | 80 |
| Crown | `tree_carve:crown` | 90 |
| Arrow | `tree_carve:arrow_right` | 100 |
| Cross | `tree_carve:cross` | 110 |

| Font | Id | Order |
|---|---|---|
| Carved (the default) | `tree_carve:carved` | 0 |
| Plain | `tree_carve:default` | 10 |
| Unifont | `tree_carve:unifont` | 20 |
| Galactic | `tree_carve:alt` | 30 |
| Illager runes | `tree_carve:illageralt` | 40 |

## When a pack is removed

**A carving stores the symbol's id, never its glyph.** Uninstall the pack and its symbols stop
drawing, but every trunk keeps the id; install the pack again and they come back as they were.
Nothing is rewritten in the meantime.

A text piece whose font entry is gone is drawn in plain Minecraft text until the font returns, so the
message stays readable.

A file that cannot be read — not a JSON object, a symbol without `glyph`, a font without `font` — is
skipped and named in the server log. The rest of the table still loads.

## Switching the tables off

Two settings stop the tables from loading at all:

| Setting | Stops |
|---|---|
| `datapackSymbols` | every `tree_carve/symbol` file |
| `datapackFonts` | every `tree_carve/font` file |

Set them with `/treecarve config datapackSymbols false` or `/treecarve config datapackFonts false`.
The change takes effect on the next `/reload`.

Off means the table is **empty, built-ins included** — the built-ins are datapack files like any
other. Carvings already on trunks keep their ids and draw again once the table is switched back on.
