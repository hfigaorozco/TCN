from dao.ruta_dao import RutaDAO
from dao.ciudad_dao import CiudadesDAO

class ControladorPantallaRutas:
    def __init__(self, ruta_dao, ciudad_dao):
        self.ruta_dao = ruta_dao
        self.ciudad_dao = ciudad_dao

    def obtener_todas_las_rutas(self):
        """
        Obtiene todas las rutas de la base de datos.
        Devuelve una lista de objetos Ruta o False si hay un error.
        """
        try:
            return self.ruta_dao.obtener_todas()
        except Exception as e:
            print(f"Error en controlador al obtener rutas: {e}")
            return False

    def obtener_ciudades_map(self):
        """
        Obtiene un mapa de nombres de ciudades a sus códigos.
        Devuelve un diccionario o False si hay un error.
        """
        try:
            ciudades = self.ciudad_dao.obtener_todas()
            ciudades_map = {ciudad.get_nombre(): ciudad.get_codigo() for ciudad in ciudades}
            return ciudades_map
        except Exception as e:
            print(f"Error en controlador al obtener ciudades: {e}")
            return False

    def agregar_nueva_ruta(self, codigo_origen, codigo_destino, distancia):
        """
        Intenta agregar una nueva ruta.
        Devuelve True si tiene éxito, o un string con el mensaje de error/información.
        """
        if not codigo_origen or not codigo_destino or not distancia:
            return "Todos los campos son obligatorios."

        if codigo_origen == codigo_destino:
            return "El origen y el destino no pueden ser la misma ciudad."

        try:
            distancia_float = float(distancia)
            if distancia_float <= 0:
                return "La distancia debe ser mayor a 0."
            if distancia_float > 200:
                return "La distancia no puede ser mayor a 200."
        except ValueError:
            return "La distancia debe ser un número válido."
        
        try:
            resultado = self.ruta_dao.insertar(codigo_origen, codigo_destino, distancia)
            return resultado # Devuelve True, "duplicado", o False
        except Exception as e:
            print(f"Error en controlador al agregar ruta: {e}")
            return "No se pudo agregar la ruta por un error interno."

    def actualizar_distancia_ruta(self, codigo_ruta, distancia):
        """
        Intenta actualizar la distancia de una ruta existente.
        Devuelve True si tiene éxito, o un string con el mensaje de error.
        """
        if not distancia:
            return "La distancia es obligatoria."
        
        try:
            distancia_numero = float(distancia)
            if distancia_numero <= 0:
                return "La distancia debe ser mayor a 0."
            elif distancia_numero > 200:
                return "La distancia no puede ser mayor a 200."
        except ValueError:
            return "La distancia debe ser un número válido."

        try:
            return self.ruta_dao.actualizar_distancia(codigo_ruta, distancia)
        except Exception as e:
            print(f"Error en controlador al actualizar distancia: {e}")
            return "No se pudo actualizar la distancia por un error interno."
