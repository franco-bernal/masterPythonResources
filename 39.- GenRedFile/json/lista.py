import json

# Ruta al archivo JSON
archivo_json = 'registros2.json'


# Función para leer y listar el contenido del archivo JSON
def listar_contenido_json(ruta_archivo):
    try:
        # Abrir el archivo JSON
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            # Cargar el contenido del archivo JSON
            contenido = json.load(archivo)

            # Mostrar el contenido en formato legible
            print("Contenido del archivo JSON:")
            print(json.dumps(contenido, indent=4, ensure_ascii=False))

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encuentra.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato incorrecto.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


# Llamar a la función para listar el contenido
listar_contenido_json("registros2.json")
