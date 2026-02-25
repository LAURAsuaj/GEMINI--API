import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)

texto_entrada = "Este libro empezó bien pero el final fue muy apresurado y decepcionante."

promptMaestro = f"""
Eres un clasificador de sentimientos de reseñas de libros. Debes responder SOLO con una palabra: POSITIVO, NEUTRAL o NEGATIVO.

EJEMPLOS:
Reseña: "Una historia increíble, personajes memorables y final perfecto."
Sentimiento: POSITIVO

Reseña: "El libro está bien, entretiene pero no destaca."
Sentimiento: NEUTRAL

Reseña: "Muy aburrido, no logré terminarlo."
Sentimiento: NEGATIVO

Ahora clasifica: Reseña: "{texto_entrada}"
Sentimiento:
"""
configuracion = types.GenerateContentConfig(
    temperature=0.7,
    max_output_tokens=2000
)

# 3. Llamada directa al servicio de modelos
response = None

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=promptMaestro,
        config=configuracion
    )
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")

# 4. Imprimir la respuesta
if response:
    print("✅ Respuesta del modelo:")
    print(response.text)