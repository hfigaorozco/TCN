import os
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QDialog, QHeaderView, QVBoxLayout, QComboBox, QLineEdit, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from vista.empresa.ciudadWidget import CiudadWidget

class PantallaRutas(QWidget):
    def __init__(self, controlador, parent=None):
        super().__init__(parent)
        
        self.controlador = controlador

        # Cargar el archivo .ui
        self.ui = self.load_ui("pantalla_rutas.ui")

        # Crear un layout y añadir el widget cargado
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)
        self.setLayout(layout)

        # Guardar estado
        self.todas_las_rutas = []
        self.ciudades_map = {}

        # Configurar la tabla
        self.ui.QtableWidget_rutas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Conectar señales a slots
        self.ui.boton_agregaruta.clicked.connect(self.abrir_dialogo_agregar)
        self.ui.boton_editaruta.clicked.connect(self.abrir_dialogo_editar)
        self.ui.boton_ciudades.clicked.connect(self.abrir_widget_ciudades)
        self.ui.comboBox_forigen.currentIndexChanged.connect(self.filtrar_rutas)
        self.ui.comboBox_fdestino.currentIndexChanged.connect(self.filtrar_rutas)
        
        # Cargar datos iniciales
        self.cargar_datos_iniciales()

    def load_ui(self, filename):
        """Carga un archivo .ui dinámicamente y devuelve el widget."""
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), filename)
        ui_file = QFile(path)
        if not ui_file.open(QIODevice.ReadOnly):
            raise IOError(f"No se puede abrir el archivo UI: {path}")
        widget = loader.load(ui_file, self)
        ui_file.close()
        return widget

    def cargar_datos_iniciales(self):
        """Llama al controlador para obtener rutas y ciudades y actualiza la UI."""
        rutas = self.controlador.obtener_todas_las_rutas()
        ciudades_map = self.controlador.obtener_ciudades_map()

        if rutas is False or ciudades_map is False:
            QMessageBox.critical(self, "Error", "No se pudieron cargar los datos iniciales desde la base de datos.")
            return

        self.todas_las_rutas = rutas if rutas is not None else []
        self.ciudades_map = ciudades_map if ciudades_map is not None else {}
        
        self.llenar_filtros_ciudades()
        self.mostrar_rutas_en_tabla(self.todas_las_rutas)

    def mostrar_rutas_en_tabla(self, rutas):
        """Puebla la tabla con la lista de rutas proporcionada."""
        self.ui.QtableWidget_rutas.setRowCount(0)
        for fila_idx, ruta in enumerate(rutas):
            self.ui.QtableWidget_rutas.insertRow(fila_idx)
            self.ui.QtableWidget_rutas.setItem(fila_idx, 0, QTableWidgetItem(str(ruta.get_codigo())))
            self.ui.QtableWidget_rutas.setItem(fila_idx, 1, QTableWidgetItem(ruta.get_ciudadorigen()))
            self.ui.QtableWidget_rutas.setItem(fila_idx, 2, QTableWidgetItem(ruta.get_ciudaddestino()))
            self.ui.QtableWidget_rutas.setItem(fila_idx, 3, QTableWidgetItem(f"{ruta.get_distancia()} km"))

    def llenar_filtros_ciudades(self):
        """Puebla los ComboBox de filtro con ciudades únicas."""
        if not self.todas_las_rutas:
            origenes = []
            destinos = []
        else:
            origenes = sorted(list(set(r.get_ciudadorigen() for r in self.todas_las_rutas)))
            destinos = sorted(list(set(r.get_ciudaddestino() for r in self.todas_las_rutas)))
        
        self.ui.comboBox_forigen.clear()
        self.ui.comboBox_fdestino.clear()
        
        self.ui.comboBox_forigen.addItem("Todos")
        self.ui.comboBox_fdestino.addItem("Todos")
        
        self.ui.comboBox_forigen.addItems(origenes)
        self.ui.comboBox_fdestino.addItems(destinos)

    def filtrar_rutas(self):
        """Filtra las rutas mostradas según la selección de los ComboBox."""
        filtro_origen = self.ui.comboBox_forigen.currentText()
        filtro_destino = self.ui.comboBox_fdestino.currentText()
        
        if not self.todas_las_rutas:
            return
        
        rutas_filtradas = []
        for ruta in self.todas_las_rutas:
            coincide_origen = (filtro_origen == "Todos" or ruta.get_ciudadorigen() == filtro_origen)
            coincide_destino = (filtro_destino == "Todos" or ruta.get_ciudaddestino() == filtro_destino)
            if coincide_origen and coincide_destino:
                rutas_filtradas.append(ruta)
        
        self.mostrar_rutas_en_tabla(rutas_filtradas)

    def abrir_dialogo_agregar(self):
        """Abre un diálogo para agregar una nueva ruta."""
        try:
            dialogo = QDialog(self)
            
            loader = QUiLoader()
            path = os.path.join(os.path.dirname(__file__), "rutawidget.ui")
            ui_file = QFile(path)
            if not ui_file.open(QIODevice.ReadOnly):
                raise IOError(f"No se puede abrir el archivo de diálogo: {path}")

            widget_dialogo = loader.load(ui_file)
            ui_file.close()

            layout = QVBoxLayout(dialogo)
            layout.addWidget(widget_dialogo)
            dialogo.setWindowTitle("Agregar Nueva Ruta")

            combo_origen = widget_dialogo.findChild(QComboBox, "ComboBox_origen")
            combo_destino = widget_dialogo.findChild(QComboBox, "ComboBox_destino")
            
            nombres_ciudades = sorted(self.ciudades_map.keys())
            combo_origen.addItems(nombres_ciudades)
            combo_destino.addItems(nombres_ciudades)

            widget_dialogo.findChild(QPushButton, "boton_agregar").clicked.connect(dialogo.accept)
            widget_dialogo.findChild(QPushButton, "boton_cancelar").clicked.connect(dialogo.reject)

            if dialogo.exec():
                nombre_origen = combo_origen.currentText()
                nombre_destino = combo_destino.currentText()
                distancia = widget_dialogo.findChild(QLineEdit, "lineEdit_distancia").text().strip()

                codigo_origen = self.ciudades_map.get(nombre_origen)
                codigo_destino = self.ciudades_map.get(nombre_destino)

                resultado = self.controlador.agregar_nueva_ruta(codigo_origen, codigo_destino, distancia)

                if resultado is True:
                    self.cargar_datos_iniciales()
                    QMessageBox.information(self, "Éxito", "Ruta agregada correctamente")
                elif resultado == "duplicado":
                    QMessageBox.information(self, "Información", f"La ruta {nombre_origen} - {nombre_destino} ya existe.")
                else:
                    QMessageBox.warning(self, "Error", resultado)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el diálogo de agregar: {e}")

    def abrir_dialogo_editar(self):
        """Abre un diálogo para editar la distancia de una ruta seleccionada."""
        fila_seleccionada = self.ui.QtableWidget_rutas.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona una ruta para editar.")
            return

        codigo_ruta = self.ui.QtableWidget_rutas.item(fila_seleccionada, 0).text()
        origen_actual = self.ui.QtableWidget_rutas.item(fila_seleccionada, 1).text()
        destino_actual = self.ui.QtableWidget_rutas.item(fila_seleccionada, 2).text()
        distancia_actual = self.ui.QtableWidget_rutas.item(fila_seleccionada, 3).text().replace(" km", "")

        try:
            dialogo = QDialog(self)
            
            loader = QUiLoader()
            path = os.path.join(os.path.dirname(__file__), "rutawidget.ui")
            ui_file = QFile(path)
            if not ui_file.open(QIODevice.ReadOnly):
                raise IOError(f"No se pudo abrir el archivo de diálogo: {path}")

            widget_dialogo = loader.load(ui_file)
            ui_file.close()

            layout = QVBoxLayout(dialogo)
            layout.addWidget(widget_dialogo)
            dialogo.setWindowTitle(f"Editar Distancia - {origen_actual} a {destino_actual}")

            combo_origen = widget_dialogo.findChild(QComboBox, "ComboBox_origen")
            combo_destino = widget_dialogo.findChild(QComboBox, "ComboBox_destino")
            line_distancia = widget_dialogo.findChild(QLineEdit, "lineEdit_distancia")
            
            combo_origen.addItem(origen_actual)
            combo_destino.addItem(destino_actual)
            combo_origen.setEnabled(False)
            combo_destino.setEnabled(False)
            line_distancia.setText(distancia_actual)
            
            boton_actualizar = widget_dialogo.findChild(QPushButton, "boton_agregar")
            boton_actualizar.setText("Actualizar Distancia")
            boton_actualizar.clicked.connect(dialogo.accept)
            widget_dialogo.findChild(QPushButton, "boton_cancelar").clicked.connect(dialogo.reject)

            if dialogo.exec():
                nueva_distancia = line_distancia.text().strip()
                
                resultado = self.controlador.actualizar_distancia_ruta(codigo_ruta, nueva_distancia)

                if resultado is True:
                    self.cargar_datos_iniciales()
                    QMessageBox.information(self, "Éxito", "Distancia actualizada correctamente.")
                else:
                    QMessageBox.warning(self, "Error", resultado)
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el diálogo de edición: {e}")

    def abrir_widget_ciudades(self):
        """Abre el widget para administrar las ciudades."""
        self.ciudad_widget_instance = CiudadWidget(self)
        self.ciudad_widget_instance.show()