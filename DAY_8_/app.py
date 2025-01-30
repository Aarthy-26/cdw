import streamlit as st
import chain
import vectordb
import random
import agents
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

            is_rag_enabled = st.checkbox("Check me to enable RAG")
            is_agent_enabled = st.checkbox("Check me to enable Agent")

            if submitted:
              if is_rag_enabled and is_agent_enabled:
                  response = agents.generate_code_with_rag_agent(language, vectordatabase)
              elif is_agent_enabled:
                  response = agents.generate_code_with_agent(language)
              elif is_rag_enabled:
                  response = chain.generate_code_rag_chain(language, vectordatabase)
              else:
                  response = chain.generate_code_chain(language)
             
              st.info(response)
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