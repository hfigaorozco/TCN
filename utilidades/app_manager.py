#Este modulo contiene todas las referencias a los controladores del programa.
class AppManager:
    def __init__(self, controlador_isd, controlador_rd):
        # Almacena los controladores como atributos
        self.controlador_isd = controlador_isd
        self.controlador_rd = controlador_rd
