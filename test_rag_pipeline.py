from src.rag_pipeline import RAGPipeline

rag = RAGPipeline()

result = rag.ask("What is Python?")

print("\nAnswer")
print("-" * 50)
print(result["answer"])

print("\nSources")
print("-" * 50)

for source in result["sources"]:
    print(source)