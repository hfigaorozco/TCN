import os
from PySide6.QtWidgets import QDialog, QVBoxLayout
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

        # Create a QDialog instance to be the actual dialog window
        self.dialog = QDialog()
        
        # Load the UI file contents into a QWidget, using the QDialog as its parent
        # The loader.load(ui_file, parent_widget) makes the widgets in the UI file children of parent_widget
        ui_form = loader.load(ui_file, self.dialog)
        ui_file.close()

        # Set the window title of the QDialog
        self.dialog.setWindowTitle(ui_form.windowTitle()) # Get title from the loaded UI form

        # Create a layout for the QDialog and add the loaded UI form to it
        layout = QVBoxLayout(self.dialog)
        layout.addWidget(ui_form)
        
        # Make the dialog modal
        self.dialog.setModal(True) # Make it modal
        
        # Connect signals and slots here if any functionality needs to be added later
        # Example: self.boton_actualizarCorrida = self.dialog.findChild(QPushButton, "boton_actualizarCorrida")

        self.dialog.exec()

    def cerrar_dialogo(self):
        if self.dialog:
            self.dialog.close()

