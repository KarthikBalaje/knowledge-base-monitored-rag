import ollama
from app.config import settings

class OllamaClient:
    def __init__(self):
        self.client=ollama.Client(host=settings.ollama_base_url)
        self.model=settings.ollama_model
    def generate(self, prompt: str) -> str:
        response=self.client.chat(model=self.model, messages=[{"role":"user","content":prompt}])
        return response["message"]["content"]
