'''
Pasar funciones como argumentos: En Python,
 puedes pasar funciones como argumentos a otras funciones.
  Esto permite la modularidad y reutilización del código
  al poder definir funciones genéricas que pueden aceptar
  diferentes funciones como entrada.
'''
def apply_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

result = apply_operation(add, 3, 4)
print(result)  # Output: 7