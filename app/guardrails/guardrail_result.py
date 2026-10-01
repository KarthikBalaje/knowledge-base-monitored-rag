from dataclasses import dataclass
@dataclass(frozen=True)
class GuardrailResult:
    allowed: bool
    reason: str = ""
