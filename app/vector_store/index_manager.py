import weaviate.classes.config as wc
from app.vector_store.schema import COLLECTION_NAME
from app.vector_store.weaviate_client import connect

def ensure_collection(client):
    if client.collections.exists(COLLECTION_NAME):
        return client.collections.get(COLLECTION_NAME)
    return client.collections.create(
        name=COLLECTION_NAME,
        vectorizer_config=wc.Configure.Vectorizer.none(),
        properties=[
            wc.Property(name="text", data_type=wc.DataType.TEXT),
            wc.Property(name="source", data_type=wc.DataType.TEXT),
            wc.Property(name="domain", data_type=wc.DataType.TEXT),
            wc.Property(name="page_number", data_type=wc.DataType.INT),
            wc.Property(name="chunk_id", data_type=wc.DataType.TEXT),
        ],
    )

def get_collection():
    client=connect()
    return client, ensure_collection(client)
