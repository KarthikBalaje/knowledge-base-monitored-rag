from app.rag.rag_pipeline import RAGPipeline
if __name__ == "__main__":
    p=RAGPipeline()
    while True:
        q=input("\nQuestion (or exit): ").strip()
        if q.lower()=="exit": break
        print(p.answer(q).answer)
