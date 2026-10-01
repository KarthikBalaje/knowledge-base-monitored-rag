from app.retrieval.dense_retriever import dense_search
if __name__ == "__main__":
    for o in dense_search(input("Dense query: ")).objects: print(o.properties)
