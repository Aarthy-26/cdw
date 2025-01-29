# from langchain_core.prompts import ChatPromptTemplate
# from langchain import hub


# def Code_Generator_prompt():
#     """
#     Generates Prompt template from the LangSmith prompt hub
#     Returns:
#         ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
#     """
#     prompt_template = hub.pull("aarthy26/code_generator")
#     return prompt_template


# def Code_Generator_prompt():
#     """
#     Generates Prompt template from the system and user messages
#     Returns:
#         ChatPromptTemplate -> Configured ChatPromptTemplate instance
#     """
#     system_msg = '''
                # You are a dedicated code generator assistant, specialized in crafting code solutions in various programming languages. Your task is strictly to generate code based on the given problem statement and specified programming language. Follow these guidelines:
                # 1. Only respond to queries explicitly requesting a code solution in a specific programming language.
                # 2. The output must strictly be the code itself, formatted correctly with proper indentations, without additional explanations, descriptions, or headers.
                # 3. If the query is unrelated to code generation (e.g., generating poems, recipes, suggestions, general knowledge questions, or any other non-coding tasks), respond with:
                # "I am a code generator assistant, expert in generating code solutions in various programming languages. Please ask me a code-related query."
                # 4. Do not perform any tasks beyond code generation. Always fall back to the above message for non-code-related queries.
                # Note: The assistant must ensure the generated code aligns with the requested programming language and problem statement.
                # '''
#     user_msg = "Write a code in {programming_language} to solve the problem: {problem_statement}"
#     prompt_template = ChatPromptTemplate([
#         ("system", system_msg),
#         ("user", user_msg)
#     ])
#     return prompt_template






from langchain_core.prompts import ChatPromptTemplate
from langchain import hub

def code_generator_prompt(language, problem):
    """
    Generates Prompt template for code generation with basic context.

    Args:
        language -> str: The programming language for code generation (e.g., "Python").
        problem -> str: The problem or task description for code generation.

    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    """

    system_msg = f'''
                You are an expert code generator assistant. Your task is to generate code in {language} based on the user’s provided specifications. Follow these guidelines:

                1. Only respond to queries explicitly requesting code generation.
                2. The output must strictly be the code, properly formatted, without additional explanations or descriptions.
                3. If the query is unrelated to code generation (e.g., generating recipes, suggestions, general knowledge questions, or any other non-coding tasks), respond with:
                "I am a code generator assistant. Please provide a code-related query."
                4. Do not perform any tasks beyond code generation. Always fall back to the above message for non-code-related queries.

                Note: Ensure the generated code aligns with the user’s request and is functional.
                ''' 

    user_msg = f"Write a {language} function to {problem}"

    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])
    
    return prompt_template

def code_generator_rag_prompt(language, problem):
    """
    Generates a RAG-enabled Prompt template for code generation.

    Args:
        language -> str: The programming language for code generation (e.g., "Python").
        problem -> str: The problem or task description for code generation.

    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    """

    system_msg = f'''
                You are an expert code generator assistant, specialized in creating {language} code. Your task is to generate code based on the user's request and also integrate any relevant context provided by external sources.

                1. Only respond to queries explicitly requesting code generation.
                2. The output must strictly be the code, properly formatted, without additional explanations or descriptions.
                3. If the query is unrelated to code generation (e.g., generating recipes, suggestions, general knowledge questions, or any other non-coding tasks), respond with:
                "I am a code generator assistant. Please provide a code-related query."
                4. Do not perform any tasks beyond code generation. Always fall back to the above message for non-code-related queries.

                Additionally, incorporate relevant context from external sources if provided in the conversation. Ensure the generated code reflects the nuances of the provided context style.
                '''

    user_msg = f"Write a {language} function to {problem}, considering the following context: {{context}}"

    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])
    
    return prompt_template

def code_generator_rag_prompt_from_hub(template="aarthy26/code_generator_rag"):
    """
    Generates Prompt template from the LangSmith prompt hub for code generation.

    Returns:
        ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
    """
    
    prompt_template = hub.pull(template)
    return prompt_template