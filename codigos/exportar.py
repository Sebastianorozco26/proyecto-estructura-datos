#+++++++++++++++++++++++++++++++++++++++++++++++
#Importar la librerias
#+++++++++++++++++++++++++++++++++++++++++++++++
import sqlite3
import os
import tkinter as tk
from tkinter import messagebox, filedialog
import base_datos
from datetime import datetime

# Intentar importar pandas y openpyxl (para Excel)
try:
    import pandas as pd
    PANDAS_DISPONIBLE = True
except ImportError:
    PANDAS_DISPONIBLE = False

try:
    import openpyxl
    OPENPYXL_DISPONIBLE = True
except ImportError:
    OPENPYXL_DISPONIBLE = False

#+++++++++++++++++++++++++++++++++++++++++++++++
# FUNCIÓN PARA EXPORTAR A EXCEL
#+++++++++++++++++++++++++++++++++++++++++++++++

def exportar_a_excel():
    """
    Exporta la base de datos de clientes a un archivo Excel
    """
    
    # Verificar si pandas está instalado
    if not PANDAS_DISPONIBLE:
        messagebox.showerror(
            "Error",
            "No se encontró la librería 'pandas'.\n\n"
            "Instala con: pip install pandas openpyxl"
        )
        return
    
    if not OPENPYXL_DISPONIBLE:
        messagebox.showerror(
            "Error",
            "No se encontró la librería 'openpyxl'.\n\n"
            "Instala con: pip install openpyxl"
        )
        return
    
    try:
        # Conectar a la base de datos
        conexion = sqlite3.connect(base_datos.ruta_db())
        
        # Consulta SQL para obtener todos los clientes
        query = """
        SELECT 
            id as 'ID',
            nombre as 'NOMBRE',
            cedula as 'CEDULA',
            telefono as 'TELEFONO',
            direccion as 'DIRECCION',
            email as 'EMAIL'
        FROM clientes
        """
        
        # Leer datos con pandas
        df = pd.read_sql_query(query, conexion)
        conexion.close()
        
        # Verificar si hay datos
        if df.empty:
            messagebox.showwarning(
                "Sin datos",
                "No hay clientes para exportar."
            )
            return
        
        # Generar nombre de archivo
        fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"Clientes_{fecha_actual}.xlsx"
        
        # Cuadro de diálogo para guardar archivo
        archivo_guardar = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Archivos Excel", "*.xlsx")],
            initialfile=nombre_archivo,
            title="Guardar Excel"
        )
        
        # Si el usuario cancela
        if not archivo_guardar:
            return
        
        # Exportar a Excel
        df.to_excel(archivo_guardar, sheet_name='Clientes', index=False)
        
        # Mensaje de éxito
        messagebox.showinfo(
            "Exportar",
            f"Datos exportados correctamente.\n"
            f"Registros: {len(df)}"
        )
        
        # Preguntar si desea abrir
        if messagebox.askyesno("Abrir", "¿Abrir archivo Excel?"):
            os.startfile(archivo_guardar)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar: {str(e)}")


#+++++++++++++++++++++++++++++++++++++++++++++++
# ACCIÓN PARA EL BOTÓN DE EXPORTAR
#+++++++++++++++++++++++++++++++++++++++++++++++

def accion_Boton4():
    """
    Función que se llama desde el botón principal
    """
    exportar_a_excel()
    print("EXPORTAR A EXCEL")