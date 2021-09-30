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



# Construccion de modelos
def newCatalog():
    catalog = {'artworks': None,
               'mediums': None,
               'artworkIds': None,
               "years": None}
    catalog['artworks'] = lt.newList('SINGLE_LINKED', compareartworksIds)

    catalog['mediums'] = mp.newMap(138500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareMediumNames)
    
    catalog['artworkIds'] = mp.newMap(138500,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapartworkIds) 





# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    mp.put(catalog['artworkIds'], artwork['ObjectID'], artwork)
    artists = artwork['artists'].split(",")  # Se obtienen los autores
    for artist in artists:
        addArtist(catalog, artist.strip(), artwork)
    addBookYear(catalog, artwork)   

def addArtist(catalog, artistname, artwork):
    authors = catalog['authors']
    existauthor = mp.contains(authors, artistname)
    if existauthor:
        entry = mp.get(authors, artistname)
        author = me.getValue(entry)
    else:
        author = newAuthor(artistname)
        mp.put(authors, artistname, author)
    lt.addLast(author['artworks'], artwork)
    
def addBookYear(catalog, artwork):
    try:
        years = catalog['years']
        if (artwork['Date'] != ''):
            pubyear = artwork['Date']
            pubyear = int(float(pubyear))
        else:
            pubyear = 2020
        existyear = mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            year = me.getValue(entry)
        else:
            year = newYear(pubyear)
            mp.put(years, pubyear, year)
        lt.addLast(year['artworks'], artwork)
    except Exception:
        return None



# Funciones para creacion de datos
def newAuthor(name):
    author = {'name': "",
              "artists": None}
    author['name'] = name
    author['artists'] = lt.newList('SINGLE_LINKED', compareAuthorsByName)
    return author

def newYear(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "books": None}
    entry['year'] = pubyear
    entry['books'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry
    
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareartworksIds(id1, id2):
    """
    Compara dos ids de dos obras de arte
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMediumNames(name, medium):
    mediumentry = me.getKey(medium)
    if (name == mediumentry):
        return 0
    elif (name > mediumentry):
        return 1
    else:
        return -1

def compareMapartworkIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1


def compareAuthorsByName(keyname, author):
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

# Funciones de ordenamiento
