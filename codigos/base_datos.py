import sqlite3
import os
#++++++++++++++++++++++++++++++++++++++++++++++++++
# RUTA DE BASE DE DATOS 
#++++++++++++++++++++++++++++++++++++++++++++++++++
def ruta_db():
    carpeta = os.path.join(os.environ["USERPROFILE"], "SistemaClientes")

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    return os.path.join(carpeta, "clientes.db")

#+++++++++++++++++++++++++++++++++++++++++++++++++
# INICIALIZAR BASE DE DATOS 
#+++++++++++++++++++++++++++++++++++++++++++++++++

def Inicializar_db():
    conexion = sqlite3.connect(ruta_db())
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nombre TEXT,
           cedula INTEGER,
           telefono INTEGER,
           direccion TEXT,
           email TEXT
    )
    ''')
    
    conexion.commit()
    conexion.close()

    #+++++++++++++++++++++++++++++++++++++++++
    # GUARDAR CLIENTE
    #+++++++++++++++++++++++++++++++++++++++++
    

def guardar_cliente(nombre, cedula, telefono, direccion, email):
    try:
        conexion = sqlite3.connect(ruta_db())
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO clientes(nombre, cedula, telefono, direccion, email)
            VALUES(?, ?, ?, ?, ?)
            """,
            (nombre, cedula, telefono, direccion, email)
        )
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Cédula duplicada
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False

#+++++++++++++++++++++++++++++++++++++++++
# OBTENER TODOS LOS CLIENTES
#+++++++++++++++++++++++++++++++++++++++++

def obtener_clientes():
    """
    Retorna todos los clientes de la base de datos
    """
    try:
        conexion = sqlite3.connect(ruta_db())
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes ORDER BY id")
        clientes = cursor.fetchall()
        conexion.close()
        return clientes
    except Exception as e:
        print(f"Error al obtener clientes: {e}")
        return []

#+++++++++++++++++++++++++++++++++++++++++
# BUSCAR CLIENTE POR CÉDULA
#+++++++++++++++++++++++++++++++++++++++++

def buscar_cliente_por_cedula(cedula):
    """
    Busca un cliente por su cédula
    """
    try:
        conexion = sqlite3.connect(ruta_db())
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes WHERE cedula = ?", (cedula,))
        cliente = cursor.fetchone()
        conexion.close()
        return cliente
    except Exception as e:
        print(f"Error al buscar cliente: {e}")
        return None

#+++++++++++++++++++++++++++++++++++++++++
# ELIMINAR CLIENTE
#+++++++++++++++++++++++++++++++++++++++++

def eliminar_cliente(id_cliente):
    """
    Elimina un cliente por su ID
    """
    try:
        conexion = sqlite3.connect(ruta_db())
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar cliente: {e}")
        return False

#+++++++++++++++++++++++++++++++++++++++++
# ACTUALIZAR CLIENTE
#+++++++++++++++++++++++++++++++++++++++++

def guardar_cliente(nombre, cedula, telefono, direccion, email):

        conexion = sqlite3.connect(ruta_db())
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO clientes(nombre, cedula, telefono, direccion, email)
            VALUES(?, ?, ?, ?, ?)
            """,
            (nombre, cedula, telefono, direccion, email)
        )
        conexion.commit()
        conexion.close()