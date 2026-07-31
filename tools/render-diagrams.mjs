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
 * Mermaid is told to paint with Material's own CSS variables, which is what Material's runtime does
 * too. The SVG therefore carries `var(--md-mermaid-*)` rather than baked colours, so an inlined
 * diagram still follows the light/dark toggle instead of freezing on the theme it was rendered in.
 */
const THEME_CSS = `
.node rect, .node circle, .node ellipse, .node polygon, .node path {
  fill: var(--md-mermaid-node-bg-color);
  stroke: var(--md-mermaid-node-fg-color);
}
.edgePath .path, .flowchart-link { stroke: var(--md-mermaid-edge-color); }
.edgeLabel, .label, .nodeLabel { color: var(--md-mermaid-label-fg-color); fill: var(--md-mermaid-label-fg-color); }
.edgeLabel rect { fill: var(--md-mermaid-label-bg-color); }
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

const wanted = new Set();
let rendered = 0;
let skipped = 0;

for (const file of walk(docs)) {
	const text = readFileSync(file, "utf8");
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
		execFileSync("npx", ["--no-install", "mmdc", "-i", input, "-o", target,
			"--cssFile", join(tmp, "theme.css"), "--backgroundColor", "transparent", "--quiet"],
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
