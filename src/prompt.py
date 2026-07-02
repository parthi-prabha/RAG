from langchain_core.prompts import ChatPromptTemplate

def get_prompt():

    prompt = ChatPromptTemplate.from_template(
        """You are an expert AI assistant.

        Use ONLY the provided context to answer the user's question.

        Instructions:
        - Answer only from the retrieved context.
        - If the answer is not found in the context, say:
          "I couldn't find the answer in the provided documents."
        - Do not make up information.
        - Keep the answer clear and concise.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

    return prompt