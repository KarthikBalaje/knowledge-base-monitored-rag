from dataclasses import dataclass

@dataclass
class Chunk:
    chunk_id: str
    text: str
    source: str
    page_number: int
    domain: str

def infer_domain(filename: str) -> str:
    value = filename.lower()
    if "pytorch" in value: return "pytorch"
    if "tensorflow" in value: return "tensorflow"
    if "nlp" in value or "natural-language" in value: return "natural_language_processing_nlp"
    if "machine" in value: return "machine_learning"
    if "deep" in value or "neural" in value: return "deep_learning"
    return "data_science"

def chunk_pages(pages, chunk_size=800, overlap=100):
    if overlap >= chunk_size: raise ValueError("overlap must be smaller than chunk_size")
    chunks=[]; counter=0
    for page in pages:
        start=0
        while start < len(page.text):
            end=min(start+chunk_size, len(page.text))
            piece=page.text[start:end].strip()
            if piece:
                chunks.append(Chunk(f"{page.source}-{page.page_number}-{counter}", piece, page.source, page.page_number, infer_domain(page.source)))
                counter += 1
            if end >= len(page.text): break
            start=end-overlap
    return chunks
