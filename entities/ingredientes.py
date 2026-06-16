#Importamos pygame y las constantes necesarias
from constants import recetas

#Definimos la clase
class Ingrediente:
    def __init__(self,nombre,datos):
        self.nombre = nombre
        self.estado = datos["estado"]
        self.estacion = datos["estacion"]
    def __str__(self):
        return self.nombre
#Prueba
datos = recetas["Japonesa"]["Sushi"]["arroz"]
ingrediente = Ingrediente("arroz", datos)