#imports de pyside
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout,
                            QDialog, QPushButton, QLineEdit, QLabel, QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QCloseEvent, QFont # Añadido QFont
from utilidades.validaciones import Validaciones


class PantallaIndex(QWidget):

    def __init__(self, controlador, parent=None):
        super().__init__(parent)
        self.controlador = controlador

        # Crear una instancia del loader
        loader = QUiLoader()

        # Esto construye la ruta correcta sin importar desde donde se ejecute el script
        path = os.path.join(os.path.dirname(__file__),"pantalla_index.ui")
        ui_file = QFile(path)

        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Error: No se puede abrir el archivo UI en: {path}")
            return
        
        # Cargar el UI en self.ui
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # Integrar el widget cargado en este QWidget usando un layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)
        self.setLayout(layout)

        # Configurar las tablas para que no sean editables y los datos estén centrados
        self.ui.QtableWidget_operadores.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QtableWidget_operadores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_operadores.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.QtableWidget_corridasact.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QtableWidget_corridasact.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_corridasact.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.ui.QtableWidget_pasajeros.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.QtableWidget_pasajeros.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.QtableWidget_pasajeros.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.cargar_datos_dashboard()

    def cargar_datos_dashboard(self):
        self.cargar_pasajeros_dashboard()
        self.cargar_corridas_dashboard()
        self.cargar_operadores_dashboard()

    def cargar_pasajeros_dashboard(self):
        try:
            pasajeros_data = self.controlador.obtener_pasajeros_dashboard()
            self.ui.QtableWidget_pasajeros.setRowCount(0)
            
            font_bold = QFont()
            font_bold.setBold(True)

            if pasajeros_data:
                for fila_idx, pasajero in enumerate(pasajeros_data):
                    numero, nombre, apellPat, apellMat, edad, telefono = pasajero
                    self.ui.QtableWidget_pasajeros.insertRow(fila_idx)
                    
                    item_numero = QTableWidgetItem(str(numero))
                    item_numero.setTextAlignment(Qt.AlignCenter)
                    item_numero.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 0, item_numero)
                    
                    item_nombre_completo = QTableWidgetItem(f"{nombre} {apellPat} {apellMat}")
                    item_nombre_completo.setTextAlignment(Qt.AlignCenter)
                    item_nombre_completo.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 1, item_nombre_completo)
                    
                    item_edad = QTableWidgetItem(str(edad))
                    item_edad.setTextAlignment(Qt.AlignCenter)
                    item_edad.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 2, item_edad)
                    
                    item_telefono = QTableWidgetItem(telefono)
                    item_telefono.setTextAlignment(Qt.AlignCenter)
                    item_telefono.setFont(font_bold)
                    self.ui.QtableWidget_pasajeros.setItem(fila_idx, 3, item_telefono)
                    
                    # Asumiendo que la columna 4 es para "Boleto", no se rellena aquí
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar pasajeros dashboard: {e}")

    def cargar_corridas_dashboard(self):
        try:
            corridas_data = self.controlador.obtener_corridas_dashboard()
            self.ui.QtableWidget_corridasact.setRowCount(0)

            font_bold = QFont()
            font_bold.setBold(True)
            
            if corridas_data:
                for fila_idx, corrida in enumerate(corridas_data):
                    numero, fecha, hora_salida, ruta = corrida # Ajustado el unpack
                    self.ui.QtableWidget_corridasact.insertRow(fila_idx)
                    
                    item_numero = QTableWidgetItem(str(numero))
                    item_numero.setTextAlignment(Qt.AlignCenter)
                    item_numero.setFont(font_bold)
                    self.ui.QtableWidget_corridasact.setItem(fila_idx, 0, item_numero)
                    
                    item_fecha = QTableWidgetItem(str(fecha))
                    item_fecha.setTextAlignment(Qt.AlignCenter)
                    item_fecha.setFont(font_bold)
                    self.ui.QtableWidget_corridasact.setItem(fila_idx, 1, item_fecha)
                    
                    item_hora_salida = QTableWidgetItem(str(hora_salida))
                    item_hora_salida.setTextAlignment(Qt.AlignCenter)
                    item_hora_salida.setFont(font_bold)
                    self.ui.QtableWidget_corridasact.setItem(fila_idx, 2, item_hora_salida)
                    
                    item_ruta = QTableWidgetItem(ruta) # Usar directamente 'ruta'
                    item_ruta.setTextAlignment(Qt.AlignCenter)
                    item_ruta.setFont(font_bold)
                    self.ui.QtableWidget_corridasact.setItem(fila_idx, 3, item_ruta)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar corridas dashboard: {e}")

    def cargar_operadores_dashboard(self):
        try:
            operadores_data = self.controlador.obtener_operadores_con_corridas_dashboard()
            self.ui.QtableWidget_operadores.setRowCount(0)

            font_bold = QFont()
            font_bold.setBold(True)
            
            if operadores_data:
                for fila_idx, operador in enumerate(operadores_data):
                    # Asumo que la consulta devuelve: numero, nombre_completo_operador, ruta_corrida, fecha_corrida
                    numero, nombre_completo, ruta_corrida, fecha_corrida = operador
                    self.ui.QtableWidget_operadores.insertRow(fila_idx)
                    
                    item_numero = QTableWidgetItem(str(numero))
                    item_numero.setTextAlignment(Qt.AlignCenter)
                    item_numero.setFont(font_bold)
                    self.ui.QtableWidget_operadores.setItem(fila_idx, 0, item_numero)
                    
                    item_nombre_completo = QTableWidgetItem(nombre_completo)
                    item_nombre_completo.setTextAlignment(Qt.AlignCenter)
                    item_nombre_completo.setFont(font_bold)
                    self.ui.QtableWidget_operadores.setItem(fila_idx, 1, item_nombre_completo)
                    
                    item_ruta = QTableWidgetItem(ruta_corrida)
                    item_ruta.setTextAlignment(Qt.AlignCenter)
                    item_ruta.setFont(font_bold)
                    self.ui.QtableWidget_operadores.setItem(fila_idx, 2, item_ruta)
                    
                    item_fecha = QTableWidgetItem(str(fecha_corrida))
                    item_fecha.setTextAlignment(Qt.AlignCenter)
                    item_fecha.setFont(font_bold)
                    self.ui.QtableWidget_operadores.setItem(fila_idx, 3, item_fecha)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar operadores dashboard: {e}")