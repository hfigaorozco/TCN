
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
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

#importando conexion
from dao.conn import Connection

#importando ui y vistas
from vista.iniciosesionDialog import InicioSesionWidget
from vista.main_ui_empresa import MainUIEmpresa


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
    dialog_iniciosesion = InicioSesionWidget() #aqui se le pasara el AppManager:opcional
    resultado = dialog_iniciosesion.exec()

    exit_code = app.exit()
    
    #Aqui se evalua si que boton presiono el usuario
    if resultado == QDialog.Accepted:
        # El usuario hizo clic en Aceptar
        print("Diálogo inicial aceptado. Abriendo la aplicación principal...")
        main_window = MainUIEmpresa()
        main_window.show()
        # sys.exit(app.exec())
        exit_code = app.exec()

    #cerrando conexion a la BD
    Connection.closeConnection()

    #Cerrando sistema
    print('Cerrando el sistema.')
    sys.exit(exit_code)


if __name__ == '__main__':
    main()