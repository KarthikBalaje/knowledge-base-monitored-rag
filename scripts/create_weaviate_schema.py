from app.vector_store.index_manager import get_collection
if __name__ == "__main__":
    client,c=get_collection(); print(f"Collection ready: {c.name}"); client.close()
