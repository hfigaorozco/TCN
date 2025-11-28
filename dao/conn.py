import mysql.connector 
from mysql.connector import Error


#Esta es una clase tipo Singleton (una instancia para todo el sistema).
class Connection:

    #parametros de la conexion
    host = 'localhost'
    port = 3306
    user = 'root'
    password = ''
    database = 'tcn'

    _conexion = None

    #este metodo regresa una sola conexion que se utilizara en todo el sistema.

    @classmethod
    def getConnection(cls):
        if cls._conexion == None or not cls._conexion.is_connected():
            try:
                cls._conexion = mysql.connector.connect(
                host = cls.host,
                port = cls.port, 
                user = cls.user, 
                password = cls.password, 
                database = cls.database,
                use_pure = True)
            except Error as e:
                cls._conexion = None
                print(f'Error: Fallo conectar con la DB.{e}')
                raise Error(f'Error de MySQL al intectar conectar con la BD. {e}')
        #si no hay falla se regresa la conexion
        return cls._conexion
    

    """Este metodo cierra la unica conexion que hay en el sistema."""
    @classmethod
    def closeConnection(cls):
        if cls._conexion and cls._conexion.is_connected():
            print('Cerrando la conexion con la BD.')
            cls._conexion.close()
        cls._conexion = None