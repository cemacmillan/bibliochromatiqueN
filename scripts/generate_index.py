#!/usr/bin/env python3
"""Generate index.html listing all palettes."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
PALETTE_DIR = ROOT / "palettes"
CSS_PATH = ROOT / "css" / "palette.css"
OUTPUT_PATH = ROOT / "index.html"


def load_palette(slug: str) -> dict | None:
    """Load palette JSON, return None if not found."""
    path = PALETTE_DIR / f"{slug}.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, KeyError):
        return None


def find_all_palettes() -> list[dict]:
    """Find all palette JSON files and load them."""
    palettes = []
    for json_file in PALETTE_DIR.glob("*.json"):
        if json_file.name == "schema.json":
            continue
        slug = json_file.stem
        palette = load_palette(slug)
        if palette:
            palettes.append(palette)
    # Sort by name for consistent ordering
    palettes.sort(key=lambda p: p.get("name", "").lower())
    return palettes


def generate_palette_card(palette: dict) -> str:
    """Generate HTML card for a palette."""
    name = palette.get("name", "Unnamed")
    slug = palette.get("slug", "")
    description = palette.get("description", "")
    metadata = palette.get("metadata", {})
    author = metadata.get("author") or metadata.get("creator", "Unknown")
    created = metadata.get("created", "")
    colors = palette.get("colors", [])
    
    # Get paper color for background
    paper_color = "#f8f8f6"  # default
    for color in colors:
        if color.get("role") == "paper":
            paper_color = color.get("hex", paper_color)
            break
    
    # Get a few accent colors for preview
    accent_colors = [c for c in colors if c.get("role") in ("accent", "highlight")][:4]
    if not accent_colors:
        accent_colors = colors[:4]
    
    swatches_html = "".join(
        f'<span class="swatch-preview" style="background: {c.get("hex", "#000")};" '
        f'aria-label="{c.get("name", "")}" title="{c.get("name", "")}"></span>'
        for c in accent_colors
    )
    
    created_str = f"<time>{created}</time>" if created else ""
    
    return f"""      <article class="palette-card">
        <div class="palette-preview" style="background: {paper_color};">
          <div class="swatch-group">{swatches_html}</div>
        </div>
        <div class="palette-info">
          <h2><a href="palettes/{slug}.html">{name}</a></h2>
          <p class="description">{description}</p>
          <div class="palette-meta">
            <span><strong>Author:</strong> {author}</span>
            {created_str and f'<span>{created_str}</span>'}
            <span><strong>Colors:</strong> {len(colors)}</span>
          </div>
        </div>
      </article>"""


def generate_index() -> str:
    """Generate the index.html content."""
    palettes = find_all_palettes()
    
    if not palettes:
        return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Bibliothèque Chromatique N.</title>
    <link rel="stylesheet" href="css/palette.css" />
  </head>
  <body>
    <main>
      <header>
        <h1>🖋️ Bibliothèque Chromatique N.</h1>
        <p><em>The Chromatic Library N.</em></p>
      </header>
      <p>No palettes found.</p>
    </main>
  </body>
</html>"""
    
    palette_cards = "\n".join(generate_palette_card(p) for p in palettes)
    
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Bibliothèque Chromatique N. — The Chromatic Library</title>
    <meta name="description" content="A free, mechanical library of color systems for art, design, and reflection. Every color defined by formula and parameter." />
    <link rel="stylesheet" href="css/palette.css" />
  </head>
  <body>
    <main>
      <header>
        <h1>🖋️ Bibliothèque Chromatique N.</h1>
        <p><em>The Chromatic Library N.</em></p>
        <p>A free, mechanical library of color systems for art, design, and reflection.<br />
        Every color here is defined by <strong>formula and parameter</strong>, not taste alone:<br />
        the hue is <em>generated</em>, not <em>declared</em>.</p>
      </header>

      <section class="palette-grid" aria-label="Available color palettes">
{palette_cards}
      </section>

      <footer>
        <p>Generated on <time>{datetime.now().astimezone().isoformat(timespec="minutes")}</time>.</p>
        <p><a href="README.md">Documentation</a> | <a href="LICENSE.md">License</a></p>
      </footer>
    </main>
  </body>
</html>"""


def main() -> int:
    """Generate index.html."""
    try:
        html = generate_index()
        OUTPUT_PATH.write_text(html, encoding="utf-8")
        print(f"✓ Generated {OUTPUT_PATH.relative_to(ROOT)}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

