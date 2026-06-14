#Importamos lo necesario
import pygame
from constants import recetas, STATION_WIDTH,STATION_HEIGHT,TIEMPOS_ESTACION,STATION_COLOR
#from ingredientes import 

#Definimos la clase station
class Station:
    def __init__(self,x,y,tipo,tipo_ingrediente=None):
        self.rect = pygame.Rect(x, y, STATION_WIDTH, STATION_HEIGHT)
        self.tipo = tipo
        self.ingrediente = None
        self.timer = 0
        self.activa = False
        if tipo == "almacen":
            self.stock = 10000
            self.tipo_ingrediente = tipo_ingrediente
        else:
            self.tiempo_min = TIEMPOS_ESTACION[tipo]["min"]
            self.tiempo_max = TIEMPOS_ESTACION[tipo]["max"]
    def recibir(self, ingrediente):
        if ingrediente.estacion == self.tipo:
            self.ingrediente = ingrediente
            self.activa = True
    def entregar(self):
        ingrediente = self.ingrediente
        self.ingrediente = None
        self.activa = False
        self.timer = 0
        return ingrediente
    def update(self, dt):
        if self.activa and self.ingrediente is not None:
            self.timer += dt
            if self.timer >= self.tiempo_max:        # ← adentro del if self.activa
                self.ingrediente.estado = "quemado"
            elif self.timer >= self.tiempo_min:      # ← adentro del if self.activa
                self.ingrediente.estado = "preparado"
    def draw(self, screen):
        pygame.draw.rect(screen, STATION_COLOR, self.rect)
