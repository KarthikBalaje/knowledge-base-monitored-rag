from app.knowledge_base.embeddings import embed_texts
def test_embedding_shape(): assert len(embed_texts(["test"])[0])==384
