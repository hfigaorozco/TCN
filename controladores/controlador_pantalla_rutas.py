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
        print(f"Controlador: Intentando agregar ruta con Origen={codigo_origen}, Destino={codigo_destino}, Distancia={distancia}")
        if not codigo_origen or not codigo_destino or not distancia:
            print("Controlador: Campos obligatorios vacíos.")
            return "Todos los campos son obligatorios."

        if codigo_origen == codigo_destino:
            print("Controlador: Origen y destino son la misma ciudad.")
            return "El origen y el destino no pueden ser la misma ciudad."

        try:
            distancia_float = float(distancia)
            if distancia_float <= 0:
                print("Controlador: Distancia menor o igual a 0.")
                return "La distancia debe ser mayor a 0."
            if distancia_float > 1500:
                print("Controlador: Distancia mayor a 1500.")
                return "La distancia no puede ser mayor a 1500."
        except ValueError:
            print(f"Controlador: Error de formato en distancia '{distancia}'.")
            return "La distancia debe ser un número válido."
        
        try:
            resultado = self.ruta_dao.insertar(codigo_origen, codigo_destino, distancia)
            print(f"Controlador: Resultado de insertar ruta en DAO: {resultado}")
            return resultado # Devuelve True, "duplicado", o False
        except Exception as e:
            print(f"Error en controlador al agregar ruta: {e}")
            return "No se pudo agregar la ruta por un error interno."

    def actualizar_distancia_ruta(self, codigo_ruta, distancia):
        """
        Intenta actualizar la distancia de una ruta existente.
        Devuelve True si tiene éxito, o un string con el mensaje de error.
        """
        print(f"Controlador: Intentando actualizar distancia de ruta {codigo_ruta} a {distancia}")
        if not distancia:
            print("Controlador: Distancia vacía para actualizar.")
            return "La distancia es obligatoria."
        
        try:
            distancia_numero = float(distancia)
            if distancia_numero <= 0:
                print("Controlador: Distancia menor o igual a 0 para actualizar.")
                return "La distancia debe ser mayor a 0."
            elif distancia_numero > 1500:
                print("Controlador: Distancia mayor a 1500 para actualizar.")
                return "La distancia no puede ser mayor a 1500."
        except ValueError:
            print(f"Controlador: Error de formato en distancia '{distancia}' para actualizar.")
            return "La distancia debe ser un número válido."

        try:
            resultado = self.ruta_dao.actualizar_distancia(codigo_ruta, distancia)
            print(f"Controlador: Resultado de actualizar distancia en DAO: {resultado}")
            return resultado
        except Exception as e:
            print(f"Error en controlador al actualizar distancia: {e}")
            return "No se pudo actualizar la distancia por un error interno."
