from dataclasses import dataclass

from app.config import settings
from app.guardrails.input_sanitizer import sanitize_query
from app.rag.context_builder import build_context
from app.rag.llm import LLM
from app.rag.prompts import build_prompt
from app.retrieval.hybrid_retriever import hybrid_search
from app.retrieval.result_formatter import format_retrieval
from app.observability.tracing import get_tracer


@dataclass
class RAGResult:
    answer: str
    sources: list[dict]


class RAGPipeline:

    def __init__(self):
        self.llm = LLM()
        self.tracer = get_tracer()

    def answer(self, question):

        with self.tracer.start_as_current_span("rag_pipeline") as span:

            span.set_attribute(
                "rag.question",
                question,
            )

            # --------------------------------------------------
            # 1. Input Guardrail
            # --------------------------------------------------

            with self.tracer.start_as_current_span(
                "input_sanitization"
            ) as guard_span:

                guard = sanitize_query(question)

                guard_span.set_attribute(
                    "guardrail.allowed",
                    guard.allowed,
                )

                if not guard.allowed:
                    guard_span.set_attribute(
                        "guardrail.reason",
                        guard.reason,
                    )

                    span.set_attribute(
                        "rag.status",
                        "blocked",
                    )

                    return RAGResult(
                        f"Request blocked by security guardrail: "
                        f"{guard.reason}",
                        [],
                    )

            # --------------------------------------------------
            # 2. Hybrid Retrieval
            # --------------------------------------------------

            with self.tracer.start_as_current_span(
                "hybrid_retrieval"
            ) as retrieval_span:

                result = hybrid_search(
                    question,
                    settings.top_k,
                    0.5,
                )

                docs = format_retrieval(result)

                retrieval_span.set_attribute(
                    "retrieval.top_k",
                    settings.top_k,
                )

                retrieval_span.set_attribute(
                    "retrieval.document_count",
                    len(docs),
                )

            # --------------------------------------------------
            # 3. Context Building
            # --------------------------------------------------

            with self.tracer.start_as_current_span(
                "context_builder"
            ) as context_span:

                context = build_context(docs)

                context_span.set_attribute(
                    "context.document_count",
                    len(docs),
                )

                context_span.set_attribute(
                    "context.length",
                    len(context),
                )

            # --------------------------------------------------
            # 4. Prompt Construction
            # --------------------------------------------------

            with self.tracer.start_as_current_span(
                "prompt_construction"
            ) as prompt_span:

                prompt = build_prompt(
                    question,
                    context,
                )

                prompt_span.set_attribute(
                    "prompt.length",
                    len(prompt),
                )

            # --------------------------------------------------
            # 5. Ollama / LLM Generation
            # --------------------------------------------------

            with self.tracer.start_as_current_span(
                "llm_generation"
            ) as llm_span:

                answer = self.llm.generate(prompt)

                llm_span.set_attribute(
                    "llm.provider",
                    "ollama",
                )

                llm_span.set_attribute(
                    "llm.answer.length",
                    len(answer),
                )

            # --------------------------------------------------
            # 6. Final RAG Result
            # --------------------------------------------------

            span.set_attribute(
                "rag.status",
                "success",
            )

            span.set_attribute(
                "rag.source_count",
                len(docs),
            )

            return RAGResult(
                answer,
                docs,
            )