"""
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
from DISClib.DataStructures import mapentry as me

def printArtistsByBegindate(total, initialYear, finalYear):
    tamaño = int(lt.size(total))
    t = tamaño - 3
    print("--------------------------------------------------------")
    print("Hay " + str(tamaño) + " artistas nacidos entre " + str(initialYear) + " y " + str(finalYear))
    print("--------------------------------------------------------")
    if t > 0:
        
        if tamaño > 3 and tamaño < 7:
            for n in lt.iterator(total):
                
                print("Nombre del artista: " + str(n["DisplayName"]) +"\n"
                + " Año de nacimiento del artista: " + str(n["BeginDate"]) +"\n"
                + " Año de fallecimiento del artista: " + str(n["EndDate"]) +"\n"
                + " Nacionalidad: " + str(n["Nationality"]) +"\n"
                + " Género: " + str(n["Gender"]))
                print("--------------------------------------------------------")
        else:
            m= 0
            for n in lt.iterator(total): 
                m= m + 1
                print("Nombre del artista: " + str(n["DisplayName"]) +"\n"
                + " Año de nacimiento del artista: " + str(n["BeginDate"]) +"\n"
                + " Año de fallecimiento del artista: " + str(n["EndDate"]) +"\n"
                + " Nacionalidad: " + str(n["Nationality"]) +"\n"
                + " Género: " + str(n["Gender"]))
                print("--------------------------------------------------------")
                if m==3:
                    break

            letra= 1
            for n in lt.iterator(total): 
                if letra > (tamaño - 3):
                    print("Nombre del artista: " + str(n["DisplayName"]) +"\n"
                    + " Año de nacimiento del artista: " + str(n["BeginDate"]) +"\n"
                    + " Año de fallecimiento del artista: " + str(n["EndDate"]) +"\n"
                    + " Nacionalidad: " + str(n["Nationality"]) +"\n"
                    + " Género: " + str(n["Gender"]))
                    print("--------------------------------------------------------")
                
                    if letra==tamaño:
                        break
                letra= letra + 1   
    else:
        if tamaño>0:
            for n in lt.iterator(total):
                print("\n")
                print("Nombre del artista: " + str(n["DisplayName"]) +"\n"
                + " Año de nacimiento del artista: " + str(n["BeginDate"]) +"\n"
                + " Año de fallecimiento del artista: " + str(n["EndDate"]) +"\n"
                + " Nacionalidad: " + str(n["Nationality"]) +"\n"
                + " Género: " + str(n["Gender"]))
                print("--------------------------------------------------------")
        else:
            print("No hay muestra")

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Catálogo.")
    print("2- Cargar información en el catálogo.")
    print("3- Consultar y listar cronológicamente los artistas que nacieron en un rango de años.")
    print("0- Salir.")
    print("*******************************************")

# Menu principal
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.initCatalog()
   
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont)
        print('Obras de arte cargadas: ' + str(controller.artworksSize(cont)))
        print('Artistas cargados: ' + str(controller.artistsSize(cont)))

    elif int(inputs[0]) == 3:
        print("\nBuscando y listando cronológicamente los artistas que nacieron en un rango de años: ")
        initialYear = input("Fecha Inicial (YYYY): ")
        finalYear = input("Fecha Final (YYYY): ")
        total = controller.getArtistsByRange(cont, int(initialYear), int(finalYear))
        printArtistsByBegindate(total, int(initialYear), int(finalYear))
        
    else:
        sys.exit(0)
sys.exit(0) 


