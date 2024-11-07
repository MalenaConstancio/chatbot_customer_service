from langchain.agents import AgentExecutor, create_openai_tools_agent

def create_agent_executor(llm, tools, memory, prompt_template):
    """
    Crea un AgentExecutor que utiliza un LLM, herramientas, memoria y un template de prompt.

    Args:
        llm: El modelo LLM que se utilizará.
        tools (list): Lista de herramientas que el agente podrá usar.
        memory: La memoria que se usará para el agente.
        prompt_template: Plantilla del prompt que define la personalidad del agente.
        verbose (bool): Si se debe mostrar información detallada durante la ejecución.

    Returns:
        AgentExecutor: El ejecutor del agente configurado.
    """
    agent = create_openai_tools_agent(llm=llm, tools=tools, prompt=prompt_template)
    return AgentExecutor(agent=agent, tools=tools, memory=memory.get_memory(), verbose=True)
