from lista import *
from alumno import Alumno
#from cola import *

import random
import json

with open("texto.json", encoding="uft8") as archivo:
    datos_nombres = json.load(archivo)

nombres = datos_nombres["nombres"]
apellidos = datos_nombres["apellidos"]


def crear_alumno():
    nombre = random.choice(nombres) + " " + random.choice(apellidos)
    nota = random.randint(10, 70)
    alumno = Alumno(nombre, nota)
    return alumno


def insertar_alumno(lista):
    nombre = input("Nombre: ")
    while True:
        promedio = input("Promedio: ")
        try:
            promedio = int(promedio)
            if promedio >= 10 and promedio <= 70:
                break
        except:
            pass

    alumno = Alumno(nombre, promedio)
    insertar(lista, alumno)


def insert_nota_indice(lista):
    while True:
        indice = input("Indice: ")
        try:
            indice = int(indice)
            if indice >= 0 and indice < tamanio(lista):
                break
        except:
            pass
    
    while True:
        nota = input("nota: ")
        try:
            nota = int(nota)
            if nota >= 10 and nota <= 70:
                break
        except:
            pass

    cambiar_nota(lista= lista, indice=indice, nombre=None, nota=nota)
    




if __name__ == "__main__":
    lista = Lista()

    for i in range(1000):
        alumno = crear_alumno()
        insertar(lista, alumno)
    
    while True:
        print("1: Insertar alumno")
        print("2: Insertar nota a indice")
        print("3: Insertar nota a nombre")
        print("4: Agregar nota a todos (nota random a todos)")


        print("9: Imprimir a todos")
        print("0: Salir")

        opcion = input()

        match opcion:
            case "1" : insertar_alumno(lista)
            case "2" : insert_nota_indice(lista)

            case "9" : imprimir_info(lista)
            case _ : break


