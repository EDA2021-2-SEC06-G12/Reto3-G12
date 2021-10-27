"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# INICIALIZACIÓN DEL CATÁLOGO
def initCatalog():
    catalog = model.newCatalog()
    return catalog

# CARGA DE DATOS AL CATÁLOGO
def loadData(catalog):
    loadUFOS(catalog)

def loadUFOS(catalog):
    ufosfile = cf.data_dir + 'UFOS/UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(ufosfile,encoding='utf-8'))
    for ufo in input_file:
        model.addUFO(catalog, ufo)

# REQUERIMIENTO 1 (CONTAR LOS AVISTAMIENTOS EN UNA CIUDAD)
def AvistamientosCiudad(ciudad, catalog):
    Algoritmo = model.AvistamientosCiudad(ciudad, catalog)
    return Algoritmo

# REQUERIMIENTO 2 (CONTAR LOS AVISTAMIENTOS POR DURACIÓN)
def avistamientosRangosec(S_min,S_max, catalog):
    Algoritmo = model.avistamientosRangosec(S_min,S_max, catalog)
    return Algoritmo

# REQUERIMIENTO 3 (CONTAR LOS AVISTAMIENTOS POR HORA/MINUTOS DEL DÍA)
def AvistamientosPorHora(H_I, H_FN, catalog):
    Algoritmo = model.AvistamientosPorHora(H_I, H_FN, catalog)
    return Algoritmo

# REQUERIMIENTO 4 (CONTAR LOS AVISTAMIENTOS EN UN RANGO DE FECHAS)
def AvistamientosRangoFechas(F_I, F_FN, catalog):
    Algoritmo = model.AvistamientosRangoFechas(F_I, F_FN, catalog)
    return Algoritmo

# REQUERIMIENTO 5 (CONTAR LOS AVISTAMIENTOS DE UNA ZONA GEOGRÁFICA)
def AvistamientosZona(L_I, L_FN, LT_I, LT_FN, catalog):
    Algoritmo = model.AvistamientosZona(L_I, L_FN, LT_I, LT_FN, catalog)
    return Algoritmo

# FUNCIONES ADICIONALES
def AvistamientosSize(catalog):
    return model.AvistamientosSize(catalog)

def indexHeight(catalog):
    return model.indexHeight(catalog)

def indexSize(catalog):
    return model.indexSize(catalog)
