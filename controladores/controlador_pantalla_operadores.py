# controladores/controlador_pantalla_operadores.py

from dao.operador_dao import OperadorDAO
# Asumiendo que existe un objeto Operador si es necesario para el controlador
# from objetos.Operador import Operador 

class ControladorPantallaOperadores:
    def __init__(self, operador_dao):
        self.operador_dao = operador_dao

    def obtener_todos(self):
        """
        Obtiene todos los operadores de la base de datos a través del DAO.
        """
        try:
            return self.operador_dao.obtener_todos()
        except Exception as e:
            print(f"Error en ControladorPantallaOperadores.obtener_todos: {e}")
            return []

    def insertar_operador(self, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato):
        """
        Intenta insertar un nuevo operador.
        """
        try:
            # Aquí se podrían añadir validaciones adicionales si el controlador las necesitara
            # por encima de las de la vista. Por ahora, se asume que la vista ya valida.
            return self.operador_dao.insertar(nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato)
        except Exception as e:
            print(f"Error en ControladorPantallaOperadores.insertar_operador: {e}")
            return False

    def actualizar_operador(self, numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato):
        """
        Intenta actualizar un operador existente.
        """
        try:
            # Aquí se podrían añadir validaciones adicionales si el controlador las necesitara
            return self.operador_dao.actualizar(numero, nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato)
        except Exception as e:
            print(f"Error en ControladorPantallaOperadores.actualizar_operador: {e}")
            return False

    def buscar_operadores(self, criterio):
        """
        Busca operadores por un criterio dado a través del DAO.
        """
        try:
            return self.operador_dao.buscar(criterio)
        except Exception as e:
            print(f"Error en ControladorPantallaOperadores.buscar_operadores: {e}")
            return []