import weaviate
from app.config import settings

def connect():
    return weaviate.connect_to_local(host=settings.weaviate_host, port=settings.weaviate_port, grpc_port=settings.weaviate_grpc_port)
