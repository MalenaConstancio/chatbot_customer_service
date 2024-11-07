from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.tools.retriever import create_retriever_tool

class CustomRetrieverTool:
    def __init__(self, persist_directory='backend/data/chroma', name='busqueda_manual_netflix', description="Searches and returns excerpts related to Netflix issues and general info"):
        self.embeddings_function = OpenAIEmbeddings()
        
        self.db = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings_function
        )
        
        self.name = name
        self.description = description
        
        self.retriever = self.db.as_retriever()
    
    def get_tool(self):
        return create_retriever_tool(
            retriever=self.retriever,
            name=self.name,
            description=self.description
        )