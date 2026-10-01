from dataclasses import dataclass
from pathlib import Path
import fitz

@dataclass
class PageText:
    source: str
    page_number: int
    text: str

def load_pdf(path: Path):
    pages = []
    with fitz.open(path) as doc:
        for i, page in enumerate(doc):
            text = page.get_text("text").strip()
            if text:
                pages.append(PageText(path.name, i + 1, text))
    return pages

def load_pdfs(root: Path):
    pages = []
    for pdf in sorted(root.rglob("*.pdf")):
        pages.extend(load_pdf(pdf))
    return pages
