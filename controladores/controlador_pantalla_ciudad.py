from dao.ciudad_dao import CiudadesDAO
from objetos.ciudad import Ciudad

class ControladorPantallaCiudad:
    def __init__(self, ciudad_dao):
        self.ciudad_dao = ciudad_dao

    def obtener_todas_las_ciudades(self):
        """
        Obtiene todas las ciudades de la base de datos.
        Devuelve una lista de objetos Ciudad.
        """
        try:
            return self.ciudad_dao.obtener_todas()
        except Exception as e:
            print(f"Error en controlador al obtener ciudades: {e}")
            return False

    def insertar_ciudad(self, codigo, nombre):
        """
        Inserta una nueva ciudad en la base de datos.
        Devuelve True si tiene éxito, o un mensaje de error.
        """
        if not codigo or not nombre:
            return "El código y el nombre son obligatorios."
        
        if len(codigo) != 3:
            return "El código de la ciudad debe tener 3 caracteres."

        ciudad = Ciudad(codigo.upper(), nombre.capitalize())
        try:
            resultado = self.ciudad_dao.insertar(ciudad)
            if resultado == "duplicado":
                return "Ya existe una ciudad con ese código o nombre."
            return resultado
        except Exception as e:
            print(f"Error en controlador al insertar ciudad: {e}")
            return "Error interno al insertar la ciudad."

    def actualizar_ciudad(self, codigo_actual, nuevo_codigo, nuevo_nombre):
        """
        Actualiza una ciudad existente.
        Devuelve True si tiene éxito, o un mensaje de error.
        """
        if not codigo_actual or not nuevo_codigo or not nuevo_nombre:
            return "Todos los campos son obligatorios."
        
        if len(nuevo_codigo) != 3:
            return "El nuevo código de la ciudad debe tener 3 caracteres."

        try:
            resultado = self.ciudad_dao.actualizar(codigo_actual, nuevo_codigo.upper(), nuevo_nombre.capitalize())
            if resultado == "duplicado":
                return "Ya existe una ciudad con el nuevo código."
            elif resultado is False:
                return "No se pudo actualizar la ciudad. Verifique el código."
            return resultado
        except Exception as e:
            print(f"Error en controlador al actualizar ciudad: {e}")
            return "Error interno al actualizar la ciudad."

    def eliminar_ciudad(self, codigo):
        """
        Elimina una ciudad de la base de datos.
        Devuelve True si tiene éxito, o un mensaje de error.
        """
        if not codigo:
            return "El código de la ciudad es obligatorio para eliminar."
        try:
            resultado = self.ciudad_dao.eliminar(codigo)
            if resultado is False:
                return "No se pudo eliminar la ciudad. Verifique el código."
            return resultado
        except Exception as e:
            print(f"Error en controlador al eliminar ciudad: {e}")
            return "Error interno al eliminar la ciudad."

    def buscar_ciudades(self, nombre):
        """
        Busca ciudades por nombre.
        Devuelve una lista de objetos Ciudad.
        """
        try:
            return self.ciudad_dao.buscar_por_nombre(nombre)
        except Exception as e:
            print(f"Error en controlador al buscar ciudades: {e}")
            return False