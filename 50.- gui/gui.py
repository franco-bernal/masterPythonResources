import tkinter as tk

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana principal")
ventana_principal.geometry("800x600")

# Crear la ventana secundaria
ventana_secundaria = tk.Toplevel(ventana_principal)
ventana_secundaria.title("Ventana secundaria")
ventana_secundaria.geometry("400x300")

# Crear el botón en la ventana secundaria
boton = tk.Button(ventana_secundaria, text="Botón en el centro")
boton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Configurar la ventana secundaria para que se abra en el centro de la ventana principal
ventana_secundaria.geometry("+%d+%d" % (ventana_principal.winfo_rootx() + 200, ventana_principal.winfo_rooty() + 150))

# Iniciar la aplicación
ventana_principal.mainloop()