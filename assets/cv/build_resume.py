"""Build the portfolio resume: python assets/cv/build_resume.py.

Requires ReportLab. Content lives in resume.json; no website runtime dependency.
"""

import json
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parent
INK = colors.HexColor("#202820")
MUTED = colors.HexColor("#4d584e")
ACCENT = colors.HexColor("#315d43")
STYLES = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=25, leading=29, textColor=INK, spaceAfter=6),
    "headline": ParagraphStyle("headline", fontName="Helvetica", fontSize=11, leading=15, textColor=ACCENT, spaceAfter=9),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=9, leading=13, textColor=MUTED, spaceAfter=3),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=ACCENT, spaceBefore=15, spaceAfter=7, keepWithNext=True),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=INK, spaceAfter=3, keepWithNext=True),
    "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=9, leading=13, textColor=MUTED, spaceAfter=7, keepWithNext=True),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=14, textColor=INK, spaceAfter=7),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=10, leading=14, textColor=INK, leftIndent=11, firstLineIndent=-9, spaceAfter=6),
}


def paragraph(text, style="body"):
    return Paragraph(escape(text), STYLES[style])


def link(label, url):
    return f'<link href="{escape(url, {chr(34): "&quot;"})}" color="#315d43">{escape(label)}</link>'


def role_block(role):
    heading = [paragraph(role["title"], "role"), paragraph(f'{role["company"]} | {role["dates"]}', "meta")]
    bullets = [paragraph("- " + item, "bullet") for item in role["bullets"]]
    return [KeepTogether(heading + bullets[:1]), *bullets[1:], Spacer(1, 5)]


def build():
    data = json.loads((ROOT / "resume.json").read_text(encoding="utf-8"))
    for role in [data["current_role"], *data["previous_roles"]]:
        if not role["company"] or not role["dates"]:
            raise ValueError(f'Confirm employer and dates before publishing: {role["title"]}')
    document = SimpleDocTemplate(
        str(ROOT / "JMCV.pdf"), pagesize=A4,
        rightMargin=43, leftMargin=43, topMargin=38, bottomMargin=39,
        title=f'{data["name"]} - Resume', author=data["name"],
        subject="Full-stack .NET development, lending platforms, releases, and developer tooling",
    )
    story = [paragraph(data["name"], "name"), paragraph(data["headline"], "headline")]
    story.append(Paragraph(
        escape(data["location"]) + " | " + escape(data["phone"]) + " | " + link(data["email"], "mailto:" + data["email"]),
        STYLES["contact"],
    ))
    story.append(Paragraph(" | ".join(link(item["label"], item["url"]) for item in data["links"]), STYLES["contact"]))
    story.extend([Spacer(1, 9), HRFlowable(width="100%", thickness=1, color=ACCENT)])
    story.extend([paragraph("PROFILE", "section"), paragraph(data["summary"])])
    story.append(paragraph("CURRENT EXPERIENCE", "section"))
    story.extend(role_block(data["current_role"]))
    story.append(paragraph("TECHNICAL SKILLS", "section"))
    for skill in data["skills"]:
        story.append(Paragraph(f'<b>{escape(skill["category"])}:</b> {escape(skill["items"])}', STYLES["body"]))

    story.extend([PageBreak(), paragraph(data["name"], "role"), paragraph("EARLIER EXPERIENCE", "section")])
    for role in data["previous_roles"]:
        story.extend(role_block(role))
    story.append(paragraph("SELECTED PUBLIC PROJECTS", "section"))
    for project in data["projects"]:
        story.append(KeepTogether([
            Paragraph(link(project["name"], project["url"]), STYLES["role"]),
            paragraph(project["description"]),
        ]))
    story.append(paragraph("EDUCATION", "section"))
    story.extend([paragraph(data["education"]["degree"], "role"), paragraph(data["education"]["details"], "body")])

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#d6ddd5"))
        canvas.line(43, 30, A4[0] - 43, 30)
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(43, 18, data["name"] + " | Resume")
        canvas.drawRightString(A4[0] - 43, 18, str(doc.page))
        canvas.restoreState()

    document.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f'Built {ROOT / "JMCV.pdf"}')


if __name__ == "__main__":
    build()
