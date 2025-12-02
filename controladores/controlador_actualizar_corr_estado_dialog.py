import os
from PySide6.QtWidgets import QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

class ControladorActualizarCorrEstadoDialog:
    def __init__(self, vista_anterior=None):
        self.dialog = None
        self.vista_anterior = vista_anterior
        self.corrida_data = None

    def mostrar_dialogo(self, corrida_data=None):
        self.corrida_data = corrida_data
        # Crear una instancia del loader
        loader = QUiLoader()
        
        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "vista", "empresa", "actualizarCorridaDialog.ui")
        ui_file = QFile(path)

        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error: No se puede abrir el archivo UI en: {path}")
            return

        # Cargar el UI en un QDialog
        self.dialog = loader.load(ui_file)
        ui_file.close()

        self.dialog.setWindowTitle(self.dialog.windowTitle())
        self.dialog.setModal(True) # Make it modal
        
        # Connect signals and slots here if any functionality needs to be added later

        self.dialog.exec()

    def cerrar_dialogo(self):
        if self.dialog:
            self.dialog.close()

