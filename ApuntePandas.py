import pandas as pd 
import numpy as np
import matplotlib as plt

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

print("")
# Agrupación por columna
locales = df.groupby('HomeTeam')['FTHG'].sum()
print("Agrupado por equipo local y después suma de goles locales")
print(locales.head())

print("")
# Promedio de tarjetas sobre equipo local
# En este caso agrupara todo lo del Madrid por ejemplo y sacará el promedio de tarjetas amarillas.
amarillas_sobre_local = df.groupby('HomeTeam')['HY'].mean()
print("Promedio de amarillas sobre equipo local: ")
print(amarillas_sobre_local.head())

print("")
# Agrupamiento por más columnas, poniendolas en arreglo para el parámetro
# Agrupa por equipo y luego agrupa sus resultados para ver cuantas veces ha ganado o perdido
doble_columna = df.groupby(['HomeTeam', 'FTR']).size()
print("Agrupamiento por doble columna")
print(doble_columna.head())

print("")
# Lista de equipos mas goleadores en casa de mayor a menor
goleadores_locales = df.groupby('HomeTeam')['FTHG'].sum().sort_values(ascending=False)
print(goleadores_locales.head())

print("")
# Goles del Real Madrid como local
# Primer método: Aplico un filtro para seleccionar donde el Madrid es local
madrid_local = df[df['HomeTeam'] == 'Real Madrid']
goles_madrid_local = madrid_local['FTHG'].sum()
print("PRIMER MÉTODO")
print("Goles del Real Madrid como local")
print(madrid_local)
print("Goles de local del Real Madrid: ", goles_madrid_local)

# Segundo método: Agrupo por equipo local y sumo los goles locales, luego busco al real madrid y devuelvo el valor
goles_equipos = df.groupby('HomeTeam')['FTHG'].sum()
goles_madrid = goles_equipos['Real Madrid']
print("SEGUNFO MÉTODO")
print(goles_equipos)
print("Goles del Real Madrid:")
print(goles_madrid)

print("")
# Equipo con más goles recibidos como visitante
goles_recibidos_equipos_visitantes = df.groupby('AwayTeam')['FTHG'].sum().sort_values(ascending=False)
equipo_visitante_mas_goleado = goles_recibidos_equipos_visitantes.idxmax() 
print("Equipos más goleados:")
print(goles_recibidos_equipos_visitantes)
print(equipo_visitante_mas_goleado)

print("")
# Promedio de goles por partido para cada equipo visitante
promedio_goles_visitantes = df.groupby("AwayTeam")['FTAG'].mean()
print("Promedio de goles por equipo visitante")
print(promedio_goles_visitantes.head())

print("")
# Ordenamiento por columnas
# Partidos con más goles del local
partidos_mas_goles_local = df.sort_values('FTHG', ascending=False)
print("Partidos con más goles del local")
print(partidos_mas_goles_local.head())

print("")
# Filtro de partidos donde Madrid fue local y anotó al menos 3 goles
madrid_local_goleador = df[(df['HomeTeam'] == 'Real Madrid') & (df['FTHG'] >= 3)]
print("Partidos donde Real Madrid anotó al menos 3 goles de local")
print(madrid_local_goleador.head())

print("")
# Nueva serie para agrupar los puntos conseguidos de cada equipo en la temporada
puntos_local = df.copy()
puntos_local['Puntos'] = np.where(puntos_local['Ganador'] == 'Local', 3, np.where(puntos_local['Ganador'] == 'Visitante', 0, 1))
puntos_visitante = df.copy()
puntos_visitante['Puntos'] = np.where(puntos_visitante['Ganador'] == 'Visitante', 3, np.where(puntos_visitante['Ganador'] == 'Local', 0, 1))
puntos_local = puntos_local.groupby('HomeTeam')['Puntos'].sum()
puntos_visitante = puntos_visitante.groupby('AwayTeam')['Puntos'].sum()
tabla_puntos = puntos_local.add(puntos_visitante, fill_value=0).sort_values(ascending=False)
print("Tabla de puntos de la temporada")
print(tabla_puntos.head())

# Exportar la tabla de puntos por equipo
tabla_puntos.to_csv('tabla_de_LaLiga.csv', index=False)
tabla_puntos.to_excel('tabla_de_LaLiga.xlsx', index=True)

# Extraer componentes de fecha
df['Año'] = df['Date'].dt.year
df['Mes'] = df['Date'].dt.month
df['Día'] = df['Date'].dt.day
df['NombreMes'] = df['Date'].dt.month_name()
df['NombreDía'] = df['Date'].dt.day_name()
# Elementos de la fecha
print("Fecha separada")
print(df.head())

print("")
# Manejo de Resample()
fechas = df.copy()
fechas.set_index('Date', inplace=True)
goles_mensuales = fechas['TG'].resample('M').sum()
print("Uso de resamble para análisis por periodos de tiempo")
print(goles_mensuales)