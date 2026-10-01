from app.knowledge_base.ingestion_pipeline import build_chunks
from app.knowledge_base.embeddings import embed_texts
from app.vector_store.index_manager import get_collection

def main():
    chunks=build_chunks()
    if not chunks: print("No PDF text found."); return
    vectors=embed_texts([c.text for c in chunks])
    client, collection=get_collection()
    try:
        with collection.batch.dynamic() as batch:
            for c,v in zip(chunks,vectors):
                batch.add_object(properties={"text":c.text,"source":c.source,"domain":c.domain,"page_number":c.page_number,"chunk_id":c.chunk_id}, vector=v.tolist())
    finally: client.close()
    print(f"Indexed {len(chunks)} chunks.")
if __name__ == "__main__": main()
