'''
Qué es el perfilado de código?

El perfilado de código es un proceso que se utiliza para medir
el rendimiento de un programa y identificar las partes del
código que consumen más tiempo y recursos. Esto se hace
mediante la recopilación de datos sobre la ejecución del
programa, como el tiempo que se tarda en ejecutar cada función,
el número de llamadas a cada función, etc.

¿Qué es cProfile?

cProfile es un módulo de Python que se utiliza para realizar el
perfilado de código. Es una herramienta que se integra con el
intérprete de Python y que recopila datos sobre la ejecución del programa en tiempo real.

Cómo funciona cProfile

cProfile funciona de la siguiente manera:

Creación de un objeto Profile: Se crea un objeto Profile que se utilizará
para recopilar los datos del perfilado.Activación del perfilado: Se activa el
perfilado mediante el método enable() del objeto Profile. Esto hace que el intérprete
de Python comience a recopilar datos sobre la ejecución del programa.
Ejecución del programa: Se ejecuta el programa que se desea perfilar.
Desactivación del perfilado: Se desactiva el perfilado mediante el método disable() del
objeto Profile. Esto hace que el intérprete de Python deje de recopilar datos sobre la ejecución del programa.
Recopilación de los datos del perfilado: Se recopilan los datos del perfilado mediante
el método print_stats() del objeto Profile. Esto imprime los datos del perfilado en la consola.
Datos del perfilado

Los datos del perfilado que se recopilan con cProfile incluyen:

Número de llamadas: El número de veces que se llamó a cada función.
Tiempo total: El tiempo total que se tardó en ejecutar cada función.
Tiempo por llamada: El tiempo que se tardó en ejecutar cada función por llamada.
Tiempo acumulado: El tiempo total que se tardó en ejecutar cada función, incluyendo el tiempo que
se tardó en ejecutar las funciones que se llamaron desde ella.
Ordenación de los datos del perfilado

Los datos del perfilado se pueden ordenar de diferentes maneras, como:

Orden alfabético: Los datos del perfilado se ordenan alfabéticamente por nombre de función.
Orden por número de llamadas: Los datos del perfilado se ordenan por número de llamadas.
Orden por tiempo total: Los datos del perfilado se ordenan por tiempo total.
Orden por tiempo por llamada: Los datos del perfilado se ordenan por tiempo por llamada.
Orden por tiempo acumulado: Los datos del perfilado se ordenan por tiempo acumulado.
Espero que esta explicación te haya ayudado a entender cómo funciona el perfilado de
código con cProfile en Python. ¡Si tienes alguna otra pregunta, no dudes en preguntar!
'''
import cProfile

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = 30
    result = fibonacci(n)
    print(f"El resultado de fibonacci({n}) es {result}")

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    profiler.print_stats(sort="cumulative")