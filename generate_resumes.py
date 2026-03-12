from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from xml.sax.saxutils import escape
import shutil


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


def build_styles():
    styles = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            textColor=colors.HexColor("#0f172a"),
            alignment=TA_LEFT,
            spaceAfter=3,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#334155"),
            spaceAfter=2,
        ),
        "heading": ParagraphStyle(
            "Heading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=14,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.2,
            leading=14,
            textColor=colors.HexColor("#1f2937"),
            spaceAfter=3,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.1,
            leading=13.5,
            textColor=colors.HexColor("#1f2937"),
            leftIndent=12,
            firstLineIndent=-8,
            spaceAfter=2,
        ),
        "project": ParagraphStyle(
            "Project",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=4,
            spaceAfter=2,
        ),
    }


def md_to_story(md_path: Path):
    styles = build_styles()
    story = []
    lines = md_path.read_text(encoding="utf-8").splitlines()
    first_heading = True

    for raw in lines:
        line = raw.strip()
        if not line:
            story.append(Spacer(1, 3))
            continue

        if line.startswith("# "):
            text = escape(line[2:].strip())
            if first_heading:
                story.append(Paragraph(text, styles["title"]))
                first_heading = False
            else:
                story.append(Paragraph(text, styles["heading"]))
            continue

        if line.startswith("## "):
            story.append(Spacer(1, 2))
            story.append(Paragraph(escape(line[3:].strip()), styles["heading"]))
            continue

        if line.startswith("### "):
            story.append(Paragraph(escape(line[4:].strip()), styles["project"]))
            continue

        if line.startswith("- **") and ":**" in line:
            left, right = line[4:].split(":**", 1)
            content = f"<b>{escape(left.strip())}:</b>{escape(right)}"
            story.append(Paragraph(content, styles["bullet"]))
            continue

        if line.startswith("- "):
            story.append(Paragraph(f"• {escape(line[2:].strip())}", styles["bullet"]))
            continue

        story.append(Paragraph(escape(line), styles["subtitle" if first_heading else "body"]))

    return story


def generate_pdf(md_name: str, pdf_name: str):
    md_path = ROOT / md_name
    pdf_path = ASSETS / pdf_name
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title=pdf_name,
        author="MD ARIF ALI",
    )
    story = md_to_story(md_path)
    doc.build(story)
    return pdf_path


def main():
    ASSETS.mkdir(exist_ok=True)
    software_pdf = generate_pdf("resume-software-engineer.md", "resume-software-engineer.pdf")
    freelance_pdf = generate_pdf("resume-freelance.md", "resume-freelance.pdf")
    shutil.copyfile(software_pdf, ASSETS / "resume.pdf")
    print(software_pdf)
    print(freelance_pdf)
    print(ASSETS / "resume.pdf")


if __name__ == "__main__":
    main()
