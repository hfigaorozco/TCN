
"""Este metodo es el metodo principal de todo el sistema.
    1. Inicia la conexion con la DB que todos usaran
    2. Hace las instancias e inyecta estas dependencias/instancias
    3. Inicia el UI
    4. Cieera el UI
    5. Cieera la conexion con la DB que todos usarion.
    6. Termina la ejecucion del sistema.
"""

#imports de librerias
import sys
import mysql.connector 
from mysql.connector import Error
from PySide6.QtWidgets import QApplication

#importando conexion
from dao.conn import Connection

#importando ui y vistas
from ui.main_ui import MainUI


def main():
    print('Iniciando Transportes Cuervo Negro')
    #Iniciando conexion que usara todo el sistema.
    try:
        Connection.getConnection()
        print('Conexion con la BD hecha.')

    except Error as e:
        print(f"ERROR IMPORTANTE: No se pudo iniciar el programita. {e}")
        Connection.closeConnection() #cerrando por si acaso algo quedo abierto en la conexion
        return #terminando la ejecucion del programa

    #Iniciando dao's
    #Iniciando controladores
    

    #iniciando UI
    print('Iniciando UI')
    app = QApplication(sys.argv)
    ventana = MainUI() #aqui se le pasara el AppManager:opcional
    ventana.show()
    
    exit_code = app.exec()

    #cerrando conexion a la BD
    Connection.closeConnection()

    sys.exit(exit_code)


if __name__ == '__main__':
    main()