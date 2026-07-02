from src.llm import get_llm
from src.retriever import get_retriever
from src.prompt import get_prompt
from src.utils import format_context, get_sources
class RAGPipeline:

    """
    Retrieval Augumented Pipeline"""

    def __init__(self):
        self.llm = get_llm()
        self.retriever = get_retriever()
        self.prompt = get_prompt()
    
    def ask(self, question: str):

        # docment retrieval
        docs = self.retriever.invoke(question)

        #context creation
        context = format_context(docs)

        # prompt creation
        prompt = self.prompt.invoke(
            {
                'context' : context,
                'question' : question
            }
        )

        #llm work
        response = self.llm.invoke(prompt)

        return {
            'answer' : response.content,
            'documents' : docs,
            'sources' : get_sources(docs)
        }


