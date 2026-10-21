"""Draw every mod's spec card from one place: `extra.mod_specs` in mkdocs.base.yml.

The same facts (Minecraft version, Cobblemon range, which side, what else to install) used to be
written by hand four times per mod: hero badges, the "Get it" table, the landing chips, and pages
that disagreed with all three. Now a page carries a marker and this hook swaps it for markdown:

    <!-- mod-badges -->          the badge row of a mod's hero
    <!-- mod-spec -->            the "Get it" table of a mod's index
    <!-- mod-chips:<mod> -->     the chips of one row of the landing's mod list
    <!-- mod-tags:<mod> -->      that row's `data-tags`, which the landing's filter buttons read
    <!-- mod-compat -->          the landing's compatibility table, one row per mod

The mod of a page is its folder under docs/, as in overrides/main.html. Links are written relative to
the page, so hooks/cross_site_links.py (which runs after this one) still rewrites the ones that leave
the site. A marker for a mod without a spec is a build error, not a silent gap.
"""

import posixpath

MODRINTH = "https://modrinth.com/mod/"
CURSEFORGE = "https://www.curseforge.com/projects/"


def _rel(target: str, page) -> str:
    return posixpath.relpath(target, posixpath.dirname(page.file.src_uri) or ".")


def _dep(key: str, config, page) -> str:
    dep = config["extra"]["deps"][key]
    if "page" in dep:
        return f"[{dep['name']}]({_rel(dep['page'], page)})"
    return f"[{dep['name']}]({MODRINTH}{dep['modrinth']})"


def _deps(keys, config, page) -> str:
    return ", ".join(_dep(k, config, page) for k in keys or [])


def _spec(mod: str, config):
    specs = config["extra"].get("mod_specs", {})
    if mod not in specs:
        raise KeyError(f"mod_specs has no entry for '{mod}' (mkdocs.base.yml)")
    return specs[mod], config["extra"]["mod_versions"][mod]


def _cobblemon(spec) -> str:
    return f"Cobblemon {spec['cobblemon']}" if spec.get("cobblemon") else "No Cobblemon"


def _chips(mod: str, config, landing: bool = False) -> list[str]:
    spec, _ = _spec(mod, config)
    deps = config["extra"]["deps"]
    chips = ["Not released yet"] if spec.get("unreleased") else []
    if landing and spec["minecraft"] != "1.21.1":
        chips.append(f"MC {spec['minecraft']}")
    if spec.get("cobblemon") or not spec.get("cobblemon_note"):
        chips.append(_cobblemon(spec))
    if spec.get("side") == "client":
        chips.append("Client-only")
    if spec.get("requires"):
        chips.append("Needs " + " + ".join(deps[k]["name"].removeprefix("Cobblemon ") for k in spec["requires"]))
    return chips


def _badges(mod: str, config) -> str:
    spec, _ = _spec(mod, config)
    badges = [f"MC {v.strip()}" for v in spec["minecraft"].split("·")] + ["Fabric", "NeoForge"]
    return " ".join(f'<span class="badge">{b}</span>' for b in badges + _chips(mod, config))


def _card(mod: str, config, page) -> str:
    spec, version = _spec(mod, config)
    # A mod with no Modrinth project yet is unreleased, and its card has no "Download" row anyway.
    download = ""
    if version.get("modrinth"):
        download = f"[Modrinth]({MODRINTH}{version['modrinth']})"
        if spec.get("curseforge"):
            download += f" · [CurseForge]({CURSEFORGE}{spec['curseforge']})"
        download += f" · [What changed]({MODRINTH}{version['modrinth']}/changelog)"
    side = ("**Client only.** It goes in your own `mods/` folder; a server does not need it"
            if spec.get("side") == "client"
            else "Server **and** every player's game")
    note = spec.get("cobblemon_note")
    if spec.get("cobblemon"):
        cobblemon = f"**{spec['cobblemon']}**" + (f" — {note}" if note else "")
    else:
        cobblemon = note[0].upper() + note[1:] if note else "Not needed"
    rows = [
        ("Version", f"**{version['version']}**"),
        ("Minecraft", spec["minecraft"]),
        ("Side", side),
        ("Cobblemon", cobblemon),
    ]
    if spec.get("requires"):
        needs = _deps(spec["requires"], config, page)
        if spec.get("requires_note"):
            needs += f" {spec['requires_note']}"
        rows.append(("Also needs", needs))
    rows.append(("Fabric", _deps(spec["fabric"], config, page)))
    rows.append(("NeoForge", _deps(spec["neoforge"], config, page)))
    if spec.get("optional"):
        rows.append(("Optional", " · ".join(f"{_dep(k, config, page)}: {why}" for k, why in spec["optional"])))
    rows += list((spec.get("notes") or {}).items())
    if not spec.get("unreleased"):
        rows.insert(0, ("Download", download))
    table = "| | |\n|---|---|\n" + "\n".join(f"| **{k}** | {v} |" for k, v in rows)
    return f'<div class="mod-spec" markdown>\n\n{table}\n\n</div>'


def _compat(config, page) -> str:
    lines = ["| Mod | Cobblemon | Side | Also needs |", "|---|---|---|---|"]
    for mod, version in config["extra"]["mod_versions"].items():
        spec, _ = _spec(mod, config)
        short = version["name"].removeprefix("Cobblemon ")
        name = f"[{short}]({_rel(mod + '/index.md', page)}) <small>{version['version']}</small>"
        cobblemon = spec.get("cobblemon") or "—"
        if not spec.get("cobblemon") and spec.get("cobblemon_note") and spec.get("requires"):
            cobblemon = "via " + config["extra"]["deps"][spec["requires"][0]]["name"].removeprefix("Cobblemon ")
        side = "Client" if spec.get("side") == "client" else "Both"
        deps = config["extra"]["deps"]
        needs = ", ".join(deps[k]["name"].removeprefix("Cobblemon ") for k in spec.get("requires", [])) or "—"
        lines.append(f"| {name} | {cobblemon} | {side} | {needs} |")
    return '<div class="mod-compat" markdown>\n\n' + "\n".join(lines) + "\n\n</div>"


def on_page_markdown(markdown, page, config, files, **kwargs):
    if "<!-- mod-" not in markdown:
        return markdown
    mod = page.file.src_uri.split("/")[0]
    if "<!-- mod-badges -->" in markdown:
        markdown = markdown.replace("<!-- mod-badges -->", _badges(mod, config))
    if "<!-- mod-spec -->" in markdown:
        markdown = markdown.replace("<!-- mod-spec -->", _card(mod, config, page))
    if "<!-- mod-compat -->" in markdown:
        markdown = markdown.replace("<!-- mod-compat -->", _compat(config, page))
    for key in config["extra"]["mod_versions"]:
        marker = f"<!-- mod-chips:{key} -->"
        if marker in markdown:
            chips = " ".join(f'<span class="badge">{c}</span>' for c in _chips(key, config, landing=True))
            markdown = markdown.replace(marker, chips)
        marker = f"<!-- mod-tags:{key} -->"
        if marker in markdown:
            spec, _ = _spec(key, config)
            tags = (["client-only"] if spec.get("side") == "client" else []) + (
                [] if spec.get("cobblemon") or spec.get("cobblemon_note") else ["no-cobblemon"])
            markdown = markdown.replace(marker, " ".join(tags))
    return markdown
