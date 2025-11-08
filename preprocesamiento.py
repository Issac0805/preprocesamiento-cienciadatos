# archivo principal de preprocesamiento
# preprocesamiento.py
# Autor: Yoryhi Isaac Cadena Acosta
# Descripción: Funciones básicas de preprocesamiento de datos usando pandas


import pandas as pd

def cargar_datos(ruta_archivo):
    "Carga un dataset en formato CSV"
    "Parámetros: ruta_archivo (str): ruta del archivo CSV"
    "Retorna: DataFrame de pandas con los datos cargados"
    
    try:
        datos = pd.read_csv(ruta_archivo)
        print("Datos cargados correctamente.")
        return datos
    except FileNotFoundError:
        print("Error: el archivo no existe.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

def limpiar_datos(df):
    "Limpia los datos eliminando valores nulos y duplicados"
    "Parámetros: df (DataFrame): dataset cargado"
    "Retorna: DataFrame limpio"
    df_limpio = df.dropna().drop_duplicates()
    print("Datos limpiados (sin nulos ni duplicados).")
    return df_limpio

def normalizar_datos(df, columnas):
    "Normaliza las columnas numéricas indicadas entre 0 y 1"
    "Parámetros: df (DataFrame): dataset limpio, columnas (list): lista de nombres de columnas numéricas a normalizar"
    "Retorna: DataFrame con columnas normalizadas"
    
    df_norm = df.copy()
    for col in columnas:
        if col in df_norm.columns:
            df_norm[col] = (df_norm[col] - df_norm[col].min()) / (df_norm[col].max() - df_norm[col].min())
    print("Columnas normalizadas:", columnas)
    return df_norm
