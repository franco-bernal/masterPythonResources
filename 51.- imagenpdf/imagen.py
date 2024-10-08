import matplotlib.pyplot as plt

# Crear una figura
fig, ax = plt.subplots()

# Agregar algún contenido a la figura (por ejemplo, un texto)
ax.text(0.5, 0.5, 'Hola, mundo!')

# Guardar la figura como una imagen PNG
plt.savefig('imagen.png')