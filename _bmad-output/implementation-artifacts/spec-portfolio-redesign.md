---
title: Editorial portfolio redesign
type: refactor
created: 2026-09-18
status: done
baseline_commit: 6b386848724d717a1e9513a58c4a1e7c95a5e756
context: []
---

<frozen-after-approval reason="User approved the redesign plan in conversation">

## Intent

**Problem:** The portfolio needs a distinctive visual identity and clearer project presentation while preserving the current local .NET and AI-assisted engineering positioning.

**Approach:** Build an editorial, charcoal-and-warm-white portfolio with an acid-lime accent, oversized typography, real project previews, concise content, accessible motion, and a responsive contact section. Use Awwwards as a reference for visual quality, not copied assets or fabricated project achievements.

## Boundaries & Constraints

**Always:** Work on `feat/portfolio-redesign` from the latest local `dev` commit. Preserve the existing projects, experience, CV, contact destinations, and workflow kit. Keep the static HTML/CSS/JavaScript architecture, relative asset paths, and GitHub Pages compatibility. Keep essential content usable without JavaScript.

**Ask First:** New backend services, changed professional claims, replacement of existing project content, or production deployment.

**Never:** Merge into `dev`, change deployment settings, invent metrics or credentials, add an unnecessary framework, hijack native scrolling, or modify unrelated workflow-kit guidance.

## I/O & Edge-Case Matrix

| Scenario | State | Expected behavior |
| --- | --- | --- |
| Navigation | Desktop or mobile | Links reach matching sections without sticky-header overlap. |
| Mobile menu | Toggle, link, Escape, outside click, viewport resize | Menu visibility and aria-expanded remain synchronized; Escape restores focus. |
| No JavaScript | Script disabled | Navigation, projects, contact, and CV remain usable. |
| Reduced motion | User preference enabled | Reveal motion and smooth scrolling are disabled. |
| Project details | Pointer or keyboard | Native disclosure exposes additional project context. |
| External resources | Link activation | Existing destinations open safely; no false submission success. |

</frozen-after-approval>

## Code Map

- `index.html`: semantic content, navigation, project previews, contact links, metadata.
- `assets/css/style.css`: responsive visual system, layout, motion, focus and disclosure states.
- `assets/js/script.js`: progressive mobile navigation and subtle reveal enhancement.
- `assets/images/`: existing screenshots and profile image, reused without changing their meaning.
- `README.md`: local preview and verification instructions.
- `workflow-kit/`: existing proof artifact; no changes planned.

## Tasks & Acceptance

**Execution:**
- [x] `index.html` — rebuild hierarchy around hero, selected work, expertise, workflow proof, experience, and contact.
- [x] `assets/css/style.css` — establish expressive typography and restrained color, layout, hover, focus, and mobile rules.
- [x] `assets/js/script.js` — implement accessible menu lifecycle and optional reduced-motion-aware reveals.
- [x] `README.md` — document preview and verification, and retain project positioning.
- [x] Verify navigation edge cases, content preservation, screenshots, no-JS behavior, local links and assets, and browser console.

**Acceptance Criteria:**
- Given the baseline content, when the redesigned page loads, then all four existing projects, workflow kit, experience entries, CV and professional contact links are accessible.
- Given desktop, tablet, and narrow mobile viewports, when browsing each section, then no text clips or horizontal overflow occurs and images retain their aspect ratio.
- Given keyboard-only navigation, when opening menus and project details, then controls are labeled and focus remains visible and usable.
- Given reduced motion or disabled JavaScript, when opening the page, then content remains visible and links work.
- Given GitHub Pages hosting under `/portfolio.dev/`, when local resources resolve, then assets and workflow links remain inside the project path.
- Given the separate feature branch, when reviewing the changes, then the original local `dev` commit remains intact.

## Design Notes

Keep the technical personality in small monospace labels and structured project context. Use a large editorial name treatment and a real portrait rather than decorative generated artwork. Alternate image-backed work with an honest typographic API preview so an unrelated screenshot is not labeled as the API. Prefer native details for project context, ordinary anchors for navigation, and CSS transitions over a motion dependency. Use fixed font sizes at breakpoints, not viewport-scaled text.

## Verification

- JavaScript syntax check with Node.
- Browser checks with desktop and mobile screenshots and interaction assertions.
- Accessibility scan plus keyboard and reduced-motion checks.
- Verify local assets, section anchors, CV, workflow link, and browser console.
- Inspect git diff and status for unrelated changes.

## Spec Change Log

- Local baseline is one commit ahead of remote `dev`; preserve it as the authoritative content source.

## Verification Results

- Passed Node syntax and Git whitespace checks.
- Passed 12 Playwright behavior checks: menu keyboard/Escape, section focus, Back to top, outside dismissal, responsive focus, native disclosures, local resources, reduced motion, no-JavaScript fallback, direct file preview, GitHub Pages subpath, and browser errors.
- No horizontal overflow at 320, 375, 390, 560, 600, 760, 768, 1000, 1024, 1280, 1440, and 1920px widths.
- Zero axe violations in the selected WCAG A/AA checks on desktop, mobile, expanded project details, and the open mobile menu. This is automated coverage, not a full accessibility certification.
- Visually inspected the full desktop page, individual sections, mobile hero, and mobile menu. Before/after screenshots and test runners are in the local user cache at `.cache/portfolio-validation`.
- All local images, CV, and workflow links returned HTTP 200. No page errors or failed local requests.
- Fixed issues found in review: sticky-header Back to top anchor, focus handoff during viewport changes, and no-JavaScript sticky-header overlap. Corrected intrinsic image dimensions to avoid avoidable layout shifts.
- Review performed inline, respecting the user's instruction to use subagents only when explicitly requested.
- Limits: Safari/Firefox and physical devices were not tested. External demo/social availability was not confirmed. No production deployment or field performance measurement was performed.

## Suggested Review Order

- Start with the hero and overall semantic page structure.
  [index.html:62](../../index.html#L62)
- Review project presentation, retained context, and native disclosures.
  [index.html:114](../../index.html#L114)
- Check menu focus handling and progressive enhancement.
  [script.js:3](../../assets/js/script.js#L3)
- Inspect visual tokens, responsive layouts, and reduced-motion rules.
  [style.css:1](../../assets/css/style.css#L1)
- Review local preview instructions and verification guidance.
  [README.md:1](../../README.md#L1)
