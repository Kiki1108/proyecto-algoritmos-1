from lista import *
from alumno import Alumno
#from cola import *

import random
import json

with open("texto.json") as archivo:
    datos_nombres = json.load(archivo)

nombres = datos_nombres["nombres"]
apellidos = datos_nombres["apellidos"]


def crear_alumno():
    nombre = random.choice(nombres) + " " + random.choice(apellidos)
    nota = random.randint(10, 70)
    alumno = Alumno(nombre, nota)
    return alumno


if __name__ == "__main__":
    lista = Lista()

    for i in range(1000):
        alumno = crear_alumno()
        insertar(lista, alumno)
    
    imprimir_info(lista)

