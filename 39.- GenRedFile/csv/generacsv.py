import csv
import random
from faker import Faker

# Crear una instancia de Faker para generar datos ficticios
fake = Faker()

# Ruta al archivo CSV
archivo_csv = 'registros2.csv'

# Generar 300 registros ficticios
registros = []
for i in range(1, 301):
    registro = {
        "id": i,
        "nombre": fake.name(),
        "edad": random.randint(18, 99),
        "ciudad": fake.city()
    }
    registros.append(registro)

# Escribir los registros en el archivo CSV
with open(archivo_csv, 'w', newline='', encoding='utf-8') as archivo:
    campo_nombres = ['id', 'nombre', 'edad', 'ciudad']
    writer = csv.DictWriter(archivo, fieldnames=campo_nombres)

    # Escribir la cabecera
    writer.writeheader()

    # Escribir los registros
    writer.writerows(registros)

print(f"Archivo '{archivo_csv}' creado con 300 registros.")
