import tkinter as tk
import time

def mostrar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    comuna = entry_comuna.get()
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Comuna: {comuna}")

def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    label_reloj.config(text=hora_actual)
    ventana.after(1000, actualizar_reloj)

ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("500x350")

logo = tk.PhotoImage(file="y.png")
label_logo = tk.Label(ventana, image=logo)
label_logo.image = logo
label_logo.grid(row=0, column=0, columnspan=2)

label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=1, column=0, sticky="w")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1, column=1, sticky="ew")

label_edad = tk.Label(ventana, text="Edad:")
label_edad.grid(row=2, column=0, sticky="w")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=2, column=1, sticky="ew")

label_comuna = tk.Label(ventana, text="Comuna:")
label_comuna.grid(row=3, column=0, sticky="w")
entry_comuna = tk.Entry(ventana)
entry_comuna.grid(row=3, column=1, sticky="ew")

boton_enviar = tk.Button(ventana, text="Enviar", command=mostrar_datos)
boton_enviar.grid(row=4, column=0, columnspan=2)

label_reloj = tk.Label(ventana, text="", font=("Arial", 24))
label_reloj.grid(row=5, column=0, columnspan=2)

actualizar_reloj()

ventana.grid_columnconfigure(1, weight=1)

ventana.mainloop()