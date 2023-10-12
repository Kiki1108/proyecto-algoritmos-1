from lista import *
from alumno import Alumno
from cola import *

import random
import json

with open("texto.json", encoding="utf8") as archivo:
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
        nota = input("Nota: ")
        try:
            nota = int(nota)
            if nota >= 10 and nota <= 70:
                break
        except:
            pass

    cambiar_nota(lista= lista, indice=indice, nombre=None, nota=nota)


def insert_nota_nombre(lista):
    while True:
        nombre = input("Nombre: ")
        if existe_alumno(lista, nombre):
            break

    while True:
        nota = input("Nota: ")
        try:
            nota = int(nota)
            if nota >= 10 and nota <= 70:
                break
        except:
            pass
    
    cambiar_nota(lista= lista, indice=None, nombre=nombre, nota=nota)


def eliminar_indice(lista):
    while True:
        indice = input("Indice: ")
        try:
            indice = int(indice)
            if indice >= 0 and indice < tamanio(lista):
                break
        except:
            pass
    eliminar_alumno(lista=lista, nombre=None, indice=indice)


def eliminar_nombre(lista):
    while True:
        nombre = input("Nombre: ")
        if existe_alumno(lista, nombre):
            break
    eliminar_alumno(lista=lista, nombre=nombre, indice=None)

def aleatorio(lista):
    lista_aleatorio = []
    while len(lista_aleatorio) != 100:
        var = random.randint(0,tamanio(lista))
        if var in lista_aleatorio:
            continue
        else:
            lista_aleatorio.append(var)
    return lista_aleatorio

        
def cola_prioridad(cola, alumno):
    lista_aleatorio = aleatorio(lista)
    for i in range(100):
        ayuda = lista_aleatorio[i]
        alumno = index(lista, ayuda)
        arribo(cola, alumno.nombre, alumno.promedio)
    return cola

def espera_index():
    while True:
        print("Ingrese un valor entero:")
        index = input()
        try:
            temp = int(eval(str(index)))
            if type(temp) == int:
                return temp
        except:
            continue

def nombre_busqueda():
    busqueda = input()
    return busqueda.strip()

if __name__ == "__main__":
    lista = Lista()
    cola = Cola()


    for i in range(1000):
        alumno = crear_alumno()
        insertar(lista, alumno)
    
    while True:
        print("1: Insertar alumno")
        print("2: Insertar nota a indice")
        print("3: Insertar nota a nombre")
        print("4: Agregar nota a todos (nota random a todos)")
        print("5: Eliminar alumno por indice")
        print("6: Eliminar alumno por nombre")
        print("7: Eliminar nota a indice")
        print("8: Eliminar nota a nombre")
        print("9: Formar la cola con prioridad")
        print("10: Tiempo de espera por índice")
        print("11: Tiempo de espera por nombre")
        print("12: imprimir cola")


        print("13: Imprimir a todos")
        print("0: Salir")

        opcion = input()

        match opcion:
            case "1" : insertar_alumno(lista)
            case "2" : insert_nota_indice(lista)
            case "3" : insert_nota_nombre(lista)
            case "4" : add_nota_random(lista)
            case "5" : eliminar_indice(lista)
            case "6" : eliminar_nombre(lista)
            case "7" : eliminar_nota_indice(lista)
            case "8" : eliminar_nota_nombre(lista)
            case "9" : cola_prioridad(cola, alumno)
            case "10" : atencion_index(cola, espera_index())
            case "11" : atencion_nombre(cola, nombre_busqueda())
            case "12" : imprimir(cola)

            case "13" : imprimir_info(lista)
            case _ : break


