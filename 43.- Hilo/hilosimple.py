import threading
import random
import time
import sys

# Variable para controlar la pausa del hilo 1
pause_hilo1 = False

def hilo1():
    global pause_hilo1
    while True:
        if not pause_hilo1:
            print("Mensaje cada 5 segundos")
        time.sleep(5)

def hilo2():
    while True:
        print("Número random cada 10 segundos:", random.randint(1, 100))
        time.sleep(10)

# Crear hilos
hilo1_thread = threading.Thread(target=hilo1)
hilo2_thread = threading.Thread(target=hilo2)

# Iniciar hilos
hilo1_thread.start()
hilo2_thread.start()

# Leer input del usuario
while True:
    comando = input()
    if comando == "x":
        pause_hilo1 = True
        print("Hilo 1 pausado")
    elif comando == "y":
        pause_hilo1 = False
        print("Hilo 1 reanudado")
    elif comando == "q":
        print("Saliendo...")
        sys.exit(0)