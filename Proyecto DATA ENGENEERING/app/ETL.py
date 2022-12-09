import pandas as pd
from FuncionesETL import limpiar_col, convert_duracion, columnas_title


#Extraemos los datasets de los csv y los convertimos en dataframes

df_amazon=pd.read_csv(r'C:\Users\jotad\OneDrive\Documentos\Sebastian\PI05\PI01_DATA05\Datasets\amazon_prime_titles.csv')
df_disney=pd.read_csv(r'C:\Users\jotad\OneDrive\Documentos\Sebastian\PI05\PI01_DATA05\Datasets\disney_plus_titles.csv')
df_hulu=pd.read_csv(r'C:\Users\jotad\OneDrive\Documentos\Sebastian\PI05\PI01_DATA05\Datasets\hulu_titles.csv')
df_netflix=pd.read_json(r'C:\Users\jotad\OneDrive\Documentos\Sebastian\PI05\PI01_DATA05\Datasets\netflix_titles.json')

# Agregamos la columna platform para cada dataframe y especificamos a qué
# plataforma pertenece cada uno

df_amazon['platform'] = 'Amazon'
df_disney['platform'] = 'Disney'
df_hulu['platform'] = 'Hulu'
df_netflix['platform'] = 'Netflix'

# Concatenamos los 4 dataframes en uno para poder trabajar de manera más sintética

dataframes = [df_amazon, df_disney, df_hulu, df_netflix]

df_plataformas = pd.concat(dataframes)

# df_completo.fillna('Sin Dato', inplace=True)

df_plataformas = limpiar_col(df_plataformas)
df_plataformas = convertir_duracion(df_plataformas)
df_plataformas = columnas_title(df_plataformas)

# Llenamos nulos y convertimos los tipos de datos necesarios

df_plataformas.duration.fillna(0, inplace=True)

df_plataformas.unit.replace('Seasons', 'Season')

df_plataformas.cast.fillna('Sin Dato', inplace=True)

df_plataformas.cast.replace('1','Sin Dato', inplace=True)

df_plataformas.duration = df_plataformas.duration.astype('int64')

df_plataformas.listed_in = df_plataformas.listed_in.astype(str)

df_plataformas.cast = df_plataformas.cast.astype(str)