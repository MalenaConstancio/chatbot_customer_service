from fastapi import FastAPI, HTTPException
from backend.agent.agent_initializer import initialize_agent
from backend.models.query_request import UserQuery

# Inicializar la API de FastAPI
api = FastAPI()

# Inicializar el agente 
agent_executor = initialize_agent()

# Endpoints
@api.post("/chat/")
async def chat_with_bot(user_query: UserQuery):
    """
    Endpoint para interactuar con el bot.
    
    Args:
        user_request (UserQuery): Consulta del usuario, incluyendo el historial de chat.
    
    Returns:
        dict: Respuesta generada por el bot.
    """
    try:
        response = agent_executor.invoke({
            'input': user_query.query,
            'chat_history': user_query.chat_history
        })  
        return {"response": response['output']}
    except ConnectionError:
        raise HTTPException(status_code=503, detail="Error de conexión al servicio externo. Intenta nuevamente más tarde.")
    except TimeoutError:
        raise HTTPException(status_code=504, detail="La solicitud al servicio externo ha expirado. Intenta nuevamente más tarde.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api.post("/reset_memory/")
async def reset_memory():
    agent_executor.memory.clear()  
    return {"detail": "Memoria reiniciada con éxito"}