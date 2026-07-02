from src.prompt import get_prompt

prompt = get_prompt()

messages = prompt.invoke(
    {
        'context' : "Python is programming language",
        'question' : "What is python"
    }
)

print(messages)