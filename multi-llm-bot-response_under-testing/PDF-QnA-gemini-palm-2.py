import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain


google_api_key = 'AIzaSyDTBeoFs1J2FPm-YnbV_DAfu0Sdl_VjtgI'

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GooglePalmEmbeddings(google_api_key=google_api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

def get_conversational_chain_geminibot():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, \n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = GoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=google_api_key)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def get_conversational_chain_palmbot(vector_store):
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=google_api_key, temperature=0.1)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
    return conversation_chain

def user_input(user_question, geminibot_chain, palmbot_chain, vector_store):
    # Get input documents for PaLM-bot
    docs = vector_store.similarity_search(user_question)
    
    # Call Gemini-bot chain
    response_gemini = geminibot_chain({"question": user_question, "input_documents": docs})
    
    # Call PaLM-bot chain
    response_palm = palmbot_chain({"question": user_question})
    
    # Display responses
    st.markdown('<p style="color: #ff7f0e; font-weight: bold;">Gemini-bot:</p>', unsafe_allow_html=True)
    st.write(response_gemini["output_text"])
    
    st.markdown('<p style="color: #ff7f0e; font-weight: bold;">PaLM-bot:</p>', unsafe_allow_html=True)
    st.write(response_palm["answer"])
    
    st.markdown("<hr>", unsafe_allow_html=True)



    
def main():
    st.set_page_config("Chat with Multiple PDFs")
    st.header("Chat with PDFs using Gemini and PaLM")
    user_question = st.text_input("Ask a Question from the PDF Files")
    
    if "chat_history_gemini" not in st.session_state:
        st.session_state.chat_history_gemini = []
    
    if "chat_history_palm" not in st.session_state:
        st.session_state.chat_history_palm = []
    
    if user_question:
        geminibot_chain = get_conversational_chain_geminibot()
        vector_store = get_vector_store(st.session_state.text_chunks)
        palmbot_chain = get_conversational_chain_palmbot(vector_store)
        
        user_input(user_question, geminibot_chain, palmbot_chain, vector_store)
        
    with st.sidebar:
        st.subheader("Upload your Documents")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Process Button", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.text_chunks = text_chunks
                st.success("Done")

if __name__ == "__main__":
    main()
