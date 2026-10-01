import json
from app.config import EVALUATION_ROOT

def load_evaluation_cases():
    return json.loads((EVALUATION_ROOT / "retrieval_eval.json").read_text(encoding="utf-8"))["evaluation_cases"]
