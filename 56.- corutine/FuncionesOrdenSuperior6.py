'''

la función create_increment_function es una función
de orden superior que crea y devuelve una función
de incremento con un paso dado. Al llamar a
create_increment_function con un paso específico,
se obtiene una función de incremento que incrementará un número por ese paso.

Al crear funciones de incremento con diferentes pasos
y luego aplicarlas a un número dado, puedes observar
 cómo las clausuras en Python permiten que las funciones
 internas recuerden y accedan al entorno en el que fueron
  creadas, en este caso, el valor del paso.

Este ejemplo ilustra cómo las funciones de orden superior
y las clausuras pueden combinarse para crear funciones más
flexibles y personalizables en Python

'''
# Función de orden superior que crea y devuelve una función de incremento con un paso dado
def create_increment_function(step):
    def increment(x):
        return x + step
    return increment

# Crear funciones de incremento con diferentes pasos
increment_by_2 = create_increment_function(2)
increment_by_5 = create_increment_function(5)

# Utilizar las funciones de incremento para aumentar un número
number = 10
incremented_by_2 = increment_by_2(number)
incremented_by_5 = increment_by_5(number)

print(f"Original number: {number}")
print(f"Number incremented by 2: {incremented_by_2}")
print(f"Number incremented by 5: {incremented_by_5}")