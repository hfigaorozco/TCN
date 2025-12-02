from PySide6.QtWidgets import QDialog, QMessageBox
from vista.empresa.actualizarCorridaDialog_ui import Ui_Form # Correct import
from dao.autobus_dao import AutobusDAO
from dao.operador_dao import OperadorDAO
from dao.corrida_dao import CorridaDAO
from objetos.autobus import Autobus
from objetos.Operador import Operador
import re # For route parsing

class ControladorActualizarCorridaDialog(QDialog):
    def __init__(self, parent=None, corrida_data=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.autobus_dao = AutobusDAO()
        self.operador_dao = OperadorDAO()
        self.corrida_dao = CorridaDAO()
        self.corrida_data = corrida_data # Data of the corrida to be updated

        self.buses = [] # To store Autobus objects
        self.operadores = [] # To store Operador objects

        self.init_ui_connections()
        self.load_initial_data()
        if self.corrida_data:
            self.populate_form_with_corrida_data()

    def init_ui_connections(self):
        self.ui.dateEdit_fechaCorrida.dateChanged.connect(self.update_available_resources)
        self.ui.boton_actualizarCorrida.clicked.connect(self.actualizar_corrida) # Changed from crear_corrida
        self.ui.boton_cancelarActualizacion.clicked.connect(self.reject) # Changed from boton_cancelar

    def load_initial_data(self):
        # Set default date to today or a reasonable future date
        self.ui.dateEdit_fechaCorrida.setDate(self.ui.dateEdit_fechaCorrida.minimumDate())
        self.update_available_resources()
        self.populate_ruta_combobox() # Populate ruta combobox

    def populate_form_with_corrida_data(self):
        # Assuming corrida_data is a dictionary with details
        if not self.corrida_data:
            return

        # Set route
        ruta_text = f"{self.corrida_data['ciudad_origen']}-{self.corrida_data['ciudad_destino']}"
        index = self.ui.comboBox_rutaCorrida.findText(ruta_text)
        if index >= 0:
            self.ui.comboBox_rutaCorrida.setCurrentIndex(index)

        # Set date and time
        from PySide6.QtCore import QDate, QTime, QDateTime
        datetime_obj = QDateTime.fromString(self.corrida_data['fecha_hora_salida'], "yyyy-MM-dd HH:mm:ss")
        self.ui.dateEdit_fechaCorrida.setDate(datetime_obj.date())
        self.ui.timeEdit_horaSalCorrida.setTime(datetime_obj.time())
        
        # Assuming hora_llegada is also in corrida_data
        # This might require parsing a separate time or calculating it.
        # For now, let's assume it's directly available or can be set.
        # If not available, you might need to calculate it based on distance and average speed.
        # For simplicity, let's assume it's part of fecha_hora_salida or a separate field.
        # If it's part of the full datetime string, extract it.
        # For this example, let's just set the arrival time from the DB value if available
        # This needs to be correctly parsed from your corrida_data
        # For example, if corrida_data has 'hora_llegada_str':
        # arrival_time_str = self.corrida_data.get('hora_llegada_str')
        # if arrival_time_str:
        #     self.ui.timeEdit_horaLegCorrida.setTime(QTime.fromString(arrival_time_str, "HH:mm:ss"))
        # As per the UI, it's 'timeEdit_horaLegCorrida'. If arrival time is stored separately.
        # Let's assume for now, it's not directly in 'fecha_hora_salida' and might need to be added to corrida_data or calculated.
        # For now, I will leave it as it is, assuming the UI's default will be fine if not explicitly set.
        
        # Set price
        self.ui.lineEdit_precioCorrida.setText(str(self.corrida_data['precio']))

        # Populate autobus and operador comboboxes with pre-selected values
        self.update_available_resources() # This will reload comboboxes
        
        # Select autobus
        if 'autobus_numero' in self.corrida_data:
            bus_numero = self.corrida_data['autobus_numero']
            for i in range(self.ui.comboBox_autobusCorrida.count()):
                item_data = self.ui.comboBox_autobusCorrida.itemData(i)
                if item_data and item_data.get_numero() == bus_numero:
                    self.ui.comboBox_autobusCorrida.setCurrentIndex(i)
                    break
        
        # Select operador
        operador_numero = self.corrida_data['operador_numero']
        for i in range(self.ui.comboBox_operadorCorrida.count()):
            item_data = self.ui.comboBox_operadorCorrida.itemData(i)
            if item_data and item_data.get_numero() == operador_numero:
                self.ui.comboBox_operadorCorrida.setCurrentIndex(i)
                break


    def populate_ruta_combobox(self):
        # Assuming rutas are static or fetched from another DAO if dynamic
        # For now, it seems they are hardcoded in the UI file
        # If they need to be fetched from DB, a RutaDAO would be needed.
        # This just ensures placeholder text is cleared and a default selection isn't made
        if self.ui.comboBox_rutaCorrida.count() > 0 and self.ui.comboBox_rutaCorrida.itemText(0) == "Ruta":
            self.ui.comboBox_rutaCorrida.removeItem(0) # Remove placeholder if present
        # If updating, don't set to -1, let populate_form_with_corrida_data handle selection
        # self.ui.comboBox_rutaCorrida.setCurrentIndex(-1)

    def update_available_resources(self):
        selected_date = self.ui.dateEdit_fechaCorrida.date().toString("yyyy-MM-dd")
        self.populate_autobus_combobox(selected_date)
        self.populate_operador_combobox(selected_date)

    def populate_autobus_combobox(self, selected_date):
        self.ui.comboBox_autobusCorrida.clear()
        all_buses = self.autobus_dao.listar_autobuses()
        
        print(f"DEBUG CTLR ACT: all_buses retrieved: {all_buses}") # Debug print
        
        self.buses = all_buses # Store all buses, no filtering
        
        if not all_buses:
            self.ui.comboBox_autobusCorrida.addItem("No hay autobuses registrados")
            self.ui.comboBox_autobusCorrida.setEnabled(False)
            print("DEBUG CTLR ACT: ComboBox autobus deshabilitado (no hay autobuses registrados).") # Debug print
        else:
            self.ui.comboBox_autobusCorrida.setEnabled(True)
            print("DEBUG CTLR ACT: ComboBox autobus habilitado. Agregando autobuses...") # Debug print
            for bus in all_buses: # Iterate through all buses
                self.ui.comboBox_autobusCorrida.addItem(f"{bus.get_numero()} - {bus.get_marca_nombre()} {bus.get_modelo_nombre()} ({bus.get_matricula()})", bus)
            # If updating, don't set to -1, let populate_form_with_corrida_data handle selection
            # self.ui.comboBox_autobusCorrida.setCurrentIndex(-1)

    def populate_operador_combobox(self, selected_date):
        self.ui.comboBox_operadorCorrida.clear()
        all_operadores = self.operador_dao.listar_operadores()
        available_operadores = []

        for operador in all_operadores:
            # When updating, the currently assigned operator should always be available
            if self.corrida_data and 'operador_numero' in self.corrida_data and operador.get_numero() == self.corrida_data['operador_numero']:
                available_operadores.append(operador)
            elif not self.corrida_dao.operador_ocupado_en_fecha(operador.get_numero(), selected_date):
                available_operadores.append(operador)
        
        self.operadores = available_operadores # Store for potential later use

        if not available_operadores:
            self.ui.comboBox_operadorCorrida.addItem("No hay operadores disponibles para esta fecha")
            self.ui.comboBox_operadorCorrida.setEnabled(False)
        else:
            self.ui.comboBox_operadorCorrida.setEnabled(True)
            for operador in available_operadores:
                self.ui.comboBox_operadorCorrida.addItem(f"{operador.get_numero()} - {operador.get_nombre_completo()}", operador)
            # If updating, don't set to -1, let populate_form_with_corrida_data handle selection
            # self.ui.comboBox_operadorCorrida.setCurrentIndex(-1)

    def get_selected_autobus(self):
        selected_index = self.ui.comboBox_autobusCorrida.currentIndex()
        if selected_index >= 0 and self.ui.comboBox_autobusCorrida.itemData(selected_index):
            return self.ui.comboBox_autobusCorrida.itemData(selected_index)
        return None

    def get_selected_operador(self):
        selected_index = self.ui.comboBox_operadorCorrida.currentIndex()
        if selected_index >= 0 and self.ui.comboBox_operadorCorrida.itemData(selected_index):
            return self.ui.comboBox_operadorCorrida.itemData(selected_index)
        return None
    
    def get_selected_ruta_codigo(self):
        selected_text = self.ui.comboBox_rutaCorrida.currentText()
        if selected_text and selected_text != "Ruta": # Avoid placeholder
            return selected_text
        return None

    def actualizar_corrida(self):
        if not self.corrida_data or 'numero_viaje' not in self.corrida_data:
            QMessageBox.critical(self, "Error", "No se proporcionaron datos de corrida para actualizar.")
            return

        numero_viaje = self.corrida_data['numero_viaje']
        ruta_codigo = self.get_selected_ruta_codigo()
        fecha = self.ui.dateEdit_fechaCorrida.date().toString("yyyy-MM-dd")
        hora_salida = self.ui.timeEdit_horaSalCorrida.time().toString("HH:mm:ss")
        hora_llegada = self.ui.timeEdit_horaLegCorrida.time().toString("HH:mm:ss") # Needs to be accurately captured
        precio_text = self.ui.lineEdit_precioCorrida.text()
        
        selected_operador = self.get_selected_operador()
        selected_autobus = self.get_selected_autobus()

        # Input validation
        if not ruta_codigo:
            QMessageBox.warning(self, "Error de Validación", "Por favor, seleccione una ruta.")
            return
        if not selected_autobus:
            QMessageBox.warning(self, "Error de Validación", "Por favor, seleccione un autobús.")
            return
        if not selected_operador:
            QMessageBox.warning(self, "Error de Validación", "Por favor, seleccione un operador.")
            return
        
        try:
            precio = float(precio_text)
            if precio <= 0:
                raise ValueError("El precio debe ser un número positivo.")
        except ValueError:
            QMessageBox.warning(self, "Error de Validación", "Por favor, ingrese un precio válido.")
            return
        
        operador_numero = selected_operador.get_numero()
        autobus_numero = selected_autobus.get_numero()
        lugares_disponibles = selected_autobus.get_cantAsientos() # Get capacity from selected bus
        estado = self.corrida_data.get('estado', 'ACT') # Preserve existing status or default to ACT

        if self.corrida_dao.actualizar_corrida(numero_viaje, ruta_codigo, fecha, hora_salida, hora_llegada, precio, operador_numero, autobus_numero, lugares_disponibles, estado):
            QMessageBox.information(self, "Éxito", "Corrida actualizada exitosamente.")
            self.accept() # Close the dialog on success
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar la corrida. Verifique los datos e intente de nuevo.")
