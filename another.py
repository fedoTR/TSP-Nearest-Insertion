# Imports
from operator import contains, iadd, sub
import os.path
import pandas as pd
import numpy as np
from itertools import permutations
import random

# currentPath = pathlib.Path(__file__).parent.absolute()
def formatFile():
    askname_File = input('Filename?: ')
    file_exists = os.path.exists(askname_File)
    print(file_exists)

    if file_exists is True:
        currrent_Filename = askname_File
        print("Working with: ", currrent_Filename)
        pass
    else:
        print("File not exist!")
        exit()
    pass

    separator = ''

    if(currrent_Filename == '48nodes.txt' or currrent_Filename == '101nodes.txt'):
        separator = " "
    else:
        separator = "\t"
    pass

    # Create a pandas's Dataframe with the labels: node, x, y
    prematureDF = pd.read_csv(currrent_Filename, sep=separator,
                              names=["node", "x", "y"])

    # Print dataframe
    print("First Dataframe:\n", prematureDF, "\n")

    # Create new pandas's Dataframe
    # only keeps the columns x and y
    # and parse it into a CSV file
    keep_col = ['x', 'y']
    secondDF = prematureDF[keep_col]
    thirdDF = prematureDF[keep_col]
    secondDF.to_csv("5nodes.csv", index=False)

    # Create the first NumPy array with
    # the secondDF
    np.Array1 = secondDF.to_numpy()
    np.goodArray = thirdDF.to_numpy()

    # Print np.Array1
    print("np.Array1: \n", np.Array1, "\n")

    # Defining rows and columns
    # based on the shape of
    # no.Array1
    rows, columns = np.Array1.shape

    # Printing shape of np.Array1
    print("Shape of np.Array1: \n", np.Array1.shape, "\n")

    distancesRawList = []

    # Starts two bucles to calculate and print
    # the euclidean distances between
    # the points
    for x in range(rows):
        for y in range(rows):
            # Define a variable which is gonna
            # take the value of the current
            # euclidean distance
            rawFloat = np.linalg.norm((np.Array1[x]) - (np.Array1[y]))
            # Round it to 2 decimals: 0.00
            # in a list called: neatFloat
            neatFloat = round(rawFloat, 2)
            # Append each value in a list
            distancesRawList.append(neatFloat)
            pass
        pass
    print("\n")

    # Transforms into a list
    i = 0
    formatedList = []
    while i < len(distancesRawList):
        formatedList.append(distancesRawList[i:i + rows])
        i += rows

    # Transform list into a NumPy array and
    # print the array
    numpyDistances = np.array(formatedList)
    distancesDataframe = pd.DataFrame(numpyDistances)
    distancesDataframe.replace(0.0, np.NaN)
    nonzerodistancesDataframe = distancesDataframe.replace(0.0, np.NaN)
    return nonzerodistancesDataframe, rows



# Print the final distancesDataframe
# and the good NumPy Array
def printFormatted(nonzerodistancesDataframe, rows):
    print("Distances Dataframe:\n", nonzerodistancesDataframe, "\n")

# Imprime el dataframe sin 0's
nonzerodistancesDataframe, rows = formatFile()
printFormatted(nonzerodistancesDataframe, rows)

# Crea una lista de nodos disponibles
'''
Empieza con unos nodos disponibles, que son
en un principio los que existen. (Todos)
'''
nodos_disponibles = []
subTour = []

# Añade a la lista de nodos disponibles todos los nodos iniciales sin usar
for numbers in range(rows):
    nodos_disponibles.append(numbers)

print("Nodos disponibles:", nodos_disponibles)
print("Subtour actual: ", subTour)

# Pide ingresar el primer nodo
while True:
    nodo_i = int(input("Ingresa el nodo_i:\n"))
    if nodo_i > rows:
        print("Ingresa un nodo valido")
    else:
        subTour.append(nodo_i)
        nodo_final = nodo_i
        subTour.append(nodo_final)
        break


# FORMACIÓN DEL SUBTOUR INICIAL
# Se actualiza la lista de nodos disponibles
nodos_disponibles = [x for x in nodos_disponibles if x not in subTour]
print("Nodos disponibles: ", nodos_disponibles)
print("Se forma el subtour: ", subTour)
# Obtiene el menor de la fila del nodo_i
print(nonzerodistancesDataframe[nodo_i].min())
# Obtiene el índice del menor de la fila del nodo_i
print(nonzerodistancesDataframe[nodo_i].idxmin())
subTour.insert(1, (nonzerodistancesDataframe[nodo_i].idxmin()))
print("El subtour T: ", subTour)
nodos_disponibles = [x for x in nodos_disponibles if x not in subTour]
print("Nodos ahora disponibles: ", nodos_disponibles)

# HASTA AQUí LLEGA EL PASO 2

distanciasCandidatos = []

def obtenerDistancia(ciudad1, ciudad2):
    distancia = nonzerodistancesDataframe[ciudad1][ciudad2]
    print("Distancia entre:", ciudad1, "y", ciudad2, "es ", distancia)
    return distancia, ciudad1, ciudad2

def deltaF(i, j, k):
    deltaF = nonzerodistancesDataframe[i][k] + nonzerodistancesDataframe[k][j] - nonzerodistancesDataframe[i][j]
    return deltaF

# Declaramos la función que itera para obtener las distancias de los nodos candidatos y nodo_k
def iterater():
    global tempminimo
    global nodo_k
    for candidatos in nodos_disponibles:
        for nodossubtour in subTour[:-1]:
            if(tempminimo == 0):
                tempminimo = obtenerDistancia(candidatos, nodossubtour)
                nodo_k = candidatos
            else:
                if(obtenerDistancia(candidatos, nodossubtour) < tempminimo):
                    tempminimo = obtenerDistancia(candidatos, nodossubtour)
                    nodo_k = candidatos
    print("Nodo k:", nodo_k)
    print("Minimo: ", tempminimo)
    return nodo_k

# Declaración de función para ir insertando los nodos
def insertandonodos():
    global minDelta
    global nodos_disponibles
    print(nodo_k)
    tempsubTour = subTour.copy()
    for lacaca in range(len(subTour)-1):
        tempsubTour.insert(lacaca+1, nodo_k)
        print(tempsubTour)
        index_nodo_k = tempsubTour.index(nodo_k)
        # Necesitamos los valores de i y j para saber entre cuáles nodos insertar el nodo_k
        i = tempsubTour[index_nodo_k-1]
        j = tempsubTour[index_nodo_k+1]
        # Obtenemos el valor de deltaF
        deltaF(i, j, nodo_k)
        # Necesitamos volver a crear el tempsubTour para no sobreescribir el mismo
        tempsubTour = subTour.copy()
        if(minDelta == 0):
            minDelta = deltaF(i, j, nodo_k)
        else:
            if(deltaF(i, j, nodo_k) < minDelta):
                minDelta = deltaF(i, j, nodo_k)
    subTour.insert(index_nodo_k, nodo_k)
    nodos_disponibles = [x for x in nodos_disponibles if x not in subTour]
    print(tempsubTour)
    print(nodos_disponibles)
    return nodos_disponibles, tempsubTour, i, j, deltaF, minDelta


# Declaración de función main
def main():
    totalCost = 0
    i = 0
    global tempminimo
    global nodo_k
    global minDelta
    while(i < rows):
        tempminimo = 0
        nodo_k = 0
        minDelta = 0
        iterater()
        insertandonodos()
        print(subTour)
        i = i + 1
        if len(nodos_disponibles) == 0:
            print("Tour final:", subTour)
            for item in range(len(subTour) - 1):
                totalCost += nonzerodistancesDataframe[subTour[item]][subTour[item+1]]
            break
        pass
    print("Costo total:", totalCost)
    pass

# Función main
if __name__ == "__main__":
    main()