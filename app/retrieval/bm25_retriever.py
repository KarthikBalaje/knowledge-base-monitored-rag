from app.vector_store.index_manager import get_collection

def bm25_search(query, limit=5):
    client, collection=get_collection()
    try: return collection.query.bm25(query=query, limit=limit)
    finally: client.close()
