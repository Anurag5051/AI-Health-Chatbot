import os
import streamlit as st
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

load_dotenv()


st.set_page_config(page_title="AI Health Chatbot", layout="wide")


st.sidebar.title("📂 Document Upload")

uploaded_file = st.sidebar.file_uploader("Upload Medical PDF", type=["pdf"])

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []


if "messages" not in st.session_state:
    st.session_state.messages = []

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if uploaded_file and st.session_state.qa_chain is None:
    with st.spinner("Processing document..."):

        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        loader = PyPDFLoader("temp.pdf")
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
        split_docs = splitter.split_documents(docs)

        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(split_docs, embeddings)

        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever
        )

        st.session_state.qa_chain = qa_chain

        st.sidebar.success("✅ Document Ready!")

st.title("🩺 AI Health Chatbot")
st.write("Ask questions from your uploaded medical document")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


query = st.chat_input("Ask your health question...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            if st.session_state.qa_chain:
                result = st.session_state.qa_chain.invoke({"query": query})
                answer = result["result"]
            else:
                answer = "⚠️ Please upload a medical PDF first."

            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})