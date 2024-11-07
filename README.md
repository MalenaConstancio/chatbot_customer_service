# Netflix Support Bot - Documentación

Este proyecto es un bot de soporte al cliente para Netflix desarrollado dentro del marco del **Bootcamp GEN IA** dictado por **Analítica Noviembre** en Septiembre de 2024. 
El mismo utiliza **FastAPI** en el backend y **Streamlit** en el frontend para interactuar con los usuarios. 
El bot está diseñado para proporcionar respuestas a problemas comunes que los usuarios pueden tener con Netflix. 
Se utilizó **LangChain** para la integración con modelos de lenguaje y herramientas de soporte.

## Requisitos previos

Para ejecutar este proyecto localmente:

- **Python 3.12.3** 
- **Git** 
- Acceso a **SerpAPI** , es necesario tener generada una api key propia https://serpapi.com/
- Acceso a **OpenAI** , es necesario tener generada una api key propia https://openai.com/api/

## Instrucciones de Instalación

Pasos para configurar el entorno:

1. **Clonar el Repositorio**

   Primero, clona este repositorio desde GitHub:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd netflix_support_bot
   ```

2. **Crear un Entorno Virtual**

   Crea un entorno virtual dentro del proyecto:
   ```bash
   python -m venv venv
   ```

3. **Activar el Entorno Virtual**

   - En **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```
   - En **Windows**:
     ```bash
     venv\Scripts\activate
     ```

4. **Instalar las Dependencias**

   Instala las dependencias usando el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar Variables de Entorno**

   Dentro del archivo `.env` en la carpeta principal del proyecto añadí las variables necesarias. 
   ```env
   SERPAPI_API_KEY = tu_clave_api_de_serpapi
   OPENAI_API_KEY = tu_clave_api_de_openai
   ```
6. **Generar la Base de Datos de Embeddings**

    Para generar la base de datos de utilizada por el bot, seguí estos pasos:

    Ejecuta el script correspondiente para generar los embeddings. Asegúrate de tener activado el entorno virtual antes de proceder:

    ```bash
    python backend/data/generate_embeddings.py
    ```

    Este script tomará los documentos almacenados en la carpeta backend/data/documents/ y generará los embeddings necesarios, que serán almacenados en la carpeta backend/data/embeddings/chroma/.

## Ejecución del Proyecto

### Backend 

Para iniciar el servidor **FastAPI**, ejecuta el siguiente comando:
```bash
uvicorn backend.main:app --reload
```
Esto iniciará el servidor en `http://localhost:8000`.

### Frontend 

Para ejecutar el frontend con **Streamlit**, utiliza el siguiente comando:
```bash
streamlit run frontend/main_front.py
```
Esto iniciará la aplicación de Streamlit en tu navegador.

## Uso del Bot

1. **Abrir el navegador** y acceder al URL generado por Streamlit.
2. **Ingresar una consulta** en la interfaz del bot.
3. El bot procesará la consulta para devolver una respuesta.
4. Si necesitas **Borrar el historial** podes presionar el icono del bote de basura y comenzar una nueva conversación.

## Estructura del Proyecto  
```
netflix_support_bot/
├── backend/                            # Carpeta principal del back-end
│   ├── agent/                          # Componentes relacionados con el comportamiento del agente
│   │   ├── agent_config.py             # Archivo de configuración del agente
│   │   ├── agent_initializer.py        # Inicializador del agente
│   │   ├── llm_config.py               # Configuración del LLM
│   │   ├── memory.py                   # Clase para manejar la memoria del bot (historial de conversaciones)
│   │   └── personality.py              # Clase para definir la personalidad del bot
│   ├── api/                            # Carpeta de la aplicación FastAPI
│   │   └── main.py                     # Punto de entrada principal para el servidor FastAPI
│   ├── config/                         # Configuración general del proyecto
│   │   └── settings.py                 # Configuraciones del proyecto (variables de entorno, claves API, etc.)
│   ├── data/                           # Datos y recursos utilizados por el LLM
│   │   ├── chroma/                     # Base de datos de Chroma para embeddings
│   │   │   ├── chroma.sqlite3          # Base de datos de Chroma
│   │   │   └── (archivos internos de Chroma)  
│   │   ├── documents/                  # Documentos para el Retriever Tool
│   │   │   └── manual_netflix.pdf      # Manual de soporte de Netflix
│   │   └── generate_embeddings.py      # Script para generar los embeddings
│   ├── models/                         # Modelos de datos utilizados en el proyecto
│   │   └── query_request.py            # Modelo de solicitud de consulta del usuario
│   └── tools/                          # Herramientas para el LLM
│       ├── faq_tool.py                 # Herramienta para preguntas frecuentes
│       └── retriever_tool.py           # Herramienta de búsqueda interna
├── frontend/
│   ├── main_front.py                   # Archivo principal de Streamlit
│   └── assets/                         # Recursos del frontend (imágenes, estilos CSS)
│       └── images/                     # Imágenes para el front-end (logos, etc.)
│           ├── landing_netflix.JPG     
│           └── logo_netflix.png        
├── .env                                # Variables de entorno (API keys)
├── README.md                           # Descripción general del proyecto
└── requirements.txt                    # Dependencias del proyecto
```


