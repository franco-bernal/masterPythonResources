'''
En este ejemplo, la corutina filter_numbers recibe
números a través de yield y los filtra en dos listas separadas:
 una para números pares y otra para números impares.
 Cada vez que un número es enviado a la corutina,
 se verifica si es par o impar y se agrega a la lista
 correspondiente. Luego, se imprimen las listas de números pares e impares actualizadas.

Al crear una instancia de la corutina filter_numbers y
llamar a next(filter_coroutine) para iniciarla, la corutina
está lista para recibir números y filtrarlos. Luego, se envían
los números de la lista numbers a la corutina uno por uno utilizando
filter_coroutine.send(number).

Al ejecutar este código, verás cómo la corutina filtra los
números pares e impares de la secuencia proporcionada y muestra
las listas actualizadas en cada paso. Las corutinas son una
 herramienta poderosa en Python para crear flujos de control asincrónicos
 y colaborativos, y este ejemplo ilustra cómo puedes usarlas para
  procesar y clasificar datos de manera eficiente. ¡Espero que
   este ejemplo te resulte útil y que te ayude a comprender mejor
    el concepto de corutinas en Python
'''
# Definir una corutina que filtra números pares e impares
def filter_numbers():
    even_numbers = []
    odd_numbers = []
    while True:
        number = yield
        if(number[0]==1):

            
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
        print(f"Even numbers: {even_numbers}")
        print(f"Odd numbers: {odd_numbers}")

# Crear una instancia de la corutina
filter_coroutine = filter_numbers()
next(filter_coroutine)  # Iniciar la corutina

# Enviar números a la corutina para filtrarlos
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    filter_coroutine.send(number)