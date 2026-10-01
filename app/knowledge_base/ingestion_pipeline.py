from app.config import DOCUMENT_ROOT, settings
from app.knowledge_base.pdf_loader import load_pdfs
from app.knowledge_base.document_processor import clean_text
from app.knowledge_base.chunker import chunk_pages

def build_chunks():
    pages=load_pdfs(DOCUMENT_ROOT)
    for page in pages: page.text=clean_text(page.text)
    return chunk_pages(pages, settings.chunk_size, settings.chunk_overlap)
