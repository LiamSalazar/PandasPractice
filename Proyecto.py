import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from RegresionLinealSimple import RegresionLineal

# Descripción del proyecto
# Analizar el desempeño de los equipos en la temporada 2011–2012 y predecir la cantidad de 
# goles que marcará un equipo en función de variables como localía, rival, jornada, rendimiento acumulado, etc.

# Lectura y casteo de datos
df = pd.read_csv("LaLiga.csv", encoding='ISO-8859-1')
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')

# Creación de columnas útiles
df['Goles Totales'] = df['FTHG'] + df['FTAG']
df['Referee'].fillna('Sin dato', inplace=True) # Rellenar columna de árbitros

# Equipos con más goles de local y visitante
goles_locales = df.groupby('HomeTeam')['FTHG'].sum().sort_values(ascending=False)
goles_visitante = df.groupby('AwayTeam')['FTAG'].sum().sort_values(ascending=False)
print("\nEquipos más goleadores locales")
print(goles_locales)
print("\nEquipos más goleadores visitantes")
print(goles_visitante)

# Distribución de resultados
resultados = df['FTR'].value_counts()
print("\nDistribución general de resultados:")
print(resultados)

# Victorias locales y visitantes
victorias_locales = df[df['FTR'] == 'H'].groupby('HomeTeam').size().sort_values(ascending=False)
victorias_visitantes = df[df['FTR'] == 'A'].groupby('AwayTeam').size().sort_values(ascending=False)

print("\nTop equipos con más victorias como local:")
print(victorias_locales.head())

print("\nTop equipos con más victorias como visitante:")
print(victorias_visitantes.head())

# Goles totales por equipo
goles_por_equipo = df.groupby('HomeTeam')['FTHG'].sum().add(
    df.groupby('AwayTeam')['FTAG'].sum(), fill_value=0
).sort_values(ascending=False)

print("\nTop equipos con más goles totales:")
print(goles_por_equipo.head())

# Empates por equipo
empates_local = df[df['FTR'] == 'D'].groupby('HomeTeam').size()
empates_visita = df[df['FTR'] == 'D'].groupby('AwayTeam').size()
empates_totales = empates_local.add(empates_visita, fill_value=0).sort_values(ascending=False)

print("\nTop equipos con más empates (local + visitante):")
print(empates_totales.head())

# Grafica de goles por equipo
goles_por_equipo.plot(kind='bar', figsize=(10, 5))
plt.title("Goles por equipo")
plt.ylabel("Goles")
plt.show()

# Grafica de partidos ganados, empatados y perdidos
resultados.head(5).plot(kind='pie', y=None, autopct='%1.1f%%', figsize=(6,6))
plt.title("Distribución de resultados")
plt.ylabel("")
plt.show()

# Predicción de goles basado en tiros a puerta considerando efectividad de los equipos
# Primero se obtendrá la efectividad por cada equipo

# Goles y tiros como local
local = df.groupby('HomeTeam')[['FTHG', 'HST']].sum()
local.columns = ['Goles', 'Tiros']

# Goles y tiros como visitante
visitante = df.groupby('AwayTeam')[['FTAG', 'AST']].sum()
visitante.columns = ['Goles', 'Tiros']

# Goles y tiros totales
efectividad = local.add(visitante, fill_value=0)

efectividad['Efectividad'] = efectividad['Goles'] / efectividad['Tiros']
efectividad = efectividad.sort_values(by='Efectividad', ascending=False)
print(efectividad.round(3))


# Elección de equipo y filtro para predicción
equipo = 'Barcelona' # Elección del equipo
datos_equipo_local = df[df['HomeTeam'] == equipo] # Obtención de datos específicos
datos_equipo_visitante = df[df['AwayTeam'] == equipo] # Obtención de datos específicos
x1 = datos_equipo_local['HST'].tolist() # Obtención de tiros a puerta
y1 = datos_equipo_local['FTHG'].tolist() # Obtención de goles hechos
x2 = datos_equipo_visitante['AST'].tolist() # Obtención de tiros a puerta
y2 = datos_equipo_visitante['FTAG'].tolist() # Obtención de goles hechos
x = x1+x2
y = y1+y2

# Limpieza de datos
x_filtrado = []
y_filtrado = []

for i in range(len(x)):
    if x[i] > 0 and y[i] / x[i] <= 1:
        x_filtrado.append(x[i])
        y_filtrado.append(y[i])


# Uso de modelo para la regresion lineal
modelo = RegresionLineal()
predicciones = modelo.estimaciones(x_filtrado,y_filtrado) # Obtención de y para la recta
m = modelo.calcularPendiente(x_filtrado, y_filtrado)
b = modelo.calcularOrdenada(x_filtrado, y_filtrado)
print(f"\nRegresión para {equipo}: y = {m:.4f}x + {b:.4f}")

# Graficación del modelo
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Datos reales')
plt.plot(x, predicciones, color='red', label='Regresión lineal')
plt.xlabel('Disparos a puerta')
plt.ylabel('Goles')
plt.title(f'Regresión lineal para {equipo}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()