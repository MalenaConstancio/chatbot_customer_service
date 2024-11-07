import os
from langchain.agents import load_tools
from langchain.memory import ConversationBufferMemory

from backend.agent.llm_config import get_llm
from backend.agent.personality import Personality
from backend.agent.memory import ChatHistoryMemory
from backend.agent.agent_config import create_agent_executor
from backend.config.settings import Settings
from backend.tools.faq_tool import faq_tool
from backend.tools.retriever_tool import CustomRetrieverTool

settings = Settings()
os.environ["SERPAPI_API_KEY"] = settings.SERPAPI_API_KEY

def initialize_agent():
    """
    Configuración del agente.

    Returns:
        AgentExecutor: Instancia del ejecutor del agente configurado.
    """
    # Configuración del LLM y la personalidad del bot
    llm = get_llm()
    bot_personality = Personality(country="Argentina")
    prompt_template = bot_personality.get_prompt_template()

    # Configuración de la memoria del bot
    memory = ChatHistoryMemory(memory_class=ConversationBufferMemory)

    # Cargar herramientas 
    serpapi_tool = load_tools(["serpapi"])  
    custom_retriever = CustomRetrieverTool()
    retriever_tool = custom_retriever.get_tool()
    
    tools = [faq_tool, retriever_tool] + serpapi_tool  

    # Crear y devolver el agente ejecutor
    return create_agent_executor(llm=llm, tools=tools, memory=memory, prompt_template=prompt_template)
