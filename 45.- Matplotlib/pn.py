import pandas as pd
import numpy as np

# Crear un conjunto de datos de ejemplo
data = {
    'Region': ['Norte', 'Sur', 'Este', 'Oeste', 'Norte', 'Sur', 'Este', 'Oeste'],
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto'],
    'Ventas': [100, 200, 300, 400, 500, 600, 700, 800]
}

# Crear un DataFrame a partir del conjunto de datos
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Calcular la suma de las ventas por región
ventas_por_region = df.groupby('Region')['Ventas'].sum()
print(ventas_por_region)

# Calcular la media de las ventas por mes
ventas_por_mes = df.groupby('Mes')['Ventas'].mean()
print(ventas_por_mes)

# Calcular la desviación estándar de las ventas por región
desviacion_estandar = df.groupby('Region')['Ventas'].std()
print(desviacion_estandar)

# Crear un gráfico de barras para mostrar las ventas por región
import matplotlib.pyplot as plt
ventas_por_region.plot(kind='bar')
plt.title('Ventas por región')
plt.xlabel('Región')
plt.ylabel('Ventas')
plt.show()