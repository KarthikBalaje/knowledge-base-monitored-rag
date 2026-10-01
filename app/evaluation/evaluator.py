def evaluate_retrieval(cases, retriever, k=5):
    results=[]
    for case in cases:
        raw=retriever(case["question"], k)
        ids=[o.properties.get("chunk_id", "") for o in getattr(raw, "objects", [])]
        relevant=set(case.get("relevant_documents", []))
        from app.evaluation.retrieval_metrics import hit_at_k, recall_at_k
        results.append({"id":case["id"], "hit_at_k":hit_at_k(ids,relevant,k), "recall_at_k":recall_at_k(ids,relevant,k)})
    return results
