from app.knowledge_base.embeddings import embed_query
from app.vector_store.index_manager import get_collection

def dense_search(query, limit=5):
    client, collection=get_collection()
    try:
        return collection.query.near_vector(near_vector=embed_query(query).tolist(), limit=limit, return_metadata=["distance"])
    finally: client.close()
