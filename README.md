# 🖋️ Bibliothèque Chromatique N.  
### *The Chromatic Library N.*

A free, mechanical library of color systems for art, design, and reflection.  
Every color here is defined by **formula and parameter**, not taste alone:  
the hue is *generated*, not *declared*.  

Born under the Antitrope project, this library exists to preserve the craft of color naming and composition as an act of *tekne* — a dialogue between material, perception, and conscience.

---

## ✨ Purpose

- Provide **open, reproducible color schemes** that respect human perception and accessibility, which may be freely used without acknowledgement, entailment, etc.
- Protect artists from unintended consequences through ethical licensing (`licenseRef:Zhsbsab0` and its `-N` variants).
- Sometimes a project simply requires an unbalanced color schema, which cannot be found in a book or list. Define your colors, give them names, test, publish via library.
- Encourage **slow, deliberate design** that allows the reader or viewer to think before acting.
- Align with UX patterns which do not rely on semantic color which is proven scientifically to impact how the user will interact with a site.
- Does not begin from time-honored patterns such as Solarized (but see our Acknowledgments below). The first palette which gave the project its motive force, emerged entirely from a dream.
- Document how each palette came to exist — its dream, its reasoning, its conversation. The well-defined palette, distinct yet having all that is required and that alone, is itself a work of art that may be used to help produce art.
- Permanent links to color and pallete allow for a legible sign-off process with a scientifically-defined color object. No fading, a URI-provided canonical reference color reproducable anywhere and referencable by library catalogue.

---

## 🎨 What It Is

Each palette in this library is a *program* that outputs its own colors in hexadecimal form.  
A palette is therefore both:

1. **A narrative** — the story or constraint that generated it.  
2. **A formula** — a deterministic set of color values reproducible anywhere that hexadecimal endures.
3. **A reference** - a catalog object, the permanent URI which leads to the generated reference color or palette.
You may use these palettes in digital or printed works, interfaces, games, or research environments,  
provided you follow the license terms attached to each.

---

## 📁 Structure

```
/palettes/
  opium-den/
    palette.json
    palette.css
    discussion.md
  exchequer/
    palette.json
    palette.css
    discussion.md
  pyjamas/
    palette.json
    palette.css
    discussion.md
/scripts/
  generate-palette.py
  preview-swatch.py
/docs/
  philosophy.md
  color-vision.md
LICENSE
README.md
```

- **palettes/** — individual color systems with metadata and swatches.  
- **scripts/** — mechanical generators and preview tools.  
- **docs/** — essays on design ethics, perception, and history.

---

## ⚙️ Using a Palette

1. Import the palette JSON or CSS file into your project.  
2. Retain its license header:

   ```text
   SPDX-License-Identifier: licenseRef-Zhsbsab0
   ```

   or, if you wish to add the non-semantic clause:

   ```text
   SPDX-License-Identifier: licenseRef-Zhsbsab0-N
   ```

3. Credit the palette by name in your documentation (required only if you name the palette or its colors as a feature of your product for some reason):

   Colors © Bibliothèque Chromatique N. – "Exchequer" palette by C.E.M.

Simply using the colors themselves, independent of chroma or palette names from the library requires no acknowledgement. We only assert license rights over the representation as published here, via our mechanisms (which are open-source and on Github as well.)
   
Such acknowledgements are nonetheless welcome to palette designers, who make their design work available to others in the hopes it will prove helpful to someone else's creation.

4. If you modify or extend a palette, record the rationale in a short note so future users can trace its lineage.

As a general rule, a palette published, is published. A palette extended preserves the original small palette space. The URI which references a given color internally, has an exposed variant which is effectively permanent (to avoid breaking links to pages within the library).


## 🤝 Contributing

Submissions are welcome — a palette, a reflection, or a script that produces either.
Please see CONTRIBUTING.md for format and accessibility requirements.

All contributions are subject to review for ethical clarity and reproducibility.
Colors may not encode hate, coercion, or identity exclusion.

---

## 🕊️ Ethics and Safety

Color is language.
It can soothe, provoke, or deceive.
This library asks that you employ it consciously and with care.

Every palette here is free to use but not free of meaning:
each carries the principle that art may show, but never enforce.
The -N suffix attached to any of our own licenses explicitly disclaims ideological endorsement.
The -S suffix 

---

## 📚 Included So Far

- **Opium Den** — jade, poppy, and silk for contemplative reading.
- **Exchequer** — stone, brass, and patina for analytic endurance.
- **Pyjamas** — madder, indigo, weld, and walnut for illustrative warmth.

New palettes will follow the same metadata format for predictable generation and display.

---

## 🧭 Acknowledgements

The project honors those who taught us to see color beyond physics — to read it as memory and moral act:
The initial “N.” stands for one such teacher, remembered here not by name but by perception.
Every artist or designer from the pre-digital world who has struggled to adapt, and complained to us in our capacity as friend who has the keys to compute and knowledge to use it.
Whoever it was
We specifically recognize Ethan Schoonover, the Solarized schema, and the literature which describes its evolution as a fundamental inspiration for this project.

---

## 🔗 Resources

- **antitrope.fr/chromatique** — canonical swatch browser
- **GitHub mirror** — source and issue tracking
- **Open Library License Project** — sibling repository

---

## ⚙️ Mechanical Color Generation

Colors in this library are mechanical — produced by small deterministic programs.
Each program’s name corresponds to a palette or pigment; its parameters define hue, gamma,
and perceptual relationships.

A minimal color generator might look like:

```python
# generate-palette.py
from library import chroma

def opium_den():
    base = chroma.seed("jade")
    return base.rotate(15).mix("poppy", 0.3).gamma(2.0).as_hex()
```

Every tone is reproducible by formula, so two independent systems given the same code will yield
identical swatches.  This ensures transparency, portability, and the longevity of your colors
even if visual rendering standards evolve.

---

## 🧶 License

Unless otherwise noted:

```
SPDX-License-Identifier: licenseRef-Zhsbsab0
```

"Zebras have stripes because stripes are beautiful (to the zebra)."  
Level and version zero.

This license allows you to do anything except claim you invented the color, or prevent others from using it. It is just a color.

Individual palettes may have specific licenses, but if published by Bibliothèque Chromatique N. / The Chromatic Library N. and presented here, they may be freely used without acknowledgement unless the palette license requires acknowledgement, or, if the palette or its color names are directly used as part of a product or work's description.

Even in this case, you are free to use individual colors to your heart's delight. They're just colors after all.
