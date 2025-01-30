from langchain.agents import create_react_agent, AgentExecutor
import tools
import model
import prompt


#### AGENT ####
def generate_code_with_agent(language):
    """
    Generate a code using a LangChain agent with a Shakespearean-style prompt.

    Args:
        language(str) : enter code statement

    Returns:
        str: Generated code.
    """
    # Define tools for the agent
    tools_list = [tools.code_generator_tool()]

    # Initialize the agent with the Shakespearean-style prompt template
    prompt_template = prompt.code_generator_agent()
    llm = model.create_chat_groq_model()
    agent = create_react_agent(tools=tools_list, llm=llm, prompt=prompt_template)
    agent_executor = AgentExecutor(agent=agent, tools=tools_list, handle_parsing_errors=True, verbose=True, stop_sequence=True, max_iterations=3)

    # Agent interaction
    response = agent_executor.invoke({"input":language})
    return response

#### AGENT WITH RAG ####
def generate_code_with_rag_agent(language, vector):
    """
    Generate a code using a LangChain agent with Retrieval-Augmented Generation (RAG).

    Args:
        language (str): enter code statement
        vector (object): Instance of vector store

    Returns:
        str: Generated code
    """
    # Define tools for the agent
    tools_list = [
        tools.rag_retriever_tool(vector),
        tools.code_generator_tool()
    ]

    # Initialize the agent with the RAG-enabled prompt template
    prompt_template = prompt.code_generator_agent_with_rag()
    llm = model.create_chat_groq_model()
    agent = create_react_agent(tools=tools_list, llm=llm, prompt=prompt_template)
    agent_executor = AgentExecutor(agent=agent, tools=tools_list, handle_parsing_errors=True, verbose=True, stop_sequence=True, max_iterations=3)

    # Agent interaction
    response = agent_executor.invoke({"input":language})
    return response
