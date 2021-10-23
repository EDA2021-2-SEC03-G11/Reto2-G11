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
assert cf
def newCatalog():
    catalog = {'artworks': None,
               'artists': None,
               "artistIds": None,
               "years": None,
               "artworkIds":None}
    catalog['artworks'] = lt.newList('SINGLE_LINKED', compareArtworkIds)
    catalog['artists'] = lt.newList('SINGLE_LINKED', compareArtistIds)

    catalog["artistIds"]= mp.newMap(15300, 
                            maptype= "PROBING", 
                            loadfactor= 0.5, 
                            comparefunction= compareMapArtistIds)
    
    catalog["years"]= mp.newMap(300000, 
                            maptype= "PROBING", 
                            loadfactor= 0.5, 
                            comparefunction= compareMapYear)
    
    catalog["artworkIds"]= mp.newMap(138500, 
                            maptype= "PROBING", 
                            loadfactor= 0.5, 
                            comparefunction= compareMapArtworkIds)

    return catalog

def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)
    mp.put(catalog['artistIds'], artist['ConstituentID'], artist)
    addArtistYear(catalog, artist)


def addArtistYear(catalog, artist):
    try:
        years = catalog['years']
        if (artist['BeginDate'] != ''):
            pubyear = artist['BeginDate']
            pubyear = int(float(pubyear))
        else:
            pubyear = 0
        existyear = mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            year = me.getValue(entry)
        else:
            year = newYear(pubyear)
            mp.put(years, pubyear, year)
        lt.addLast(year['artists'], artist)
    
    except Exception:
        return None

def newYear(pubyear):
    entry = {'year': "", "artists": None}
    entry['year'] = pubyear
    entry['artists'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry

def getArtistsByRange(catalog, initialYear, finalYear):
    ch= initialYear
    ListadeAños= lt.newList('SINGLE_LINKED')
    while ch <= finalYear:
        year = mp.get(catalog['years'], ch)
        if year:
            r= me.getValue(year)['artists']
            for cosa in lt.iterator(r):
                lt.addLast(ListadeAños, cosa)
        ch= ch + 1
    return (ListadeAños)

def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    mp.put(catalog['artworkIds'], artwork['ObjectID'], artwork)
    
def artworksSize(catalog):
    return lt.size(catalog['artworks'])

def artistsSize(catalog):
    return lt.size(catalog['artists'])
# ==============================
# Funciones de Comparacion
# ==============================
def compareArtworkIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareArtistIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapArtistIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0

def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0

def compareMapArtworkIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1