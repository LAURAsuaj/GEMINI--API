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

promptMaestro = f"""
Eres un Gerente de Finanzas amable pero firme encargado de la gestión de cuentas por cobrar.
TAREA:Redacta un correo profesional para un cliente que presenta pagos pendientes, solicitando el pago y ofreciendo opciones de regularización.
CONTEXTO:El correo debe mantener una relación comercial positiva, evitando un tono agresivo pero dejando clara la urgencia del pago.
TONO:Formal, cordial y firme.
DELIMITADORES:Usa ### para separar los datos del cliente del resto de la instrucción.
###
DATOS DEL CLIENTE:
- Nombre del cliente: Teresa Casallas
- Empresa: ENEL
- Facturas pendientes: [Listado:
ENERO: 250.000
FEBRERO: 210.000 + RETASO:70.000
MARZO: 205.000 + RETRASO ACUMULADO: 150.000]
- Monto total adeudado: 815.000
- Fecha de vencimiento: 31/03/2026
- Opciones de pago: TRANSFERENCIA BANCARIA
###

FORMATO DE SALIDA:
1. Asunto del correo.
2. Cuerpo del correo profesional.
3. Cierre formal.
4. Resumen final en una tabla con:
   - Número de factura
   - Fecha de vencimiento
   - Monto
   - Estado
"""
configuracion = types.GenerateContentConfig(
    temperature=0.7,
    max_output_tokens=2048
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