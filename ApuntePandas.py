import pandas as pd 

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

#print(df.head())

# 1. Número de partidos
print("Número de partidos:", df.shape[0])

# 2. Total de goles
print("Goles totales:", df['FTHG'].sum() + df['FTAG'].sum())

# 3. Número de empates
print("Empates:", df[df['FTR'] == 'D'].shape[0])

# Filtro de partidos donde:
# - el resultado final fue victoria visitante ('A')
# - y el visitante anotó más de 2 goles (FTAG > 2)

filtro = (df['FTR'] == 'A') & (df['FTAG'] > 2)
df_filtrado = df[filtro]

#print(df_filtrado[['Date', 'HomeTeam', 'AwayTeam', 'FTAG', 'FTR']])

# Partidos jugados de local por R. Madrid
real_madrid_local = df[df['HomeTeam'] == 'Real Madrid']
print("Partidos locales del Real Madrid:")
print(real_madrid_local)

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