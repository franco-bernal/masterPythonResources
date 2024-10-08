import psutil

def obtener_cantidad_ram_utilizada_en_mb():
    ram_total = psutil.virtual_memory().total / (1024.0 ** 2)
    ram_utilizada = psutil.virtual_memory().used / (1024.0 ** 2)
    ram_libre = ram_total - ram_utilizada
    porcentaje_ram_utilizada = (ram_utilizada / ram_total) * 100
    return ram_utilizada

print(obtener_cantidad_ram_utilizada_en_mb())