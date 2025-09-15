from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding_model = OpenAIEmbeddings()

def load_and_split(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return text_splitter.split_documents(documents)

def get_embeddings(chunks):
    return embedding_model.embed_documents([chunk.page_content for chunk in chunks])