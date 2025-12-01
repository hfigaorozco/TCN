import os
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from controladores.controlador_ciudad import ControladorCiudad

class CiudadWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlador = ControladorCiudad()
        self.ui = self.load_ui()
        self.setup_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "ciudadWidget.ui")
        ui_file = QFile(path)
        if not ui_file.open(QIODevice.ReadOnly):
            raise IOError(f"No se puede abrir el archivo UI: {path}")
        widget = loader.load(ui_file, self)
        ui_file.close()
        return widget

    def setup_ui(self):
        self.setWindowTitle("Administrar Ciudades")
        
        # Configurar la tabla
        self.ui.tableWidget_ciudad.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_ciudad.setSelectionBehavior(QWidget.SelectRows)
        self.ui.tableWidget_ciudad.setEditTriggers(QWidget.NoEditTriggers)

        # Conectar señales a slots
        self.ui.boton_agregar.clicked.connect(self.agregar_ciudad)
        self.ui.boton_editar.clicked.connect(self.editar_ciudad)
        self.ui.boton_cancelar.clicked.connect(self.limpiar_campos)
        
        self.ui.tableWidget_ciudad.itemSelectionChanged.connect(self.seleccionar_ciudad)
        self.ui.lineEdit_ciudad.textChanged.connect(self.buscar_ciudad)

        self.cargar_ciudades()
        self.limpiar_campos()

    def cargar_ciudades(self):
        ciudades = self.controlador.obtener_todas_las_ciudades()
        self.ui.tableWidget_ciudad.setRowCount(0)
        if ciudades:
            for i, ciudad in enumerate(ciudades):
                self.ui.tableWidget_ciudad.insertRow(i)
                self.ui.tableWidget_ciudad.setItem(i, 0, QTableWidgetItem(ciudad.get_codigo()))
                self.ui.tableWidget_ciudad.setItem(i, 1, QTableWidgetItem(ciudad.get_nombre()))

    def agregar_ciudad(self):
        codigo = self.ui.lineEdit_codigo.text()
        nombre = self.ui.lineEdit_ciudad.text()
        
        resultado = self.controlador.agregar_nueva_ciudad(codigo, nombre)
        
        if resultado is True:
            QMessageBox.information(self, "Éxito", "Ciudad agregada correctamente.")
            self.cargar_ciudades()
            self.limpiar_campos()
        elif resultado == "duplicado":
            QMessageBox.warning(self, "Error", "El código o nombre de la ciudad ya existe.")
        elif resultado == "codigo_invalido":
            QMessageBox.warning(self, "Error", "El código debe tener exactamente 3 caracteres.")
        else:
            QMessageBox.critical(self, "Error", resultado)

    def editar_ciudad(self):
        fila_seleccionada = self.ui.tableWidget_ciudad.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona una ciudad para editar.")
            return

        codigo_actual = self.ui.tableWidget_ciudad.item(fila_seleccionada, 0).text()
        nuevo_codigo = self.ui.lineEdit_codigo.text()
        nuevo_nombre = self.ui.lineEdit_ciudad.text()

        resultado = self.controlador.actualizar_ciudad(codigo_actual, nuevo_codigo, nuevo_nombre)

        if resultado is True:
            QMessageBox.information(self, "Éxito", "Ciudad actualizada correctamente.")
            self.cargar_ciudades()
            self.limpiar_campos()
        elif resultado == "duplicado":
            QMessageBox.warning(self, "Error", "El nuevo código de ciudad ya existe.")
        elif resultado == "codigo_invalido":
            QMessageBox.warning(self, "Error", "El código debe tener exactamente 3 caracteres.")
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar la ciudad.")

    def buscar_ciudad(self):
        texto_busqueda = self.ui.lineEdit_ciudad.text()
        # Solo buscar si el modo no es de edición
        if self.ui.boton_editar.isEnabled():
            ciudades_filtradas = self.controlador.buscar_ciudades_por_nombre(texto_busqueda)
            self.mostrar_ciudades_en_tabla(ciudades_filtradas)

    def seleccionar_ciudad(self):
        fila_seleccionada = self.ui.tableWidget_ciudad.currentRow()
        if fila_seleccionada == -1:
            return

        codigo = self.ui.tableWidget_ciudad.item(fila_seleccionada, 0).text()
        nombre = self.ui.tableWidget_ciudad.item(fila_seleccionada, 1).text()

        self.ui.lineEdit_codigo.setText(codigo)
        self.ui.lineEdit_ciudad.setText(nombre)
        
        self.ui.boton_agregar.setEnabled(False)
        self.ui.boton_editar.setEnabled(True)

    def limpiar_campos(self):
        self.ui.lineEdit_codigo.clear()
        self.ui.lineEdit_ciudad.clear()
        self.ui.tableWidget_ciudad.clearSelection()
        
        self.ui.boton_agregar.setEnabled(True)
        self.ui.boton_editar.setEnabled(False)
        
        # Si la búsqueda borró la tabla, la recargamos
        if self.ui.tableWidget_ciudad.rowCount() == 0:
            self.cargar_ciudades()

    def mostrar_ciudades_en_tabla(self, ciudades):
        self.ui.tableWidget_ciudad.setRowCount(0)
        for i, ciudad in enumerate(ciudades):
            self.ui.tableWidget_ciudad.insertRow(i)
            self.ui.tableWidget_ciudad.setItem(i, 0, QTableWidgetItem(ciudad.get_codigo()))
            self.ui.tableWidget_ciudad.setItem(i, 1, QTableWidgetItem(ciudad.get_nombre()))
