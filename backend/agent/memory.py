from langchain.memory import ConversationBufferMemory, ChatMessageHistory

class ChatHistoryMemory:
    """
    Clase personalizada para manejar la memoria del bot con diferentes clases de memoria base.

    Args:
        memory_class: Clase de memoria base que se utilizará.
        memory_key (str): Clave para acceder a la memoria en el contexto.
        k (int): Número de mensajes que se almacenarán.
        return_messages (bool): Si se deben devolver los mensajes almacenados.
        **kwargs: Argumentos adicionales que podrían ser requeridos por la clase de memoria base.
    """

    def __init__(self, 
                 memory_class, 
                 memory_key: str = 'chat_history', 
                 k: int = 6, 
                 return_messages: bool = True, 
                 **kwargs):
        self.memory = memory_class(
            memory_key=memory_key,
            k=k,
            return_messages=return_messages,
            **kwargs
        )
        
    def get_memory(self):
        """
        Método para obtener la instancia de la memoria.

        Returns:
            memory_class: Instancia de la clase de memoria utilizada.
        """
        return self.memory
