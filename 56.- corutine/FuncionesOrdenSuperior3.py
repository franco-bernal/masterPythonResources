'''
Funciones lambda: Las funciones lambda son funciones
anónimas y simples que se pueden definir en línea.
Son comúnmente utilizadas en conjunto con funciones de
orden superior para escribir código más conciso y legible.
'''
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

