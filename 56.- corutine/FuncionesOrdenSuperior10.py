import threading

# Definir una corutina que recibe y procesa datos identificando el origen
def process_data():
    while True:
        data_origin, data = yield
        print(f"Dato recibido de {data_origin}: {data}")
        # Aquí puedes realizar cualquier procesamiento adicional con los datos recibidos

# Crear una instancia de la corutina
data_coroutine = process_data()
next(data_coroutine)  # Iniciar la corutina

# Función que solicita un carácter al usuario y lo envía a la corutina
def send_character():
    while True:
        char = input("Por favor, introduce un carácter: ")
        data_coroutine.send(("Función 1", char))

# Función que envía un texto al usuario y lo envía a la corutina identificando su origen
def send_text():
    while True:
        text = input("Por favor, introduce un texto: ")
        data_coroutine.send(("Función 2", text))

# Ejecutar las funciones en hilos separados
thread_character = threading.Thread(target=send_character)
thread_text = threading.Thread(target=send_text)

thread_character.start()
thread_text.start()

thread_character.join()
thread_text.join()