# **COMO PUBLICAR UN PAQUETE**

## Supongamos que tienes un módulo Python llamado mi_paquete que contiene una función hola_mundo:

# mi_paquete/__init__.py
def hola_mundo():
    print("Hola, mundo!")
Crear un paquete

Para crear un paquete, debes crear un archivo setup.py en el directorio raíz de tu proyecto:


# setup.py
from setuptools import setup

setup(
    name='mi_paquete',
    version='1.0',
    packages=['mi_paquete'],
    install_requires=[],
    author='Tu nombre',
    author_email='tu_email@example.com'
)

#### Crear un archivo de distribución

Abre la terminal y navega hasta el directorio raíz de tu proyecto.
Ejecuta el comando "_**python setup.py sdist**_" en la terminal. 
Esto creará un archivo de distribución en el directorio dist.

### **Publicar el paquete**

Para publicar el paquete, debes ejecutar el comando python setup.py sdist en la terminal. 
Esto creará un archivo mi_paquete-1.0.tar.gz en el directorio dist.

**Subir el paquete a PyPI**
Para subir el paquete a PyPI (Python Package Index), debes crear una cuenta en PyPI 
y luego ejecutar el comando "**_twine upload dist/*_**" en la terminal. Esto subirá el paquete a PyPI.

#### **Instalar el paquete**

Una vez que el paquete esté publicado en PyPI, puedes instalarlo utilizando pip: pip install mi_paquete.

##### **Uso del paquete**

Una vez instalado, puedes utilizar el paquete de la siguiente manera:

from nombre_del_paquete import funcion_del_paquete

funcion_del_paquete()  # Llama a la función del paquete
Reemplaza 'nombre_del_paquete' con el nombre del paquete. 

# ejemplo.py
from mi_paquete import hola_mundo

hola_mundo()  # Imprime "Hola, mundo!"