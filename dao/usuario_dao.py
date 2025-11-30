from objetos.usuario import Usuario
from dao.conn import Connection
from mysql.connector import Error

class UsuarioDAO:
    conn = None

    def consultarUsuario(self,phone):

        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = f'SELECT * FROM usuario WHERE phone = {phone}'
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()

            #mapeando respuestas a un objeto
    
            usuario = None
            for fila in resultado:
                usuario = (Usuario(id_usuario=fila[0],phone=fila[1],password=fila[2],es_admin=fila[3]))

            cursor.close()
            return usuario
        
        except Error as e:
            print(f'Error en RutaDAO (consultarTodasRutas): {e}')
            raise e


    
    def consultarCiudadesOrigen(self):

        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = 'SELECT DISTINCT c.nombre AS Nombre FROM ruta INNER JOIN ciudad AS c ON ruta.ciudadOrigen = c.codigo ORDER BY c.nombre ASC'
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()
            
            cursor.close()
            return resultado
        
        except Error as e:
            print(f'Error en RutaDAO (consultar ciudades origen): {e}')
            raise e

        
    
    def consultarCiudadesDestino(self):
            
        try:
            conn = Connection.getConnection() #llamnado a la conexion
            #verificando conexion
            if not conn and not conn.is_connected():
                raise Error('No se puede establecer conexion con la BD.')

            query = 'SELECT DISTINCT c.nombre AS Nombre FROM ruta INNER JOIN ciudad AS c ON ruta.ciudadDestino = c.codigo ORDER BY c.nombre ASC'
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()
            
            cursor.close()
            return resultado
        
        except Error as e:
            print(f'Error en RutaDAO (consultarCiudadesDestino): {e}')
            raise e