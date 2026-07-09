#+++++++++++++++++++++++++++++++++++++++++++++++
#Importar la librerias
#+++++++++++++++++++++++++++++++++++++++++++++++
import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Button, Frame
import formulario
import base_datos
import os
import sys
import consultar
import exportar

#+++++++++++++++++++++++++++++++++++++
# FUNCION PARA MANEJO DE RUTAS 
#+++++++++++++++++++++++++++++++++++++

def ruta_recursos(rel_path):
    try:
        base_path = sys._MEIPASS #cuando es ejecutable 
    except AttributeError:
        base_path = os.path.abspath(".") # cuando es .py
    return os.path.join(base_path, rel_path) 
#+++++++++++++++++++++++++++++++++++++++
# INICIARLIZAR BASE DE DATOS ANTES
#+++++++++++++++++++++++++++++++++++++++

base_datos.Inicializar_db()


#+++++++++++++++++++++++++++++++++++++++++++++++
#Crear la ventana 
#+++++++++++++++++++++++++++++++++++++++++++++++
ventana =tk.Tk()

ventana.title("APLICACION PYTHON")#titulo de la ventana
ventana.resizable(True,True)#modificar ventana
ventana.iconbitmap(r"C:\Users\AMD\Documents\curso python\proyecto\icono.ico")#ruta del icono en carpeta
ventana.geometry("650x650")#resolucion de la ventana
ventana.config(bg="red")#color de la pantalla


#+++++++++++++++++++++++++++++++++++++++++++++++
#Definir acciones de los botones
#+++++++++++++++++++++++++++++++++++++++++++++++
#def accion_Boton1(): #Boton 1
    #messagebox.showinfo("Este mensaje es informativo")
    #messagebox.showerror("ocurrio un error en el sistema")
    #messagebox.showinfo("Este es un mensaje de advertencia")
    #print("MENSAJE")

def accion_Boton2(): #Boton 2 - INGRESAR CLIENTES
    formulario.abrir_formulario()#Abre la ventana del formulario
    print("INGRESAR CLIENTE")

def accion_Boton3():
    consultar.accion_Boton3(ventana)
    print("CONSULTAR CLIENTE")

def accion_Boton4(): #Boton 4 - EXPORTAR
    exportar.accion_Boton4()
    print("EXPORTAR A EXCEL")

def accion_Boton5(): #Boton 5 - SALIR
    print("Saliste de la ventana")
    ventana.destroy()

#+++++++++++++++++++++++++++++++++++++++++++++++
#Creacion de los botones
#+++++++++++++++++++++++++++++++++++++++++++++++
#BOTON 1 - MOSTRAR MENSAJE
#Boton1=tk.Button(
    #ventana,
    #text="MENSAJE",         #Nombre Boton
    #width=15, height=2,     #Tamaño  Boton
    #font=("Arial", 16),     #Fuente de texto
    #fg=("Blue"),            #Color del texto
    #bg=("lightblue"),       #Color del boton
    #command = accion_Boton1 #Acción Boton
   # )
#Boton1.pack(side="top", pady=5)
#Boton1.pack(expand=True)
#Boton1.place(relx=0.5, rely=0.3, anchor="center")

#BOTON 2 - ABRIR FORMULARIO
Boton2=tk.Button(
    ventana,
    text="INGRESAR CLIENTE",      #Nombre Boton
    width=17, height=2,     #Tamaño  Boton
    font=("Arial", 16),     #Fuente de texto
    fg=("Blue"),            #Color del texto
    bg=("lightblue"),       #Color del boton
    command = accion_Boton2 #Acción Boton
    )
Boton2.pack(side="top", pady=5)
Boton2.pack(expand=True)
Boton2.place(relx=0.5, rely=0.4, anchor="center")

#BOTON 3 - CONSULTAR CLIENTE
Boton3 = tk.Button(
    ventana,
    text="CONSULTAR",
    width=17,
    height=2,
    font=("Arial", 16),
    fg="Blue",
    bg="lightblue",
    command=accion_Boton3
)
Boton3.pack(side="top", pady=5)
Boton3.pack(expand=True)
Boton3.place(relx=0.5, rely=0.5, anchor="center")

#BOTON 4 - EXPORTAR A EXCEL - NUEVO
Boton4 = tk.Button(
    ventana,
    text="EXPORTAR",
    width=17,
    height=2,
    font=("Arial", 16),
    fg="Blue",
    bg="lightblue",
    command=accion_Boton4
)
Boton4.pack(side="top", pady=5)
Boton4.pack(expand=True)
Boton4.place(relx=0.5, rely=0.6, anchor="center")

#BOTON 5 - SALIR DE LA VENTANA
Boton5=tk.Button(
    ventana,
    text="SALIR",          #Nombre Boton
    width=17, height=2,     #Tamaño  Boton
    font=("Arial", 16),     #Fuente de texto
    fg=("Blue"),            #Color del texto
    bg=("lightblue"),       #Color del boton
    command = accion_Boton5 #Acción Boton
    )
Boton5.pack(side="top", pady=5)
Boton5.pack(expand=True)
Boton5.place(relx=0.5, rely=0.7, anchor="center")

#+++++++++++++++++++++++++++++++++++++++++++++++
#Crear base de datos automatica cuando inicia la aplicacion
#+++++++++++++++++++++++++++++++++++++++++++++++    

#base_datos.conectar()

#+++++++++++++++++++++++++++++++++++++++++++++++
#Finalizar metodo
#+++++++++++++++++++++++++++++++++++++++++++++++    
ventana.mainloop()