from app.retrieval.hybrid_retriever import hybrid_search
if __name__ == "__main__":
    for o in hybrid_search(input("Hybrid query: ")).objects: print(o.properties)
