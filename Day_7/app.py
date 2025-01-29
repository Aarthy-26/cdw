# import random
# from dotenv import load_dotenv
# import streamlit as st
# import chain

# load_dotenv()

# def Code_Generator():
#     """
#     Code Generator Bot
#     """
#     with st.form("Code_Generator"):
#         st.write("## 🤖 The No-Nonsense Code Generator")
    
#         language= st.text_input("Yo, what language we talkin' today? 🗣️")
#         problem_statement = st.text_input("💡 Tell me your problem! 🧐 (Not emotional problems, though—I’m not here for that stuff.) 🤷‍♀️")
#         submitted = st.form_submit_button("Here u go again!!!",type="primary")
#         if(submitted):
#             response =chain.Generate_code(language,problem_statement)
#             st.info(response)
#             st.write(random.choice([
#                 "🤓 Boom! Now go and pretend you wrote this yourself.",
                
#             ]))

        

# Code_Generator()

import streamlit as st
import chain
import vectordb
import random
def code_generator_app():
    """
    Generates Code Generator App with Streamlit, providing user input and displaying output.
    Includes a sidebar with two sections: Code Generator and File Ingestion for RAG.
    """

    # Sidebar configuration
    st.sidebar.title("🚀 Code Generator Hub")
    section = st.sidebar.radio(
        "🔍 Choose a section:",
        ("Code Generator RAG", "RAG File Ingestion")
    )

    # db initialization
    vectordatabase = vectordb.initialize_chroma()

    # Condition for code generation page
    if section == "Code Generator RAG":
        st.title("🤖 The No-Nonsense Code Generator")

        with st.form("code_generator"):
            # Input for the programming language
            language = st.selectbox(
                "Yo, what language we talkin' today? 🗣️",
                ("Python", "JavaScript", "C++", "Java", "Ruby", "Go", "PHP","...")
            )
            
            # Input for the problem
            problem = st.text_input(
                "💡 Tell me your problem! 🧐 (Not emotional problems, though—I’m not here for that stuff.) 🤷‍♀️"
            )
            submitted = st.form_submit_button("Submit")

            toggle_state = st.checkbox("Check me to enable RAG")

            if submitted:
                if toggle_state:
                    # Passing both problem and language for code generation with RAG
                    response = chain.generate_code_rag_chain(language, problem, vectordatabase)
                else:
                    # Passing both problem and language for basic code generation
                    response = chain.generate_code_chain(language, problem)
                
                st.code(response, language=language.lower())
                st.write(random.choice([
                "🤓 Boom! Now go and pretend you wrote this yourself.",
                
                ]))

    
    # Condition for RAG File Ingestion
    elif section == "RAG File Ingestion":
        st.title("RAG File Ingestion")

        uploaded_file = st.file_uploader("Upload a file:", type=["txt", "csv", "docx", "pdf"])

        if uploaded_file is not None:
            vectordb.store_pdf_in_chroma(uploaded_file, vectordatabase)
            st.success(f"File '{uploaded_file.name}' uploaded and file embedding stored in vectordb successfully!")

code_generator_app()