from lista import *
from alumno import Alumno
from cola import *
from arbol import *

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


def eliminar_nota_indice_main(lista):
    while True:
        indice = input("Indice: ")
        try:
            indice = int(indice)
            if indice >= 0 and indice < tamanio(lista):
                break
        except:
            pass

    while True:
        nota = input("Nota a eliminar: ")
        try:
            nota = int(nota)
            if nota >= 10 and nota <= 70:
                break
        except:
            pass
    eliminar_nota_indice(lista, indice, nota)


def eliminar_nota_nombre_main(lista):
    while True:
        nombre = input("Nombre: ")
        if existe_alumno(lista, nombre):
            break
    while True:
        nota = input("Nota a eliminar: ")
        try:
            nota = int(nota)
            if nota >= 10 and nota <= 70:
                break
        except:
            pass
    eliminar_nota_nombre(lista, nombre, nota)
    


def cola_prioridad(lista, cola):
    contador = 0
    while contador < 100:
        num = random.randint(0, tamanio(lista)-1)
        alumno = index(lista, num)
        if not existe_alumno_en_cola(cola, alumno):
            arribo(cola, alumno.nombre, alumno.promedio)
            contador += 1
    return cola


def generar_arbol(lista, arbol):
    contador = 0
    while contador < 300:
        num = random.randint(0, tamanio(lista)-1)
        alumno = index(lista, num)
        if not existe_alumno_en_arbol(arbol, alumno):
            arbol = insertarNodo(arbol, alumno)
            contador += 1
    return arbol


def espera_index():
    if not esVacia(cola):
        while True:
            print("Ingrese un valor entero:")
            index = input()
            try:
                temp = int(eval(str(index)))
                if type(temp) == int:
                    return temp
            except:
                continue
    else:
        print("La cola está vacía.")

def nombre_busqueda():
    if not esVacia(cola):
        print("Ingrese el nombre y apellido, con las mayúsculas y tildes correspondientes.")
        busqueda = input()
        return busqueda.strip()
    else:
        print("La cola está vacía.")


if __name__ == "__main__":
    lista = Lista()
    cola = Cola()
    arbol = None

    for i in range(1000):
        alumno = crear_alumno()
        insertar(lista, alumno)
    
    while True:
        print("1: Insertar alumno                               2: Insertar nota a indice")
        print("3: Insertar nota a nombre                        4: Agregar nota a todos (nota random a todos")
        print("5: Eliminar alumno por indice                    6: Eliminar alumno por nombre")
        print("7: Eliminar nota por indice                      8: Eliminar nota por nombre")
        print("9: Formar la cola con prioridad                  10: Tiempo de espera por índice")
        print("11: Tiempo de espera por nombre                  12: imprimir cola")
        print("13: Imprimir a todos                             14: Imprimir media del promedio")
        print("15: Generar arbol binario                        16: Buscar por nombre")
        print("17: Imprimir pre orden")
        print("\n0: Salir")

        opcion = input()

        print("-"*30)

        match opcion:
            case "1" : insertar_alumno(lista)
            case "2" : insert_nota_indice(lista)
            case "3" : insert_nota_nombre(lista)
            case "4" : add_nota_random(lista)
            case "5" : eliminar_indice(lista)
            case "6" : eliminar_nombre(lista)
            case "7" : eliminar_nota_indice_main(lista)
            case "8" : eliminar_nota_nombre_main(lista)
            case "9" : cola_prioridad(lista, cola)
            case "10" : atencion_index(cola, espera_index())
            case "11" : atencion_nombre(cola, nombre_busqueda())
            case "12" : imprimir(cola)
            case "13" : imprimir_info(lista)
            case "14" : 
                print("-"*30)
                print("Media de los promedios: ", media_promedios(lista))
                print("-"*30)
            case "15" : arbol = generar_arbol(lista, arbol)
            case "16" : buscar_arbol_nombre(arbol)
            case "17" : imprimirPreOrden(arbol)
            case _ : break


