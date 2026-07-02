from src.retriever import get_retriever

retriever = get_retriever()

docs = retriever.invoke("What is python")

for doc in docs:
    print(doc.page_content)