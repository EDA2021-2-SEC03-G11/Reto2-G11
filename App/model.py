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
               'artists': None}
    catalog['artworks'] = lt.newList('SINGLE_LINKED', cmpfunction=compareartworksIds)
    catalog['artists'] = lt.newList('SINGLE_LINKED', cmpfunction=compareArtists)

    catalog["artist_work"]= mp.newMap(138500, maptype= "PROBING", loadfactor= 0.5, comparefunction= compareArtistsName)
    return catalog


# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)

def creatArtistWork(catalog):
    for artist in lt.iterator(catalog["artists"]):
        name= artist["DisplayName"]
        artistWork= lt.newList('SINGLE_LINKED', cmpfunction=compareartworksIds)
        for artwork in lt.iterator(catalog["artworks"]):
            if artist["ConstituentID"] in eval(artwork["ConstituentID"]):
                lt.addLast(artistWork, artwork)
        if not mp.contains(catalog["artist_work"], name):
            mp.put(catalog["artist_work"], name, artistWork)
        elif mp.contains(catalog["artist_work"], artist):
            mapWork = mp.get(catalog["artist_work"], artist)
            mapWork = me.getValue(mapWork)
            for work in lt.iterator(mapWork):
                lt.addLast(artistWork, work)
            mp.put(catalog["artist_work"], name, artistWork)


def addArtist2(catalog, artist):
    authors = catalog['authors']
    existauthor = mp.contains(authors, artist)
    if existauthor:
        entry = mp.get(authors, artist)
        author = me.getValue(entry)
    else:
        author = newAuthor(artist)
        mp.put(authors, artist, author)
    lt.addLast(author['artworks'], artwork)



# Funciones para creacion de datos
def newArtist(Ids, displayname, artistbio, nacionality, gender, begindate, enddate, wikiQID, ULAN ):
    artist = {'ConstituentID': Ids,
              "DisplayName": displayname,
              "ArtistBio": artistbio, 
              "Nationality": nacionality, 
              "Gender": gender,
              "BeginDate": begindate,
              "EndDate": enddate,
              "Wiki QID": wikiQID,
              "ULAN": ULAN}
    return artist
    
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

def compareArtists(artist1, artist2):
    if (artist1["ConstituentID"] == artist2["ConstituentID"]):
        return 0
    elif artist1["ConstituentID"] > artist2["ConstituentID"]:
        return 1
    else:
        return -1

def compareArtistsName(artist1, artist2):
    if str(artist1["DisplayName"]) == str(artist2["DisplayName"]):
        return 0
    elif str(artist1["DisplayName"]) > str(artist2["DisplayName"]):
        return 1
    else:
        return -1

# Funciones de ordenamiento
