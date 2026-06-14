import random
#import pygame

class Order:
    def __init__(self, recetas_disponibles, tiempo_limite):
        self.receta = random.choice(recetas_disponibles) #Modifica si es necesario Abi
        self.tiempo_limite = tiempo_limite #Modifica si es necesario Abi
        self.timer = 0 #Modifica si es necesario Abi
        self.completada = False
    def update(self, dt):
        if not self.completada:
            self.timer += dt
    def esta_expirada(self):
        return self.timer >= self.tiempo_limite
    def completar(self):
        self.completada = True
    def draw(self, screen):
        pass #Te toca dibujar esto Abi 