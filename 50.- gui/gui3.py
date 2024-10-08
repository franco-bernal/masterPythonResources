import tkinter as tk

def mostrar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    comuna = entry_comuna.get()
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Comuna: {comuna}")

ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("500x300")

label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.grid(row=0, column=1)

label_edad = tk.Label(ventana, text="Edad:")
label_edad.grid(row=1, column=0)
entry_edad = tk.Entry(ventana, width=30)
entry_edad.grid(row=1, column=1)

label_comuna = tk.Label(ventana, text="Comuna:")
label_comuna.grid(row=2, column=0)
entry_comuna = tk.Entry(ventana, width=30)
entry_comuna.grid(row=2, column=1)

boton_enviar = tk.Button(ventana, text="Enviar", command=mostrar_datos)
boton_enviar.grid(row=3, column=0, columnspan=2)

ventana.mainloop()