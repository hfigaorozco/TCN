from PySide6.QtWidgets import QDialog
from vista.empresa.actualizarCorrEstadoDialog_ui import Ui_Dialog

class ControladorActualizarCorrEstadoDialog(QDialog):
    def __init__(self, parent=None, corrida_data=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.corrida_data = corrida_data # Store corrida data
        self.ui.pushButton_cerrar.clicked.connect(self.accept) # Connect close button