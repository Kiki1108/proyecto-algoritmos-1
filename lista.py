import random
class nodoListaSimple(object):
    Alumno = None
    siguiente = None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0
        self.promedio = 0


def insertar(lista, alumno):
    nodo = nodoListaSimple()
    nodo.alumno = alumno
    if lista.inicio is None:
        nodo.siguiente = lista.inicio
        lista.inicio = nodo
    else:
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while siguiente is not None:
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        nodo.siguiente = siguiente
        actual.siguiente = nodo

    suma = lista.promedio * lista.tamanio
    suma = suma + alumno.promedio
    lista.tamanio += 1
    lista.promedio = suma / (lista.tamanio)


def imprimir(lista):
    actual = lista.inicio
    while actual is not None:
        print(actual.alumno)
        actual = actual.siguiente


def imprimir_info(lista):
    actual = lista.inicio
    while actual is not None:
        print(actual.alumno.nombre, actual.alumno.promedio)
        actual = actual.siguiente


def tamanio(lista):
    return lista.tamanio


def media_promedios(lista):
    return int(lista.promedio)


def eliminar(lista, alumno):
    data = None
    # saber si es el primero de la lista
    if(lista.inicio.alumno == alumno):
        data = lista.incio
        lista.inicio = lista.inicio.siguiente
        lista.promedio = (lista.promedio * lista.tamanio - alumno.promedio) / (lista.tamanio -1)
        lista.tamanio -= 1
    else:      
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while (siguiente is not None and alumno != siguiente.alumno):
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        # saber si es el ultimo de la lista
        if(siguiente is not None):
            data = siguiente.alumno
            actual.siguiente = siguiente.siguiente
            lista.promedio = (lista.promedio * lista.tamanio - alumno.promedio) / (lista.tamanio -1)
            lista.tamanio -= 1
    return data


def return_index(lista, alumno):
    actual = lista.inicio
    contador = 0

    while actual.alumno != alumno:
        actual = actual.siguiente
        contador += 1
        if actual == None:
            return None
        
    return contador


def index(lista, index):
    actual = lista.inicio
    if index == 0:
        return actual.alumno

    for i in range(index):
        if actual == None:
            return None
        actual = actual.siguiente

    return actual.alumno


def cambiar_nota(lista, indice, nombre, nota):
    if nombre == None:
        actual = lista.inicio
        for i in range(indice):
            actual = actual.siguiente

    elif indice == None:
        actual = lista.inicio
        for i in range(tamanio(lista)):
            if actual.alumno.nombre == nombre:
                break
            actual = actual.siguiente
    
    print("-"*30)
    print("Nombre: ", actual.alumno.nombre)
    print("Promedio anterior: ", actual.alumno.promedio)
    actual.alumno.add_nota(nota)
    print("Promedio actual: ", actual.alumno.promedio)
    print("-"*30)


def existe_alumno(lista, nombre):
    actual = lista.inicio
    for i in range(tamanio(lista)):
        if actual == None:
            return False
        elif actual.alumno.nombre == nombre:
            return True
        actual = actual.siguiente


def add_nota_random(lista):
    actual = lista.inicio
    for i in range(tamanio(lista)):
        nota = random.randint(10, 70)
        actual.alumno.add_nota(nota)
        actual = actual.siguiente


def eliminar_alumno(lista, nombre, indice):
    if nombre == None:
        actual = lista.inicio
        for i in range(indice):
            actual = actual.siguiente

    if indice == None:
        actual = lista.inicio
        for i in range(tamanio(lista)):
            if actual.alumno.nombre == nombre:
                break
            actual = actual.siguiente
    
    eliminar(lista, actual.alumno)
    print("-"*30)
    print("Eliminado: ", actual.alumno.nombre, actual.alumno.promedio)
    print("-"*30)


def eliminar_nota_indice(lista, indice, nota):
    actual = lista.inicio
    for _ in range(indice):
        actual = actual.siguiente

    print("-"*30)
    print(actual.alumno.nombre)
    print("Promedio anterior: ", actual.alumno.promedio)
    actual.alumno.quitar_nota(nota)
    print("Promedio actual: ", actual.alumno.promedio)
    print("-"*30)


def eliminar_nota_nombre(lista, nombre, nota):
    actual = lista.inicio
    for i in range(tamanio(lista)):
        if actual.alumno.nombre == nombre:
            break
        actual = actual.siguiente

    print("-"*30)
    print(actual.alumno.nombre)
    print("Promedio anterior: ", actual.alumno.promedio)
    actual.alumno.quitar_nota(nota)
    print("Promedio actual: ", actual.alumno.promedio)
    print("-"*30)


