from langchain_core.output_parsers import StrOutputParser
import model
import prompt
import vectordb


#### GENERATION ####
def generate_code_chain(language, problem):
    """
    Generate Code using basic prompt LLM chain based on the programming language and problem.

    Args:
        language - Programming language for the code generation.
        problem - Problem/task description for the code generation.

    Returns:
        response.content -> str
    """
    llm = model.create_chat_groq_model()

    # Modify the prompt to include language and problem
    prompt_template = prompt.code_generator_prompt(language, problem)

    chain = prompt_template | llm

    response = chain.invoke({
        "language": language,
        "problem": problem
    })
    return response.content


#### RETRIEVAL and GENERATION ####

def generate_code_rag_chain(language, problem, vector):
    """
    Creates a RAG chain for code generation using retrieval based on the programming language and problem.

    Args:
        language - Programming language for the code generation.
        problem - Problem/task description for the code generation.
        vectorstore -> Instance of vector store 

    Returns:
        rag_chain -> rag chain
    """
    # Prompt
    prompts = prompt.code_generator_rag_prompt(language, problem)

    # LLM
    llm = model.create_chat_groq_model()

    # Post-processing
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    retriever = vectordb.retrieve_from_chroma(problem, vectorstore=vector)
    
    # Chain
    rag_chain = prompts | llm | StrOutputParser()

    response = rag_chain.invoke({
        "context": format_docs(retriever),
        "language": language,
        "problem": problem
    })    

    return response