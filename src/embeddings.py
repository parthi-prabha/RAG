from langchain_huggingface import HuggingFaceEmbeddings

from src.config import EMBEDDING_MODEL

def get_embeddings():
    """
    Load and return the huggingface embedding model
    """

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return embeddings
