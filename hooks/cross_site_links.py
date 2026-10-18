"""Keep links between the wiki's sub-sites working, while authors write plain relative links.

Each mod builds as its own site (mkdocs.<mod>.yml) and the landing pages as another
(mkdocs.landing.yml). All of them keep `docs_dir: docs` and drop what is not theirs with
`exclude_docs`, so `../nuzlocke/commands.md` written in a Routes page points at a file that exists
on disk but is not in the Routes build. MkDocs only logs that at INFO, so `--strict` stays green and
the link ships as a 404.

So this hook rewrites exactly those links — the target exists under docs/ but is excluded from this
build — into the absolute URL of the site that does publish it:

    <wiki.url><mod>/<wiki.alias>/<page>     a page or file under a mod's folder
    <wiki.url><page>                        anything else, which is the landing site

Authors keep writing `[x](../nuzlocke/commands.md)`, the combined build (mkdocs.yml, which has no
`wiki_site`) is left untouched, and the URL layout lives in `extra.wiki` and nowhere else.

A mod site also gets an `index.html` at its root: docs/index.md belongs to the landing, so without it
`<mod>/<version>/` itself would be a 404 and the mod's home sits one folder down at `<mod>/`.
"""

import posixpath
import re
from pathlib import Path

# The target of an inline link or image: `](target)` or `](target "title")`. Matching from the
# closing bracket means a logo wrapped in a link, `[![](logo.png)](index.md)`, has both rewritten.
LINK = re.compile(r'\]\(([^)\s]+)((?:\s+"[^"]*")?)\)')

LANDING = "landing"


def _site(config) -> str | None:
    return config["extra"].get("wiki_site")


def _url_for(uri: str, config) -> str:
    wiki = config["extra"]["wiki"]
    top = uri.split("/", 1)[0]
    base = wiki["url"]
    if top in config["extra"]["mod_versions"]:
        base += f"{top}/{wiki['alias']}/"
    if not uri.endswith(".md"):
        return base + uri
    stem = uri[: -len(".md")]
    if posixpath.basename(stem) == "index":
        return base + posixpath.dirname(stem) + ("/" if "/" in stem else "")
    return base + (stem + "/" if config["use_directory_urls"] else stem + ".html")


def on_page_markdown(markdown, page, config, files, **kwargs):
    if _site(config) is None:
        return markdown
    docs_dir = Path(config["docs_dir"])
    page_dir = posixpath.dirname(page.file.src_uri)

    def rewrite(match: re.Match) -> str:
        target, title = match.group(1), match.group(2)
        path, _, fragment = target.partition("#")
        if not path or path.startswith("/") or ":" in path:
            return match.group(0)
        uri = posixpath.normpath(posixpath.join(page_dir, path))
        if uri.startswith(".."):
            return match.group(0)
        in_build = files.get_file_from_path(uri)
        if in_build is not None and not in_build.inclusion.is_excluded():
            return match.group(0)
        # A target that does not exist at all stays as written, so MkDocs reports it as usual.
        if not (docs_dir / uri).is_file():
            return match.group(0)
        url = _url_for(uri, config) + (f"#{fragment}" if fragment else "")
        return f"]({url}{title})"

    return LINK.sub(rewrite, markdown)


def on_post_build(config, **kwargs):
    site = _site(config)
    if site is None or site == LANDING:
        return
    index = Path(config["site_dir"]) / "index.html"
    if index.exists():
        return
    index.write_text(
        "<!doctype html>\n<meta charset=\"utf-8\">\n"
        f"<meta http-equiv=\"refresh\" content=\"0; url={site}/\">\n"
        f"<link rel=\"canonical\" href=\"{site}/\">\n"
        f"<a href=\"{site}/\">{config['site_name']}</a>\n",
        encoding="utf-8",
    )
