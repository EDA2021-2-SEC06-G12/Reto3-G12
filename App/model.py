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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.bstnode import getValue
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
    
    catalog['time'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    
    catalog['Latitud'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)

    catalog['Duration'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)

    return catalog

# CARGA DE DATOS AL CATÁLOGO
def addUFO(catalog, ufo):
    lt.addLast(catalog['UFO'], ufo)
    adddatetime(catalog['datetime'], ufo)
    addDuration(catalog['Duration'], ufo)
    addtime(catalog['time'], ufo)
    addLatitud(catalog['Latitud'], ufo)
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
    entry['City'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    entry['UFOS'] = lt.newList('SINGLE_LINKED', compareDates)

    return entry

def addAvistamiento(datentry, ufo):
    lst = datentry['UFOS']
    lt.addLast(lst, ufo)
    City = datentry['City']
    Citentry = om.get(City, ufo['city'])
    if (Citentry is None):
        entry = newCityEntry(ufo['city'], ufo)
        lt.addLast(entry['UFOS'], ufo)
        om.put(City, ufo['city'], entry)
    else:
        entry = me.getValue(Citentry)
        lt.addLast(entry['UFOS'], ufo)
    return datentry

def newCityEntry(offensegrp, crime):
    CTentry = {'City': None, 'UFOS': None}
    CTentry['City'] = offensegrp
    CTentry['UFOS'] = lt.newList('SINGLE_LINKED', compareCity)
    return CTentry

#Requerimiento 2
def addDuration(map, ufo):
    avistamiento = ufo['duration (seconds)']
    entry = om.get(map, float(avistamiento))
    if entry is None:
        datentry = newAvistamiento(ufo)
        om.put(map, float(avistamiento), datentry)
    else:
        datentry = me.getValue(entry)
    addAvistamiento(datentry, ufo)
    return map

#Requerimiento 3
def addtime(map, ufo):
    avistamiento = ufo['datetime']
    fecha_avistamiento = datetime.datetime.strptime(avistamiento, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, fecha_avistamiento.time())
    if entry is None:
        datentry = newAvist(ufo)
        om.put(map, fecha_avistamiento.time(), datentry)
    else:
        datentry = me.getValue(entry)
    addAvist(datentry, ufo)
    return map

def newAvist(ufo):
    entry = {'Date': None, 'UFOS': None}
    entry['Date'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    entry['UFOS'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def addAvist(datentry, ufo):
    lst = datentry['UFOS']
    lt.addLast(lst, ufo)
    avistamiento = ufo['datetime']
    fecha_avistamiento = datetime.datetime.strptime(avistamiento, '%Y-%m-%d %H:%M:%S')
    Date = datentry['Date']
    Datentry = om.get(Date, fecha_avistamiento.date())
    if (Datentry is None):
        entry = newDateEntry(fecha_avistamiento.date(), ufo)
        lt.addLast(entry['UFOS'], ufo)
        om.put(Date, fecha_avistamiento.date(), entry)
    else:
        entry = me.getValue(Datentry)
        lt.addLast(entry['UFOS'], ufo)
    return datentry

def newDateEntry(offensegrp, crime):
    DTentry = {'Date': None, 'UFOS': None}
    DTentry['Date'] = offensegrp
    DTentry['UFOS'] = lt.newList('SINGLE_LINKED', compareCity)
    return DTentry

#Requerimiento 5
def addLatitud(map, ufo):
    avistamiento = float(ufo['latitude'])
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

    entry = {'Long': None, 'UFOS': None}
    entry['Long'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareCity)
    entry['UFOS'] = lt.newList('SINGLE_LINKED', compareDates)

    return entry

def addAvistamientoL(datentry, ufo):
    lst = datentry['UFOS']
    lt.addLast(lst, ufo)
    City = datentry['Long']
    Citentry = mp.get(City, round(float(ufo['longitude']), 3))
    if (Citentry is None):
        entry = newLatEntry(round(float(ufo['longitude']), 3), ufo)
        lt.addLast(entry['UFOS'], ufo)
        mp.put(City, round(float(ufo['longitude']), 3), entry)
    else:
        entry = me.getValue(Citentry)
        lt.addLast(entry['UFOS'], ufo)
    return datentry

def newLatEntry(offensegrp, crime):
    CTentry = {'Long': None, 'UFOS': None}
    CTentry['Long'] = offensegrp
    CTentry['UFOS'] = lt.newList('SINGLE_LINKED', compareCity)
    return CTentry

# REQUERIMIENTO 1 (CONTAR LOS AVISTAMIENTOS EN UNA CIUDAD)
def AvistamientosCiudad(ciudad, catalog):
    datos = lt.newList('ARRAY_LIST')   #O(1)
    cuantos = 0            #O(1)
    valores = om.keySet(catalog['datetime']) #O(n)
    for i in lt.iterator(valores):     #O(n)
        fecha = om.get(catalog['datetime'], i) #O(nlogn)
        mapcity = me.getValue(fecha)['City'] #O(1)
        city = om.get(mapcity, ciudad)#O(nlogn)
        if city is not None:  #O(1)
            avist = me.getValue(city)['UFOS'] #O(1)
            avistamientos = lt.size(avist) #O(1)
            cuantos += avistamientos    #O(1)
            data = avist['first']['info']  #O(1)
            lt.addLast(datos, data)  #O(1)
    
    primeros_3 = lt.subList(datos, 1, 3)  #O(1)
    ultimos_3 = lt.subList(datos, lt.size(datos) - 2, 3)  #O(1)
    
    return cuantos, primeros_3['elements'], ultimos_3['elements']

# REQUERIMIENTO 2 (CONTAR LOS AVISTAMIENTOS POR DURACIÓN)
def avistamientosRangosec(S_min, S_max, catalog):
    maxima_d = om.maxKey(catalog['Duration']) #O(1)
    datos = lt.newList('ARRAY_LIST') #O(1)
    rango = om.values(catalog['Duration'], float(S_min), float(S_max)) #O(n)
    for i in lt.iterator(rango):#O(n)
        valores = om.valueSet(i['City']) #O(n)
        for j in lt.iterator(valores): #O(n)
            for data in lt.iterator(j['UFOS']):#O(n)
                lt.addLast(datos, data)#O(1)
    
    cuantos = lt.size(datos) #O(1)

    primeros_3 = lt.subList(datos, 1, 3) #O(1)
    ultimos_3 = lt.subList(datos, lt.size(datos) - 2, 3) #O(1)

    return cuantos, primeros_3['elements'], ultimos_3['elements'], maxima_d

# REQUERIMIENTO 3 (CONTAR LOS AVISTAMIENTOS POR HORA/MINUTOS DEL DÍA)
def AvistamientosPorHora(H_I, H_FN, catalog):
    maxima_h = om.maxKey(catalog['time']) #O(1)
    H_I = datetime.datetime.strptime(H_I, '%H:%M:%S') #O(1)
    H_FN = datetime.datetime.strptime(H_FN, '%H:%M:%S') #O(1)
    datos = lt.newList('ARRAY_LIST') #O(1)
    rango = om.values(catalog['time'], H_I.time(), H_FN.time()) #O(n)
    for i in lt.iterator(rango): #O(n)
        valores = om.valueSet(i['Date']) #O(n)
        for j in lt.iterator(valores): #O(n)
            for data in lt.iterator(j['UFOS']): #O(n)
                lt.addLast(datos, data) #O(1)

    cuantos = lt.size(datos) #O(1)

    primeros_3 = lt.subList(datos, 1, 3) #O(1)
    ultimos_3 = lt.subList(datos, lt.size(datos) - 2, 3) #O(1)

    return cuantos, primeros_3['elements'], ultimos_3['elements'], maxima_h

# REQUERIMIENTO 4 (CONTAR LOS AVISTAMIENTOS EN UN RANGO DE FECHAS)
def AvistamientosRangoFechas(F_I, F_FN, catalog):
    F_I = datetime.datetime.strptime(F_I, '%Y-%m-%d') #O(1)
    F_FN = datetime.datetime.strptime(F_FN, '%Y-%m-%d') #O(1)
    datos = lt.newList('ARRAY_LIST') #O(1)
    cuantos = 0 #O(1)
    rango = om.values(catalog['datetime'], F_I.date(), F_FN.date()) #O(n)
    for avistamiento in lt.iterator(rango): #O(n)
        avist = avistamiento['UFOS'] #O(1)
        data = avist['first']['info'] #O(1)
        lt.addLast(datos, data) #O(1)
        cuantos += lt.size(avistamiento['UFOS']) #O(1)
    
    primeros_3 = lt.subList(datos, 1, 3) #O(1)
    ultimos_3 = lt.subList(datos, lt.size(datos) - 2, 3) #O(1)

    return cuantos, primeros_3['elements'], ultimos_3['elements']

# REQUERIMIENTO 5 (CONTAR LOS AVISTAMIENTOS DE UNA ZONA GEOGRÁFICA)
def AvistamientosZona(L_I, L_FN, LT_I, LT_FN, catalog):
    datos = lt.newList('ARRAY_LIST') #O(1)
    rango = om.values(catalog['Latitud'], float(LT_I), float(LT_FN)) #O(n)
    for i in lt.iterator(rango): #O(n)
        Long = mp.keySet(i['Long']) #O(1)
        for j in lt.iterator(Long): #O(n)
            if j <= float(L_I) and j >= float(L_FN): #O(1)
                avista = mp.get(i['Long'], j) #O(1)
                avi = me.getValue(avista) #O(1)
                for data in lt.iterator(avi['UFOS']): #O(n)
                    lt.addLast(datos, data) #O(1)
    
    cuantos = lt.size(datos) #O(1)

    primeros_5 = lt.subList(datos, 1, 5) #O(1)
    ultimos_5 = lt.subList(datos, lt.size(datos) - 4, 5) #O(1)

    return cuantos, primeros_5['elements'], ultimos_5['elements'], primeros_5, ultimos_5

# REQUERIMIENTO 6 (VISUALIZAR LOS AVISTAMIENTOS DE UNA ZONA GEOGRÁFICA)
def AvistamientosGeo(L_I, L_FN, LT_I, LT_FN, catalog):
    avistamientos = AvistamientosZona(L_I, L_FN, LT_I, LT_FN, catalog) #O(1)
    primeros_5 = avistamientos[3] #O(1)
    ultimos_5 = avistamientos[4] #O(1)
    mapa = folium.Map()
    tooltip = '¡Click para ver las coordenadas!' #O(1)
    for i in lt.iterator(primeros_5): #O(n)
        coordenadas = ('latitud:', i['latitude']), ('longitud:', i['longitude']) #O(1)
        folium.Marker([i['latitude'], i['longitude']], tooltip=tooltip,
                        popup=coordenadas).add_to(mapa)
    for j in lt.iterator(ultimos_5): #O(n)
        coordenadas = ('latitud:', j['latitude']), ('longitud:', j['longitude']) #O(1)
        folium.Marker([j['latitude'], j['longitude']], tooltip=tooltip,
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
    