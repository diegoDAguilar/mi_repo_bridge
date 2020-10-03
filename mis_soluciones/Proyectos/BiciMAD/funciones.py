def dist_estaciones(est1, est2, comunidad):
    """ Calcula la distancia entre 2 estaciones a partir de sus IDs
    y de la comunidad"""
    pareja_estaciones = [e for e in comunidad.estaciones if e.id in [est1, est2]]

    # Si encuentra 2 estaciones procede a realizar la comparacion
    if len(pareja_estaciones) == 2:
        d = pareja_estaciones[0].distancia(pareja_estaciones[1].longitude, pareja_estaciones[1].latitude)
    else:
        d = 0
    return d
