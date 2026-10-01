from app.rag.rag_pipeline import RAGPipeline

def main():
    pipeline = RAGPipeline()
    question = input("Question: ").strip()
    result = pipeline.answer(question)
    print("\nAnswer:\n")
    print(result.answer)

if __name__ == "__main__":
    main()
