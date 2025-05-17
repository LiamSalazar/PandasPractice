import pandas as pd 
import numpy as np

# Creación de una serie
serie = pd.Series([1,2,3,4,5,6,7,8,9])
#print(serie)

# Creacion de un Data Frame
datos = {
    'Nombres':["Alisson","Marco","José"],
    'Edades':[18, 19, 20]
}
df = pd.DataFrame(datos)
#print(df)

# Lectura de un csv
df = pd.read_csv("LaLiga.csv", encoding='ISO-8859-1')

df.head()          # Primeras 5 filas
df.tail()          # Últimas 5 filas
df.columns         # Lista de columnas
df.shape           # Dimensión del DataFrame (filas, columnas)
#df.info()          # Información general (tipo de datos, valores nulos)
df.describe()      # Estadísticas básicas de columnas numéricas

print("")

# 1. Número de partidos
print("Número de partidos:", df.shape[0])

# 2. Total de goles
print("Goles totales:", df['FTHG'].sum() + df['FTAG'].sum())

# 3. Número de empates
print("Empates:", df[df['FTR'] == 'D'].shape[0])

print("")
# Filtro de partidos
filtro = (df['FTR'] == 'A') & (df['FTAG'] > 2)
df_filtrado = df[filtro]
# Partidos jugados de local por R. Madrid
real_madrid_local = df[df['HomeTeam'] == 'Real Madrid']
print("Partidos locales del Real Madrid:")
print(real_madrid_local)

print("")
# Partidos locales del Madrid con más de 3 goles
print("Partidos locales del Real Madrid con mas de 3 goles:")
madrid_local_goles = df[(df['HomeTeam'] == 'Real Madrid') & (df['FTHG'] > 3)]
print(madrid_local_goles)

# df.loc accede a un dato con loc[fila, nombreColumna]
# df.iloc accede a un dato con iloc[fila, columna], solo índices
# Si solo se pone un valor se toma la fila completa con ese índice en ambos casos
df.loc[0]        
df.loc[0, 'HomeTeam']  
df.iloc[0]        
df.iloc[0, 1]

print("")
# Diferencia de goles
# Se crea una nueva columna restando por cada columna los goles visitantes de los locales
df['DiferenciaGoles'] = df['FTHG'] - df['FTAG']
print("Nuevo DataFrame con diferencia de goles:")
print(df.head())

print("")
# Detectar nulos
df.isnull().sum()  # Número de valores nulos por columna

#df.dropna(inplace=True)  # Elimina filas con cualquier NaN

# Cambiar tipo de dato a entero
# sdf['FTAG'] = df['FTAG'].astype(int)

print("")
# Nueva columna con total de goles del partido
df['TG'] = df['FTAG'] + df['FTHG']
print("Tabla con goles totales por partido")
print(df.head())

print("")
# Nueva columna que diga si ganó el local, visitante o fue empate
df['Ganador'] = np.where(df['FTR'] == 'H', 'Local',
                np.where(df['FTR'] == 'A', 'Visitante', 'Empate'))

# Otra alternativa
def determinar_ganador(resultado):
    if resultado == 'H':
        return 'Local'
    elif resultado == 'A':
        return 'Visitante'
    else:
        return 'Empate'

# df['Ganador'] = df['FTR'].apply(determinar_ganador)

print("Nueva tabla que dice si gana local o visitante")
print(df.head())

print("")
# Cambiar formato de columna fecha para hacer que sea tipo fecha
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y') # En el formato paso el formato actual en que está la fecha para agilizar
print("Nuevo formato de fecha")
print(df.head())

print("")
# Rellenar donde los valores sean NaN en Referee
df['Referee'] = df['Referee'].fillna('Sin dato')
print("Tabla sin valores nulos en referee")
print(df.head())
