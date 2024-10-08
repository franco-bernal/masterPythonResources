'''
Devolver funciones como resultado: Las funciones de orden
 superior también pueden devolver funciones como resultado.
 Esto es útil para crear funciones especializadas
 o configurables en tiempo de ejecución.
'''
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiply_by_3 = create_multiplier(3)
result = multiply_by_3(5)
print(result)  # Output: 15
