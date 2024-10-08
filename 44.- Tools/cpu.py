import psutil
import time

def obtener_porcentaje_cpu():
    cpu_porcentaje = psutil.cpu_percent(interval=1)  # Medir cada 1 segundo
    return cpu_porcentaje

print(obtener_porcentaje_cpu())
