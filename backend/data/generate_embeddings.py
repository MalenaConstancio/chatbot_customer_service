from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from backend.config.settings import Settings
import os

settings = Settings()

file_path = os.path.abspath(os.path.join("backend", "data", "documents", "manual_netflix.pdf"))
loader = PyPDFLoader(file_path)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  
    chunk_overlap=100  
)
split_documents = text_splitter.split_documents(documents)

embedding_model = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

Chroma.from_documents(
    documents=split_documents,
    embedding=embedding_model,
    persist_directory="backend/data/chroma"
)

