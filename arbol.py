from cola import *

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

def insertarNodo(raiz, info):
    if(raiz is None):
        raiz = nodoArbol(info)
    elif(info.nombre < raiz.info.nombre):
        raiz.izq = insertarNodo(raiz.izq,info)
    else:
        raiz.der = insertarNodo(raiz.der,info)
    return raiz

def arbolVacio(raiz):
    return raiz is None

def remplazar(raiz):
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

def eliminarNodo(raiz,info):
    x = None
    if(raiz is not None):
        if(info<raiz.info):
            raiz.izq, x = eliminarNodo(raiz.izq,info)
        elif(info>raiz.info):
            raiz.der, x = eliminarNodo(raiz.der,info)
        else:
            x=raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

def imprimirPorNivel(raiz):
    pendientes = Cola()
    arribo(pendientes, raiz)
    while(not esVacia(pendientes)):
        nodo = atencion(pendientes)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(pendientes,nodo.izq)
        if(nodo.der is not None):
            arribo(pendientes, nodo.der)


def buscar(raiz, info):
    if(raiz is None):
        return None
    elif(info == raiz.info):
        return raiz.info
    elif(info < raiz.info):
        return buscar(raiz.izq,info)
    else:
        return buscar(raiz.der,info)


def imprimirInOrden(raiz):
    if(raiz is not None):
        imprimirInOrden(raiz.izq)
        print(raiz.info)
        imprimirInOrden(raiz.der)

def imprimirPreOrden(raiz):
    if(raiz is not None):
        print(raiz.info.nombre)
        print(raiz.info.promedio)
        imprimirPreOrden(raiz.izq)
        imprimirPreOrden(raiz.der)

def imprimirPostOrden(raiz):
    if(raiz is not None):
        print(raiz.info.nombre)
        imprimirPostOrden(raiz.der)
        imprimirPostOrden(raiz.izq)


def existe_alumno_en_arbol(raiz, alumno):
    existe = False
    if(raiz is not None):
        if raiz.info.nombre == alumno.nombre:
            return True
        if not existe:
            existe = existe_alumno_en_arbol(raiz.izq, alumno)
        if not existe:
            existe = existe_alumno_en_arbol(raiz.der, alumno)
    return existe


def buscar_alumno_en_arbol(raiz, nombre):
    existe = False
    if(raiz is not None):
        if raiz.info.nombre == nombre:
            return raiz.info
        if not existe:
            existe = buscar_alumno_en_arbol(raiz.izq, nombre)
        if not existe:
            existe = buscar_alumno_en_arbol(raiz.der, nombre)
    return existe


def prueba_busqueda_arbol(raiz, alumno):
    if(raiz is None):
        return None
    elif(alumno == raiz.info.nombre):
        return True
    elif(alumno < raiz.info.nombre):
        return prueba_busqueda_arbol(raiz.izq,alumno)
    else:
        return prueba_busqueda_arbol(raiz.der,alumno)
    

