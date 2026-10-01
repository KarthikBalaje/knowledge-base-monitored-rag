# Evaluation

Retrieval evaluation data is stored in:

data/evaluation/retrieval_eval.json

The evaluation module provides retrieval-quality metrics including:

- Hit@K
- Recall@K
- Mean Reciprocal Rank (MRR)

Run the evaluation with:

```powershell
python scripts/run_evaluation.py
```

The evaluation results are intended to provide evidence that can be inspected through Phoenix.
