from app.knowledge_base.embeddings import embed_query
from app.vector_store.index_manager import get_collection

def hybrid_search(query, limit=5, alpha=0.5):
    client, collection=get_collection()
    try: return collection.query.hybrid(query=query, vector=embed_query(query).tolist(), alpha=alpha, limit=limit)
    finally: client.close()
