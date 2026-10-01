import re
from app.guardrails.injection_patterns import INJECTION_PATTERNS
from app.guardrails.guardrail_result import GuardrailResult

def sanitize_query(query: str) -> GuardrailResult:
    normalized=re.sub(r"\s+", " ", query.lower()).strip()
    for pattern in INJECTION_PATTERNS:
        if pattern in normalized:
            return GuardrailResult(False, f"Prompt injection pattern detected: {pattern}")
    return GuardrailResult(True)
