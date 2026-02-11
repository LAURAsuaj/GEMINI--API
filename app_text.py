import os
from google import genai
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)


# 3. Llamada directa al servicio de modelos
try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="""Actualiza el nombre Juan por Ing. Leandro y 
        el cargo Docente por Consultor en el siguiente texto:

        'Leandro es un Docente con amplia experiencia en el campo de la educación.
        Ha trabajado en el sector prvado y público, como gerente de proyectos.'
        """
    )
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")

# 4. Imprimir la respuesta
if response:
    print("✅ Respuesta del modelo:")
    print(response.text)