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

ensayo = """
La inteligencia artificial se ha convertido en uno de los motores principales del cambio en la sociedad contemporánea. En el ámbito educativo, permite personalizar el aprendizaje, adaptando contenidos a las necesidades y ritmos de cada estudiante. Esto facilita que los alumnos comprendan mejor los temas y desarrollen habilidades de manera progresiva. Además, los docentes pueden utilizar herramientas de análisis de datos para identificar dificultades y mejorar sus estrategias pedagógicas.

Sin embargo, la integración de la inteligencia artificial también plantea desafíos importantes. Existe el riesgo de una dependencia excesiva de la tecnología, lo que podría afectar el pensamiento crítico y la autonomía del estudiante si no se utiliza adecuadamente. Asimismo, surgen preocupaciones relacionadas con la privacidad de los datos y la equidad en el acceso a estas herramientas.

Por esta razón, la inteligencia artificial debe implementarse como un complemento del proceso educativo y no como un reemplazo del docente. Su uso responsable puede potenciar la creatividad, la colaboración y la resolución de problemas, preparando a los estudiantes para un entorno digital en constante evolución.
"""

promptMaestro = f"""
ROL:Eres un evaluador académico de ensayos.
TAREA:Analizar el ensayo proporcionado.
REGLAS CONDICIONALES:
- Si el ensayo tiene menos de 100 palabras:
  Recházalo y pide más contenido.
- Si el ensayo tiene 100 palabras o más:
  Evalúalo según:
  - Ortografía
  - Coherencia
  - Argumentación
FORMATO DE SALIDA:Devuelve SOLO un objeto JSON con:
- nota_final (0-5)
- comentarios (texto breve)
ENSAYO:
\"\"\"{ensayo}\"\"\"
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