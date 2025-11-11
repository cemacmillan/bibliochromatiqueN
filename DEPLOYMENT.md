# URL Structure & Deployment Best Practices

## Current Structure

The site is designed to work with **relative paths** throughout, which provides maximum flexibility for deployment scenarios.

### File Structure (as deployed)
```
/antitrope/bibliochromatiqueN/
  ├── index.html          # Main entry point
  ├── README.md
  ├── LICENSE.md
  ├── css/
  │   └── palette.css
  ├── palettes/
  │   ├── exchequer.html
  │   ├── exchequer.json
  │   ├── opium-den.html
  │   ├── opium-den.json
  │   └── schema.json
  └── scripts/
      ├── generate_palette
      ├── generate_index.py
      └── generate_all.py
```

### URL Paths

**Primary deployment path:**
- `antitrope.fr/antitrope/bibliochromatiqueN/` → serves `index.html`
- `antitrope.fr/antitrope/bibliochromatiqueN/palettes/exchequer.html` → palette pages

**Desired entry point:**
- `antitrope.fr/chromatique` → should redirect to the main library

## Best Practice Recommendation

### ✅ Recommended Approach: Server-Side Redirect

**Why this is best:**
1. **Relative paths work everywhere** - All internal links use relative paths (`../css/palette.css`, `palettes/exchequer.html`), so they work regardless of the base path
2. **No code changes needed** - The generated HTML doesn't need to know about the deployment structure
3. **Flexible** - Easy to change redirects without regenerating content
4. **SEO-friendly** - Proper HTTP redirects preserve link equity

### Implementation

**Apache (.htaccess):**
```apache
# Redirect /chromatique to the library
Redirect 301 /chromatique /antitrope/bibliochromatiqueN/

# Optional: redirect trailing slash variations
RedirectMatch 301 ^/chromatique/?$ /antitrope/bibliochromatiqueN/
```

**Nginx:**
```nginx
location = /chromatique {
    return 301 /antitrope/bibliochromatiqueN/;
}

location = /chromatique/ {
    return 301 /antitrope/bibliochromatiqueN/;
}
```

### Alternative: Base Path Configuration (if needed)

If you need to support both paths simultaneously without redirects, you could add a base path configuration to the generators, but this adds complexity and is generally unnecessary.

## Path Resolution

All paths in generated HTML are relative:
- `index.html` → `css/palette.css` (same directory level)
- `palettes/exchequer.html` → `../css/palette.css` (one level up)
- `index.html` → `palettes/exchequer.html` (subdirectory)

This works correctly whether accessed via:
- `/antitrope/bibliochromatiqueN/`
- `/chromatique/` (after redirect)
- Any other base path

## Future Considerations

When the library moves to its own host:
1. **No code changes needed** - Relative paths continue to work
2. **Update redirect** - Point `/chromatique` to the new domain
3. **Update schema.json** - Already fixed to use `bibliochromatiqueN` in the `$id` field

## Generation Scripts

- `scripts/generate_palette <slug>` - Generate individual palette page
- `scripts/generate_index.py` - Generate index.html listing all palettes
- `scripts/generate_all.py` - Generate all palettes + index (batch operation)

Run `scripts/generate_all.py` after adding new palettes to regenerate all static content.

