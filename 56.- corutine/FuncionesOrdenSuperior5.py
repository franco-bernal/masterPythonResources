'''
la función apply_transform es una función de orden
superior que aplica una función de transformación a
cada elemento de una lista y devuelve una nueva
lista con los resultados transformados.
Las funciones square, double y cube son funciones
de transformación que elevan al cuadrado,
duplican y elevan al cubo un número respectivamente.

Al aplicar diferentes transformaciones a la lista
de números utilizando la función de orden superior
apply_transform, puedes obtener fácilmente las listas
de números al cuadrado, duplicados y al cubo.
Este enfoque demuestra el poder y la flexibilidad
de las funciones de orden superior en Python para
aplicar operaciones de manera genérica a los datos
'''
# Definir una función de orden superior que toma una función de transformación como argumento
def apply_transform(func, data):
    return [func(x) for x in data]

# Definir funciones de transformación
def square(x):
    return x ** 2

def double(x):
    return x * 2

def cube(x):
    return x ** 3

# Crear una lista de números
numbers = [1, 2, 3, 4, 5]

# Aplicar diferentes transformaciones a la lista de números usando la función de orden superior
squared_numbers = apply_transform(square, numbers)
doubled_numbers = apply_transform(double, numbers)
cubed_numbers = apply_transform(cube, numbers)

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Doubled numbers:", doubled_numbers)
print("Cubed numbers:", cubed_numbers)