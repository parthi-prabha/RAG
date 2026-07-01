from src.embeddings import get_embeddings

embedding = get_embeddings()

vector = embedding.embed_query("What is python")

print(type(vector))
print(len(vector))
print(vector)
print(vector[:5])