from src.llm import get_llm

llm = get_llm()

query = input("Enter your query: ")
response = llm.invoke(query)

print(response.content)