from objetos.Operador import Operador
from dao.conn import Connection
from mysql.connector import Error

class OperadorDAO:
    def obtener_todos(self):
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = "SELECT numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato FROM operador"
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()

            operadores = []
            for fila in resultado:
                operador = Operador(numero=fila[0], nombre=fila[1], apellPat=fila[2], apellMat=fila[3], fechaNac=fila[4], telefono=fila[5], fechaContrato=fila[6])
                operadores.append(operador)

            cursor.close()
            return operadores
        
        except Error as e:
            print(f'Error en OperadorDAO (obtener_todos): {e}')
            raise e

    def insertar(self, operador: Operador):
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = "INSERT INTO operador (nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = conn.cursor()
            cursor.execute(query, (operador.get_nombre(), operador.get_apellPat(), operador.get_apellMat(), operador.get_fechaNac(), operador.get_telefono(), operador.get_fechaContrato()))
            conn.commit()
            cursor.close()
            return True
        
        except Error as e:
            print(f'Error en OperadorDAO (insertar): {e}')
            raise e

    def actualizar(self, operador: Operador):
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = "UPDATE operador SET nombre = %s, apellPat = %s, apellMat = %s, fechaNac = %s, telefono = %s WHERE numero = %s"
            cursor = conn.cursor()
            cursor.execute(query, (operador.get_nombre(), operador.get_apellPat(), operador.get_apellMat(), operador.get_fechaNac(), operador.get_telefono(), operador.get_numero()))
            conn.commit()
            cursor.close()
            return True
        
        except Error as e:
            print(f'Error en OperadorDAO (actualizar): {e}')
            raise e

    def buscar(self, criterio):
        try:
            conn = Connection.getConnection()
            if not conn or not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = """
            SELECT numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato 
            FROM operador 
            WHERE nombre LIKE %s 
            OR apellPat LIKE %s 
            OR apellMat LIKE %s 
            OR numero LIKE %s
            """
            
            cursor = conn.cursor()
            criterio_like = f'%{criterio}%'
            cursor.execute(query, (criterio_like, criterio_like, criterio_like, criterio_like))
            resultado = cursor.fetchall()

            operadores = []
            for fila in resultado:
                operador = Operador(numero=fila[0], nombre=fila[1], apellPat=fila[2], apellMat=fila[3], fechaNac=fila[4], telefono=fila[5], fechaContrato=fila[6])
                operadores.append(operador)

            cursor.close()
            return operadores
        
        except Error as e:
            print(f'Error en OperadorDAO (buscar): {e}')
            raise e
