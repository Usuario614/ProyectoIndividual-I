import pandas as pd

#Con esta función limpiamos las columnas que no nos sirven para las query

def limpiar_col(df):
    colums=['type','title','cast','release_year','duration','listed_in','platform']
    
    df=df.drop(columns=[col for col in df if col not in columns])
    return df

#Con esta funcion vamos a dividirla columna duration en duration y unit | Luego se une con el dataframe original y las renombra por default 0 y 1

def convert_duration(df_plataformas):
    columnas = df_plataformas.duration.split(expand=True)
    
    df_plataformas=pd.concat([df_plataformas, columnas], axis=1)
    
    df_plataformas.drop(columns='duration', inplace=True)
    
    df_plataformas.rename(columns={0:'duration', 1: 'unit'}, inplace=True)
    return df_plataformas

 # Esta función aplica el método title en todas las columnas que no sean duration o release_year

def columnas_title(df):
       

    for n in df:
        if n == 'duration' or n == 'release_year':
            pass
        else:
            df[f'{n}'] = df[f'{n}'].str.title()
    
    return df