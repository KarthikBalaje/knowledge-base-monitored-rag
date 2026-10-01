from app.retrieval.bm25_retriever import bm25_search
if __name__ == "__main__":
    for o in bm25_search(input("BM25 query: ")).objects: print(o.properties)
