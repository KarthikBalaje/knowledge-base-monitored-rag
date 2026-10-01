from app.evaluation.retrieval_metrics import hit_at_k, recall_at_k
def test_hit(): assert hit_at_k(["a","b"],["b"],2)==1.0
def test_recall(): assert recall_at_k(["a","b"],["b"],2)==1.0
