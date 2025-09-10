import pandas as pd
def minus(df):
  """
    Convierte a minúsculas los valores de todas las columnas de tipo objeto en un DataFrame.

    Para cada columna de tipo texto (object), transforma las cadenas a minúsculas,
    facilitando la homogeneidad de los datos y evitando problemas al comparar valores.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las columnas a procesar.

    Returns
    -------
    None
        El DataFrame es modificado en el lugar (inplace).
    """
  for col in df.select_dtypes(include='O').columns:
    df[col]=df[col].str.lower()
  def comas(df):
   """
    Reemplaza comas con puntos en columnas de tipo texto y convierte a valores numéricos.

    Para cada columna de tipo texto (object), intenta reemplazar las comas (',') por puntos ('.'),
    y convertir la columna a tipo numérico (float64). Si la conversión falla, se mantiene como texto.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las columnas a procesar.

    Returns
    -------
    None
        El DataFrame es modificado en el lugar (inplace).
    """
  for col in df.select_dtypes(include='O').columns:
    df[col]=df[col].str.replace(',','.')
    try:
      df[col]=df[col].astype('float64')
    except:
      pass
def espacios(df):
   """
    Reemplaza espacios con guiones bajos en los valores de todas las columnas de tipo texto.

    Para cada columna del DataFrame, intenta reemplazar los espacios en blanco (' ')
    por guiones bajos ('_') en los valores de texto, facilitando el manejo de datos sin espacios.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las columnas a procesar.

    Returns
    -------
    None
        El DataFrame es modificado en el lugar (inplace).
    """
   for col in df.select_dtypes(include='O').columns:
     df[col]=df[col].str.replace('  ','_')