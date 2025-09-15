import streamlit as st
from embedder import load_and_split, get_embeddings
from vectordb import VectorStore
from retriever import get_query_embedding, construct_prompt
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

st.title("🧠 ChatGPT-Powered Personal Assistant with RAG")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
if uploaded_file:
    with open(f"data/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())
    st.success("File uploaded successfully!")

    # Load, split and embed
    chunks = load_and_split(f"data/{uploaded_file.name}")
    embeddings = get_embeddings(chunks)
    store = VectorStore(dimension=len(embeddings[0]))
    store.add(embeddings, [chunk.page_content for chunk in chunks])

    query = st.text_input("Ask a question about the document")
    if query:
        query_embedding = get_query_embedding(query)
        relevant_docs = store.search(query_embedding)
        prompt = construct_prompt(query, relevant_docs)

        llm = OpenAI(temperature=0)
        response = llm(prompt)
        st.write(response)