import platform
import psutil
import wmi
import subprocess

# Obtener el número de serie de la CPU
cpu_info = subprocess.check_output('wmic cpu get ProcessorId').decode().split('\n')[1].strip()
print("Número de serie de la CPU:", cpu_info)

# Obtener el número de serie de la placa base
w = wmi.WMI()
motherboard_info = w.Win32_BaseBoard()
for board in motherboard_info:
    print("Número de serie de la placa base:", board.SerialNumber)

# Obtener el número de serie del disco duro
disk_info = psutil.disk_partitions()
for disk in disk_info:

    print("Tipo de sistema de archivos del disco duro:", disk.fstype)
