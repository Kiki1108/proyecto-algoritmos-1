class nodoPila(object):
    info, siguiente = None, None


class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, info):
    nuevoNodo = nodoPila()
    nuevoNodo.info = info
    nuevoNodo.siguiente = pila.cima
    pila.cima = nuevoNodo
    pila.tamanio += 1


def apilar_orden(pila, info):
    nuevoNodo = nodoPila()
    nuevoNodo.info = info
    if pila.cima == None:
        nuevoNodo.siguiente = pila.cima
        pila.cima = nuevoNodo 
    elif info.promedio >= pila.cima.info.promedio:
        nuevoNodo.siguiente = pila.cima
        pila.cima = nuevoNodo
    else:
        pila_auxiliar = Pila()
        while True:
            saliente = desapilar(pila)
            apilar(pila_auxiliar, saliente)
            if pila.cima == None:
                nuevoNodo.siguiente = pila.cima
                pila.cima = nuevoNodo
                break
            elif info.promedio >= pila.cima.info.promedio:
                nuevoNodo.siguiente = pila.cima
                pila.cima = nuevoNodo
                break
        while not esVacia(pila_auxiliar):
            saliente = desapilar(pila_auxiliar)
            apilar(pila, saliente)
    pila.tamanio += 1


def desapilar(pila):
    info = pila.cima.info
    pila.cima = pila.cima.siguiente
    pila.tamanio -= 1
    return info


def esVacia(pila):
    return pila.cima is None


def imprimir(pila):
    pilaAuxiliar = Pila()
    while not esVacia(pila):
        info = desapilar(pila)
        print(info)
        apilar(pilaAuxiliar, info)
    while not esVacia(pilaAuxiliar):
        info = desapilar(pilaAuxiliar)
        apilar(pila, info)


def imprimir_alumnos_pila(pila):
    pilaAuxiliar = Pila()
    while not esVacia(pila):
        info = desapilar(pila)
        print(info.nombre, info.promedio)
        apilar(pilaAuxiliar, info)
    while not esVacia(pilaAuxiliar):
        info = desapilar(pilaAuxiliar)
        apilar(pila, info)


def enCima(pila):
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None
    

def index_pila(pila, info):
    pilaAuxiliar = Pila()
    indice = 0
    while pila.cima.info != info:
        cima_auxiliar = desapilar(pila)
        apilar(pilaAuxiliar, cima_auxiliar)
        indice += 1
        if esVacia(pila):
            indice = -1
            break
    while not esVacia(pilaAuxiliar):
        nueva_cima = desapilar(pilaAuxiliar)
        apilar(pila, nueva_cima)

    if indice >-1:
        return indice
    else:
        return None
    

def premiar(pila):
    pilaAuxiliar = Pila()
    for i in range(3):
        anterior = 0
        while not esVacia(pila):
            info = desapilar(pila)
            apilar(pilaAuxiliar, info)
            if anterior <= info.promedio:
                print(f"Lugar {i+1}: {info.nombre}, {info.promedio}")
                apilar(pilaAuxiliar, info)
                desapilar(pilaAuxiliar)
            else:
                break
            anterior = info.promedio
    while not esVacia(pilaAuxiliar):
        info = desapilar(pilaAuxiliar)
        apilar(pila, info)