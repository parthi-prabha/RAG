import typesense
from langchain_community.vectorstores import Typesense

from src.config import TYPESENSE_CONFIG, COLLECTION_NAME
from src.embeddings import get_embeddings

def get_retriever():

    # Typesense Client
    client = typesense.Client(TYPESENSE_CONFIG) 

    # Embeddings
    embeddings = get_embeddings()

    # Typesense Vector Store
    vector_store = Typesense(
        typesense_client=client,
        typesense_collection_name=COLLECTION_NAME,
        embedding=embeddings,
        text_key="text"
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    return retriever