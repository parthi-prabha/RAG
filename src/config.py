import os
from dotenv import load_dotenv

load_dotenv()

# Groq configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "openai/gpt-oss-20b"

# Typesense configuration
TYPESENSE_CONFIG = {
    'nodes' : [{
        'host' : os.getenv("TYPESENSE_HOST"),
        'port' : os.getenv("TYPESENSE_PORT", "443"),
        'protocol' : 'https'
    }],
    'api_key' : os.getenv("TYPESENSE_API_KEY"),
    'connection_timeout_seconds' : 30

}

COLLECTION_NAME = "lang-chain"

# Embedding model configuration
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"



