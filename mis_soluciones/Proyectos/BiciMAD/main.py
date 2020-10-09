from classes import *
from funciones import *

import pandas as pd

df = pd.read_excel("2018_Julio_Bases_Bicimad_EMT.xlsx")


tot_est = []
for index, row in df.iterrows():
    estacion = Estacion(row[0], row[3], row[1], row[6], row[4], row[5])
    tot_est.append(estacion)

comunidad = ComunidadMadrid(tot_est)
while True:
    print('''
    Escoge una opcion:
        1. Busca estacion (nombre)
        2. Calcula distancia (entre ids)
        3. Salir del programa''')
    try:
        opcion_seleccionada = int(input())
    except ValueError:
        print('Error. Introduzca un numero')
        continue

    if opcion_seleccionada == 3:
        break
    elif opcion_seleccionada == 1:
        estacion = input('Nombre de la estacion:')
        tipo_busqueda = 'name'
        resultado = comunidad.busca_estacion(estacion, tipo_busqueda)
        if resultado:
            print(resultado.name)
            print('Que mas deseas hacer?')
        else:
            print('No encontre la estacion')
    elif opcion_seleccionada == 2:
        try:
            id1 = int(input('Introduzca el id de la primera estacion: '))
            id2 = int(input('Introduzca el id de la segunda estacion: '))
            print(dist_estaciones(id1, id2, comunidad))
        except ValueError:
            print('Error. Introduzca un numero')
            continue

    else:
        print('Respuesta no valida')

comunidad2 = ComunidadMadrid(tot_est)
