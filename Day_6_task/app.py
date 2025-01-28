import random
from dotenv import load_dotenv
import streamlit as st
import chain

load_dotenv()

def Code_Generator():
    """
    Code Generator Bot
    """
    with st.form("Code_Generator"):
        st.write("## 🤖 The No-Nonsense Code Generator")
    
        language= st.text_input("Yo, what language we talkin' today? 🗣️")
        problem_statement = st.text_input("💡 Tell me your problem! 🧐 (Not emotional problems, though—I’m not here for that stuff.) 🤷‍♀️")
        submitted = st.form_submit_button("Here u go again!!!",type="primary")
        if(submitted):
            response =chain.Generate_code(language,problem_statement)
            st.info(response)
            st.write(random.choice([
                "🤓 Boom! Now go and pretend you wrote this yourself.",
                
            ]))

        

Code_Generator()