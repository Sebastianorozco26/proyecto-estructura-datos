import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
#+++++++++++++++++++++++++++++++++++++++++++++++
#FUNCIÓN PARA EL BOTÓN CONSULTAR
#+++++++++++++++++++++++++++++++++++++++++++++++
def accion_Boton3(ventana_principal):  # ← RECIBE LA VENTANA PRINCIPAL COMO PARÁMETRO
    print("CONSULTAR CLIENTE")
    
    # Crear ventana de consulta
    ventana_consulta = tk.Toplevel(ventana_principal)  # ← USA ventana_principal
    ventana_consulta.title("Consultar Cliente")
    ventana_consulta.geometry("400x220")
    ventana_consulta.config(bg="lightblue")
    ventana_consulta.resizable(False, False)
    
    # Centrar la ventana
    ventana_consulta.transient(ventana_principal)  # ← USA ventana_principal
    ventana_consulta.grab_set()
    
    # Título
    tk.Label(ventana_consulta, 
             text="CONSULTAR CLIENTE", 
             font=("Arial", 16, "bold"), 
             bg="lightblue", 
             fg="blue").pack(pady=20)
    
    # Frame para entrada
    frame_entrada = tk.Frame(ventana_consulta, bg="lightblue")
    frame_entrada.pack(pady=10)
    
    tk.Label(frame_entrada, 
             text="Número de Cédula:", 
             font=("Arial", 12, "bold"), 
             bg="lightblue", 
             fg="blue").pack(side='left', padx=5)
    
    entry_cedula = tk.Entry(frame_entrada, 
                            font=("Arial", 12), 
                            width=20, 
                            justify="center")
    entry_cedula.pack(side='left', padx=5)
    entry_cedula.focus()
    
    # Función para buscar en la base de datos
    def buscar_cliente():
        cedula = entry_cedula.get().strip()
        
        if not cedula:
            messagebox.showwarning("Aviso", "Por favor ingrese un número de cédula")
            return
        
        try:
            # Ruta de la base de datos
            carpeta = os.path.join(os.environ["USERPROFILE"], "SistemaClientes")
            ruta_bd = os.path.join(carpeta, "clientes.db")
            
            # Conectar a la base de datos
            conn = sqlite3.connect(ruta_bd)
            cursor = conn.cursor()
            
            # Consultar por cédula
            cursor.execute("SELECT * FROM clientes WHERE cedula = ?", (cedula,))
            resultado = cursor.fetchone()
            
            conn.close()
            
            if resultado:
                ventana_consulta.destroy()
                mostrar_datos_cliente(resultado, ventana_principal)  # ← PASAR ventana_principal
            else:
                messagebox.showinfo("No encontrado", 
                                  f"No existe cliente con cédula: {cedula}")
        
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error: {e}")
    
    # Frame para botones
    frame_botones = tk.Frame(ventana_consulta, bg="lightblue")
    frame_botones.pack(pady=20)
    
    # Botón BUSCAR
    tk.Button(frame_botones, 
              text="BUSCAR", 
              command=buscar_cliente,
              font=("Arial", 11, "bold"), 
              bg="blue", 
              fg="white", 
              width=10,
              height=1).pack(side='left', padx=10)
    
    # Botón CANCELAR
    tk.Button(frame_botones, 
              text="CANCELAR", 
              command=ventana_consulta.destroy,
              font=("Arial", 11, "bold"), 
              bg="red", 
              fg="white", 
              width=10,
              height=1).pack(side='left', padx=10)
    
    # Permitir buscar con tecla Enter
    entry_cedula.bind('<Return>', lambda event: buscar_cliente())


#+++++++++++++++++++++++++++++++++++++++++++++++
#FUNCIÓN PARA MOSTRAR DATOS DEL CLIENTE
#+++++++++++++++++++++++++++++++++++++++++++++++
def mostrar_datos_cliente(datos, ventana_principal):  # ← RECIBE ventana_principal
    """Muestra los datos del cliente encontrado"""
    ventana_datos = tk.Toplevel(ventana_principal)  # ← USA ventana_principal
    ventana_datos.title("Datos del Cliente")
    ventana_datos.geometry("450x400")
    ventana_datos.config(bg="lightblue")
    ventana_datos.resizable(False, False)
    
    # Centrar ventana
    ventana_datos.transient(ventana_principal)  # ← USA ventana_principal
    ventana_datos.grab_set()
    
    # Título
    tk.Label(ventana_datos, 
             text="✅ CLIENTE ENCONTRADO", 
             font=("Arial", 16, "bold"), 
             bg="lightblue", 
             fg="blue").pack(pady=20)
    
    # Frame para datos
    frame_datos = tk.Frame(ventana_datos, bg="lightblue", padx=20)
    frame_datos.pack(fill='both', expand=True, pady=10)
    
    # Campos según tu tabla: id, nombre, cedula, telefono, direccion, email
    campos = ["ID", "Nombre", "Cédula", "Teléfono", "Dirección", "Email"]
    
    for i, campo in enumerate(campos):
        frame_fila = tk.Frame(frame_datos, bg="lightblue")
        frame_fila.pack(fill='x', pady=5)
        
        tk.Label(frame_fila, 
                 text=f"{campo}:", 
                 font=("Arial", 11, "bold"), 
                 bg="lightblue", 
                 fg="blue",
                 width=12,
                 anchor='e').pack(side='left', padx=5)
        
        valor = str(datos[i]) if i < len(datos) else "No disponible"
        tk.Label(frame_fila, 
                 text=valor, 
                 font=("Arial", 11), 
                 bg="lightblue", 
                 fg="black",
                 anchor='w').pack(side='left', padx=5)
    
    # Botón Cerrar
    tk.Button(ventana_datos, 
              text="CERRAR", 
              command=ventana_datos.destroy,
              font=("Arial", 12, "bold"), 
              bg="blue", 
              fg="white", 
              width=15,
              height=2).pack(pady=20)