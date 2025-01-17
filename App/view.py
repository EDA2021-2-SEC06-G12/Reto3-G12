﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Contar los avistamientos en una ciudad")
    print("4- Contar los avistamientos por duración")
    print("5- Contar avistamientos por Hora/Minutos del día")
    print("6- Contar los avistamientos en un rango de fechas")
    print("7- Contar los avistamientos de una Zona Geográfica")
    print("8- Visualizar los avistamientos de una zona geográfica")
    print("0- Salir del Menu")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....\n")
        cont = controller.initCatalog()
        print("Catálogo Inicializado\n")

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....\n")
        controller.loadData(cont)
        print("Avistamientos cargados:", str(controller.AvistamientosSize(cont)), "\n")
        print("Altura del arbol:", str(controller.indexHeight(cont)), "\n")
        print("Elementos en el arbol:", str(controller.indexSize(cont)), "\n")
    
    elif int(inputs[0]) == 3:
        ciudad = input('Ingrese la ciudad a consultar: ')#las vegas
        Algoritmo = controller.AvistamientosCiudad(ciudad, cont)
        print("\nEn la ciudad de", ciudad + ",", "hay un total de", Algoritmo[0], "avistamientos.\n")
        print("Los primeros 3 avistamientos en", ciudad, "son:\n", Algoritmo[1])
        print("\nLos últimos 3 avistamientos en", ciudad, "son:\n", Algoritmo[2], "\n")
    
    elif int(inputs[0]) == 4:#INDIVIDUAL 1
        S_min=input('Ingresa los segundos minimos: ') #30.0
        S_max= input('Ingresa los segundos mayores: ') #150.0
        Algoritmo = controller.avistamientosRangosec(S_min,S_max, cont)
        print("\nDentro de la base de datos, la duración más tardía registrada es:", Algoritmo[3], "\n")
        print("Dentro del rango especificado, hay un total de", Algoritmo[0], "avistamientos.\n")
        print("Los primeros 3 avistamientos son:\n", Algoritmo[1])
        print("\nLos últimos 3 avistamientos son:\n", Algoritmo[2], "\n")
    
    elif int(inputs[0]) == 5:#INDIVIDUAL 2
        H_I = input('Ingresa la hora inicial (HH:MM): ')#20:45
        H_I = H_I + ':00'
        H_FN = input('Ingresa la hora final (HH:MM): ')#23:15
        H_FN = H_FN + ':00'
        Algoritmo = controller.AvistamientosPorHora(H_I, H_FN, cont)
        print("\nDentro de la base de datos, la hora más tardía registrada es:", Algoritmo[3], "\n")
        print("Dentro del rango especificado, hay un total de", Algoritmo[0], "avistamientos.\n")
        print("Los primeros 3 avistamientos son:\n", Algoritmo[1])
        print("\nLos últimos 3 avistamientos son:\n", Algoritmo[2], "\n")
    
    elif int(inputs[0]) == 6:
        F_I = input('Ingresa la fecha inicial (AAAA-MM-DD): ')#1945-08-06
        F_FN = input('Ingresa la fecha final (AAAA-MM-DD): ')#1984-11-15
        Algoritmo = controller.AvistamientosRangoFechas(F_I, F_FN, cont)
        print("\nDentro del rango especificado, hay un total de", Algoritmo[0], "avistamientos.\n")
        print("Los primeros 3 avistamientos son:\n", Algoritmo[1])
        print("\nLos últimos 3 avistamientos son:\n", Algoritmo[2], "\n")
    
    elif int(inputs[0]) == 7:
        L_I = input('Ingresa la longitud inicial: ')#-103.00
        L_FN = input('Ingresa la longitud final: ')#-109.05
        LT_I = input('Ingresa la latitud inicial: ')#31.33
        LT_FN = input('Ingresa la latitud final: ')#37.00
        Algoritmo = controller.AvistamientosZona(L_I, L_FN, LT_I, LT_FN, cont)
        print("\nDentro del rango especificado, hay un total de", Algoritmo[0], "avistamientos.\n")
        print("Los primeros 5 avistamientos son:\n", Algoritmo[1])
        print("\nLos últimos 5 avistamientos son:\n", Algoritmo[2], "\n")
    
    elif int(inputs[0]) == 8:
        L_I = input('Ingresa la longitud inicial: ')#-103.00
        L_FN = input('Ingresa la longitud final: ')#-109.05
        LT_I = input('Ingresa la latitud inicial: ')#31.33
        LT_FN = input('Ingresa la latitud final: ')#37.00
        Algoritmo = controller.AvistamientosGeo(L_I, L_FN, LT_I, LT_FN, cont)
        Algoritmo

    else:
        sys.exit(0)
sys.exit(0)
