from lista import *
from alumno import Alumno
from cola import *
from arbol import *
from pila import *

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


def buscar_arbol_nombre(arbol):
    while True:
        nombre = input("Nombre: ")
        if existe_alumno_en_arbol(arbol, Alumno(nombre, 0)):
            break
    alumno = buscar_alumno_en_arbol(arbol, nombre)
    
    print("-"*30)
    print(alumno.nombre)
    print("Promedio: ",alumno.promedio)
    print("-"*30)


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


def generar_pila(lista):
    pila = Pila()
    for i in range(tamanio(lista)):
        alumno = index(lista, i)
        apilar_orden(pila, alumno)
    return pila


if __name__ == "__main__":
    lista = Lista()
    cola = Cola()
    arbol = None

    for i in range(1000):
        match i:
            case 0: alumno = Alumno("Miguel Oyarce", random.randint(10, 70))
            case 1: alumno = Alumno("Alejandro Ide", random.randint(10, 70))            
            case 2: alumno = Alumno("Amanda Pérez", random.randint(10, 70))
            case 3: alumno = Alumno("Cristian Pavez", random.randint(10, 70))
            case 4: alumno = Alumno("Felipe Mendez", random.randint(10, 70))
            case 5: alumno = Alumno("Francisco Abdala", random.randint(10, 70))
            case 6: alumno = Alumno("Gabriel Rojas", random.randint(10, 70))
            case 7: alumno = Alumno("Matias Gajardo", random.randint(10, 70))
            case 8: alumno = Alumno("Ricardo Macaya", random.randint(10, 70))
            case 9: alumno = Alumno("Wladimir Fernández", random.randint(10, 70))
            case _: alumno = crear_alumno()
        insertar(lista, alumno)
    
    while True:
        print("""
*Funciones de Lista:*                   *Funciones de Cola:*                        *Funciones de Arbol Binario:*
1: Insertar Alumno                      11: Generar Colo con Prioridad              15: Generar Arbol Binario
2: Insertar Nota por Indice             12: Imprimir Tiempo de espera por Índice    16: Buscar por Nombre
3: Insertar Nota por Nombre             13: Imprimir Tiempo de espera por Nombre    17: Imprimir pre orden
4: Agregar Nota a Todos (Tomar prueba)  14: Imprimir Cola                           
5: Eliminar Alumno por Inidice                                                      *Funciones de Pila:*
6: Eliminar Alumno por Nombre                                                       18: Generar Pila
7: Eliminar Nota por Indice                                                         19: Imprimir Alumnos
8: ELiminar Nota por Nombre                                                         20: Premiar a los mejores
9: Imprimir a todos
10: Imprimir Promedio Generar 

Cualquier otra entrada = salir""")

        opcion = input("Entrada:")

        print("-"*30)
        try:
            match opcion:
                case "1" : insertar_alumno(lista)
                case "2" : insert_nota_indice(lista)
                case "3" : insert_nota_nombre(lista)
                case "4" : add_nota_random(lista)
                case "5" : eliminar_indice(lista)
                case "6" : eliminar_nombre(lista)
                case "7" : eliminar_nota_indice_main(lista)
                case "8" : eliminar_nota_nombre_main(lista)
                case "9" : imprimir_info(lista)
                case "10" : 
                    print("-"*30)
                    print("Media de los promedios: ", media_promedios(lista))
                    print("-"*30)
                case "11" : cola_prioridad(lista, cola)
                case "12" : atencion_index(cola, espera_index())
                case "13" : atencion_nombre(cola, nombre_busqueda())
                case "14" : imprimir(cola)
                case "15" : arbol = generar_arbol(lista, arbol)
                case "16" : buscar_arbol_nombre(arbol)
                case "17" : imprimirPreOrden(arbol)
                case "18" : pila = generar_pila(lista)
                case "19" : imprimir_alumnos_pila(pila)
                case "20" : premiar(pila)
                case _ : break
        except:
            print("!"*60)
            print("Oh, Algo salió mal intente revisar sus pasos anteriores")
            print("Presione enter para continuar")
            input("!"*60)


