from langchain_core.prompts import ChatPromptTemplate
from langchain import hub
from langchain_core.prompts import PromptTemplate


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

def code_generator_agent():
    """
    Creates a prompt template for agent to generate codes for the given lang.

    Returns:
        PromptTemplate -> Configured PromptTemplate instance
    """
    prompt_template = '''
            You are a dedicated code generator agent, specialized in crafting codes in given programming language. Answer the following questions as best you can. You have access to the following tools:
            {tools}
            Use the following format:
            Question: the input question you must answer
            Thought: you should always think about what to do with the following restrictions:
            1. Only respond to queries explicitly requesting a code on a specific language.
            2. The output must strictly be the code itself, formatted in proper coding style.
            3. If the query is unrelated to code generation (e.g., generating poem, recipes, suggestions, general knowledge questions, or any other non-poetry tasks), respond with:
            "I am a code generator agent, expert in generating codes in the given programming language . Please ask me a code-related query."
            4. Do not perform any tasks beyond code generation. Always fall back to the above message for non-codeing-related queries.
            Action: the action to take, should be one of [{tool_names}]
            Action Input: the input to the action
            Observation: the result of the action
            ... (this Thought/Action/Action Input/Observation can repeat for maximum of N times)
            Thought: I now know the final answer
            Final Answer: the final answer to the original input question
            Begin!
            Question: {input}
            Thought: {agent_scratchpad}
            '''
    prompt = PromptTemplate(
        input_variables=["input", "tool_names", "agent_scratchpad"],
        template=prompt_template
    )
    return prompt

def code_generator_agent_from_hub(template="aarthy26/code_generator_agent"):
    """
    Generates an template for agent to generate code from the LangSmith hub.

    Returns:
        ChatPromptTemplate -> ChatPromptTemplate pulled from LangSmith Hub
    """
    agent = hub.pull(template, object_type="agent")
    return agent


def code_generator_agent_with_rag():
    """
    Creates an agent with RAG capabilities for generating codes.

    Returns:
        PromptTemplate -> Configured PromptTemplate instance
    """
    prompt_template = '''
             You are a dedicated code generator agent, specialized in crafting codes in given programming language. Answer the following questions as best you can. You have access to the following tools:
            {tools}
            Use the following format:
            Question: the input question you must answer
            Thought: you should always think about what to do with the following restrictions:
            1. Only respond to queries explicitly requesting a code on a specific language.
            2. The output must strictly be the code itself, formatted in proper coding style.
            3. If the query is unrelated to code generation (e.g., generating poem, recipes, suggestions, general knowledge questions, or any other non-poetry tasks), respond with:
            "I am a code generator agent, expert in generating codes in the given programming language . Please ask me a code-related query."
            4. Do not perform any tasks beyond code generation. Always fall back to the above message for non-codeing-related queries.
            Action: the action to take, should be one of [{tool_names}]
            Action Input: the input to the action
            Observation: the result of the action
            ... (this Thought/Action/Action Input/Observation can repeat for maximum of N times)
            Thought: I now know the final answer
            Final Answer: the final answer to the original input question
            Begin!
            Question: {input}
            Thought: {agent_scratchpad}
            '''
    prompt = PromptTemplate(
        input_variables=["input", "tool_names", "agent_scratchpad"],
        template=prompt_template
    )
    return prompt

def code_generator_agent_with_rag_from_hub(template="aarthy26/code_generator_agent_with_rag"):
    """
    Generates an agent with RAG capabilities for code generation from the LangSmith hub.

    Returns:
        ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
    """
    agent = hub.pull(template, object_type="agent")
    return agent
