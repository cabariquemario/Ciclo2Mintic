
#%%
def informes_covid (filename: str) -> dict:
    '''
    Función para analizar los datos de covid del reto
    Input: filename con la ruta del archivo
    output: diccionario con datos del país con mayor número de contagios
    '''

    import pandas as pd
    import numpy as np

    df = pd.read_csv(filename, sep=',')
    
    mayor_contagio = df['País de procedencia'].value_counts().index[0]
    cantidad_contagios = df['País de procedencia'].value_counts()[0]
    # print(cantidad_contagios)
    # print(df[['País de procedencia','Fecha de muerte']][(df['País de procedencia'] == mayor_contagio)]['Fecha de muerte'].value_counts().sum())
    recuperados = df[['País de procedencia','Fecha recuperado']][(df['País de procedencia'] == mayor_contagio)]['Fecha recuperado'].value_counts().sum()
    fallecidos = cantidad_contagios - recuperados

    d = {}
    d['mayor_contagio'] = mayor_contagio
    d['cantidad_contagios'] = cantidad_contagios
    d['fallecidos'] = fallecidos
    d['recuperados'] = recuperados
    
    return d

print(informes_covid ('casos_covid.csv'))

#%%
import pandas as pd
import numpy as np
filename = 'casos_covid.csv'
df = pd.read_csv(filename, sep=',')
mayor_contagio = df['País de procedencia'].value_counts().index[0]
cantidad_contagios = df['País de procedencia'].value_counts()[0]
print(cantidad_contagios)
# print(df[['País de procedencia','Fecha de muerte']][(df['País de procedencia'] == mayor_contagio)]['Fecha de muerte'].value_counts().sum())
recuperados = df[['País de procedencia','Fecha recuperado']][(df['País de procedencia'] == mayor_contagio)]['Fecha recuperado'].value_counts().sum()
fallecidos = cantidad_contagios - recuperados

d = {}
d['mayor_contagio'] = mayor_contagio
d['cantidad_contagios'] = cantidad_contagios
d['fallecidos'] = fallecidos
d['recuperados'] = recuperados

print(d)

#%%
print(df.columns)
print(df.head())