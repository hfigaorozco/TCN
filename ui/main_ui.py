from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configurar stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Cargar todas las interfaces
        self.cargar_interfaces()
        self.setup_connections()
        
        # Mostrar MainWindow por defecto (índice 0)
        self.stacked_widget.setCurrentIndex(0)
    
    def cargar_interfaces(self):
        # Cargar todas las interfaces
        self.main_widget = self.load_ui('ui/MainWindow.ui')
        self.hola_widget = self.load_ui('ui/hola.ui')
        self.adios_widget = self.load_ui('ui/adios.ui')
        
        # Agregar al stacked widget en orden
        self.stacked_widget.addWidget(self.main_widget)  # Índice 0
        self.stacked_widget.addWidget(self.hola_widget)  # Índice 1
        self.stacked_widget.addWidget(self.adios_widget) # Índice 2
    
    def load_ui(self, ui_path):
        file = QFile(ui_path)
        if file.open(QFile.ReadOnly):
            loader = QUiLoader()
            ui = loader.load(file)
            file.close()
            return ui
        return None
    
    def setup_connections(self):
        # Desde MainWindow (índice 0)
        if self.main_widget:
            boton_hola = self.main_widget.findChild(QWidget, "boton_hola")
            if boton_hola:
                boton_hola.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
            
            boton_adios = self.main_widget.findChild(QWidget, "boton_adios")
            if boton_adios:
                boton_adios.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        
        # Desde Hola (índice 1)
        if self.hola_widget:
            boton_regresar = self.hola_widget.findChild(QWidget, "boton_regresar")
            if boton_regresar:
                boton_regresar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        # Desde Adios (índice 2)
        if self.adios_widget:
            boton_regresar = self.adios_widget.findChild(QWidget, "boton_regresar")
            if boton_regresar:
                boton_regresar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))