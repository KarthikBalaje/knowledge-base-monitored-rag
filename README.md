# Case Study 3 — Knowledge Base Monitored RAG

An observable, guarded, and evaluation-enabled Retrieval-Augmented Generation (RAG) knowledge assistant for Data Science, Machine Learning, Deep Learning, PyTorch, TensorFlow, and Natural Language Processing (NLP).

The project combines:

- PDF knowledge-base ingestion
- Local embedding generation
- Weaviate vector storage
- Dense vector retrieval
- Sparse BM25 retrieval
- Hybrid retrieval
- Prompt-injection input sanitization
- Local Ollama LLM generation
- Arize Phoenix observability and tracing
- Retrieval-quality evaluation
- Phoenix span annotations for evaluation evidence
- Automated tests

---

## 1. Project Objective

The objective of this case study is to implement a production-oriented RAG workflow that is not only capable of answering questions from a curated knowledge base, but is also:

1. **Observable** — RAG execution is traced through Arize Phoenix.
2. **Guarded** — incoming user queries are checked for prompt-injection patterns.
3. **Hybrid** — retrieval combines dense semantic search and sparse BM25 search.
4. **Locally runnable** — embeddings and LLM generation can run locally.
5. **Evaluated** — retrieval quality is measured using Hit@K and Recall@K.
6. **Evidence-driven** — evaluation scores and traces are recorded in Phoenix.

---

## 2. Evaluation Rubric

The implementation was designed against the following 100-point rubric:

| Area | Points | Status |
|---|---:|---|
| Observability setup — Phoenix installed/launched locally and dashboard reachable | 15 | ✅ |
| Vector indexing — Weaviate + local embeddings + PDF ingestion | 15 | ✅ |
| Hybrid search — dense + sparse BM25 | 20 | ✅ |
| Input sanitization guardrail | 20 | ✅ |
| Phoenix tracing integration | 15 | ✅ |
| Retrieval-quality evaluation visible in Phoenix | 15 | ✅ |
| **Total** | **100** | **✅** |

---

## 3. Knowledge Domains

The knowledge base contains documents covering:

1. Data Science
2. Machine Learning
3. Deep Learning
4. PyTorch
5. TensorFlow
6. Natural Language Processing (NLP)

The current knowledge base contains **12 PDF documents**.

### Document distribution

| Domain | PDFs |
|---|---:|
| Data Science | 2 |
| Machine Learning | 2 |
| Deep Learning | 3 |
| Natural Language Processing | 3 |
| PyTorch | 1 |
| TensorFlow | 1 |
| **Total** | **12** |

The ingestion pipeline produced **924 indexed chunks**.

---

## 4. Architecture

```text
                         ┌──────────────────────┐
                         │      User Query      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Input Sanitization   │
                         │ Prompt Injection     │
                         │ Guardrail             │
                         └──────────┬───────────┘
                                    │
                                    ▼
                  ┌─────────────────────────────────────┐
                  │          Hybrid Retrieval           │
                  │                                     │
                  │  Dense Semantic Search + BM25      │
                  │                │                    │
                  │                ▼                    │
                  │             Weaviate                │
                  └────────────────┬────────────────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │   Context Builder    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Prompt Construction  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Ollama / Qwen3   │
                         │     Local LLM        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Final Answer      │
                         └──────────────────────┘

        ───────────────────────────────────────────────────
                     Arize Phoenix Observability
        ───────────────────────────────────────────────────
        Pipeline → Guardrail → Retrieval → Context →
        Prompt → LLM → Evaluation
```

---

## 5. Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.10 |
| RAG framework | Custom Python pipeline |
| Vector database | Weaviate |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` |
| Sparse retrieval | BM25 |
| LLM runtime | Ollama |
| Local LLM | Qwen3 8B |
| Observability | Arize Phoenix |
| Tracing | OpenTelemetry / Phoenix OTEL |
| Evaluation | Hit@5, Recall@5 |
| Documents | PDF |
| Testing | pytest |
| Containerization | Docker Compose |

---

## 6. Project Structure

```text
knowledge-base-monitored-rag/
│
├── app/
│   ├── config.py
│   ├── main.py
│   │
│   ├── evaluation/
│   │   ├── evaluation_dataset.py
│   │   ├── evaluator.py
│   │   ├── phoenix_evaluation.py
│   │   └── retrieval_metrics.py
│   │
│   ├── guardrails/
│   │   ├── guardrail_result.py
│   │   ├── injection_patterns.py
│   │   └── input_sanitizer.py
│   │
│   ├── knowledge_base/
│   │   ├── chunker.py
│   │   ├── document_processor.py
│   │   ├── embeddings.py
│   │   ├── ingestion_pipeline.py
│   │   └── pdf_loader.py
│   │
│   ├── observability/
│   │   ├── phoenix.py
│   │   ├── span_helpers.py
│   │   └── tracing.py
│   │
│   ├── rag/
│   │   ├── context_builder.py
│   │   ├── llm.py
│   │   ├── ollama_client.py
│   │   ├── prompts.py
│   │   └── rag_pipeline.py
│   │
│   ├── retrieval/
│   │   ├── bm25_retriever.py
│   │   ├── dense_retriever.py
│   │   ├── hybrid_retriever.py
│   │   └── result_formatter.py
│   │
│   └── vector_store/
│       ├── index_manager.py
│       ├── schema.py
│       └── weaviate_client.py
│
├── data/
│   ├── documents/
│   │   ├── data_science/
│   │   ├── machine_learning/
│   │   ├── deep_learning/
│   │   ├── pytorch/
│   │   ├── tensorflow/
│   │   └── natural_language_processing_nlp/
│   │
│   └── evaluation/
│       └── retrieval_eval.json
│
├── docs/
│   ├── architecture.md
│   ├── evaluation-mapping.md
│   ├── evaluation.md
│   ├── ingestion.md
│   ├── knowledge-base.md
│   ├── observability.md
│   ├── retrieval.md
│   └── security.md
│
├── evidence/
│   ├── 01_observability/
│   ├── 02_vector_indexing/
│   ├── 03_hybrid_search/
│   ├── 04_guardrail/
│   ├── 05_tracing/
│   └── 06_evaluation/
│
├── scripts/
│   ├── create_weaviate_schema.py
│   ├── ingest_documents.py
│   ├── run_demo.py
│   ├── run_evaluation.py
│   ├── start_phoenix.py
│   ├── test_bm25_search.py
│   ├── test_dense_search.py
│   └── test_hybrid_search.py
│
├── tests/
│   ├── test_bm25_retrieval.py
│   ├── test_chunking.py
│   ├── test_dense_retrieval.py
│   ├── test_embeddings.py
│   ├── test_evaluation.py
│   ├── test_guardrail.py
│   ├── test_hybrid_retrieval.py
│   ├── test_pdf_loader.py
│   ├── test_rag_pipeline.py
│   └── test_weaviate.py
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── pyproject.toml
└── requirements.txt
```

---

# 7. Prerequisites

## 7.1 Python

Python 3.10 is used for this implementation.

Verify:

```powershell
python --version
```

Expected:

```text
Python 3.10.x
```

## 7.2 Virtual environment

Create:

```powershell
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 7.3 Install dependencies

```powershell
pip install -r requirements.txt
```

Install the project:

```powershell
pip install -e .
```

---

# 8. Ollama Setup

Install Ollama and verify:

```powershell
ollama --version
```

Pull the local LLM:

```powershell
ollama pull qwen3:8b
```

Pull the local embedding model:

```powershell
ollama pull nomic-embed-text
```

The RAG generation path uses Ollama locally.

The vector-indexing implementation uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

for the Weaviate knowledge-base embeddings.

---

# 9. Weaviate Setup

The project uses Weaviate locally through Docker Compose.

Start Weaviate:

```powershell
docker compose up -d
```

Check:

```powershell
docker ps
```

The configured host port is:

```text
8081
```

The container's internal HTTP port remains:

```text
8080
```

The configured gRPC port is:

```text
50051
```

Verify Weaviate:

```powershell
Invoke-WebRequest http://localhost:8081/v1/meta -UseBasicParsing
```

A successful response confirms that the server is reachable.

---

# 10. Environment Configuration

Copy:

```powershell
Copy-Item .env.example .env
```

The important configuration includes:

```text
WEAVIATE_HOST=localhost
WEAVIATE_PORT=8081
WEAVIATE_GRPC_PORT=50051
```

The implementation uses:

```text
KnowledgeChunk
```

as the Weaviate collection.

---

# 11. Create the Weaviate Schema

From the project root:

```powershell
$env:PYTHONPATH = (Get-Location).Path
python scripts/create_weaviate_schema.py
```

Expected result:

```text
Collection ready: KnowledgeChunk
```

---

# 12. Ingest the Knowledge Base

The PDFs are organized by domain under:

```text
data/documents/
```

Run:

```powershell
$env:PYTHONPATH = (Get-Location).Path
python scripts/ingest_documents.py
```

The completed implementation indexed:

```text
924 chunks
```

from:

```text
12 PDFs
```

---

# 13. Retrieval Architecture

The project implements three retrieval modes.

## 13.1 Dense retrieval

Dense retrieval uses semantic embeddings to retrieve conceptually related content.

Test:

```powershell
python scripts/test_dense_search.py
```

Example query:

```text
What is Pytorch & Tensorflow? What is the difference between them?
```

---

## 13.2 BM25 sparse retrieval

BM25 provides lexical keyword-based retrieval.

Test:

```powershell
python scripts/test_bm25_search.py
```

Example:

```text
What is the difference between ML and DL?
```

---

## 13.3 Hybrid retrieval

Hybrid retrieval combines:

```text
Dense semantic relevance
        +
BM25 lexical relevance
```

Test:

```powershell
python scripts/test_hybrid_search.py
```

Example:

```text
What is NLP?
```

The hybrid retriever combines the two retrieval signals and returns the final ranked context.

---

# 14. Input Sanitization Guardrail

Incoming user queries pass through a prompt-injection guardrail before retrieval and generation.

The implementation includes:

```text
app/guardrails/
├── guardrail_result.py
├── injection_patterns.py
└── input_sanitizer.py
```

The sanitizer checks incoming queries against configured prompt-injection patterns.

If the request is allowed:

```text
User Query
    ↓
Guardrail
    ↓
Retrieval
```

If the request is blocked:

```text
User Query
    ↓
Guardrail
    ↓
Blocked
```

Test:

```powershell
pytest -q tests/test_guardrail.py
```

Expected:

```text
2 passed
```

---

# 15. RAG Pipeline

The RAG pipeline follows this sequence:

```text
1. Receive user question
2. Sanitize input
3. Execute hybrid retrieval
4. Format retrieved documents
5. Build context
6. Construct prompt
7. Send prompt to local Ollama LLM
8. Return answer and sources
9. Record observability spans
```

The main implementation is:

```text
app/rag/rag_pipeline.py
```

---

# 16. Run the End-to-End Demo

Set the project path:

```powershell
$env:PYTHONPATH = (Get-Location).Path
```

Run:

```powershell
python scripts/run_demo.py
```

Example question:

```text
What is the difference between machine learning and deep learning?
```

The response is generated from the indexed knowledge base using hybrid retrieval and the local Ollama model.

---

# 17. Arize Phoenix Observability

Phoenix is used to monitor and inspect the RAG pipeline.

The project uses:

```text
Arize Phoenix 20.16.0
```

and Phoenix OTEL components.

## Start Phoenix

The working local launch command is:

```powershell
$env:PHOENIX_HOST="127.0.0.1"
$env:PHOENIX_PORT="6006"

python -m phoenix.server.main serve
```

Open:

```text
http://127.0.0.1:6006
```

The Phoenix project used by this application is:

```text
knowledge-base-monitored-rag
```

---

# 18. Phoenix Tracing

The RAG pipeline is instrumented with OpenTelemetry/Phoenix spans.

A normal successful RAG request produces a trace similar to:

```text
rag_pipeline
│
├── input_sanitization
│
├── hybrid_retrieval
│
├── context_builder
│
├── prompt_construction
│
└── llm_generation
```

The root span records attributes such as:

```text
rag.question
rag.status
rag.source_count
```

Retrieval records:

```text
retrieval.top_k
retrieval.document_count
```

The guardrail records:

```text
guardrail.allowed
guardrail.reason
```

Context construction records:

```text
context.document_count
context.length
```

LLM generation records:

```text
llm.provider
llm.answer.length
```

---

# 19. Phoenix Evaluation

Retrieval evaluation is performed against a curated evaluation dataset:

```text
data/evaluation/retrieval_eval.json
```

The evaluation currently contains five validated cases:

| Case | Domain |
|---|---|
| ds-001 | Data Science |
| ml-001 | Machine Learning |
| dl-001 | Deep Learning |
| pt-001 | PyTorch |
| nlp-001 | NLP |

The TensorFlow evaluation case was not retained because the currently indexed TensorFlow document did not provide a sufficiently explicit top-ranked `tf.data` relevance target. The evaluation dataset therefore avoids fabricating relevance labels.

---

# 20. Retrieval Metrics

The implementation calculates:

## Hit@K

Hit@K measures whether at least one relevant document appears in the top K retrieved documents.

```text
Hit@K = 1 if a relevant document appears in top K
        0 otherwise
```

## Recall@K

Recall@K measures the proportion of known relevant documents retrieved within the top K.

```text
Recall@K =
relevant retrieved documents / total relevant documents
```

The project also contains reciprocal-rank utilities for future evaluation extensions.

---

# 21. Run Evaluation

Run:

```powershell
$env:PYTHONPATH = (Get-Location).Path
python scripts/run_evaluation.py
```

The verified evaluation output is:

```text
ds-001: Hit@5=1.000 Recall@5=1.000
ml-001: Hit@5=1.000 Recall@5=1.000
dl-001: Hit@5=1.000 Recall@5=1.000
pt-001: Hit@5=1.000 Recall@5=1.000
nlp-001: Hit@5=1.000 Recall@5=1.000
```

The evaluation script also submits:

```text
retrieval_hit_at_5
retrieval_recall_at_5
```

as Phoenix span annotations.

The verified implementation successfully submitted:

```text
10 annotations
```

corresponding to two evaluation metrics for each of the five cases.

---

# 22. Evaluation Evidence in Phoenix

The Phoenix evaluation spans contain attributes including:

```text
evaluation.case_id
evaluation.question
evaluation.hit_at_5
evaluation.recall_at_5
```

The Phoenix annotations contain:

```text
retrieval_hit_at_5
retrieval_recall_at_5
```

Each verified evaluation case currently has:

```text
Hit@5    = 1.0
Recall@5 = 1.0
```

Evaluation screenshots are stored under:

```text
evidence/06_evaluation/
```

---

# 23. Automated Testing

Run the complete test suite:

```powershell
$env:PYTHONPATH = (Get-Location).Path
pytest -q
```

Verified result:

```text
............ [100%]

12 passed in 12.58s
```

The test suite covers:

- PDF loading
- Chunking
- Embeddings
- Weaviate
- Dense retrieval
- BM25 retrieval
- Hybrid retrieval
- Guardrails
- RAG pipeline
- Evaluation

---

# 24. Evidence Organization

The project maintains evidence by rubric section:

```text
evidence/
│
├── 01_observability/
│
├── 02_vector_indexing/
│
├── 03_hybrid_search/
│
├── 04_guardrail/
│
├── 05_tracing/
│
└── 06_evaluation/
```

## Evidence mapping

### 01 — Observability

Evidence should demonstrate:

- Phoenix installation
- Phoenix startup
- Phoenix dashboard
- Project availability on port 6006

### 02 — Vector Indexing

Evidence should demonstrate:

- Weaviate running
- `KnowledgeChunk` collection
- PDF ingestion
- 924 indexed chunks
- local embeddings

### 03 — Hybrid Search

Evidence should demonstrate:

- Dense retrieval
- BM25 retrieval
- Hybrid retrieval

### 04 — Guardrail

Evidence should demonstrate:

- allowed query
- prompt-injection detection
- blocked malicious request

### 05 — Tracing

Evidence should demonstrate the Phoenix trace:

```text
rag_pipeline
├── input_sanitization
├── hybrid_retrieval
├── context_builder
├── prompt_construction
└── llm_generation
```

### 06 — Evaluation

Evidence should demonstrate:

- evaluation cases
- Hit@5
- Recall@5
- Phoenix annotations

---

# 25. Reproducibility

A clean reproduction follows this order:

```powershell
# 1. Activate environment
.\.venv\Scripts\Activate.ps1

# 2. Configure Python path
$env:PYTHONPATH = (Get-Location).Path

# 3. Start Weaviate
docker compose up -d

# 4. Create schema
python scripts/create_weaviate_schema.py

# 5. Ingest PDFs
python scripts/ingest_documents.py

# 6. Start Phoenix separately
$env:PHOENIX_HOST="127.0.0.1"
$env:PHOENIX_PORT="6006"
python -m phoenix.server.main serve

# 7. Run RAG demo
python scripts/run_demo.py

# 8. Run evaluation
python scripts/run_evaluation.py

# 9. Run tests
pytest -q
```

---

# 26. Operational Notes

## Weaviate Port

The local Windows environment already had another service using port 8080. Therefore the project maps:

```text
Host:      8081
Container: 8080
```

Do not change this configuration unless the local environment changes.

## Phoenix Port

Phoenix uses:

```text
127.0.0.1:6006
```

## Python Version

The verified environment uses:

```text
Python 3.10.11
```

The current Phoenix OTEL setup uses the installed compatible Phoenix OTEL release rather than upgrading to a release that requires Python 3.11+.

---

# 27. Known Implementation Detail — Phoenix OTEL

The installed Phoenix environment includes:

```text
arize-phoenix 20.16.0
arize-phoenix-otel 0.17.1
```

The project's tracing implementation uses Phoenix OTEL components directly:

```text
TracerProvider
SimpleSpanProcessor
HTTPSpanExporter
```

instead of the higher-level `phoenix.otel.register()` helper.

This was necessary in the verified Python 3.10 environment because the installed dependency combination otherwise produced an exporter/header compatibility error.

The resulting tracing setup has been verified by sending traces successfully to:

```text
http://127.0.0.1:6006
```

---
## Conclusion

This case study demonstrates an observable and guarded RAG knowledge assistant that combines semantic and lexical retrieval, local model inference, prompt-injection protection, distributed tracing, and retrieval-quality evaluation.
