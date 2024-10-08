import tkinter as tk

def mostrar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    comuna = entry_comuna.get()
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Comuna: {comuna}")
    ventana.destroy()
    ventana_gracias = tk.Tk()
    ventana_gracias.title("Gracias")
    ventana_gracias.geometry("300x200")
    label_gracias = tk.Label(ventana_gracias, text="Gracias por llenar el formulario")
    label_gracias.place(x=10, y=10)
    def finalizar():
        ventana_gracias.destroy()
    boton_finalizar = tk.Button(ventana_gracias, text="Finalizar", command=finalizar)
    boton_finalizar.place(x=10, y=50)
    ventana_gracias.mainloop()

ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("500x350")

fondo = tk.PhotoImage(file="y.png")
label_fondo = tk.Label(ventana, image=fondo)
label_fondo.image = fondo
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.place(x=10, y=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.place(x=120, y=10, width=360)

label_edad = tk.Label(ventana, text="Edad:")
label_edad.place(x=10, y=50)
entry_edad = tk.Entry(ventana)
entry_edad.place(x=120, y=50, width=360)

label_comuna = tk.Label(ventana, text="Comuna:")
label_comuna.place(x=10, y=90)
entry_comuna = tk.Entry(ventana)
entry_comuna.place(x=120, y=90, width=360)

boton_enviar = tk.Button(ventana, text="Enviar", command=mostrar_datos)
boton_enviar.place(x=120, y=130, width=360)

ventana.mainloop()