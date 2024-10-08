import threading
import random
import time
import sys
import os
import ctypes

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

# Establecer prioridad máxima para el hilo 1
if os.name == 'nt':  # Windows
    # Get the current thread handle
    hilo1_handle = ctypes.windll.kernel32.OpenThread(0x02000000, False, hilo1_thread.ident)
    # Set the priority to high
    ctypes.windll.kernel32.SetThreadPriority(hilo1_handle, 2)
    # Close the thread handle
    ctypes.windll.kernel32.CloseHandle(hilo1_handle)
elif os.name == 'posix':  # Linux, macOS
    # Get the current thread ID
    hilo1_id = hilo1_thread.ident
    # Set the priority to high
    os.system(f"renice -n -1 -p {hilo1_id}")

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