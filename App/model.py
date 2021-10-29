﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import folium
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# INICIALIZACIÓN DE CATÁLOGO
# Catálogo Vacío
def newCatalog():
    catalog = {'UFO': None,
                'datetime': None,
                'Longitud': None}

    catalog['UFO'] = lt.newList('SINGLE_LINKED')
    catalog['datetime'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    
    catalog['Longitud'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)

    return catalog

# CARGA DE DATOS AL CATÁLOGO
def addUFO(catalog, ufo):
    lt.addLast(catalog['UFO'], ufo)
    adddatetime(catalog['datetime'], ufo)
    addLongitud(catalog['Longitud'], ufo)
    
    return catalog

def adddatetime(map, ufo):
    avistamiento = ufo['datetime']
    fecha_avistamiento = datetime.datetime.strptime(avistamiento, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, fecha_avistamiento.date())
    if entry is None:
        datentry = newAvistamiento(ufo)
        om.put(map, fecha_avistamiento.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addAvistamiento(datentry, ufo)

    return map

def newAvistamiento(ufo):

    entry = {'City': None, 'UFOS': None}
    entry['City'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareCity)
    entry['UFOS'] = lt.newList('SINGLE_LINKED', compareDates)

    return entry

def addAvistamiento(datentry, ufo):
    lst = datentry['UFOS']
    lt.addLast(lst, ufo)
    City = datentry['City']
    Citentry = mp.get(City, ufo['city'])
    if (Citentry is None):
        entry = newCityEntry(ufo['city'], ufo)
        lt.addLast(entry['UFOS'], ufo)
        mp.put(City, ufo['city'], entry)
    else:
        entry = me.getValue(Citentry)
        lt.addLast(entry['UFOS'], ufo)
    return datentry

def newCityEntry(offensegrp, crime):
    CTentry = {'City': None, 'UFOS': None}
    CTentry['City'] = offensegrp
    CTentry['UFOS'] = lt.newList('SINGLE_LINKED', compareCity)
    return CTentry

#Requerimiento 5
def addLongitud(map, ufo):
    avistamiento = float(ufo['longitude'])
    avistamiento = round(avistamiento, 3)
    entry = om.get(map, avistamiento)
    if entry is None:
        datentry = newAvistamientoL(ufo)
        om.put(map, avistamiento, datentry)
    else:
        datentry = me.getValue(entry)
    addAvistamientoL(datentry, ufo)
    return map

def newAvistamientoL(ufo):

    entry = {'Lat': None, 'UFOS': None}
    entry['Lat'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareCity)
    entry['UFOS'] = lt.newList('SINGLE_LINKED', compareDates)

    return entry

def addAvistamientoL(datentry, ufo):
    lst = datentry['UFOS']
    lt.addLast(lst, ufo)
    City = datentry['Lat']
    Citentry = mp.get(City, round(float(ufo['latitude']), 3))
    if (Citentry is None):
        entry = newLatEntry(round(float(ufo['latitude']), 3), ufo)
        lt.addLast(entry['UFOS'], ufo)
        mp.put(City, round(float(ufo['latitude']), 3), entry)
    else:
        entry = me.getValue(Citentry)
        lt.addLast(entry['UFOS'], ufo)
    return datentry

def newLatEntry(offensegrp, crime):
    CTentry = {'Lat': None, 'UFOS': None}
    CTentry['Lat'] = offensegrp
    CTentry['UFOS'] = lt.newList('SINGLE_LINKED', compareCity)
    return CTentry

# REQUERIMIENTO 1 (CONTAR LOS AVISTAMIENTOS EN UNA CIUDAD)
def AvistamientosCiudad(ciudad, catalog):
    datos = lt.newList('ARRAY_LIST')
    cuantos = 0
    valores = om.keySet(catalog['datetime'])
    for i in lt.iterator(valores):
        fecha = om.get(catalog['datetime'], i)
        if fecha['key'] is not None:
            mapcity = me.getValue(fecha)['City']
            city = mp.get(mapcity, ciudad)
            if city is not None:
                avist = me.getValue(city)['UFOS']
                avistamientos = mp.size(avist)
                cuantos += avistamientos
                data = avist['first']['info']
                lt.addLast(datos, data)
    
    primeros_3 = lt.subList(datos, 1, 3)
    ultimos_3 = lt.subList(datos, lt.size(datos) - 2, 3)
    
    return cuantos, primeros_3['elements'], ultimos_3['elements']

# REQUERIMIENTO 2 (CONTAR LOS AVISTAMIENTOS POR DURACIÓN)
def avistamientosRangosec(S_min, S_max, catalog):
    datos = lt.newList('ARRAY_LIST')
    valores = om.keySet(catalog['datetime'])
    for i in lt.iterator(valores):
        fecha = om.get(catalog['datetime'], i)
        if fecha['key'] is not None:
            mapcity = me.getValue(fecha)['City']
            city = mp.valueSet(mapcity)
            for j in lt.iterator(city):
                avist = j['UFOS']['first']['info']
                dur = avist['duration (seconds)']
                if float(dur) >= float(S_min) and float(dur) <= float(S_max):
                    data = avist
                    lt.addLast(datos, data)
    
    cuantos = lt.size(datos)

    primeros_3 = lt.subList(datos, 1, 3)
    ultimos_3 = lt.subList(datos, lt.size(datos) - 2, 3)

    return cuantos, primeros_3['elements'], ultimos_3['elements']

# REQUERIMIENTO 3 (CONTAR LOS AVISTAMIENTOS POR HORA/MINUTOS DEL DÍA)
def AvistamientosPorHora(H_I, H_FN, catalog):
    H_I = datetime.datetime.strptime(H_I, '%H:%M:%S')
    H_FN = datetime.datetime.strptime(H_FN, '%H:%M:%S')
    datos = lt.newList('ARRAY_LIST')
    valores = om.keySet(catalog['datetime'])
    for i in lt.iterator(valores):
        fecha = om.get(catalog['datetime'], i)
        if fecha['key'] is not None:
            mapcity = me.getValue(fecha)['City']
            city = mp.valueSet(mapcity)
            for j in lt.iterator(city):
                avist = j['UFOS']['first']['info']
                hora = datetime.datetime.strptime(avist['datetime'], '%Y-%m-%d %H:%M:%S')
                if hora.time() >= H_I.time() and hora.time() <= H_FN.time():
                    data = avist
                    lt.addLast(datos, data)
    
    cuantos = lt.size(datos)

    primeros_3 = lt.subList(datos, 1, 3)
    ultimos_3 = lt.subList(datos, lt.size(datos) - 2, 3)

    return cuantos, primeros_3['elements'], ultimos_3['elements']

# REQUERIMIENTO 4 (CONTAR LOS AVISTAMIENTOS EN UN RANGO DE FECHAS)
def AvistamientosRangoFechas(F_I, F_FN, catalog):
    F_I = datetime.datetime.strptime(F_I, '%Y-%m-%d')
    F_FN = datetime.datetime.strptime(F_FN, '%Y-%m-%d')
    datos = lt.newList('ARRAY_LIST')
    cuantos = 0
    rango = om.values(catalog['datetime'], F_I.date(), F_FN.date())
    for avistamiento in lt.iterator(rango):
        avist = avistamiento['UFOS']
        data = avist['first']['info']
        lt.addLast(datos, data)
        cuantos += lt.size(avistamiento['UFOS'])
    
    primeros_3 = lt.subList(datos, 1, 3)
    ultimos_3 = lt.subList(datos, lt.size(datos) - 2, 3)

    return cuantos, primeros_3['elements'], ultimos_3['elements']

# REQUERIMIENTO 5 (CONTAR LOS AVISTAMIENTOS DE UNA ZONA GEOGRÁFICA)
def AvistamientosZona(L_I, L_FN, LT_I, LT_FN, catalog):
    datos = lt.newList('ARRAY_LIST')
    valores = om.keySet(catalog['Longitud'])
    for i in lt.iterator(valores):
        if i <= float(L_I) and i >= float(L_FN):
            Long = om.get(catalog['Longitud'], i)
            if Long['key'] is not None:
                mapLat = me.getValue(Long)['Lat']
                Lat = mp.keySet(mapLat)
                for j in lt.iterator(Lat):
                    if j >= float(LT_I) and j <= float(LT_FN):
                        Lati = mp.get(mapLat, j)
                        Lati = me.getValue(Lati)
                        for data in lt.iterator(Lati['UFOS']):
                            lt.addLast(datos, data)
    
    cuantos = lt.size(datos)

    primeros_3 = lt.subList(datos, 1, 5)
    ultimos_3 = lt.subList(datos, lt.size(datos) - 4, 5)

    return cuantos, primeros_3['elements'], ultimos_3['elements'], datos

# REQUERIMIENTO 6 (VISUALIZAR LOS AVISTAMIENTOS DE UNA ZONA GEOGRÁFICA)
def AvistamientosGeo(L_I, L_FN, LT_I, LT_FN, catalog):
    avistamientos = AvistamientosZona(L_I, L_FN, LT_I, LT_FN, catalog)
    datos = avistamientos[3]
    mapa = folium.Map()
    tooltip = '¡Click para ver las coordenadas!'
    for i in lt.iterator(datos):
        coordenadas = ('latitud:', i['latitude']), ('longitud:', i['longitude'])
        folium.Marker([i['latitude'], i['longitude']], tooltip=tooltip,
                        popup=coordenadas).add_to(mapa)
    mapa.save('Avistamientos en la zona.html')


# FUNCIONES DE COMPARACIÓN
def compareDates(date1, date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareCity(City1, City2):
    City = me.getKey(City2)
    if (City1 == City):
        return 0
    elif (City1 > City):
        return 1
    else:
        return -1

# FUNCIONES ADICIONALES
def AvistamientosSize(catalog):
    return lt.size(catalog['UFO'])

def indexHeight(catalog):
    return om.height(catalog['datetime'])

def indexSize(catalog):
    return om.size(catalog['datetime'])
    