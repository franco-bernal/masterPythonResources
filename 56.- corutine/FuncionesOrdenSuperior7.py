'''
or supuesto, otro concepto avanzado relacionado
con las funciones de orden superior en Python
 es el uso de funciones generadoras y corutinas.
 Las funciones generadoras son un tipo especial
 de funciones que pueden pausar su ejecución y luego
 reanudarla, lo que permite generar secuencias
 de valores de manera eficiente. Por otro lado,
 las corutinas son rutinas colaborativas que pueden
  enviar y recibir valores entre sí de manera asincrónica.
'''
# Definir una función generadora que genera una secuencia infinita de números pares
def generate_even_numbers():
    n = 0
    while True:
        yield n
        n += 2

# Definir una corutina que recibe números, los multiplica por un factor y devuelve el resultado
def multiplier_coroutine(factor):
    while True:
        number = yield
        result = number * factor
        print(f"Result: {result}")

# Crear una instancia de la corutina con un factor de multiplicación
coroutine = multiplier_coroutine(5)
next(coroutine)  # Iniciar la corutina

# Utilizar la función generadora para generar números pares y enviarlos a la corutina
even_number_generator = generate_even_numbers()
for _ in range(5):
    even_number = next(even_number_generator)
    coroutine.send(even_number)

'''
En este ejemplo, la función generate_even_numbers es una
 función generadora que produce una secuencia infinita de
  números pares. La corutina multiplier_coroutine recibe 
  números, los multiplica por un factor y muestra el 
  resultado. Al combinar la función generadora con la 
  corutina, podemos generar números pares y enviarlos 
  a la corutina para ser multiplicados.

Las funciones generadoras y corutinas son herramientas 
avanzadas en Python que permiten trabajar con secuencias 
y operaciones asincrónicas de manera eficiente y flexible.
 Este ejemplo ilustra cómo puedes utilizar estas funcionalidades 
 avanzadas para crear flujos de datos interactivos 
 y colaborativos en tus programas.
'''
'''
Nota:
la línea next(coroutine) se utiliza para iniciar la corutina
 antes de enviarle valores. Cuando se crea una instancia 
 de la corutina utilizando multiplier_coroutine(5), 
 la corutina está en un estado de "suspensión" en 
 la primera línea de la función, esperando a que se le envíe un valor.

Al llamar a next(coroutine), se avanza la corutina 
hasta el primer punto de pausa (representado por yield),
 lo que permite preparar la corutina para recibir valores a través de send().
  En esencia, next(coroutine) "arranca" la corutina y la coloca en un 
  estado listo para recibir datos.

Después de llamar a next(coroutine) para inicializar 
la corutina, el bucle for recorre los primeros 5 números 
pares generados por la función generadora generate_even_numbers. 
En cada iteración del bucle, se obtiene un número par utilizando 
next(even_number_generator) y se envía ese número a la corutina 
mediante coroutine.send(even_number). La corutina recibe el número, 
lo multiplica por el factor establecido (en este caso, 5) y muestra el resultado.

En resumen, la línea next(coroutine) se utiliza para iniciar la 
corutina antes de comenzar a enviarle valores, preparándola para 
recibir datos a través de send(). Es un paso importante para asegurarse 
de que la corutina esté lista para funcionar correctamente y procesar 
los valores que se le enviarán. 
'''