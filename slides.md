---
marp: true
title: Marp: Markdown Presentation Ecosystem
author: Anand S
theme: default
paginate: true
class: lead
---

<!-- _header: "Marp: Markdown Presentation Ecosystem" -->
<!-- _footer: "Contact: <24f2000604@ds.study.iitm.ac.in>" -->

<!-- Custom theme/style for this deck -->
<style>
/* Gentle darkened gradient background for all slides */
section {
  background: linear-gradient(180deg,#0f1724 0%, #111827 100%);
  color: #e6eef8;
  font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif;
}

h1, h2, h3 {
  color: #ffd54f;
  letter-spacing: 0.6px;
}

/* Smaller page number style */
footer, .marp-footer {
  color: rgba(230,238,248,0.75);
  font-size: 0.9em;
}

/* Style for the email link in content */
a.email-link { color: #9be7ff; text-decoration: underline; }

/* Make code blocks more compact */
pre, code { font-family: SFMono-Regular, Menlo, Monaco, 'Roboto Mono', 'Courier New', monospace; }

/* Slide-specific utility class */
.section-center { display: flex; align-items: center; justify-content: center; flex-direction: column; }

/* Small-screen adjustments */
@media (max-width: 600px) {
  section { font-size: 14px; }
}
</style>

---

# Marp: Markdown Presentation Ecosystem

Create presentations in Markdown and never use PowerPoint again.

- Technical talks, docs, teaching, conference slides
- Easy export to HTML, PDF, PPTX

<!-- _class: lead center -->

---

## Installation

Use the Marp CLI or the VS Code extension.

```bash
# global install
npm install -g @marp-team/marp-cli

# one-off use
npx @marp-team/marp-cli@latest

# as dev dependency
npm install --save-dev @marp-team/marp-cli
```

<!-- _fragment:  -->

---

## Basic Structure

Every Marp file uses YAML front matter and `---` to separate slides.

Example front matter is shown on the first slide of this deck.

---

## Directives & Customization

Directives control slide-level metadata.

<!-- _header: "Marp – Quick Reference" -->
<!-- _footer: "Contact: 24f2000604@ds.study.iitm.ac.in" -->

- `<!-- _class: lead -->` — assign classes
- `<!-- _backgroundColor: #123456 -->` — set slide color
- `<!-- _footer: ... -->` and `<!-- _header: ... -->` for per-slide header/footer

---

## Code Blocks

```python
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

---

## Math & Algorithmic Complexity

Marp supports KaTeX/MathJax for math. Use inline $...$ and block $$...$$.

Block example for merge-sort complexity:

$$
T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n) \implies T(n) = \Theta(n\log n)
$$

Also show Big-O examples inline: $O(n)$, $O(n\log n)$, $O(n^2)$.

---

<!-- _class: lead -->

![bg cover](images/bg-slide.svg)

## Slide with Background Image

This slide uses an embedded SVG background stored in `images/bg-slide.svg`.

You can replace the SVG with any image; exports will include it.

---

## Presentation Export Tips

- HTML: `marp slides.md -o slides.html`
- PDF: `marp slides.md --pdf --allow-local-files`
- PowerPoint: `marp slides.md --pptx`

<!-- _footer: "Generated with Marp • Contact: 24f2000604@ds.study.iitm.ac.in" -->

---

# Contact & Next Steps

Questions? Reach out:

[Email me](mailto:24f2000604@ds.study.iitm.ac.in){.email-link}

- Keep slides short and focused
- Put code in separate files if large
- Use themes for consistent branding

<!-- _class: center -->

---

<!-- Speaker notes example -->

Note: Use VS Code Marp extension for live preview and quick exports.
