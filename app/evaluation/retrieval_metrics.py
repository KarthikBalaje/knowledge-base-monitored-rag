def hit_at_k(retrieved_ids, relevant_ids, k): return float(bool(set(retrieved_ids[:k]) & set(relevant_ids)))
def recall_at_k(retrieved_ids, relevant_ids, k):
    relevant=set(relevant_ids)
    return 0.0 if not relevant else len(set(retrieved_ids[:k]) & relevant)/len(relevant)
def reciprocal_rank(retrieved_ids, relevant_ids):
    relevant=set(relevant_ids)
    for rank, item in enumerate(retrieved_ids, 1):
        if item in relevant: return 1.0/rank
    return 0.0
def mean_reciprocal_rank(results):
    return sum(reciprocal_rank(a,b) for a,b in results)/len(results) if results else 0.0
