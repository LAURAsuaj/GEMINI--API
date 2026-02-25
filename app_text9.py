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

texto_entrada = "In recent years, Internet has transformed how we communicat e."
prompt = f"""Se te proporcionará un texto delimitado por tildes invertidas. SI el texto está escrito en inglés, verifica si contiene la palabra clave 'tec hnology'. SI la contiene, sugiere un título. DE LO CONTRARIO, escribe 'Palabra clave no encontrada'. ``` {texto_entrada} ``` """
configuracion = types.GenerateContentConfig(
    temperature=0.7,
    max_output_tokens=300
)

# 3. Llamada directa al servicio de modelos
try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config=configuracion
    )
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")

# 4. Imprimir la respuesta
if response:
    print("✅ Respuesta del modelo:")
    print(response.text)