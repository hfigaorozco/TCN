import os
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QLabel, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Signal
from dao.corrida_dao import CorridaDAO # Import the DAO

class ControladorActualizarCorrEstadoDialog:
    estado_actualizado = Signal() # Signal to emit when status is updated

    def __init__(self, corrida_dao: CorridaDAO, vista_anterior=None):
        self.dialog = None
        self.vista_anterior = vista_anterior
        self.corrida_data = None
        self.corrida_dao = corrida_dao # Store the DAO instance

        # UI elements
        self.lineEdit_numeroCorrida = None
        self.label_estadoActual = None # To display the current status
        self.comboBox_estadoCorrida = None
        self.boton_actualizar = None
        self.boton_cancelar = None

    def cerrar_dialogo(self):
        if self.dialog:
            self.dialog.close()

    def mostrar_dialogo(self, corrida_data=None):
        self.corrida_data = corrida_data
