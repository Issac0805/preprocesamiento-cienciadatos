# archivo principal de preprocesamiento
# preprocesamiento.py
# Autor: Yoryhi Isaac Cadena Acosta
# Descripción: Funciones básicas de preprocesamiento de datos usando pandas


import pandas as pd

def cargar_datos(ruta_archivo):
    "Carga un dataset en formato CSV."
    "Parámetros: ruta_archivo (str): ruta del archivo CSV."
    "Retorna: DataFrame de pandas con los datos cargados."
    
    try:
        datos = pd.read_csv(ruta_archivo)
        print("Datos cargados correctamente.")
        return datos
    except FileNotFoundError:
        print("Error: el archivo no existe.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")