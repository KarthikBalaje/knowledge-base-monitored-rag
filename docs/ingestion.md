# Ingestion

The document ingestion pipeline performs:

1. PDF discovery
2. PDF text extraction using PyMuPDF
3. Metadata extraction
4. Text chunking
5. Local embedding generation using
   `sentence-transformers/all-MiniLM-L6-v2`
6. Indexing into Weaviate

Run:

```powershell
python scripts/ingest_documents.py
```
