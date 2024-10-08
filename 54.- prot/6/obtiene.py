import requests
from urllib.parse import urlparse
from datetime import datetime

url = "https://file.io/qtAeAvtwxey0"  # reemplaza "your_file_id" con el ID de tu archivo en file.io
response = requests.get(url, stream=True)

if response.status_code == 200:
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    file_name = f"{fecha_actual}.py"
    with open(file_name, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print("Archivo descargado con éxito!")
else:
    print("Error al descargar el archivo:", response.status_code)