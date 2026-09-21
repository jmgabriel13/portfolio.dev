"""Build the resume while retaining the original one-page visual design."""

import io
import json
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
PAGE_W, PAGE_H = 612, 792
BLUE = colors.HexColor("#24669b")
TEXT = colors.HexColor("#111111")
SIDEBAR = colors.HexColor("#eeeeee")


def wrap(c, text, x, y, width, size=7.4, leading=9.2, font="Helvetica", color=TEXT):
    c.setFont(font, size)
    c.setFillColor(color)
    words, line = text.split(), ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if c.stringWidth(candidate, font, size) > width and line:
            c.drawString(x, y, line)
            y -= leading
            line = word
        else:
            line = candidate
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def heading(c, label, x, y, width):
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(BLUE)
    c.drawString(x, y, label)
    c.setStrokeColor(BLUE)
    c.setLineWidth(0.5)
    c.line(x + 82, y + 2, x + width, y + 2)
    return y - 20


def bullet(c, text, x, y, width, size=7.2):
    c.setFillColor(BLUE)
    c.circle(x + 3, y + 2, 2.5, fill=1, stroke=0)
    return wrap(c, text, x + 14, y, width - 14, size=size, leading=9)


def build():
    data = json.loads((ROOT / "resume.json").read_text(encoding="utf-8"))
    roles = [data["current_role"], *data["previous_roles"]]
    for role in roles:
        if not role["company"] or not role["dates"]:
            raise ValueError(f'Confirm employer and dates before publishing: {role["title"]}')

    overlay = io.BytesIO()
    c = canvas.Canvas(overlay, pagesize=(PAGE_W, PAGE_H))
    c.setFillColor(SIDEBAR); c.rect(82, 55, 188, 575, fill=1, stroke=0)
    c.setFillColor(colors.white); c.rect(286, 35, 285, 755, fill=1, stroke=0)

    x, y, w = 96, 596, 160
    c.setFont("Helvetica-Bold", 10); c.setFillColor(colors.HexColor("#555555")); c.drawString(x, y, "SOFTWARE ENGINEER")
    y -= 30; y = heading(c, "PROFILE", x, y, w)
    y = wrap(c, "Software engineer specializing in .NET and full-stack development across lending applications, production delivery, and developer tooling.", x, y, w, size=7.2, leading=9)
    y -= 14; y = heading(c, "CONTACT", x, y, w)
    for line in [data["phone"], data["email"], data["location"], "linkedin.com/in/johnmarkgabriel", "jmgabriel13.github.io/portfolio.dev"]:
        y = wrap(c, line, x, y, w, size=7.2, leading=10, color=BLUE if "http" in line or "linkedin" in line or "@" in line else TEXT); y -= 2
    y -= 8; y = heading(c, "TECHNOLOGY", x, y, w)
    for skill in data["skills"]:
        y = wrap(c, skill["category"].upper(), x, y, w, size=7.2, leading=9, font="Helvetica-Bold", color=colors.HexColor("#555555"))
        y = wrap(c, skill["items"], x, y, w, size=7, leading=9); y -= 5
    y = heading(c, "FOCUS", x, y, w)
    for line in ["Lending workflows", "Release coordination", "Production investigation", "Developer experience"]:
        y = bullet(c, line, x, y, w, size=7.1)

    x, y, w = 304, 735, 245
    y = heading(c, "EDUCATION", x, y, w)
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(TEXT); c.drawString(x, y, "BACHELOR OF SCIENCE IN COMPUTER SCIENCE")
    y -= 10; c.setFont("Helvetica", 7.2); c.drawString(x, y, "The University of Manila | 2016 - 2020"); y -= 24
    y = heading(c, "PROFESSIONAL EXPERIENCE", x, y, w)
    for role in roles:
        c.setFillColor(BLUE); c.circle(x + 3, y + 2, 2.5, fill=1, stroke=0)
        y = wrap(c, role["title"].upper(), x + 14, y, w - 14, size=8, leading=9, font="Helvetica-Bold")
        y = wrap(c, f'{role["company"]} | {role["dates"]}', x + 14, y, w - 14, size=7, leading=9)
        for item in role["bullets"]: y = bullet(c, item, x + 10, y - 1, w - 10, size=6.7)
        y -= 7
    y = heading(c, "SELECTED PUBLIC PROJECTS", x, y, w)
    for project in data["projects"]:
        y = wrap(c, project["name"], x, y, w, size=7.3, leading=9, font="Helvetica-Bold", color=BLUE)
        y = wrap(c, project["description"], x, y, w, size=6.7, leading=8.5); y -= 5
    c.save(); overlay.seek(0)
    base = PdfReader(str(ROOT / "template-original.pdf")); page = base.pages[0]
    page.pop("/Annots", None)
    page.merge_page(PdfReader(overlay).pages[0])
    writer = PdfWriter(); writer.add_page(page); writer.add_metadata({"/Title": f'{data["name"]} - Resume', "/Author": data["name"]})
    with (ROOT / "JMCV.pdf").open("wb") as stream: writer.write(stream)
    print(f"Built {ROOT / 'JMCV.pdf'}")


if __name__ == "__main__":
    build()
