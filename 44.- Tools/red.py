import psutil
import time

def obtener_trafico_red_por_segundo():
    trafico_red_anterior = psutil.net_io_counters()
    time.sleep(1)
    trafico_red_actual = psutil.net_io_counters()
    diferencia_trafico_red = {
        'bytes_sent': trafico_red_actual.bytes_sent - trafico_red_anterior.bytes_sent,
        'bytes_recv': trafico_red_actual.bytes_recv - trafico_red_anterior.bytes_recv,
        'packets_sent': trafico_red_actual.packets_sent - trafico_red_anterior.packets_sent,
        'packets_recv': trafico_red_actual.packets_recv - trafico_red_anterior.packets_recv,
    }
    return diferencia_trafico_red

print(obtener_trafico_red_por_segundo())