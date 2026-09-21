---
title: Current role resume and portfolio update
type: chore
created: 2026-09-21
status: done
route: one-shot
---

# Current role resume and portfolio update

## Intent

**Problem:** The resume and portfolio understate current lending-platform, release,
production-investigation, and developer-tooling responsibilities. The existing
employment history still describes Collabera as current.

**Approach:** Update public wording using the supplied JD and user-provided work
analysis, retain an accurate formal title, and produce a readable PDF with editable
source. Do not publish private identifiers or infer quantified business impact.

## Content basis

- The supplied JD names Mid .Net Developer. The user confirmed starting at MONEYME
  on May 13, 2024 and leaving Collabera one month before. Public dates use May 2024
  and April 2024. The user requested MONEYME as the public company label, omitting
  the Philippine provider migration, and identified it as an Australian FinTech company.
- The user's work analysis supports scope descriptions; its underlying Jira,
  repositories, and internal tools were not independently audited in this task.
- Avoid unaudited ticket totals, inferred senior titles, company-wide adoption claims,
  and invented savings or impact metrics. Describe tooling as supporting the user's workflow.
- Keep internal tool names, ticket IDs, repository paths, and incident implementation
  details out of public copy. Public project descriptions remain based on existing site content.
- Preserve earlier experience, education, and contact details from the existing resume.
- Resume and timeline now use the confirmed title, company label, and employment dates.
  The generator refuses missing employer or date fields before writing the PDF.

## Progress and validation

- Updated hero, metadata, expertise, and workflow copy in `index.html`.
- Added an editable resume source and a ReportLab generator. Replaced the downloadable
  PDF and visually inspected both rendered pages. Verified complete responsibility text,
  title and dates, six clickable links, page count, and text bounds.
- Marked PDFs binary in `.gitattributes` to prevent Git line-ending conversion of the
  generated PDF's byte offsets and inappropriate whitespace checks on binary content.
- Narrow-screen inspection exposed existing Poiesis wordmark overflow. Added a fixed
  wordmark size and allowed project grid items to shrink without changing the layout.
- Passed Chrome checks at 320, 390, 760, 768, 1024, and 1440px, with disclosures both
  open and closed. Passed mobile navigation, keyboard disclosures, local asset and anchor
  checks, no-JavaScript visibility, and page-error checks.
- Zero automated WCAG A/AA violations in the selected axe checks at 390 and 1440px.
  Not a full accessibility certification. Browser QA script and screenshots are in the
  system temporary directory `portfolio-role-update-20260921`.
- Review performed locally in accordance with the user's no-subagent instruction.
- Final Chrome checks passed after the timeline update. Node syntax and Git whitespace
  checks passed. No push or deployment; remote availability and other browsers were not tested.

## Suggested Review Order

- [Portfolio content](../../index.html): updated positioning, expertise, and delivery tooling.
- [Resume source](../../assets/cv/resume.json): supported responsibilities and preserved history.
- [Resume generator](../../assets/cv/build_resume.py): readable text layout and incomplete-data guard.
- [Responsive styling](../../assets/css/style.css): narrow-screen project-label fix.
- [Maintenance instructions](../../README.md): rebuilding and checking the downloadable resume.
