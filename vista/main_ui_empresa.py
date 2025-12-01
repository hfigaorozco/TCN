import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent

#importaciones de las pantallas de vista empresa y vista usuario
from vista.empresa.pantalla_reservaciones import PantallaReservaciones
from vista.empresa.pantalla_corridas import PantallaCorridas
from vista.empresa.pantalla_autobuses import PantallaAutobuses
from vista.empresa.pantalla_rutas import PantallaRutas
from vista.empresa.pantalla_operadores import PantallaOperadores
from vista.empresa.pantalla_pasajeros import PantallaPasajeros
from vista.empresa.pantalla_index import PantallaIndex

class MainUIEmpresa(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        
        # Configurar stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        #Varibales para que el recolector de basura no haga su chamba
        self.index_ui = None
        self.pagina_autobuses_widget = None
        self.pagina_corridas_widget = None
        self.pagina_operadores_widget = None
        self.pagina_pasajeros_widget = None
        self.pagina_reservaciones_widget = None
        self.pagina_rutas_widget = None
        
        # Cargar todas las interfaces
        self.cargar_interfaces()
        self.setup_connections()

        # Mostrar MainWindow por defecto (índice 0)
        self.stacked_widget.setCurrentIndex(0)
        self.setWindowTitle('Transportes Cuervo Negro - Administrador')
        self.showMaximized()

        
    def cargar_interfaces(self):
        # Cargar todas las interfaces
        base_path = os.path.dirname(__file__) # Ruta del directorio de main_ui.py
        # Cargar el resto de interfaces con rutas absolutas
        self.index_ui = PantallaIndex(self.app_manager.controlador_index)
        self.pagina_reservaciones_widget = PantallaReservaciones(self.app_manager.controlador_pr)
        self.pagina_corridas_widget = PantallaCorridas(self.app_manager.controlador_pc)
        self.pagina_autobuses_widget = PantallaAutobuses(self.app_manager.controlador_pa)
        self.pagina_rutas_widget = PantallaRutas(self.app_manager.controlador_prutas)
        self.pagina_operadores_widget = PantallaOperadores(self.app_manager.controlador_po)
        self.pagina_pasajeros_widget = PantallaPasajeros(self.app_manager.controlador_pp)
                                                    
        # Agregar al stacked widget en orden (el índice 0 ya está ocupado por main_index_widget)
        if self.index_ui: self.stacked_widget.addWidget(self.index_ui) #Index 0
        if self.pagina_reservaciones_widget: self.stacked_widget.addWidget(self.pagina_reservaciones_widget) # Index 1
        if self.pagina_corridas_widget: self.stacked_widget.addWidget(self.pagina_corridas_widget)  # Index
        if self.pagina_autobuses_widget: self.stacked_widget.addWidget(self.pagina_autobuses_widget) # Index
        if self.pagina_rutas_widget: self.stacked_widget.addWidget(self.pagina_rutas_widget) # Index
        if self.pagina_operadores_widget: self.stacked_widget.addWidget(self.pagina_operadores_widget) # Index 5
        if self.pagina_pasajeros_widget: self.stacked_widget.addWidget(self.pagina_pasajeros_widget) # Index 6

    
    def load_ui(self, ui_path):
        file = QFile(ui_path)
        if not file.open(QFile.ReadOnly):
            print(f"ERROR: No se pudo abrir el archivo UI: {ui_path}")
            return None # Retorna None explícitamente en caso de error
        
        loader = QUiLoader()
        ui = loader.load(file)
        file.close()
        return ui

    
    def setup_connections(self):
        '''Agregando evento a los botones de navegacion del index.ui'''
        # Si el boton de inicio es presionado
        if self.index_ui:
            boton_inicio = self.index_ui.findChild(QWidget, "boton_inicio")
            if boton_inicio:
                boton_inicio.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Si el boton reservaciones es presionado
        if self.pagina_reservaciones_widget:
            boton_reservaciones = self.index_ui.findChild(QWidget, "boton_reservaciones")
            if boton_reservaciones:
                boton_reservaciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Si el boton corridas es presionado
        if self.pagina_corridas_widget:
            boton_corridas = self.index_ui.findChild(QWidget, "boton_corridas")
            if boton_corridas:
                boton_corridas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Si el boton autobuses es presionado
        if self.pagina_autobuses_widget:
            boton_autobuses = self.index_ui.findChild(QWidget, "boton_autobuses")
            if boton_autobuses:
                boton_autobuses.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Si el boton rutas es presionado
        if self.pagina_rutas_widget:
            boton_rutas = self.index_ui.findChild(QWidget, "boton_rutas")
            if boton_rutas:
                boton_rutas.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Si el boton operadores es presionado
        if self.pagina_operadores_widget:
            boton_operadores = self.index_ui.findChild(QWidget, "boton_operadores")
            if boton_operadores:
                boton_operadores.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))


    def closeEvent(self, event: QCloseEvent):
        """
        Este metodo que se llama cuando se preciona la X en esta ventana.
        """
        print("Terminando programa.")

        event.accept() 
        
        #Nota: Luego de esto event.accept(), el flujo del programa regresa al main.py