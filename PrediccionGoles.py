import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Cargar datos
df = pd.read_csv("LaLiga.csv", encoding='ISO-8859-1')
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
df['Referee'].fillna('Sin dato', inplace=True)

# Elegir equipo
equipo = 'Real Madrid'

# Filtrar partidos donde fue local o visitante
datos_local = df[df['HomeTeam'] == equipo]
datos_visita = df[df['AwayTeam'] == equipo]

# Crear DataFrame unificado con variables y goles
datos_local = datos_local[['HST', 'HS', 'HTHG', 'HF', 'FTHG']]
datos_visita = datos_visita[['AST', 'AS', 'HTAG', 'AF', 'FTAG']]
datos_visita.columns = ['HST', 'HS', 'HTHG', 'HF', 'FTHG']  # renombrar para unificar

# Unir todos los partidos
datos_equipo = pd.concat([datos_local, datos_visita], ignore_index=True)

# Variables independientes (X) y dependiente (y)
X = datos_equipo[['HST', 'HS', 'HTHG', 'HF']]
y = datos_equipo['FTHG']

# Entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción
y_pred = modelo.predict(X)

# Evaluación del modelo
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"\nError cuadrático medio (MSE): {mse:.4f}")
print(f"Coeficiente de determinación (R²): {r2:.4f}")

# Visualizar predicción con valores reales
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y)), y, label='Goles reales', color='blue')
plt.plot(range(len(y_pred)), y_pred, label='Goles predichos', color='red')
plt.xlabel('Partido')
plt.ylabel('Goles')
plt.title(f'Predicción de goles para {equipo} (Regresión múltiple)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
