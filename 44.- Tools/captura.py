import datetime
import pyautogui

# Obtener la fecha y hora actual
fecha_hora = datetime.datetime.now()
nombre_archivo = fecha_hora.strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"

# Capturar la pantalla
img = pyautogui.screenshot()

# Guardar la imagen como archivo JPG
img.save(nombre_archivo)

print("Captura de pantalla guardada como:", nombre_archivo)