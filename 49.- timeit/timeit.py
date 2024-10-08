import timeit

def ejemplo_funcion():
    resultado = 0
    for i in range(1000000):
        resultado += i
    return resultado

# Medir el tiempo de ejecución de la función
tiempo_ejecucion = ti.timeit(ejemplo_funcion, number=100)

print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")

# Medir el tiempo de ejecución de una expresión
expresion = "1 + 2 + 3 + 4 + 5"
tiempo_ejecucion_expresion = ti.timeit(expresion, number=1000)

print(f"Tiempo de ejecución de la expresión: {tiempo_ejecucion_expresion:.6f} segundos")

# Medir el tiempo de ejecución de un bloque de código
bloque_codigo = """
x = 0
for i in range(1000):
    x += i
"""
tiempo_ejecucion_bloque = ti.timeit(bloque_codigo, number=100)

print(f"Tiempo de ejecución del bloque de código: {tiempo_ejecucion_bloque:.6f} segundos")