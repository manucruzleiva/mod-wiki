// Renders every ```mermaid fence in docs/ to docs/assets/diagrams/<sha1>.svg, once, so readers do
// not have to download a 3.4 MB renderer to look at a flowchart. hooks/prerender_mermaid.py inlines
// the result at build time and falls back to browser rendering for anything not rendered yet.
//
//   npm install --no-save @mermaid-js/mermaid-cli
//   node tools/render-diagrams.mjs
//
// Only missing hashes are rendered, so re-running it after editing one diagram costs one render.
// Pass --prune to also delete SVGs no diagram points at any more.

import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { mkdirSync, readFileSync, readdirSync, writeFileSync, existsSync, unlinkSync, rmSync } from "node:fs";
import { join, dirname, relative } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const docs = join(root, "docs");
const outDir = join(docs, "assets", "diagrams");
const tmp = join(root, ".diagram-tmp");

const FENCE = /^```mermaid\n([\s\S]*?)^```/gm;

/**
 * The text is set in Inter, the site's own font, so the label boxes are measured at render time in the
 * font the reader sees them in; measured in Mermaid's default font they clipped the last letter.
 *
 * Mermaid is told to paint with Material's own CSS variables, which is what Material's runtime does
 * too. The SVG therefore carries `var(--md-mermaid-*)` rather than baked colours, so an inlined
 * diagram still follows the light/dark toggle instead of freezing on the theme it was rendered in.
 */
const THEME_CSS = `
#my-svg, #my-svg .label, #my-svg .nodeLabel, #my-svg .edgeLabel, #my-svg foreignObject * {
  font-family: Inter, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
}
#my-svg .node rect, #my-svg .node circle, #my-svg .node ellipse, #my-svg .node polygon, #my-svg .node path {
  fill: var(--md-mermaid-node-bg-color) !important;
  stroke: var(--md-mermaid-node-fg-color) !important;
  stroke-width: 1.5px !important;
}
#my-svg .node rect { rx: 9px; ry: 9px; }
#my-svg .edgePath .path, #my-svg .flowchart-link { stroke: var(--md-mermaid-edge-color) !important; stroke-width: 1.6px; }
#my-svg .marker, #my-svg marker path { fill: var(--md-mermaid-edge-color) !important; stroke: var(--md-mermaid-edge-color) !important; }
#my-svg .edgeLabel, #my-svg .label, #my-svg .nodeLabel { color: var(--md-mermaid-label-fg-color) !important; fill: var(--md-mermaid-label-fg-color) !important; }
#my-svg .edgeLabel rect, #my-svg .edgeLabel p, #my-svg .labelBkg { fill: var(--md-mermaid-label-bg-color) !important; background: var(--md-mermaid-label-bg-color) !important; }
`;

function walk(dir) {
	const out = [];
	for (const entry of readdirSync(dir, { withFileTypes: true })) {
		const full = join(dir, entry.name);
		if (entry.isDirectory()) {
			out.push(...walk(full));
		} else if (entry.name.endsWith(".md")) {
			out.push(full);
		}
	}
	return out;
}

mkdirSync(outDir, { recursive: true });
mkdirSync(tmp, { recursive: true });
writeFileSync(join(tmp, "theme.css"), THEME_CSS);
// Mermaid sizes each label box by measuring the text in its configured font, not in the CSS above.
const FONT = 'Inter, "Segoe UI", Roboto, Helvetica, Arial, sans-serif';
writeFileSync(join(tmp, "config.json"), JSON.stringify({ fontFamily: FONT, themeVariables: { fontFamily: FONT } }));

const wanted = new Set();
let rendered = 0;
let skipped = 0;

for (const file of walk(docs)) {
	// MkDocs normaliza los finales de linea antes de que el hook vea el markdown, asi que un archivo
	// con CRLF hashea distinto aca que alla y su diagrama quedaba sin renderizar para siempre.
	const text = readFileSync(file, "utf8").replace(/\r\n/g, "\n");
	for (const match of text.matchAll(FENCE)) {
		const source = match[1].trim();
		const digest = createHash("sha1").update(source, "utf8").digest("hex").slice(0, 16);
		wanted.add(`${digest}.svg`);
		const target = join(outDir, `${digest}.svg`);
		if (existsSync(target)) {
			skipped++;
			continue;
		}
		const input = join(tmp, `${digest}.mmd`);
		writeFileSync(input, source + "\n");
		console.log(`rendering ${digest}  <- ${relative(root, file)}`);
		// MMDC_PUPPETEER_CONFIG: a puppeteer config for mmdc's -p, e.g. to point it at an installed
		// Chromium or run it without the sandbox in a container.
		const puppeteer = process.env.MMDC_PUPPETEER_CONFIG ? ["-p", process.env.MMDC_PUPPETEER_CONFIG] : [];
		execFileSync("npx", ["--no-install", "mmdc", "-i", input, "-o", target, ...puppeteer,
			"--cssFile", join(tmp, "theme.css"), "--configFile", join(tmp, "config.json"), "--backgroundColor", "transparent", "--quiet"],
			{ stdio: "inherit", shell: process.platform === "win32" });
		rendered++;
	}
}

if (process.argv.includes("--prune")) {
	for (const name of readdirSync(outDir)) {
		if (name.endsWith(".svg") && !wanted.has(name)) {
			unlinkSync(join(outDir, name));
			console.log(`pruned ${name}`);
		}
	}
}

rmSync(tmp, { recursive: true, force: true });
console.log(`\n${rendered} rendered, ${skipped} already there, ${wanted.size} diagram(s) total.`);
