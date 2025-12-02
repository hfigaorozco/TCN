import mysql.connector
from mysql.connector import Error
from dao.conn import Connection
from objetos.autobus import Autobus

class AutobusDAO:
    def __init__(self):
        pass

    def listar_autobuses(self):
        autobuses = []
        conexion = None
        cursor = None
        try:
            conexion = Connection.getConnection()
            cursor = conexion.cursor()
            query = """
                SELECT
                    a.numero,
                    a.matricula,
                    a.cantAsientos,
                    a.tipoAutobus,
                    a.estado,
                    a.marca AS marca_clave,
                    a.modelo AS modelo_clave,
                    m.nombre AS marca_nombre,
                    mo.nombre AS modelo_nombre
                FROM
                    autobus a
                JOIN
                    marca m ON a.marca = m.clave
                JOIN
                    modelo mo ON a.modelo = mo.clave
            """
            cursor.execute(query)
            resultados = cursor.fetchall()

            for fila in resultados:
                autobus = Autobus(
                    fila[0], fila[1], fila[2], fila[3], fila[4], # numero, matricula, cantAsientos, tipoAutobus, estado
                    fila[5], fila[6], # marca_clave, modelo_clave
                    fila[7], fila[8]  # marca_nombre, modelo_nombre
                )
                autobuses.append(autobus)
                print(f"DEBUG DAO: Autobús cargado: {autobus}") # Re-added Debug print

        except Error as e:
            print(f"Error al listar autobuses: {e}")
        finally:
            if cursor:
                cursor.close()
            # Not closing the connection here because it's a Singleton
            # and should be managed by the main application flow.
            # Connection.closeConnection()
        return autobuses