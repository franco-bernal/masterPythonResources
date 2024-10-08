import psutil

def obtener_procesos_en_ejecucion():
    procesos = []
    for proc in psutil.process_iter(['pid', 'name']):
        procesos.append((proc.info['pid'], proc.info['name']))
    return procesos

procesos_en_ejecucion = obtener_procesos_en_ejecucion()
for proc in procesos_en_ejecucion:
    print(f"PID: {proc[0]}, Nombre: {proc[1]}")