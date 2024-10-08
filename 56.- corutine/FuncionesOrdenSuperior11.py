'''
Definición de la corutina process_data:

Se define una corutina llamada process_data que recibe y procesa datos identificando su origen.
La corutina espera a recibir datos con data_origin, data = yield.
Si el dato recibido es la letra "q", el programa muestra un mensaje de finalización y termina.
Creación de la instancia de la corutina:

Se crea una instancia de la corutina data_coroutine y se inicializa con next(data_coroutine).
Función send_data_1:

La función send_data_1 solicita un carácter al usuario y lo envía a la corutina identificando que proviene de la "Función 1".
Si se ingresa la letra "q", el programa se detiene.
Luego de solicitar el carácter, la función también solicita un texto al usuario y lo envía a la corutina identificando que proviene de la "Función 2".
Si se ingresa la letra "q" en la solicitud de texto, el programa también se detiene.
Ejecución del programa:

Se llama a la función send_data_1 para comenzar la interacción con el usuario.
La función solicita datos al usuario alternadamente entre un carácter y un texto, enviándolos a la corutina.
En resumen, este programa permite que dos funciones soliciten datos al usuario de forma intercalada, con la posibilidad de detener el programa al ingresar la letra "q" en cualquiera de las solicitudes. La comunicación entre las funciones y la corutina se gestiona de manera eficiente utilizando corutinas en Python.
'''
# Definir una corutina que recibe y procesa datos identificando el origen
def process_data():
    while True:
        data_origin, data = yield
        if data == 'q':
            print("Programa terminado.")
            break
        print(f"Dato recibido de {data_origin}: {data}")
        # Aquí puedes realizar cualquier procesamiento adicional con los datos recibidos

# Crear una instancia de la corutina
data_coroutine = process_data()
next(data_coroutine)  # Iniciar la corutina

# Función que solicita un carácter al usuario y lo envía a la corutina
def send_data_1():
    while True:
        char = input("Función 1 - Por favor, introduce un carácter ('q' para salir): ")
        data_coroutine.send(("Función 1", char))
        if char == 'q':
            break
        text = input("Función 2 - Por favor, introduce un texto ('q' para salir): ")
        data_coroutine.send(("Función 2", text))
        if text == 'q':
            break

# Ejecutar la función para solicitar datos
send_data_1()
