#Tratamiento de datos
import pandas as pd

"""
Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

Este análisis incluye:
- Muestra aleatoria de 5 filas del DataFrame.
- Información general del DataFrame (tipo de datos, nulos, etc.).
- Porcentaje de valores nulos por columna.
- Conteo de filas duplicadas.
- Distribución de valores para columnas categóricas.

Parameters:
    df (pd.DataFrame): DataFrame a analizar.

Returns:
    None
"""

def eda_preliminar(df):
  display(df.sample(5))

  print('-------')
  print('DIMENSIONES')
  print(f'Nuestro conjunto de datos tiene {df.shape[0]} filas y {df.shape[1]} columnas')
  print('-------')
  print('INFO')
  display(df.info())
  print('-------')
  print('NULOS')
  display(df.isnull().mean()*100)
  print('------')
  print('DUPLICADOS')
  print(f' Tenemos un total de {df.duplicated().sum()}')
  print('------')
  print('FRECUENCIA CATEGORICAS')
  for col in df.select_dtypes(include='O').columns:
    print(col.upper())
    print(df[col].value_counts())
    print('-----------')

