"""Serve the diagrams as SVG instead of shipping a 3.4 MB renderer to every reader.

Material draws ```mermaid fences in the browser, which means pulling Mermaid.js — 3.4 MB, and it
used to come from unpkg.com — on every page that has one. Nineteen pages here do.

So the rendering happens ONCE, at authoring time, and the result is committed:

    tools/render-diagrams.mjs   renders every fence to docs/assets/diagrams/<sha1>.svg
    this hook                   swaps the fence for that SVG, inlined

Named by the hash of the diagram source, so editing a diagram simply looks up a file that does not
exist yet — and then this hook LEAVES THE FENCE ALONE and the browser renders it the old way. A
missing SVG is never a broken page, only a slower one. `mkdocs build --strict` stays green either
way, and running the renderer again picks it up.

The SVG is inlined rather than linked with <img> on purpose: Mermaid's output references Material's
own CSS variables (--md-mermaid-*), so an inlined diagram still follows the light/dark toggle. Inside
an <img> it would be sandboxed from the page and would freeze on whichever theme rendered it.
"""

import hashlib
import re
from pathlib import Path

FENCE = re.compile(r"^```mermaid\n(.*?)^```", re.MULTILINE | re.DOTALL)

_missing: set[str] = set()


def _diagrams_dir(config) -> Path:
    return Path(config["docs_dir"]) / "assets" / "diagrams"


def on_page_markdown(markdown, page, config, files, **kwargs):
    out_dir = _diagrams_dir(config)

    def swap(match: re.Match) -> str:
        source = match.group(1)
        # The init directive travels with the source, so re-colouring a diagram changes its hash and
        # asks for a re-render, exactly as editing the diagram does.
        digest = hashlib.sha1(source.strip().encode("utf-8")).hexdigest()[:16]
        svg = out_dir / f"{digest}.svg"
        if not svg.exists():
            _missing.add(f"{page.file.src_path}  ({digest})")
            return match.group(0)
        markup = svg.read_text(encoding="utf-8")
        # Strip the XML prolog: this is going inside an HTML document, not standing on its own.
        markup = re.sub(r"^<\?xml[^>]*\?>\s*", "", markup)
        markup = re.sub(r"^<!DOCTYPE[^>]*>\s*", "", markup, flags=re.IGNORECASE)
        return f'<div class="mermaid-static">\n{markup}\n</div>'

    return FENCE.sub(swap, markdown)


def on_post_build(config, **kwargs):
    if not _missing:
        return
    print(
        f"\nINFO    -  {len(_missing)} diagram(s) have no pre-rendered SVG and will be drawn in the "
        f"browser (3.4 MB of Mermaid.js). Run `node tools/render-diagrams.mjs` to fix:"
    )
    for item in sorted(_missing):
        print(f"           {item}")
