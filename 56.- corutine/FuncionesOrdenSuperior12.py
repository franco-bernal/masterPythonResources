'''
En este ejemplo, se definen dos corutinas data_coroutine_1
y data_coroutine_2, ambas conectadas a la función
process_data que recibe y procesa los datos.
Las funciones send_data_1 y send_data_2 se encargan
de enviar datos a cada corutina respectivamente.

Al ejecutar este código, ambas corutinas estarán
activas y recibirán datos de las funciones send_data_1
y send_data_2. Cada corutina enviará los datos recibidos
 a la función process_data, que los procesará según su origen.

Este ejemplo muestra cómo dos corutinas pueden coexistir
y enviar datos de forma independiente a una tercera función
en Python, permitiendo una comunicación paralela y concurrente
entre las corutinas y la función receptora.

'''
# Definir la tercera función que recibe datos de las corutinas
def process_data():
    while True:
        data_origin, data = yield
        print(f"Dato recibido de {data_origin}: {data}")
        # Aquí puedes realizar cualquier procesamiento adicional con los datos recibidos

# Crear instancias de las corutinas
data_coroutine_1 = process_data()
next(data_coroutine_1)  # Iniciar la corutina 1
data_coroutine_2 = process_data()
next(data_coroutine_2)  # Iniciar la corutina 2

# Función que envía datos a la primera corutina
def send_data_1():
    while True:
        char = input("Corutina 1 - Por favor, introduce un carácter: ")
        data_coroutine_1.send(("Corutina 1", char))

# Función que envía datos a la segunda corutina
def send_data_2():
    while True:
        text = input("Corutina 2 - Por favor, introduce un texto: ")
        data_coroutine_2.send(("Corutina 2", text))

# Ejecutar las funciones para enviar datos a las corutinas
send_data_1()
send_data_2()