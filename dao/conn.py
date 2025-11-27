import mysql.connector 
from mysql.connector import Error

class MyConnection:
    
    def __init__ (self):
        
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "tcn",
                port = 3306,
                use_pure = True
            )
        except Error as e:
            print("Error de conexion")
            print(e) 