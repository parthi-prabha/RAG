from langchain_core.documents import Document


def format_context(documents: list[Document]) -> str:
    """
    Convert a list of LangChain Documents into a single context string.
    """

    return "\n\n".join(doc.page_content for doc in documents)


def get_sources(documents: list[Document]) -> list[str]:
    """
    Extract unique source file names from retrieved documents.
    """

    sources = []

    for doc in documents:
        source = doc.metadata.get("source", "Unknown")

        if source not in sources:
            sources.append(source)

    return sources