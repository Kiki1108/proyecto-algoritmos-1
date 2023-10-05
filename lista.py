# Nodo simplemente enlazado
class nodoListaSimple(object):
    info, siguiente = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

def insertar(lista, info):
    nodo = nodoListaSimple()
    nodo.info = info
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
    lista.tamanio += 1

def imprimir(lista):
    actual = lista.inicio
    while actual is not None:
        print(actual.info)
        actual = actual.siguiente

def tamanio(lista):
    return lista.tamanio

def eliminar(lista, info):
    data = None
    # saber si es el primero de la lista
    if(lista.inicio.info == info):
        data = lista.incio
        lista.inicio = lista.inicio.siguiente
        lista.tamanio -= 1
    else:      
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while (siguiente is not None and info != siguiente.info):
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        # saber si es el ultimo de la lista
        if(siguiente is not None):
            data = siguiente.info
            actual.siguiente = siguiente.siguiente
            lista.tamanio -= 1
    return data


def return_index(lista, info):
    actual = lista.inicio
    contador = 0

    while actual.info != info:
        actual = actual.siguiente
        contador += 1
        if actual == None:
            return None
        
    return contador


def index(lista, index):
    actual = lista.inicio

    for i in range(index):
        actual = actual.siguiente

        if actual == None:
            return None

    return actual.info