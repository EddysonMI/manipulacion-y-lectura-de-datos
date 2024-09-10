import pandas as pd
import numpy as np


df = pd.read_csv('datos.csv')


print("Datos leídos del CSV:\n", df)


print("\nEstadísticas descriptivas:\n", df.describe())


pesos_numpy = df['peso'].values

print("\nArray de NumPy con los pesos:\n", pesos_numpy)


promedio_peso = np.mean(pesos_numpy)
print("\nEl promedio de los pesos es:", promedio_peso)
