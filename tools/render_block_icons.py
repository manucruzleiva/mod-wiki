"""Render block recipe icons the way the game's inventory draws them: the 3D model, not a flat texture.

A block item in an inventory slot is its model drawn at the `gui` display transform (rotation
[30, 225, 0], scale 0.625); there is no flat picture of it anywhere in the game. The recipe grids used
to show the bare 16x16 texture for planks, wool, sponge and slabs, next to 3D chest and furniture
renders, and read as broken icons. This draws each model's boxes through that same transform, with a
depth buffer and vanilla's per-face inventory shading, at 2x (a 16px slot is a 32px icon here).

It also renders the slab in every wood and the Picnic table in every wool x wood pair, so the cycling
recipe slots show the item you actually get instead of oak for everything.

Sources are in tools/block_textures/: flat vanilla textures, the 2x wool/planks strips, and Picnic's
table cloths (copied from cobblemon-picnic art/assets/cobblemon_picnic/textures/block/table/).
Outputs go to docs/assets/items/. Re-run after adding a texture:

    python3 tools/render_block_icons.py
"""
import math
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "block_textures"
OUT = ROOT / "docs" / "assets" / "items"

SIZE = 32          # icon px; the chest and furniture renders are 32x32
PX = 2 * 0.625     # icon px per model unit: 2x a 16px slot, times the gui display scale
SHADE = {"up": 1.0, "left": 0.80, "right": 0.62, "down": 0.5}  # vanilla's inventory lighting

# Vanilla order, the order the strips and the Picnic recipes cycle through.
WOOLS = ["white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray",
         "light_gray", "cyan", "purple", "blue", "brown", "green", "red", "black"]
WOODS = ["acacia", "bamboo", "birch", "cherry", "crimson", "dark_oak", "jungle", "mangrove",
         "oak", "spruce", "warped"]
NORMALS = {"up": (0, 1, 0), "down": (0, -1, 0), "north": (0, 0, -1), "south": (0, 0, 1),
           "west": (-1, 0, 0), "east": (1, 0, 0)}


def _rotation():
    """Model space -> view space for the gui transform: Rx(30) . Ry(225)."""
    a, b = math.radians(-30), math.radians(225)  # GUI space has y down, so the tilt flips sign here
    rx = np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])
    ry = np.array([[math.cos(b), 0, math.sin(b)], [0, 1, 0], [-math.sin(b), 0, math.cos(b)]])
    return rx @ ry


ROT = _rotation()


def _faces(lo, hi):
    """Each face of a box: (name, corner at uv origin, u edge, v edge, default uv), model units."""
    (x1, y1, z1), (x2, y2, z2) = lo, hi
    dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
    return [
        ("up",    (x1, y2, z1), (dx, 0, 0),  (0, 0, dz),  (x1, z1, x2, z2)),
        ("down",  (x1, y1, z2), (dx, 0, 0),  (0, 0, -dz), (x1, 16 - z2, x2, 16 - z1)),
        ("north", (x2, y2, z1), (-dx, 0, 0), (0, -dy, 0), (16 - x2, 16 - y2, 16 - x1, 16 - y1)),
        ("south", (x1, y2, z2), (dx, 0, 0),  (0, -dy, 0), (x1, 16 - y2, x2, 16 - y1)),
        ("west",  (x1, y2, z1), (0, 0, dz),  (0, -dy, 0), (z1, 16 - y2, z2, 16 - y1)),
        ("east",  (x2, y2, z2), (0, 0, -dz), (0, -dy, 0), (16 - z2, 16 - y2, 16 - z1, 16 - y1)),
    ]


def render(boxes):
    """boxes: [(from, to, {face: texture | (texture, uv)})] in model units -> SIZE x SIZE RGBA."""
    color = np.zeros((SIZE, SIZE, 4), np.uint8)
    depth = np.full((SIZE, SIZE), np.inf)  # the viewer looks down +z: smaller z is nearer
    ys, xs = np.mgrid[0:SIZE, 0:SIZE] + 0.5
    for lo, hi, textures in boxes:
        for name, origin, u, v, default_uv in _faces(lo, hi):
            if name not in textures:
                continue
            tex, uv = textures[name] if isinstance(textures[name], tuple) else (textures[name], default_uv)
            o = ROT @ (np.array(origin, float) - 8)
            eu, ev = ROT @ np.array(u, float), ROT @ np.array(v, float)
            normal = ROT @ np.array(NORMALS[name], float)
            if normal[2] >= -1e-9:  # facing away from the viewer
                continue
            # Pixel = centre + PX * (o + s*eu + t*ev), y flipped; invert for (s, t) at every pixel.
            inv = np.linalg.inv(np.array([[eu[0], ev[0]], [-eu[1], -ev[1]]]) * PX)
            px, py = xs - (SIZE / 2 + o[0] * PX), ys - (SIZE / 2 - o[1] * PX)
            s = inv[0, 0] * px + inv[0, 1] * py
            t = inv[1, 0] * px + inv[1, 1] * py
            z = o[2] + s * eu[2] + t * ev[2]
            eps = 1e-6  # shared edges belong to both faces, so no seam opens between them
            hit = (s >= -eps) & (s <= 1 + eps) & (t >= -eps) & (t <= 1 + eps) & (z < depth)
            arr = np.asarray(tex)
            h, w = arr.shape[:2]
            u1, v1, u2, v2 = uv
            tu = np.clip(np.floor((u1 + s * (u2 - u1)) * w / 16).astype(int), 0, w - 1)
            tv = np.clip(np.floor((v1 + t * (v2 - v1)) * h / 16).astype(int), 0, h - 1)
            texel = arr[tv, tu].astype(float)
            hit &= texel[..., 3] > 0  # cutout
            light = name if name in ("up", "down") else "left" if normal[0] < 0 else "right"
            texel[..., :3] *= SHADE[light]
            color[hit] = texel[hit].astype(np.uint8)
            depth[hit] = z[hit]
    return Image.fromarray(color, "RGBA")


def block(texture, height=16):
    """A full block, or a bottom slab with height=8, with one texture on every face."""
    return render([((0, 0, 0), (16, height, 16), {f: texture for f in NORMALS})])


def table(cloth, planks):
    """Picnic's table item: cobblemon_picnic block/template/table_full_split, four legs and a top."""
    sides = {f: planks for f in ("north", "east", "south", "west", "down")}
    legs = [((x, 0, z), (x + 2, 13, z + 2), sides) for x in (0, 14) for z in (0, 14)]
    return render(legs + [((0, 13, 0), (16, 16, 16), dict(sides, up=(cloth, (2, 12, 0, 8))))])


def load(name):
    return Image.open(SRC / name).convert("RGBA")


def frames(name, names):
    """A 2x strip of 32px frames -> {name: 16x16 texture}."""
    src = load(name)
    small = src.resize((src.width // 2, 16), Image.NEAREST)
    assert small.width == 16 * len(names), name
    return {n: small.crop((i * 16, 0, i * 16 + 16, 16)) for i, n in enumerate(names)}


def save_strip(icons, out):
    strip = Image.new("RGBA", (len(icons) * SIZE, SIZE), (0, 0, 0, 0))
    for i, icon in enumerate(icons):
        strip.paste(icon, (i * SIZE, 0))
    strip.save(OUT / "strips" / out)


def main():
    for name in ("oak_planks", "apricorn_planks", "sponge", "wet_sponge", "white_wool"):
        block(load(f"{name}.png")).save(OUT / f"{name}.png")
    block(load("oak_planks.png"), height=8).save(OUT / "oak_slab.png")

    wool = frames("wool_strip.png", WOOLS)
    planks = frames("planks_strip.png", WOODS)
    save_strip([block(wool[c]) for c in WOOLS], "wool.png")
    save_strip([block(planks[w]) for w in WOODS], "planks.png")
    save_strip([block(planks[w], height=8) for w in WOODS], "slab.png")
    # 16 and 11 are coprime, so stepping wool and wood together visits all 176 pairs exactly once:
    # frame i is wool i % 16 on wood i % 11, the pair the two cycling ingredient slots show.
    cloths = {c: load(f"table/{c}.png") for c in WOOLS}
    pairs = [(WOOLS[i % 16], WOODS[i % 11]) for i in range(len(WOOLS) * len(WOODS))]
    save_strip([table(cloths[c], planks[w]) for c, w in pairs], "table.png")


if __name__ == "__main__":
    main()
