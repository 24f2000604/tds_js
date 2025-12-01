---
marp: true
theme: default
paginate: true
title: Product Documentation Presentation
author: 24f2000604@ds.study.iitm.ac.in
footer: "24f2000604@ds.study.iitm.ac.in"
header: "Product Documentation"
math: mathjax
style: |
  section {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: #eaeaea;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1, h2, h3 {
    color: #f9ca24;
  }
  a {
    color: #74b9ff;
  }
  footer, header {
    color: rgba(255,255,255,0.6);
    font-size: 0.7em;
  }
  code {
    background: #2d3436;
    color: #81ecec;
  }
  .email {
    color: #fd79a8;
    font-weight: bold;
  }
---

<!-- _class: lead -->
<!-- _backgroundColor: #0d1b2a -->
<!-- _color: #ffffff -->

# Product Documentation

## Marp Markdown Presentation

**Author:** 24f2000604@ds.study.iitm.ac.in

<!-- _footer: "Contact: 24f2000604@ds.study.iitm.ac.in | Page 1" -->

---

<!-- _class: lead -->
<!-- _header: "24f2000604@ds.study.iitm.ac.in" -->
<!-- _footer: "Email: 24f2000604@ds.study.iitm.ac.in" -->
<!-- _backgroundColor: #1b263b -->

## About This Presentation

- Created with **Marp** (Markdown Presentation Ecosystem)
- Custom theme with gradient backgrounds
- Page numbers enabled via paginate: true
- Mathematical equations using MathJax/KaTeX
- Contact: **24f2000604@ds.study.iitm.ac.in**

---

<!-- _class: lead -->

![bg](images/bg-slide.svg)

## Background Image Slide

This slide demonstrates the **background image** feature.

Using the bg image syntax.

Email: 24f2000604@ds.study.iitm.ac.in

---

![bg left:40%](images/bg-slide.svg)

<!-- _header: "Split Background Layout" -->
<!-- _footer: "24f2000604@ds.study.iitm.ac.in" -->

## Split Background

This slide uses a **split background** layout.

The image appears on the left 40% of the slide.

---

![bg right:50% fit](images/bg-slide.svg)

<!-- _backgroundColor: #0f0f23 -->

## Another Background Example

Using bg right:50% fit for right-side background.

### Features Shown:
- Background image positioning
- Custom background color directive
- Page numbers (bottom right)

Contact: 24f2000604@ds.study.iitm.ac.in

---

<!-- _class: lead -->
<!-- _header: "Mathematical Equations" -->
<!-- _footer: "24f2000604@ds.study.iitm.ac.in" -->

## Mathematical Equations

### Inline Math
Time complexity: $O(n \log n)$, Space: $O(n)$

### Block Equations

$$
T(n) = 2T\left(\frac{n}{2}\right) + O(n)
$$

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

---

<!-- _backgroundColor: #2c3e50 -->
<!-- _color: #ecf0f1 -->

## More Mathematical Examples

### Big-O Notation

| Algorithm | Time Complexity |
|-----------|-----------------|
| Binary Search | $O(\log n)$ |
| Merge Sort | $O(n \log n)$ |
| Quick Sort | $O(n^2)$ worst |

### Quadratic Formula

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

---

<!-- _class: lead -->
<!-- _header: "Custom Directives Demo" -->
<!-- _footer: "Styled with Marp Directives | 24f2000604@ds.study.iitm.ac.in" -->
<!-- _backgroundColor: #2d3436 -->
<!-- _color: #dfe6e9 -->

## Custom Styling with Directives

This slide uses multiple **Marp directives**:

- _class: lead — centered layout
- _backgroundColor: #2d3436 — dark background
- _color: #dfe6e9 — light text
- _header: custom header
- _footer: custom footer

---

![bg cover](images/bg-slide.svg)

<!-- _class: lead -->

## Full Background Cover

Using bg cover for full coverage.

### Contact Information

Email: **24f2000604@ds.study.iitm.ac.in**

$$
E = mc^2
$$

---

<!-- _backgroundColor: #1e272e -->
<!-- _header: "Algorithm Complexity" -->
<!-- _footer: "24f2000604@ds.study.iitm.ac.in" -->

## Algorithm Complexity Analysis

### Master Theorem

For recurrence $T(n) = aT(n/b) + f(n)$:

$$
T(n) = \Theta(n^{\log_b a})
$$

When $f(n) = O(n^{\log_b a - \epsilon})$

$$
T(n) = \Theta(n^{\log_b a} \log n)
$$

When $f(n) = \Theta(n^{\log_b a})$

---

![bg opacity:0.3](images/bg-slide.svg)

<!-- _class: lead -->
<!-- _footer: "Thank you! | 24f2000604@ds.study.iitm.ac.in" -->

# Thank You

## Questions?

**Email:** 24f2000604@ds.study.iitm.ac.in

**Presentation Features Used:**
- Custom theme (YAML style block)
- Page numbers (paginate: true)
- Background images (bg syntax)
- Marp directives (_class, _backgroundColor, etc.)
- Math equations (KaTeX/MathJax)
- Email: 24f2000604@ds.study.iitm.ac.in
