#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel, QMessageBox)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent
from utilidades.validaciones import Validaciones


class PantallaReservaciones(QWidget):

    def __init__(self, controlador, parent=None):
        super().__init__(parent)
        self.controlador = controlador

        # Crear una instancia del loader
        loader = QUiLoader()

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__),"pantalla_reservaciones.ui")
        ui_file = QFile(path)

        # 3. Abrir el archivo.
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error: No se puede abrir el archivo UI en: {path}")
            # Si no se carga el UI, no tiene sentido continuar
            return

        # 4. Cargar el UI. El loader devuelve un NUEVO WIDGET.
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        
        # 5. Crear un layout para nuestro QDialog.
        #    El QWidget está vacío por defecto, necesitamos un layout para organizar su contenido.
        layout = QVBoxLayout()

        # 6. Añadir el widget que cargamos (self.ui) al layout.
        layout.addWidget(self.ui)

        # 7. Establecer el layout en nuestro QDialog. Ahora el contenido del .ui es visible.
        self.setLayout(layout)

        # Opcional: Ajustar el tamaño del diálogo al contenido del UI
        self.resize(self.ui.size())
        self.setContentsMargins(0,0,0,0)

        #Obteniendo componentes del .ui
        self.boton_crear_reservacion = self.ui.findChild(QPushButton,'boton_crear_reservacion')
        self.boton_editar_reservacion = self.ui.findChild(QPushButton,'boton_editar_reservacion')

        self.line_edit_buscar_reservacion = self.ui.findChild(QLineEdit,'lineEdit_buscar')
        self.combo_box_filtro = self.ui.findChild(QLabel,'comboBox_filtros')
        
        # Si el boton crear reservacion fue recuperado as True, entonces ejecuata el metodo determinado.
        if self.boton_crear_reservacion:
            self.boton_crear_reservacion.clicked.connect(self.crearReservacion)

        # Si el boton editar fue recuperado as True, entonces ejecuata el metodo determinado.
        if self.boton_editar_reservacion:
            self.boton_crear_reservacion.clicked.connect(self.editarReservacion)
 

    def crearReservacion(self):
        pass

    def editarReservacion(self):
        pass
