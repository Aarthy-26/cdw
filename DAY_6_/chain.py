from model import create_chat_groq
import prompt
def generate_poem(topic):
    """ 
    function to generate_poem

    Args:
        topic(str)

    returns 
        response.content(str)
    """

    prompt_template=prompt.poem_generator_prompt()
    llm = create_chat_groq()

    chain = prompt_template | llm

    response = chain.invoke({"topic":topic})
    return response.content
