# Evaluation Mapping

The project implementation maps to the 100-point evaluation rubric:

| Requirement | Points | Implementation |
|---|---:|---|
| Phoenix Observability | 15 | `app/observability/` |
| Vector Indexing | 15 | `app/vector_store/` |
| Hybrid Search | 20 | `app/retrieval/` |
| Input Sanitization Guardrail | 20 | `app/guardrails/` |
| Phoenix Tracing | 15 | `app/observability/tracing.py` |
| Retrieval Evaluation | 15 | `app/evaluation/` |
| **Total** | **100** | |

Evidence for each requirement is stored under:

```text
evidence/
```

with separate folders for each rubric item.
