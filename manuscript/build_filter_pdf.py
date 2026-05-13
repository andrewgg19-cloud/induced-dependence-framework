from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "manuscript" / "filter_can_create_correlations.tex"
OUT = ROOT / "manuscript" / "filter_can_create_correlations.pdf"


def tex_to_text(text: str) -> str:
    replacements = {
        r"\textbf": "",
        r"\textit": "",
        r"\small": "",
        r"\&": "&",
        r"\sim": "~",
        r"\mid": "|",
        r"\parallel": "||",
        r"\to": "->",
        r"\in": "in",
        r"\mathbb{R}": "R",
        r"\Delta_{obs}": "Delta_obs",
        r"\mathcal{D}_{KL}": "D_KL",
        r"\Phi": "Phi",
        r"\alpha": "alpha",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\\href\{mailto:[^}]+\}\{([^}]+)\}", r"\\1", text)
    text = re.sub(r"\\cite\{([^}]+)\}", r"[\1]", text)
    text = text.replace("{", "").replace("}", "")
    text = text.replace("\\", "")
    return text


def add_footer(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#52606d"))
    canvas.drawCentredString(letter[0] / 2, 0.42 * inch, f"The Filter Can Also Create Correlations | Page {doc.page}")
    canvas.restoreState()


def build_pdf() -> None:
    source = TEX.read_text(encoding="utf-8")

    title = re.search(r"\\title\{(.+?)\}", source, re.DOTALL).group(1)
    title = tex_to_text(title)

    author = "German Garcia | Investigador Titular Independiente | andrewgg19@gmail.com"
    date = "May 13, 2026"

    abstracts = re.findall(r"\\begin\{abstract\}(.+?)\\end\{abstract\}", source, re.DOTALL)
    spanish_abstract = tex_to_text(abstracts[0].strip())
    english_abstract = tex_to_text(abstracts[1].strip())

    body = source.split(r"\section{Introduction}", 1)[1]
    body = r"\section{Introduction}" + body
    body = body.split(r"\end{document}", 1)[0]

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="PaperTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=19,
            leading=23,
            textColor=colors.HexColor("#1f4e79"),
            alignment=TA_CENTER,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Meta",
            parent=styles["Normal"],
            fontSize=10,
            leading=14,
            textColor=colors.HexColor("#52606d"),
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=colors.HexColor("#1f4e79"),
            spaceBefore=9,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Subheading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=15,
            textColor=colors.HexColor("#28784f"),
            spaceBefore=7,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.8,
            leading=13,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Equation",
            parent=styles["Code"],
            fontName="Courier",
            fontSize=9,
            leading=12,
            backColor=colors.HexColor("#f0f4f8"),
            borderPadding=5,
            spaceBefore=3,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="AbstractLabel",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#1f4e79"),
            spaceBefore=8,
            spaceAfter=4,
        )
    )

    story = [
        Paragraph(title, styles["PaperTitle"]),
        Paragraph(author, styles["Meta"]),
        Paragraph(date, styles["Meta"]),
        Spacer(1, 0.08 * inch),
        Paragraph("Resumen", styles["AbstractLabel"]),
        Paragraph(spanish_abstract, styles["Body"]),
        Paragraph("Abstract", styles["AbstractLabel"]),
        Paragraph(english_abstract, styles["Body"]),
        PageBreak(),
    ]

    tokens = re.split(r"(\\section\{[^}]+\}|\\subsection\{[^}]+\}|\\begin\{equation\}|\\end\{equation\}|\\begin\{thebibliography\}\{99\}|\\end\{thebibliography\})", body)
    in_equation = False
    in_bib = False
    paragraph_buffer: list[str] = []

    def flush_paragraph() -> None:
        if paragraph_buffer:
            text = " ".join(part.strip() for part in paragraph_buffer if part.strip())
            if text:
                story.append(Paragraph(tex_to_text(text), styles["Body"]))
            paragraph_buffer.clear()

    for token in tokens:
        if not token:
            continue
        section = re.match(r"\\section\{([^}]+)\}", token)
        subsection = re.match(r"\\subsection\{([^}]+)\}", token)
        if section:
            flush_paragraph()
            story.append(Paragraph(tex_to_text(section.group(1)), styles["Heading"]))
            continue
        if subsection:
            flush_paragraph()
            story.append(Paragraph(tex_to_text(subsection.group(1)), styles["Subheading"]))
            continue
        if token == r"\begin{equation}":
            flush_paragraph()
            in_equation = True
            continue
        if token == r"\end{equation}":
            in_equation = False
            continue
        if token == r"\begin{thebibliography}{99}":
            flush_paragraph()
            in_bib = True
            story.append(Paragraph("References", styles["Heading"]))
            continue
        if token == r"\end{thebibliography}":
            flush_paragraph()
            in_bib = False
            continue
        if in_equation:
            eq = tex_to_text(token.strip())
            if eq:
                story.append(Paragraph(eq, styles["Equation"]))
            continue
        if in_bib:
            for line in token.splitlines():
                line = line.strip()
                if not line:
                    continue
                line = re.sub(r"\\bibitem\{[^}]+\}", "•", line)
                story.append(Paragraph(tex_to_text(line), styles["Body"]))
            continue
        for block in token.split("\n\n"):
            block = block.strip()
            if block:
                paragraph_buffer.append(block)
                flush_paragraph()

    flush_paragraph()

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        rightMargin=0.65 * inch,
        leftMargin=0.65 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.7 * inch,
        title="The Filter Can Also Create Correlations",
        author="German Garcia",
    )
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)


if __name__ == "__main__":
    build_pdf()
