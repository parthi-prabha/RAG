from langchain_core.documents import Document

from src.utils import format_context, get_sources

docs = [
    Document(
        page_content="Python is a programming language.",
        metadata={"source": "python_intro.txt"},
    ),
    Document(
        page_content="Python supports OOP.",
        metadata={"source": "python_intro.txt"},
    ),
    Document(
        page_content="RAG combines retrieval and generation.",
        metadata={"source": "rag.txt"},
    ),
]

print("Context:")
print(format_context(docs))

print("\nSources:")
print(get_sources(docs))