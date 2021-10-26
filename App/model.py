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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
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
                'datetime': None
                }

    catalog['UFO'] = lt.newList('SINGLE_LINKED')
    catalog['datetime'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    return catalog

# CARGA DE DATOS AL CATÁLOGO
def addUFO(catalog, ufo):
    lt.addLast(catalog['UFO'], ufo)
    adddatetime(catalog['datetime'], ufo)
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

# REQUERIMIENTO 1 (CONTAR LOS AVISTAMIENTOS EN UNA CIUDAD)
def AvistamientosCiudad(ciudad, catalog):
    valores = om.valueSet(catalog['datetime'])



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