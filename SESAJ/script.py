# Importar librerías
from collections import defaultdict
import pandas as pd
import re
import sys

# Verificar que se haya pasado un argumento
if len(sys.argv) != 2:
    print("Uso: python script.py <nombre_del_archivo_csv>")
    sys.exit(1)

# Obtener el nombre del archivo CSV desde los argumentos
nombre_archivo = sys.argv[1]

# Cargar datos
df = pd.read_csv(nombre_archivo, encoding='utf-8')

# Definir patrón para identificar códigos
patron = r'\[E\d+[A-Za-z]?\.\d+[A-Za-z]?\]'


# Función para extraer las preguntas, respuestas y frecuencias
def extraer_preguntas_respuestas_y_frecuencia(df):
    codigos_preguntas_agrupadas = defaultdict(lambda: {'pregunta': None, 'respuesta': None, 'conteo_total': 0})

    for columna in df.columns:
        for respuesta in df[columna]:
            if pd.isna(respuesta):
                continue
            
            # Buscar el código en la respuesta
            codigos = re.findall(patron, str(respuesta))
            if not codigos:
                continue  # Si no hay código, saltar esta respuesta
            
            # Extraer la respuesta (eliminar el código y limpiar el texto)
            respuesta_limpia = re.sub(patron, '', str(respuesta)).strip()  # Eliminar el código
            respuesta_limpia = respuesta_limpia.split('\t')[-1]  # Dividir por \t y tomar la última parte
            respuesta_limpia = re.sub(r'^[A-Za-z]\)\s*', '', respuesta_limpia)
            respuesta_limpia = respuesta_limpia.rstrip('.')  # Eliminar el punto final si existe
            
            for codigo in codigos:
                # Si es la primera vez que se encuentra esta pregunta para este código, guardarla
                if codigos_preguntas_agrupadas[codigo]['pregunta'] is None:
                    codigos_preguntas_agrupadas[codigo]['pregunta'] = columna
                    codigos_preguntas_agrupadas[codigo]['respuesta'] = respuesta_limpia
                
                # Sumar al conteo total
                codigos_preguntas_agrupadas[codigo]['conteo'] += 1

    return codigos_preguntas_agrupadas

# Llamar a la función
codigos_preguntas_frecuencia = extraer_preguntas_respuestas_y_frecuencia(df)

# Convertir el resultado en un DataFrame
resultados = []
for codigo, datos in codigos_preguntas_frecuencia.items():
    resultados.append({
        'Código': codigo,
        'Pregunta': datos['pregunta'],
        'Respuesta': datos['respuesta'],
        'Conteo': datos['conteo']
    })

df_resultado = pd.DataFrame(resultados)     # dataframe

# Añadir columnas de interés
df_resultado['Eje'] = df_resultado['Código'].str[2] # Eje
df_resultado['Inciso'] = df_resultado['Código'].str[-2] # Inciso de respuesta

# Dar formato final al df
df_resultado = df_resultado[['Eje', 'Pregunta', 'Respuesta', 'Inciso', 'Conteo']]       # Omitimos la columna del código

# Exportar el Archivo
df_resultado.to_excel('archivo_procesado.xlsx', index=False)

print(f'Archivo {nombre_archivo} procesado correctamente!')





