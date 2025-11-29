# CLASE ASIENTO objetos > asiento

class Asiento:
    
    claveAsiento = ""
    numAsiento = 0
    ubicacion = ""
    estado = ""
    autobus = 0
    
    
    def __init__(self, claveAsiento, numAsiento, ubicacion, estado, autobus):
        self.claveAsiento = claveAsiento
        self.numAsiento = numAsiento
        self.ubicacion = ubicacion
        self.estado = estado
        self.autobus = autobus
        
    def get_claveAsiento(self):
        return self.claveAsiento
    
    def get_numAsiento(self):
        return self.numAsiento
    
    def get_ubicacion(self):
        return self.ubicacion
    
    def get_estado(self):
        return self.estado
    
    def get_autobus(self):
        return self.autobus
    
    def set_claveAsiento(self, claveAsiento):
        self.claveAsiento = claveAsiento
    
    def set_numAsiento(self, numAsiento):
        self.numAsiento = numAsiento
    
    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion
    
    def set_estado(self, estado):
        self.estado = estado
    
    def set_autobus(self, autobus):
        self.autobus = autobus