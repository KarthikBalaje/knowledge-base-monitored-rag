# Architecture

PDF documents
    |
    v
PDF extraction
    |
    v
Text chunking
    |
    v
Local MiniLM embeddings
    |
    v
Weaviate vector index
    |
    +------------------+
    |                  |
    v                  v
Dense retrieval     BM25 retrieval
    |                  |
    +--------+---------+
             |
             v
       Hybrid retrieval
             |
             v
       Context builder
             |
             v
        Ollama LLM
             |
             v
          Answer

Arize Phoenix provides observability and tracing.
