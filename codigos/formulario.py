import tkinter as tk
import base_datos

def abrir_formulario():
    ventana_form = tk.Toplevel()
    ventana_form.title("Registro de Clientes")
    ventana_form.geometry("400x300")

    tk.Label(ventana_form,text="Nombre").grid(row=0,column=0,padx=10, pady=5)
    nombre = tk.Entry(ventana_form)
    nombre.grid(row=0,column=1)

    tk.Label(ventana_form,text="Cedula").grid(row=1,column=0,padx=10, pady=5)
    cedula = tk.Entry(ventana_form)
    cedula.grid(row=1,column=1)

    
    tk.Label(ventana_form,text="Telefono").grid(row=2,column=0,padx=10, pady=5)
    telefono = tk.Entry(ventana_form)
    telefono.grid(row=2,column=1)

    tk.Label(ventana_form,text="Direccion").grid(row=3,column=0,padx=10, pady=5)
    direccion = tk.Entry(ventana_form)
    direccion.grid(row=3,column=1)

    tk.Label(ventana_form,text="Email").grid(row=4,column=0,padx=10, pady=5)
    email = tk.Entry(ventana_form)
    email.grid(row=4,column=1)

    def guardar():
        base_datos.guardar_cliente(
            nombre.get(),
            cedula.get(),
            telefono.get(),
            direccion.get(),
            email.get()
        )

        nombre.delete(0, tk.END)
        cedula.delete(0, tk.END)
        telefono.delete(0, tk.END)
        direccion.delete(0, tk.END)
        email.delete(0, tk.END)


    tk.Button(ventana_form,text="Guardar" ,command=guardar).grid(row=5,column=1,pady=10)