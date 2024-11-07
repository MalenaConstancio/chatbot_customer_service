import base64
import streamlit as st
from PIL import Image
import time
import requests

# Logo
img = Image.open("frontend/assets/images/logo_netflix.png")
st.set_page_config(page_title="Netflix", page_icon=img)

# Background
file_path = "frontend/assets/images/landing_netflix.JPG"

with open(file_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
        }}
            
        div.stButton > button {{
            background-color: #e50914;  /* Color de fondo similar al rojo de Netflix */
            color: white;  /* Color de texto blanco */
            border: none;
            padding: 10px 10px;
            border-radius: 5px;
            cursor: pointer;
        }}
        
        div.stButton > button:hover {{
            background-color: #b00710;  /* Color de fondo al pasar el cursor */
        }}
        
        .user-message {{
            background-color: #f0f0f0b8;  /* Color de fondo para los mensajes del usuario */
            color: black;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            width: 640px;
        }}

        .assistant-message {{
            background-color: #e50914c2;  /* Color de fondo para los mensajes del asistente */
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            width: 640px;
        }}
        
        header[data-testid="stHeader"] {{visibility: hidden;}} 
        
        footer {{visibility: hidden;}}
        
        [data-testid="stBottom"] > div {{
            background-color: transparent !important;
        }}
        
        [data-testid="ScrollToBottomContainer"] {{
           margin-top: 120px;
           margin-bottom: 2%;
        }}
        
        [data-testid="stChatInput"] {{
           background-color: rgb(22 23 26);
        }}
        
        [data-testid="stChatMessage"] {{
           background-color: rgb(6 6 6 / 50%);
        }}
         
             
    </style>
    """,
    unsafe_allow_html=True
)


col1, col2= st.columns([90, 10])
with col1:
    pass
with col2:
    if st.button("🗑️"):
        st.session_state.messages = []
        chat_history = []
        
        url = "http://127.0.0.1:8000/reset_memory/"  
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            pass 
        
usuario = "😊"
bot = "🔴"

# Inicializar historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

# Historial
for message in st.session_state.messages:
    avatar = usuario if message["role"] == "user" else bot
    message_class = "user-message" if message["role"] == "user" else "assistant-message"
    
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(
            f"""
            <div class="{message_class}">
                {message["content"]}
            </div>
            """,
            unsafe_allow_html=True,
        )


def chatbot(user_query,chat_history):
    url = "http://127.0.0.1:8000/chat/"  
    payload = {
        "query": user_query,
        "chat_history": [msg["content"] for msg in st.session_state.messages if msg["role"] == "user"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("response", "Error: Respuesta vacía.")
    except requests.exceptions.RequestException as e:
        return f"Error: No se pudo conectar al servidor. Detalles: {e}"

# Aceptar entrada del usuario
if prompt := st.chat_input("Ingresa tu consulta:"):
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Mostrar mensaje del usuario en la interfaz
    with st.chat_message("user", avatar=usuario):
        st.markdown(
            f"""
            <div class="user-message">
                {prompt}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Obtener historial de chat del usuario
    chat_history = "\n".join([message["content"] for message in st.session_state.messages if message["role"] == "user"])

    # Mostrar respuesta del bot en la interfaz
    with st.chat_message("assistant", avatar=bot):
        contenedor_respuesta = st.empty()
        full_response = ""

        # Llamar a la API del back-end para obtener la respuesta
        respuesta = chatbot(prompt, chat_history)
        for chunk in respuesta.split():
            full_response += chunk + ' '
            time.sleep(0.10)
            contenedor_respuesta.markdown(
                f"""
                <div class="assistant-message">
                    {full_response}▌
                </div>
                """,
                unsafe_allow_html=True,
            )
            
        contenedor_respuesta.markdown(
            f"""
            <div class="assistant-message">
                {respuesta}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Agregar mensaje del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
