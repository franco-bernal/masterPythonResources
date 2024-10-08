'''
Otra forma de utilizar funciones de orden
 superior en Python es a través del uso de
  funciones como objetos de primera clase.
   Esto significa que las funciones se pueden asignar a variables,
    almacenar en estructuras de datos, pasar como argumentos
    y devolver como valores de otras funciones. Aquí tienes un
    ejemplo de cómo se puede lograr esto:
'''
def greet(func):
    return func()

def say_hello():
    return "Hello!"

def say_goodbye():
    return "Goodbye!"

# Asignar funciones a variables
my_func = say_hello
print(my_func())  # Output: Hello!

# Almacenar funciones en una lista
func_list = [say_hello, say_goodbye]
for func in func_list:
    print(greet(func))  # Output: Hello! Goodbye!