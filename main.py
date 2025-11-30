
"""Este metodo es el metodo principal de todo el sistema.
    1. Inicia la conexion con la DB que todos usaran
    2. Hace las instancias e inyecta estas dependencias/instancias
    3. Inicia el UI
    4. Cierra el UI
    5. Cieera la conexion con la DB que todos usaron.
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
from vista.iniciosesionDialog import InicioSesionDialog
from vista.registroDialog import RegistroDialog
from vista.main_ui_empresa import MainUIEmpresa
from vista.main_ui_usuario import MainUIUsuario

#importando app manager
from utilidades.app_manager import AppManager

#importando dao's
from dao.usuario_dao import UsuarioDAO

#importando controladores
from controladores.controlador_inicio_sesion_dialog import ControladorInicioSesionDialog
from controladores.controlador_registro_dialog import ControladorRegistroDialog


def main():
    print('Iniciando Transportes Cuervo Negro')
    app = QApplication(sys.argv) # inicia la app
    #Iniciando conexion que usara todo el sistema.
    try:
        Connection.getConnection()
        print('Conexion con la BD hecha.')

    except Error as e:
        error = f"ERROR IMPORTANTE: No se pudo iniciar el programita. {e}"
        QMessageBox.information(None,"Mensaje", error)
        
        Connection.closeConnection() #cerrando por si acaso algo quedo abierto en la conexion
        return #terminando la ejecucion del programa

    #Iniciando dao's
    usuario_dao = UsuarioDAO()
    #Iniciando controladores
    controlador_isd = ControladorInicioSesionDialog(usuario_dao=usuario_dao)
    controlador_rd = ControladorRegistroDialog(usuario_dao=usuario_dao)

    #iniciando app manager
    app_manager = AppManager(controlador_isd=controlador_isd, controlador_rd=controlador_rd)

    #iniciando UI
    print('Iniciando UI')
    
    contador = 0
    while True: # Bucle principal de navegación 
        contador+=1
        #Si es la primera vez abre el dialog, si no, no lo hace, para no duplicar dialogs
        if contador == 1:        
            dialog_iniciosesion = InicioSesionDialog(app_manager)
            resultado = dialog_iniciosesion.exec()

        if resultado == InicioSesionDialog.ENTRAR_VISTA_EMPRESA:
            # Si el login es exitoso, salimos del bucle para abrir la app principal
            print("Abriendo la vista empresa...")
            main_window = MainUIEmpresa()
            main_window.show()
            exit_code = app.exec() #Inica el bucle de la app   
            break 
        
        elif resultado == InicioSesionDialog.ENTRAR_VISTA_CLIENTE:
            # Si el login es exitoso, salimos del bucle para abrir la app principal
            print("Abriendo la vista cliente...")
            main_window = MainUIUsuario()
            main_window.show()
            exit_code = app.exec() #Inica el bucle de la app
            break

        elif resultado == RegistroDialog.ABRIR_INICIO_SESION_DIALOG:
            resultado = dialog_iniciosesion.exec()

        elif resultado == QDialog.Rejected:
            # Si el usuario cerro el dialogo (con la 'X' o 'Cancelar')
            # el bucle termina y la app se cierra limpiamente.
            print("Login cancelado o cerrado. Saliendo de la aplicación.")
            Connection.closeConnection() # Cerramos la conexión aquí
            sys.exit(0) # Salimos directamente    

    #cerrando conexion a la BD
    Connection.closeConnection()

    #Cerrando sistema
    print('Cerrando el sistema...')
    sys.exit(exit_code)


if __name__ == '__main__':
    main()