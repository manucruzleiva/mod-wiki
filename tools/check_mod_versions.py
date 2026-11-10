"""Keep the wiki describing what each mod actually ships.

`extra.mod_versions` in mkdocs.base.yml says which version of a mod its section documents. The wiki
went wrong twice the same way: the number was bumped and the pages were not rewritten, so a section
said 3.0.0 and described 2.5.4. This script is the guard on both ends:

    bumps <base> <head>   fails when a mod's version changes between two commits and nothing under
                          docs/<mod>/ does. Run by checks.yml on every pull request and push.
    main                  compares every documented version with the mod_version on the default
                          branch of the mod's repo (`repo` in mod_versions; the wiki follows main,
                          not Modrinth) and prints one tab-separated line per mod it could check:
                          stale    <mod>  <name>  <documented>  <main>  <repo>
                          current  <mod>  <name>
                          Run daily by modrinth-watch.yml, which keeps one issue per stale mod. A
                          mod it could not read prints an error instead and fails the run; its
                          issue stays as is. Needs GH_TOKEN able to read the (private) mod repos.

Standard library only, so the workflows need no pip install. mkdocs.base.yml is read with a regex,
not a YAML loader: it carries !!python tags that only MkDocs resolves, and the mod_versions block is
one flow mapping per line, which is what this reads.
"""

import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

BASE = "mkdocs.base.yml"
ENTRY = re.compile(r"^ {4}([a-z0-9-]+):\s*\{(.*)\}\s*$")
FIELD = re.compile(r"(\w+):\s*([^,]+?)\s*(?=,\s*\w+:|$)")
OWNER = "manucruzleiva"
MOD_VERSION = re.compile(r"^(?:mod_version|modVersion)\s*=\s*(\S+)", re.M)


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


def main_version(repo: str, token: str) -> str | None:
    # No `ref`: the contents API answers from the repo's default branch, main or master alike.
    req = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{repo}/contents/gradle.properties",
        headers={"Accept": "application/vnd.github.raw+json", "Authorization": f"Bearer {token}",
                 "User-Agent": "mod-wiki-staleness-check"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        m = MOD_VERSION.search(r.read().decode("utf-8"))
    return m.group(1) if m else None


def main_branch() -> int:
    with open(BASE, encoding="utf-8") as f:
        mods = mod_versions(f.read())
    token, missed = os.environ.get("GH_TOKEN", ""), []
    for mod, entry in mods.items():
        repo, documented = entry.get("repo"), entry.get("version", "")
        if not repo:
            print(f"{mod}: no repo, skipped", file=sys.stderr)
            continue
        try:
            latest = main_version(repo, token)
        except urllib.error.HTTPError as e:
            # 404 here is almost always the token: the mod repos are private.
            print(f"::error::{mod}: GitHub answered {e.code} for {OWNER}/{repo}", file=sys.stderr)
            missed.append(mod)
            continue
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"::error::{mod}: GitHub unreachable ({e})", file=sys.stderr)
            missed.append(mod)
            continue
        if latest is None:
            print(f"::error::{mod}: no mod_version/modVersion in {repo}/gradle.properties", file=sys.stderr)
            missed.append(mod)
        elif key(latest) != key(documented):
            print("\t".join(["stale", mod, entry.get("name", mod), documented, latest, repo]))
        else:
            print("\t".join(["current", mod, entry.get("name", mod)]))
    # A mod that could not be checked fails the run, so it never goes quiet the way #142 did.
    return 1 if missed else 0


if __name__ == "__main__":
    if sys.argv[1:2] == ["bumps"] and len(sys.argv) == 4:
        sys.exit(bumps(sys.argv[2], sys.argv[3]))
    if sys.argv[1:] == ["main"]:
        sys.exit(main_branch())
    sys.exit(__doc__)
