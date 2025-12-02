#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel, QMessageBox, QTableWidget,
                            QTableWidgetItem, QComboBox)
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
        self.boton_buscar = self.ui.findChild(QPushButton,'boton_buscar')

        self.line_edit_buscar_reservacion = self.ui.findChild(QLineEdit,'lineEdit_buscar')
        self.combo_box_filtro = self.ui.findChild(QComboBox,'comboBox_filtros')

        self.table_widget = self.ui.findChild(QTableWidget,'tabla_reservaciones')

        # Si el boton crear reservacion fue recuperado as True, entonces ejecuata el metodo determinado.
        if self.boton_crear_reservacion:
            self.boton_crear_reservacion.clicked.connect(self.filtrarPorComboBox)

        # Si el boton editar fue recuperado as True, entonces ejecuata el metodo determinado.
        if self.boton_editar_reservacion:
            self.boton_crear_reservacion.clicked.connect(self.editarReservacion)

        if self.combo_box_filtro:
            self.combo_box_filtro.currentIndexChanged.connect(self.filtrarPorComboBox)

        if self.boton_buscar:
            self.boton_buscar.clicked.connect(self.buscarPorCorrida)


        self.llenarTablaAlInicio()

    def crearReservacion(self):
        pass

    def buscarPorCorrida(self):
        corridas = self.controlador.buscarReservacionPorCorrida(str(self.line_edit_buscar_reservacion.text()))
        self.__llenar_tabla_reservaciones(corridas)

    def editarReservacion(self):
        """
        Obtiene los datos de la fila que está actualmente seleccionada o enfocada.
        Retorna una lista con el contenido de cada celda de esa fila.
        """

        tabla = self.table_widget  # Asume que 'self.tableWidget' es tu QTableWidget

        # 1. Obtener el indice de la fila actualmente seleccionada/enfocada
        fila_actual = tabla.currentRow()

        # 2. Verificar si hay alguna fila seleccionada (-1 si no hay)
        if fila_actual < 0:
            print("No hay ninguna fila actualmente seleccionada o enfocada.")
            return None  # Retorna None si no hay selección

        # 3. Obtener la cantidad de columnas de la tabla (Método clave)
        num_columnas = tabla.columnCount()

        datos_fila = []

        # 4. Iterar sobre las columnas de la fila actual para extraer los datos
        for col_index in range(num_columnas):

            # Obtener el QTableWidgetItem en la posición (fila, columna)
            item = tabla.item(fila_actual, col_index)

            if item is not None:
                # Extraer el texto del QTableWidgetItem (Método clave)
                dato = item.text()
                datos_fila.append(dato)
            else:
                # Manejar celdas vacías si es posible
                datos_fila.append("")

        print(f"Datos de la fila {fila_actual}: {datos_fila}")
        return datos_fila

    def filtrarPorComboBox(self):
        if self.combo_box_filtro.currentText() == "Reservaciones Activas":
            if True:
                pass
        elif self.combo_box_filtro.currentText() == "Reservaciones Pendientes":
            pass
        elif self.combo_box_filtro.currentText() == "Nombre de cliente":
            pass
        elif self.combo_box_filtro.currentText() == "Origen":
            datos_tabla = self.controlador.buscarReservacionPorCiudad(str(self.line_edit_buscar_reservacion.text()))
            if datos_tabla:
                self.__llenar_tabla_reservaciones(datos_tabla)
        elif self.combo_box_filtro.currentText() == "Destino":
            datos_tabla = self.controlador.buscarReservacionPorCiudad(str(self.line_edit_buscar_reservacion.text()))
            if datos_tabla:
                self.__llenar_tabla_reservaciones(datos_tabla)
        elif self.combo_box_filtro.currentText() == "Fecha":
            pass

        

    def llenarTablaAlInicio(self):
        datos_tabla = self.controlador.consultarTodasReservacionesParaTabla()
        self.__llenar_tabla_reservaciones(datos_tabla)

    def __llenar_tabla_reservaciones(self,datos_tabla):
        # columnas = ["Nombre", "Edad", "Ciudad"]
        
        # Establecer la estructura
        self.table_widget.setRowCount(len(datos_tabla))
        num_columnas = self.table_widget.columnCount()

        num_cols_datos = len(datos_tabla[0])

        if not datos_tabla:
            self.table_widget.setRowCount(0) # Vacía la tabla si no hay datos
            print("No hay datos para llenar la tabla.")
            return

        for row_index, row_data in enumerate(datos_tabla):
        # Usamos el minimo entre las columnas de los datos y las columnas de la tabla 
        # para evitar errores si las dimensiones no coinciden.
            for col_index in range(min(num_cols_datos, self.table_widget.columnCount())):
                item_data = row_data[col_index]

                # Crear y configurar el ítem
                item = QTableWidgetItem(str(item_data))

                # 4. Insertar el item en la celda
                self.table_widget.setItem(row_index, col_index, item)

                # Si la columna es la 2 (indice 1), la centramos
                if col_index == 1: 
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
        # Ajustar el ancho de las columnas al contenido
        # self.table_widget.resizeColumnsToContents()
    
