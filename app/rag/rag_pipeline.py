from dataclasses import dataclass
from app.config import settings
from app.guardrails.input_sanitizer import sanitize_query
from app.rag.context_builder import build_context
from app.rag.llm import LLM
from app.rag.prompts import build_prompt
from app.retrieval.hybrid_retriever import hybrid_search
from app.retrieval.result_formatter import format_retrieval

@dataclass
class RAGResult:
    answer: str
    sources: list[dict]

class RAGPipeline:
    def __init__(self): self.llm=LLM()
    def answer(self, question):
        guard=sanitize_query(question)
        if not guard.allowed: return RAGResult(f"Request blocked by security guardrail: {guard.reason}", [])
        result=hybrid_search(question, settings.top_k, 0.5)
        docs=format_retrieval(result)
        answer=self.llm.generate(build_prompt(question, build_context(docs)))
        return RAGResult(answer, docs)
