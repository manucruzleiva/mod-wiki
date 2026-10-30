"""Render the recipe icons of full blocks as the game draws them: a 3D cube, not a flat texture.

A block item in an inventory slot is its model rendered at `rotation: [30, 225, 0]`; there is no flat
picture of it anywhere in the game. The recipe grids used to show the bare 16x16 texture for planks,
wool, sponge and slabs, which sat next to the 3D chest and furniture renders and read as a different,
broken kind of icon. This projects each texture onto an isometric cube instead, shaded per face the
way vanilla shades it (same construction as cobblemon-hms art/gen_discs.py `iso_cube`).

Sources are the flat textures in tools/block_textures/; outputs go to docs/assets/items/. Re-run after
adding a texture:

    python3 tools/render_block_icons.py
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "block_textures"
OUT = ROOT / "docs" / "assets" / "items"

SIZE = 32  # the chest and furniture renders are 32x32; a texel lands on ~one pixel
SHADE = (1.0, 0.80, 0.62)  # top, left, right — vanilla's inventory lighting


def _face(texture, affine, polygon, shade):
    # Edge pixels sample a hair outside 0..16; a 1px clamped border keeps them from coming out transparent.
    padded = Image.fromarray(np.pad(np.asarray(texture), ((1, 1), (1, 1), (0, 0)), mode="edge"))
    a, b, c, d, e, f = affine
    warped = padded.transform((SIZE, SIZE), Image.AFFINE, (a, b, c + 1, d, e, f + 1), Image.NEAREST)
    if shade < 1.0:
        r, g, b, a = warped.split()
        lut = [int(i * shade) for i in range(256)]
        warped = Image.merge("RGBA", (r.point(lut), g.point(lut), b.point(lut), a))
    mask = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(mask).polygon(polygon, fill=255)
    return warped, Image.composite(warped.getchannel("A"), Image.new("L", (SIZE, SIZE), 0), mask)


def block(texture, height=1.0):
    """A 16x16 texture as a block `height` blocks tall (0.5 = slab), in a SIZE x SIZE icon."""
    S = float(SIZE)
    drop = (1 - height) * S / 2  # a slab's top sits lower; its sides show the texture's bottom half
    side = texture.copy()
    side.paste((0, 0, 0, 0), (0, 0, 16, round(16 * (1 - height))))
    out = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    for tex, affine, polygon, shade in (
        # texture, affine (dest -> source), the polygon it is clipped to, brightness
        (side, (32 / S, 0.0, 0.0, -16 / S, 32 / S, -8.0),
         [(0, S / 4), (S / 2, S / 2), (S / 2, S), (0, S * 3 / 4)], SHADE[1]),
        (side, (32 / S, 0.0, -16.0, 16 / S, 32 / S, -24.0),
         [(S / 2, S / 2), (S, S / 4), (S, S * 3 / 4), (S / 2, S)], SHADE[2]),
        (texture, (16 / S, -32 / S, 8.0 + 32 * drop / S, 16 / S, 32 / S, -8.0 - 32 * drop / S),
         [(S / 2, drop), (S, S / 4 + drop), (S / 2, S / 2 + drop), (0, S / 4 + drop)], SHADE[0]),
    ):
        warped, mask = _face(tex, affine, polygon, shade)
        out.paste(warped, (0, 0), mask)
    return out


def load(name):
    return Image.open(SRC / name).convert("RGBA")


def strip(name, out):
    """A cycling-slot strip: 32px frames of 2x textures in, 32px frames of rendered blocks out."""
    src = load(name)
    n = src.width // 32
    textures = src.resize((n * 16, 16), Image.NEAREST)
    result = Image.new("RGBA", (n * SIZE, SIZE), (0, 0, 0, 0))
    for i in range(n):
        result.paste(block(textures.crop((i * 16, 0, i * 16 + 16, 16))), (i * SIZE, 0))
    result.save(OUT / "strips" / out)


def main():
    for name in ("oak_planks", "apricorn_planks", "sponge", "wet_sponge", "white_wool"):
        block(load(f"{name}.png")).save(OUT / f"{name}.png")
    block(load("oak_planks.png"), height=0.5).save(OUT / "oak_slab.png")
    strip("wool_strip.png", "wool.png")
    strip("planks_strip.png", "planks.png")


if __name__ == "__main__":
    main()
