# Retrieval

The retrieval layer contains three components:

- Dense vector retrieval
- Sparse BM25 retrieval
- Hybrid retrieval

Dense retrieval uses local embeddings.

BM25 provides lexical keyword matching.

Hybrid retrieval combines semantic and lexical search signals.

Test the retrieval components with:

```powershell
python scripts/test_dense_search.py
python scripts/test_bm25_search.py
python scripts/test_hybrid_search.py
```
