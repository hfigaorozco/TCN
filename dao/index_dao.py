from .conn import Connection
from mysql.connector import Error

class IndexDAO:
    def __init__(self):
        self.db = Connection.getConnection()

    def cargar_pasajeros_dashboard(self):
        'Carga pasajeros recientemente registrados'
        try:
            comando = """
            SELECT numero, nombre, apellPat, apellMat, 
                   TIMESTAMPDIFF(YEAR, fechaNac, CURDATE()) as edad,
                   telefono
            FROM pasajero 
            ORDER BY numero DESC 
            
            """
            
            cursor = self.db.cursor()
            cursor.execute(comando)
            pasajeros = cursor.fetchall()
            cursor.close()
            return pasajeros
                
        except Error as e:
            print(f"Error en IndexDAO.cargar_pasajeros_dashboard: {e}")
            return []

    def cargar_corridas_dashboard(self):
        'Carga las corridas recientes o del día actual'
        try:
            comando = """
            SELECT numero as numero, fecha, hora_salida as horasalida, 
                   ruta as ruta
            FROM corrida 
            WHERE c.fecha >= CURDATE()
            ORDER BY c.fecha, c.hora_salida
            """
            
            cursor = self.db.cursor()
            cursor.execute(comando)
            corridas = cursor.fetchall()
            cursor.close()
            return corridas
                
        except Error as e:
            print(f"Error en IndexDAO.cargar_corridas_dashboard: {e}")
            return []

    def cargar_operadores_con_corridas_dashboard(self):
        'Carga operadores y sus corridas asignadas para el dashboard'
        try:
            comando = """
            SELECT
                op.numero,
                CONCAT(op.nombre, ' ', op.apellPat, ' ', op.apellMat) AS nombre_completo_operador,
                c.ruta AS ruta_corrida,
                c.fecha AS fecha_corrida
            FROM operador op
            JOIN corrida c ON op.numero = c.operador
            ORDER BY op.numero, c.fecha DESC
            
            """
            
            cursor = self.db.cursor()
            cursor.execute(comando)
            operadores_corridas = cursor.fetchall()
            cursor.close()
            return operadores_corridas
                
        except Error as e:
            print(f"Error en IndexDAO.cargar_operadores_con_corridas_dashboard: {e}")
            return []