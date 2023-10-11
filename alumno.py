
class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.cantidad_notas = 1
        self.promedio = nota

    def add_nota(self, nota):
        ponderado = self.promedio * self.cantidad_notas
        ponderado += nota
        self.cantidad_notas += 1
        self.promedio = int(ponderado / self.cantidad_notas)

    def quitar_nota(self, nota):
        ponderado = self.promedio * self.cantidad_notas
        ponderado -= nota
        self.cantidad_notas -= 1
        self.promedio = int(ponderado / self.cantidad_notas)

    def set_nombre(self, nombre):
        self.nombre =  nombre
         
    