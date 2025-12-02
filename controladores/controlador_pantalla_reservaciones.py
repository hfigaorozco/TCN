from mysql.connector import Error
from utilidades.validaciones import Validaciones

class ControlardorPantallaReservaciones:
    def __init__(self, reservacion_dao):
        self.reservacion_dao = reservacion_dao

    def getTotalReservaciones(self):
        try:
            return self.servicio_de_consulta.consultarNumeroReservaciones()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTotalReservaciones()): {e}')
            raise e


    def consultarTodasReservacionesParaTabla(self):
        try:
            return self.servicio_de_consulta.consultarTodasReservacionesParaTabla()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservaciones()): {e}')
            raise e
        

    def consultarTablaReservacionesActuales(self):
        try:
            return self.servicio_de_consulta.consultarTablaReservacionesActuales()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservaciones()): {e}')
            raise e
        

    def consultarTablaReservacionesPasadas(self):
        try:
            return self.servicio_de_consulta.consultarTablaReservacionesPasadas()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservaciones()): {e}')
            raise e
        

    def buscarReservacionPorNumero(self,numero):

        if not Validaciones.validar_id(numero):
            return False
        try:
            return self.servicio_de_consulta.buscarReservacionPorNumero(numero)
        except Error as e:
            print(f'Error en ControladorVEReservaciones (buscarReservacionesPorNUmero()): {e}')
            raise e
        
    def consultarTotalReservacionesPasadas(self):
        try:
            return self.servicio_de_consulta.consultarTotalReservacionesPasadas()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservacionesPasadas()): {e}')
            raise e
        

    def consultarTotalReservacionesActivas(self):
        try:
            return self.servicio_de_consulta.consultarTotalReservacionesActivas()
        except Error as e:
            print(f'Error en ControladorVEReservaciones (getTodasReservacionesActivas()): {e}')
            raise e