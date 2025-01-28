from model import create_chat_gorq
from prompt import Code_Generator_prompt

def Generate_code(language,problem_statement):
    """
    Function to initialize chat gorq
    Args:
        language (str) - programming language for which code is to be generated
        problem_statement (str) - the problem statement for the code generation
    Returns:
        response.content (str) - generated code as a response
    """
    prompt_template = Code_Generator_prompt()
    llm =create_chat_gorq()
    
    chain = prompt_template | llm
    
    response = chain.invoke({
        "programming_language": language,
        "problem_statement": problem_statement
    })
    return response.content