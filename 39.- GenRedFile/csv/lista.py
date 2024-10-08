import csv

# Ruta al archivo CSV
file_path = 'registros2.csv'

# Abrir el archivo CSV
with open(file_path, 'r') as file:
    # Crear un objeto lector de CSV
    csv_reader = csv.reader(file)

    # Obtener la primera fila (encabezados)
    headers = next(csv_reader)

    # Recorrer los registros
    for row in csv_reader:
        # Acceder a los valores de cada columna
        col1 = row[0]
        col2 = row[1]
        col3 = row[2]

        # Hacer algo con los valores de cada registro
        print(f"----------------------------------------")
        print(f"Registro: {csv_reader.line_num}")
        print(f"  Columna 1: {col1}")
        print(f"  Columna 2: {col2}")
        print(f"  Columna 3: {col3}")
        print(f"----------------------------------------")