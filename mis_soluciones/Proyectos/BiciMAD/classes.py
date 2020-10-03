import math


class Estacion:
    def __init__(self, name, id, num_bicis, address, longitude,
                 latitude):
        self.name = name
        self.id = id
        self.num_bicis = num_bicis
        self.address = address
        self.longitude = longitude
        self.latitude = latitude

    def distancia(self, longitude, latitude):
        lat1, lon1 = self.latitude, self.longitude
        lat2, lon2 = latitude, longitude
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d


class ComunidadMadrid:
    def __init__(self, estaciones):
        """ estaciones es una lista de objetos Estacion"""
        self.estaciones = estaciones

    def get_ids(self):
        """Devuelve una lista con los identificadores de
        las estaciones"""
        lista_ids = [int(e.id) for e in self.estaciones]
        return lista_ids

    def busca_estacion(self, estacion, tipo_busqueda):
        """Busca el valor @estacion en el param @tipo_busqueda,
        @tipo_busqueda puede ser id o name"""
        if tipo_busqueda == 'id':
            estacion = [e for e in self.estaciones if e.id == estacion]
        elif tipo_busqueda == 'name':
            estacion = [e for e in self.estaciones if e.name == estacion]
        else:
            estacion = []

        # No hay estacion si el valor tipo_busqueda era erroneo
        # o si la estacion buscada no existia
        if not estacion:
            estacion = None
        else:
            estacion = estacion[0]

        return estacion

