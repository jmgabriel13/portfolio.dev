# JM Gabriel Portfolio

Personal portfolio for JM Gabriel, an AI-augmented .NET Full-Stack Developer.
An editorial layout brings together selected business systems, technical strengths,
professional experience, and an AI engineering workflow kit.

Production site: https://jmgabriel13.github.io/portfolio.dev/

## Local preview

Open `index.html` directly in a browser, or serve this directory with a local static
server. No build step, package installation, or runtime framework is required.
The redesign lives on `feat/portfolio-redesign`; switching branches changes the
local preview. The production site changes only through the existing deployment process.

## Structure

- `index.html` — semantic content, project disclosures, navigation, and metadata
- `assets/css/style.css` — visual tokens, responsive layout, focus states, and motion
- `assets/js/script.js` — progressive navigation and optional entrance animations
- `assets/images/` — existing portrait and project screenshots
- `assets/cv/JMCV.pdf` — résumé
- `workflow-kit/` — proof artifact for AI-assisted engineering workflow design
- `_bmad-output/implementation-artifacts/spec-portfolio-redesign.md` — approved scope, validation, and review order

## Design and behavior

Charcoal, warm white, and a lime accent support large typography and staggered
project previews. The page draws on the editorial grids and portfolio presentation
featured on [Awwwards](https://www.awwwards.com/), with an original composition.
Reference directions include [typography on a grid](https://www.awwwards.com/inspiration/font-sized-grid-inspired-by-the-first-computers-with-primitive-software)
and [minimal portfolio scrolling](https://www.awwwards.com/inspiration/scroll-portfolio).

Core content and navigation work without JavaScript. Project context uses native
`details` elements. The enhanced mobile menu supports keyboard navigation, Escape,
outside clicks, and focus handoff. Animations respect reduced-motion preferences;
content never waits for an animation to become visible.

Relative asset paths support both direct file previews and GitHub Pages hosting
under `/portfolio.dev/`. Google Fonts are optional external requests with system
font fallbacks. The contact links use the visitor's email client; there is no form backend.

## Verification

Run `node --check assets/js/script.js` for a syntax check. For browser verification:

1. Check desktop, tablet, and 320px-wide mobile layouts for overflow and clipping.
2. Open the mobile menu, navigate with Tab, dismiss with Escape, and resize across 760px.
3. Follow section links and Back to top; verify headings clear the sticky header.
4. Open each project's details with Enter or Space.
5. Verify the résumé, images, workflow kit, and external destinations.
6. Repeat with JavaScript disabled and reduced motion enabled.

The redesign was checked with headless Chrome, Playwright interaction assertions,
and axe accessibility scans. Test tools are isolated from the project's runtime.
Detailed results and remaining test limits are in the implementation spec.
