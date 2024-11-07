from langchain.tools import BaseTool
from pydantic import Field

from langchain.tools import BaseTool

class FAQTool(BaseTool):
    name: str = "faq_tool"
    description: str = "Provides answers to frequently asked questions about Netflix and general information."
    faq_data: dict = None 

    def __init__(self, faq_data=None, **kwargs):
        """
        Inicializa el FAQTool con un diccionario de preguntas frecuentes opcional.
        :param faq_data: Un diccionario con preguntas y respuestas frecuentes (pregunta: respuesta).
        """
        super().__init__(**kwargs)
        self.faq_data = faq_data or {
            "¿Qué es Netflix?": "Netflix es un servicio de streaming que ofrece una amplia variedad de series, películas, documentales y más.",
            "¿Cómo puedo cancelar mi suscripción?": "Para cancelar tu suscripción, ve a la configuración de tu cuenta en Netflix y selecciona 'Cancelar membresía'.",
            "¿Cómo puedo cambiar mi plan de suscripción?": "Puedes cambiar tu plan de suscripción en cualquier momento desde la configuración de tu cuenta en Netflix.",
            "¿Puedo descargar contenido para verlo sin conexión?": "Sí, Netflix permite descargar algunos títulos para verlos sin conexión en dispositivos móviles.",
            "¿Cuántos perfiles puedo crear en una cuenta de Netflix?": "Puedes crear hasta 5 perfiles en una cuenta de Netflix.",
            "¿Cómo cambio mi método de pago?": "Ve a la configuración de tu cuenta en Netflix y selecciona 'Administrar información de pago' para cambiar tu método de pago.",
            "¿Por qué algunos títulos no están disponibles en mi país?": "El catálogo de Netflix varía según la región debido a restricciones de licencias y derechos de contenido.",
            "¿Por qué la calidad del video es baja?": "La calidad del video depende de la velocidad de tu conexión a internet y del plan de suscripción que tengas.",
            "¿Puedo ver Netflix en varios dispositivos al mismo tiempo?": "La cantidad de dispositivos en los que puedes ver Netflix simultáneamente depende del plan de suscripción que tengas.",
            "¿Cómo configuro los controles parentales?": "Puedes configurar controles parentales y restricciones de contenido en la configuración de la cuenta de Netflix.",
            "¿Qué hago si olvidé mi contraseña?": "En la pantalla de inicio de sesión, selecciona '¿Olvidaste tu contraseña?' y sigue las instrucciones para restablecerla.",
            "¿Cómo puedo eliminar un perfil de mi cuenta?": "Desde la sección de administración de perfiles, selecciona el perfil que deseas eliminar y elige la opción para borrarlo.",
            "¿Por qué mi cuenta de Netflix fue suspendida?": "Tu cuenta puede ser suspendida si no se pudo procesar el pago o si hubo alguna actividad sospechosa. Verifica los detalles en la configuración de tu cuenta.",
            "¿Netflix ofrece un período de prueba gratuito?": "Actualmente, Netflix no ofrece un período de prueba gratuito. Consulta su página web para conocer las ofertas actuales.",
            "¿Cómo activo o desactivo los subtítulos?": "Puedes activar o desactivar los subtítulos durante la reproducción de un video seleccionando el ícono de 'Subtítulos'.",
            "¿Qué hago si no puedo iniciar sesión?": "Asegúrate de que tus datos de inicio de sesión sean correctos. Si olvidaste tu contraseña, selecciona '¿Olvidaste tu contraseña?' en la pantalla de inicio.",
            "¿Cómo puedo ver mi historial de visualización?": "En la configuración de tu cuenta, puedes ver el historial de visualización en la sección 'Actividad de visualización'.",
            "¿Puedo compartir mi cuenta con amigos o familiares?": "Netflix permite compartir tu cuenta con personas dentro de tu mismo hogar. Compartir fuera del hogar puede violar los términos de uso.",
            "¿Qué hago si tengo problemas con la reproducción de un video?": "Verifica tu conexión a internet, actualiza la app de Netflix, o intenta reiniciar tu dispositivo. Si el problema persiste, contacta a soporte.",
            "¿Cómo configuro la reproducción automática de capítulos?": "En la configuración de tu cuenta, puedes activar o desactivar la reproducción automática de episodios.",
            "¿Cómo contacto con el servicio de atención al cliente de Netflix?": "Puedes contactar a atención al cliente desde la app o el sitio web de Netflix en la sección de ayuda.",
            "¿Qué hago si la aplicación de Netflix no funciona en mi dispositivo?": "Intenta reiniciar el dispositivo, actualizar la app, o reinstalarla. Si el problema persiste, revisa la compatibilidad del dispositivo con Netflix.",
            "¿Qué costos tienen los planes en Argentina?": "Los costos de los planes de Netflix en Argentina son los siguientes: Plan Básico: Tiene un costo mensual de ARS 4299 al mes. Plan Estándar: Tiene un costo mensual de  ARS 7199 al mes. Plan Premium: Tiene un costo mensual de ARS 9699 al mes. Estos precios pueden variar, así que te recomendaría verificar la página oficial de Netflix para ver los costos actualizados."
        }

    def _run(self, query):
        """
        Maneja la consulta y proporciona respuestas a preguntas frecuentes.
        :param query: La pregunta del usuario.
        :return: Respuesta a la pregunta frecuente o mensaje vacío si no se encuentra.
        """
        return self.faq_data.get(query, "Lo siento no tengo una respuesta para esa pregunta")

    async def _arun(self, query):
        return self._run(query)

faq_tool = FAQTool()
