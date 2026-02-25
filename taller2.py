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

texto_entrada = "Hola, mi factura #789 tiene un cobro que no reconozco."

promptMaestro = f"""
Eres un asistente que clasifica mensajes.
INSTRUCCIONES:
Se te dará un texto delimitado por ```.
REGLAS:
- Si el texto menciona "factura" o "pago" → responde: URGENTE-FINANZAS,
extrae el número de factura si existe.
- Si menciona "error" o "no funciona" → responde: SOPORTE ESTANDAR,
Responde: "Gracias, un técnico lo revisará".
- Si no → responde: OTRO
Responde solo con la categoría.
TEXTO:
```{texto_entrada}```
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