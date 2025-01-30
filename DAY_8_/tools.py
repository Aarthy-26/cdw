from langchain.agents import Tool
import chain
from vectordb import retrieve_from_chroma

def code_generator_tool():
    """
    Generate a tool that can create codes.

    Args:
        topic - enter programming language

    Returns:
        Code generator Tool 
    """
    return Tool(
            name="Code Generator",
            func=lambda language: chain.generate_code_chain(language),
            description="Generates a code based on a given language.",
        )

def rag_retriever_tool(vector):
    """
    Create a Tool for retrieving relevant documents using RAG

    Args:
        vector (object): The vector store instance.

    Returns:
        Tool: A LangChain Tool object for RAG retrieval.
    """
    return Tool(
            name="RAG Retriever",
            func=lambda language: "\n\n".join(
                doc.page_content for doc in retrieve_from_chroma(language, vectorstore=vector)
            ),
            description="Retrieves relevant documents for a given topic using a vector store."
        )
