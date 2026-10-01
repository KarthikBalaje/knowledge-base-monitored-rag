from app.knowledge_base.chunker import chunk_pages
from app.knowledge_base.pdf_loader import PageText
def test_chunking(): assert len(chunk_pages([PageText("x.pdf",1,"a"*2000)],800,100)) >= 2
