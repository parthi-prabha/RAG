from langchain_groq import ChatGroq

from src.config import GROQ_API_KEY, LLM_MODEL

def get_llm():
    """
    Initialize and return the Groq LLM model
    """
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=LLM_MODEL,
        temperature=0
    )

    return llm