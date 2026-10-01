from sentence_transformers import SentenceTransformer
from app.config import settings

_model = None

def get_embedding_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(settings.embedding_model)
    return _model

def embed_texts(texts):
    return get_embedding_model().encode(texts, batch_size=settings.embedding_batch_size, normalize_embeddings=True, show_progress_bar=True)

def embed_query(query):
    return get_embedding_model().encode(query, normalize_embeddings=True)
