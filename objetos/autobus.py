# objetos/autobus.py

class Autobus:
    def __init__(self, numero, matricula, cantAsientos, tipoAutobus, estado, marca_clave, modelo_clave, marca_nombre=None, modelo_nombre=None):
        self.__numero = numero
        self.__matricula = matricula
        self.__cantAsientos = cantAsientos
        self.__tipoAutobus = tipoAutobus
        self.__estado = estado
        self.__marca_clave = marca_clave
        self.__modelo_clave = modelo_clave
        self.__marca_nombre = marca_nombre
        self.__modelo_nombre = modelo_nombre

    def __str__(self):
        return (f"Número: {self.__numero}, Matrícula: {self.__matricula}, Asientos: {self.__cantAsientos}, "
                f"Tipo: {self.__tipoAutobus}, Estado: {self.__estado}, Marca: {self.__marca_nombre or self.__marca_clave}, "
                f"Modelo: {self.__modelo_nombre or self.__modelo_clave}")

    # Getters
    def get_numero(self):
        return self.__numero

    def get_matricula(self):
        return self.__matricula

    def get_cantAsientos(self):
        return self.__cantAsientos

    def get_tipoAutobus(self):
        return self.__tipoAutobus

    def get_estado(self):
        return self.__estado

    def get_marca_clave(self):
        return self.__marca_clave

    def get_modelo_clave(self):
        return self.__modelo_clave
    
    def get_marca_nombre(self):
        return self.__marca_nombre
    
    def get_modelo_nombre(self):
        return self.__modelo_nombre

    # Setters
    def set_numero(self, numero):
        self.__numero = numero

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_cantAsientos(self, cantAsientos):
        self.__cantAsientos = cantAsientos

    def set_tipoAutobus(self, tipoAutobus):
        self.__tipoAutobus = tipoAutobus

    def set_estado(self, estado):
        self.__estado = estado

    def set_marca_clave(self, marca_clave):
        self.__marca_clave = marca_clave

    def set_modelo_clave(self, modelo_clave):
        self.__modelo_clave = modelo_clave

    def set_marca_nombre(self, marca_nombre):
        self.__marca_nombre = marca_nombre

    def set_modelo_nombre(self, modelo_nombre):
        self.__modelo_nombre = modelo_nombre
