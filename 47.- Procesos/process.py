import psutil
import time

# Ejecuta el código Python que deseas supervisar
process = psutil.Popen(['python', 'pro.py'])

while True:
    # Verifica si el proceso sigue en ejecución
    if process.poll() is not None:
        # Si el proceso se detuvo, reinícialo
        process = psutil.Popen(['python', 'pro.py'])
    time.sleep(1)