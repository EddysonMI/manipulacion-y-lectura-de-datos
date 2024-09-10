import pandas as pd


data = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis'],
        'Edad': [28, 34, 45, 29, 50],
        'Ciudad': ['Peru', 'Chile', 'Argentina', 'Brasil', 'Uruguay'],
        'Salario': [35000, 40000, 50000, 38000, 45000]}
df = pd.DataFrame(data)


df_seleccion = df[['Nombre', 'Salario']]
print(df_seleccion)


df_madrid = df[df['Ciudad'] == 'Madrid']
print(df_madrid)
