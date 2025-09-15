from langchain.embeddings import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()

def get_query_embedding(query):
    return embedding_model.embed_query(query)

def construct_prompt(query, retrieved_docs):
    context = "\n---\n".join(retrieved_docs)
    return f"Answer the question based on the context:\n{context}\n\nQuestion: {query}\nAnswer:"