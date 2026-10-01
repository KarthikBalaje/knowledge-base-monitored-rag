from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen3:8b"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_batch_size: int = 32
    weaviate_host: str = "localhost"
    weaviate_port: int = 8081
    weaviate_grpc_port: int = 50051
    phoenix_host: str = "localhost"
    phoenix_port: int = 6006
    chunk_size: int = 800
    chunk_overlap: int = 100
    top_k: int = 5
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCUMENT_ROOT = PROJECT_ROOT / "data" / "documents"
EVALUATION_ROOT = PROJECT_ROOT / "data" / "evaluation"
