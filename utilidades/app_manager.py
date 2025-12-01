#Este modulo contiene todas las referencias a los controladores del programa.
class AppManager:
    def __init__(self, controlador_index,controlador_isd, controlador_rd, controlador_pr, 
                controlador_pc,controlador_pa,controlador_prutas, controlador_po,controlador_pp):
        # Almacena los controladores como atributos
        self.controlador_index = controlador_index
        self.controlador_isd = controlador_isd
        self.controlador_rd = controlador_rd
        self.controlador_pr = controlador_pr
        self.controlador_pc = controlador_pc
        self.controlador_pa = controlador_pa
        self.controlador_prutas = controlador_prutas
        self.controlador_po = controlador_po
        self.controlador_pp = controlador_pp
