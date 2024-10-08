import random
import time
import string

max_iteraciones = 10
iteracion = 0

while iteracion < max_iteraciones:
    caracter = random.choice(string.ascii_letters)
    print(caracter)
    time.sleep(1)
    iteracion += 1