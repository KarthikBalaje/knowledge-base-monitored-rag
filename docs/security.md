# Security and Guardrails

User queries are inspected before entering the RAG pipeline.

The input sanitizer detects common prompt-injection patterns such as:

- Ignore previous instructions
- Ignore all previous instructions
- Reveal the system prompt
- Show the hidden prompt
- Bypass safety instructions
- Override previous instructions
- Jailbreak-style instructions

Blocked queries do not continue through retrieval or generation.

Retrieved documents are treated as untrusted reference material.
