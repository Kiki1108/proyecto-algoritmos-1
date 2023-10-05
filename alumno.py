
class Alumno():
    def __init__(self):
        self.nombre = None
        self.cantidad_notas = 0
        self.promedio = 0

    def add_nota(self, nota):
        ponderado = self.promedio * self.cantidad_notas
        ponderado += nota
        self.cantidad_notas += 1
        self.promedio = ponderado / self.cantidad_notas

    def quitar_nota(self, nota):
        ponderado = self.promedio * self.cantidad_notas
        ponderado -= nota
        self.cantidad_notas -= 1
        self.promedio = ponderado / self.cantidad_notas

    def set_nombre(self, nombre):
        self.nombre =  nombre
         
    