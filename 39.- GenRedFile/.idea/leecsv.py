import csv

# Ruta al archivo CSV
archivo_csv = 'registros.csv'


# Función para leer y mostrar el contenido del archivo CSV
def leer_csv(ruta_archivo):
    try:
        # Abrir el archivo CSV
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            # Mostrar el contenido
            print("Contenido del archivo CSV:")
            for fila in lector:
                print(fila)

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encuentra.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


# Llamar a la función para leer el archivo CSV
leer_csv("registros2.csv")
