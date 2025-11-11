#!/usr/bin/env python3
"""Generate all palette pages and index.html."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
PALETTE_DIR = ROOT / "palettes"


def find_palette_slugs() -> list[str]:
    """Find all palette JSON files."""
    slugs = []
    for json_file in PALETTE_DIR.glob("*.json"):
        if json_file.name != "schema.json":
            slugs.append(json_file.stem)
    return sorted(slugs)


def main() -> int:
    """Generate all palettes and index."""
    generate_palette = SCRIPTS_DIR / "generate_palette"
    generate_index = SCRIPTS_DIR / "generate_index.py"
    
    if not generate_palette.exists():
        print(f"Error: {generate_palette} not found", file=sys.stderr)
        return 1
    
    if not generate_index.exists():
        print(f"Error: {generate_index} not found", file=sys.stderr)
        return 1
    
    # Generate all palette pages
    slugs = find_palette_slugs()
    if not slugs:
        print("No palettes found.", file=sys.stderr)
        return 1
    
    errors = []
    for slug in slugs:
        result = subprocess.run(
            [str(generate_palette), slug],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            errors.append(f"{slug}: {result.stderr.strip()}")
        else:
            print(result.stdout.strip())
    
    # Generate index
    result = subprocess.run(
        [sys.executable, str(generate_index)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        errors.append(f"index: {result.stderr.strip()}")
    else:
        print(result.stdout.strip())
    
    if errors:
        print("\nErrors:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    
    print(f"\n✓ Generated {len(slugs)} palette(s) and index.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

