class nodoCola(object):
    info, siguiente, prioridad = None, None, None

class Cola(object):
    def __init__(self):
        self.entrada, self.salida = None, None
        self.tamanio = 0

def arribo(cola, info, prioridad):
    nuevoNodo = nodoCola()
    nuevoNodo.info = info
    nuevoNodo.prioridad = prioridad
    #Si la cola está vacía, el nuevo nodo se convierte en la salida y en la entrada.
    if cola.salida is None:
        cola.salida = nuevoNodo
        cola.entrada = nuevoNodo
    #Si la prioridad del nuevo nodo es menor que la prioridad del nodo actual en salida, 
    #nuevo nodo se coloca antes del nodo actual y se actualiza la salida.
    elif prioridad < cola.salida.prioridad:
        nuevoNodo.siguiente = cola.salida
        cola.salida = nuevoNodo
    #Se busca el lugar correcto en la cola para insertar el nuevo nodo manteniendo el orden de prioridad.
    else:
        nodo_actual = cola.salida
        while nodo_actual.siguiente is not None and nodo_actual.siguiente.prioridad <= prioridad:
            nodo_actual = nodo_actual.siguiente
        nuevoNodo.siguiente = nodo_actual.siguiente
        nodo_actual.siguiente = nuevoNodo  
    cola.tamanio += 1

def atencion(cola):
    info = cola.salida
    cola.salida = cola.salida.siguiente
    if cola.salida is None:
        cola.entrada = None
    cola.tamanio -= 1
    return info

def esVacia(cola):
    return cola.entrada is None

def imprimir(cola):
    colaAuxiliar = Cola()
    while not esVacia(cola):
        info = atencion(cola)
        print(info.info, info.prioridad)
        arribo(colaAuxiliar, info.info, info.prioridad)

    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info.info, info.prioridad)


def atencion_index(cola, busqueda):
    colaAuxiliar = Cola()
    contador = 1
    t_espera = 0
    help = False
    while not esVacia(cola):
        info = atencion(cola)
        if contador != busqueda:
            if help is False:
                contador += 1
                if info.prioridad < 40:
                    t_espera += 10
                else:
                    t_espera += 5
        else:
            help = True
        arribo(colaAuxiliar, info.info, info.prioridad)

    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info.info, info.prioridad)
    if help is True:
        print(f"La persona del puesto {contador}, tiene un tiempo de espera de {t_espera} minutos.")
    else:
        print("No se encontraron coincidencias.")

def atencion_nombre(cola, busqueda):
    colaAuxiliar = Cola()
    contador = 1
    t_espera = 0
    help = False
    while not esVacia(cola):
        info = atencion(cola)
        if info.info != busqueda:
            if help is False:
                contador += 1
                if info.prioridad < 40:
                    t_espera += 10
                else:
                    t_espera += 5
        else:
            help = True
        arribo(colaAuxiliar, info.info, info.prioridad)

    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info.info, info.prioridad)
    
    if help is True:
        print(f"Se encuentra en el puesto {contador}, tiene un tiempo de espera de {t_espera} minutos.")
    else:
        print("No se encontraron coincidencias.")


def existe_alumno_en_cola(cola, alumno):
    colaAuxiliar = Cola()
    existe = False
    while not esVacia(cola):
        actual = atencion(cola)
        arribo(colaAuxiliar, actual.info, actual.prioridad)
        if alumno.nombre == actual.info and alumno.promedio == actual.prioridad:
            existe = True

    while not esVacia(colaAuxiliar):
        actual = atencion(colaAuxiliar)
        arribo(cola, actual.info, actual.prioridad)
        
    return existe

