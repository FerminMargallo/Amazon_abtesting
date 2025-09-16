import pandas as pd
import scipy.stats as stats

def exploracion_df_abtesting(df,col_control):
  for categoria in df[col_control].unique():
    df_filtrado=df[df[col_control]==categoria]
    print(f'Los principales estadísticos de las columnas categóricas para el grupo {categoria.upper()} son: ')
    display(df_filtrado.describe(include='O').T)
    print(f'Los principales estadísticos de las columnas numericas para el grupo {categoria.upper()} son: ')
    display(df_filtrado.describe(include='number').T)
    print('----------------')

def normalidad(df,lista_metricas):
  for metrica in lista_metricas:
        statistic,pvalue=stats.shapiro(df[metrica])
        if pvalue >0.05:
          print(f'Para la columna {metrica} los datos siguen una distribución normal')
        else:
          print(f'Para la columna {metrica} los datos no siguen una distribución normal')

def homocedasticidad(df,col_control,lista_metricas):
  for metrica in lista_metricas:
    df_grupos=[]
    for valor in df[col_control].unique():
      df_grupos.append(df[df[col_control]==valor][metrica])
    statistic,pvalue=stats.levene(*df_grupos)
    if pvalue >0.05:
        print(f'Para la columna {metrica.upper()} las varianzas son homógeneas, es decir, NO hay homocedasticidad')
    else:
        print(f'Para la columna {metrica.upper()} las varianzas no son homógeneas, es decir, HAY homocedasticidad')

def mannwhitneyu(df,col_control,lista_metricas):
  for metrica in lista_metricas:
    valores_control=df[col_control].unique()
    control=df[df[col_control]==valores_control[0]][metrica]
    test=df[df[col_control]==valores_control[1]][metrica]
    statistic,p_value=stats.mannwhitneyu(control,test)
    if p_value>0.05:
        print(f'Para la metrica {metrica.upper()}, NO existen diferencias significativas entre los dos grupos')
    else:
        print(f'Para la metrica {metrica.upper()}, SI EXISTEN diferencias significativas entre los dos grupos')