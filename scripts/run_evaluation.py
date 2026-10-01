import json

import pandas as pd

from app.config import EVALUATION_ROOT
from app.evaluation.evaluator import evaluate_retrieval
from app.evaluation.retrieval_metrics import (
    hit_at_k,
    recall_at_k,
)
from app.observability.tracing import (
    get_tracer,
    setup_tracing,
)
from app.retrieval.hybrid_retriever import hybrid_search
from app.retrieval.result_formatter import format_retrieval

from phoenix.client import Client


PHOENIX_URL = "http://127.0.0.1:6006"


def load_evaluation_cases():
    return json.loads(
        (EVALUATION_ROOT / "retrieval_eval.json").read_text(
            encoding="utf-8"
        )
    )["evaluation_cases"]


def main():

    cases = load_evaluation_cases()

    tracer = get_tracer()

    phoenix_client = Client(
        base_url=PHOENIX_URL
    )

    annotations = []

    print("\n=== Retrieval Evaluation ===\n")

    for case in cases:

        with tracer.start_as_current_span(
            "retrieval_evaluation"
        ) as span:

            question = case["question"]
            relevant = set(
                case.get("relevant_documents", [])
            )

            result = hybrid_search(
                question,
                5,
                0.5,
            )

            docs = format_retrieval(result)

            retrieved_ids = [
                doc.get("chunk_id", "")
                for doc in docs
            ]

            hit = hit_at_k(
                retrieved_ids,
                relevant,
                5,
            )

            recall = recall_at_k(
                retrieved_ids,
                relevant,
                5,
            )

            span.set_attribute(
                "evaluation.case_id",
                case["id"],
            )

            span.set_attribute(
                "evaluation.question",
                question,
            )

            span.set_attribute(
                "evaluation.hit_at_5",
                hit,
            )

            span.set_attribute(
                "evaluation.recall_at_5",
                recall,
            )

            print(
                f"{case['id']}: "
                f"Hit@5={hit:.3f} "
                f"Recall@5={recall:.3f}"
            )

            span_context = span.get_span_context()

            span_id = format(
                span_context.span_id,
                "016x",
            )

            annotations.append(
                {
                    "span_id": span_id,
                    "annotation_name": "retrieval_hit_at_5",
                    "annotator_kind": "CODE",
                    "score": hit,
                    "label": "hit_at_5",
                    "explanation": (
                        f"Hit@5 for evaluation case "
                        f"{case['id']}"
                    ),
                }
            )

            annotations.append(
                {
                    "span_id": span_id,
                    "annotation_name": "retrieval_recall_at_5",
                    "annotator_kind": "CODE",
                    "score": recall,
                    "label": "recall_at_5",
                    "explanation": (
                        f"Recall@5 for evaluation case "
                        f"{case['id']}"
                    ),
                }
            )

            # Build evaluation annotations after all evaluation spans are created.
    annotation_df = pd.DataFrame(annotations)

    # Force the OpenTelemetry provider to export the spans to Phoenix
    # before we attempt to attach annotations to those spans.
    tracer_provider = setup_tracing()
    tracer_provider.force_flush()

    if not annotation_df.empty:
        for annotation in annotations:
            phoenix_client.spans.add_span_annotation(
                span_id=annotation["span_id"],
                annotation_name=annotation["annotation_name"],
                annotator_kind=annotation["annotator_kind"],
                score=annotation["score"],
                label=annotation["label"],
                explanation=annotation["explanation"],
                sync=True,
            )

    print("\n=== Phoenix Evaluation Annotations ===")

    print(
        annotation_df[
            [
                "span_id",
                "annotation_name",
                "score",
            ]
        ].to_string(index=False)
    )

    print(
        "\nEvaluation annotations successfully "
        "submitted to Phoenix."
    )

if __name__ == "__main__":
    main()