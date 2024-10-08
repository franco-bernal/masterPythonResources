# Definir una corutina que recibe y procesa caracteres
def process_character():
    while True:
        character = yield
        print(f"Carácter recibido: {character}")
        # Aquí puedes realizar cualquier procesamiento adicional con el carácter recibido

# Crear una instancia de la corutina
character_coroutine = process_character()
next(character_coroutine)  # Iniciar la corutina

# Función que solicita un carácter al usuario y lo envía a la corutina
def request_character():
    while True:
        char = input("Por favor, introduce un carácter: ")
        character_coroutine.send(char)

# Ejecutar la función que solicita un carácter
request_character()