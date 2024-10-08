import json
import random
from faker import Faker

# Crear una instancia de Faker para generar datos ficticios
fake = Faker()

# Generar 200 registros ficticios
registros = []
for i in range(1, 201):
    registro = {
        "id": i,
        "nombre": fake.name(),
        "edad": random.randint(18, 99),
        "ciudad": fake.city()
    }
    registros.append(registro)

# Ruta al archivo JSON
archivo_json = 'archivo5.json'

# Guardar los registros en el archivo JSON
with open(archivo_json, 'w', encoding='utf-8') as archivo:
    json.dump(registros, archivo, indent=4, ensure_ascii=False)

print(f"Archivo '{archivo_json}' creado con 200 registros.")
