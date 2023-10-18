from main import crear_alumno
from arbol import *
from lista import *
from alumno import *
from cola import *

import time
import random


def generar_arbol(lista, arbol,numero_prueba):
    for i in range(numero_prueba):
        alumno = index(lista, i)
        arbol = insertarNodo(arbol, alumno)
    return arbol


def generar_buscados(lista, numero_prueba):
    buscados = []
    for _ in range(10):
        num = random.randint(0, numero_prueba)
        buscados.append(index(lista,num-1).nombre)
    return buscados


def main():
    # buscar 10 personas posibles y tomar el tiempo en cada una
    # repeir el tiempo
    numero_prueba = 3000
    lista = Lista()
    arbol = None
    time_lista = []
    time_arbol = []

    for _ in range(numero_prueba):
        alumno = crear_alumno()
        insertar(lista, alumno)

    arbol = generar_arbol(lista, arbol,numero_prueba)

    for _ in range(10):
        buscados = generar_buscados(lista, numero_prueba)

        for i in buscados:
            inicio = time.time()
            existe_alumno(lista, i)
            fin = time.time()
            time_lista.append(fin-inicio)

            inicio = time.time()
            prueba_busqueda_arbol(arbol, i)
            fin = time.time()
            time_arbol.append(fin-inicio)
    
    suma = 0
    for i in time_lista:
        suma += i
    promedio_lista = suma/len(time_lista)

    suma = 0
    for i in time_arbol:
        suma += i
    promedio_arbol = suma/len(time_arbol)

    print(promedio_lista)
    print(promedio_arbol)



main()
