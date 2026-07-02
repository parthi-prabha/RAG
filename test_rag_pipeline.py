from src.rag_pipeline import RAGPipeline

rag = RAGPipeline()

result = rag.ask("What is Python?")

print("\nAnswer:\n")
print(result["answer"])

print("\nRetrieved Documents:\n")

for i, doc in enumerate(result["documents"], start=1):
    print(f"Document {i}")
    print("-" * 50)
    print(doc.page_content[:300])
    print()