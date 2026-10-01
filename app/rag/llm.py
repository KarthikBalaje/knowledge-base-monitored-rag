from app.rag.ollama_client import OllamaClient
class LLM:
    def __init__(self): self.client=OllamaClient()
    def generate(self, prompt): return self.client.generate(prompt)
