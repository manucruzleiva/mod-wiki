"""Keep the wiki describing what each mod actually ships.

`extra.mod_versions` in mkdocs.base.yml says which version of a mod its section documents. The wiki
went wrong twice the same way: the number was bumped and the pages were not rewritten, so a section
said 3.0.0 and described 2.5.4. This script is the guard on both ends:

    bumps <base> <head>   fails when a mod's version changes between two commits and nothing under
                          docs/<mod>/ does. Run by checks.yml on every pull request and push.
    modrinth              compares every documented version with the newest release on Modrinth and
                          prints one tab-separated line per mod it could check:
                          stale    <mod>  <name>  <documented>  <modrinth>  <slug>
                          current  <mod>  <name>
                          Run daily by modrinth-watch.yml, which keeps one issue per stale mod. A
                          mod Modrinth did not answer for prints nothing, so its issue stays as is.

Standard library only, so the workflows need no pip install. mkdocs.base.yml is read with a regex,
not a YAML loader: it carries !!python tags that only MkDocs resolves, and the mod_versions block is
one flow mapping per line, which is what this reads.
"""

import json
import re
import subprocess
import sys
import urllib.error
import urllib.request

BASE = "mkdocs.base.yml"
ENTRY = re.compile(r"^ {4}([a-z0-9-]+):\s*\{(.*)\}\s*$")
FIELD = re.compile(r"(\w+):\s*([^,]+?)\s*(?=,\s*\w+:|$)")
SEMVER = re.compile(r"\d+\.\d+\.\d+")


def mod_versions(text: str) -> dict[str, dict[str, str]]:
    mods, inside = {}, False
    for line in text.splitlines():
        if re.match(r"^ {2}mod_versions:\s*$", line):
            inside = True
            continue
        if inside:
            m = ENTRY.match(line)
            if m:
                mods[m.group(1)] = dict(FIELD.findall(m.group(2)))
            elif line.strip() and not line.lstrip().startswith("#"):
                break
    return mods


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def bumps(base: str, head: str) -> int:
    before = mod_versions(git("show", f"{base}:{BASE}"))
    after = mod_versions(git("show", f"{head}:{BASE}"))
    bad = []
    for mod, entry in after.items():
        old, new = before.get(mod, {}).get("version"), entry.get("version")
        if old == new:
            continue
        touched = git("diff", "--name-only", base, head, "--", f"docs/{mod}/").strip()
        print(f"{mod}: {old} -> {new}, " + ("pages changed too" if touched else "NO page changed"))
        if not touched:
            bad.append(mod)
    for mod in bad:
        print(
            f"::error file={BASE}::{after[mod].get('name', mod)} moved to {after[mod]['version']} "
            f"but nothing under docs/{mod}/ changed. Bump the number in the same change that "
            "rewrites the pages for that release, so the label never runs ahead of the content."
        )
    return 1 if bad else 0


def key(version: str) -> tuple[int, ...]:
    return tuple(int(x) for x in version.split("-")[0].split("."))


def newest_release(slug: str) -> str | None:
    req = urllib.request.Request(
        f"https://api.modrinth.com/v2/project/{slug}/version",
        headers={"User-Agent": "manucruzleiva/mod-wiki (wiki staleness check)"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        versions = [v for v in json.load(r) if v.get("version_type") == "release"]
    if not versions:
        return None
    v = max(versions, key=lambda v: v["date_published"])
    # version_number can carry the Minecraft version and the loader (1.2.119+1.21.1-fabric); the
    # mod's own number is the x.y.z that is not one of the game versions it lists.
    games = set(v.get("game_versions", []))
    found = [s for s in SEMVER.findall(v["version_number"]) if s not in games]
    return found[0] if found else None


def modrinth() -> int:
    with open(BASE, encoding="utf-8") as f:
        mods = mod_versions(f.read())
    for mod, entry in mods.items():
        slug, documented = entry.get("modrinth"), entry.get("version", "")
        if not slug:
            print(f"{mod}: no modrinth slug, skipped", file=sys.stderr)
            continue
        try:
            latest = newest_release(slug)
        except urllib.error.HTTPError as e:
            print(f"::warning::{mod}: Modrinth answered {e.code} for '{slug}'", file=sys.stderr)
            continue
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"::warning::{mod}: Modrinth unreachable ({e})", file=sys.stderr)
            continue
        if latest is None:
            print(f"{mod}: no release on Modrinth yet", file=sys.stderr)
        elif key(latest) != key(documented):
            print("\t".join(["stale", mod, entry.get("name", mod), documented, latest, slug]))
        else:
            print("\t".join(["current", mod, entry.get("name", mod)]))
    return 0


if __name__ == "__main__":
    if sys.argv[1:2] == ["bumps"] and len(sys.argv) == 4:
        sys.exit(bumps(sys.argv[2], sys.argv[3]))
    if sys.argv[1:] == ["modrinth"]:
        sys.exit(modrinth())
    sys.exit(__doc__)
