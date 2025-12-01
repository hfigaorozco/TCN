from dao.conn import Connection

class CorridaDAO:
    def __init__(self):
        pass

    def obtener_todas_las_corridas_detalladas(self):
        corridas_detalladas = []
        try:
            conn = Connection.getConnection()
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT
                    c.numero AS numero_viaje,
                    ro.nombre AS ciudad_origen,
                    rd.nombre AS ciudad_destino,
                    r.distancia,
                    CONCAT(c.fecha, ' ', c.hora_salida) AS fecha_hora_salida,
                    CONCAT(o.nombre, ' ', o.apellPat, ' ', COALESCE(o.apellMat, '')) AS nombre_operador,
                    a.numero AS numero_autobus,
                    a.matricula,
                    a.cantAsientos AS cantidad_asientos,
                    (SELECT COUNT(*) FROM reservacion res WHERE res.corrida = c.numero) AS cantidad_pasajeros
                FROM
                    corrida c
                JOIN
                    ruta r ON c.ruta = r.codigo
                JOIN
                    ciudad ro ON r.ciudadOrigen = ro.codigo
                JOIN
                    ciudad rd ON r.ciudadDestino = rd.codigo
                JOIN
                    operador o ON c.operador = o.numero
                JOIN
                    autobus a ON c.autobus = a.numero
            """
            cursor.execute(query)
            corridas_detalladas = cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener corridas detalladas: {e}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
        return corridas_detalladas