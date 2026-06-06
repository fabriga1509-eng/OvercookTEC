import pygame 
from constants import PLAYER_SPEED, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR
class Player:
    def __init__(self,x,y,teclas):
        self.rect = pygame.Rect(x,y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocidad = PLAYER_SPEED
        self.ingrediente = None
        self.teclas = teclas
    def mover(self,keys):
        if keys[self.teclas['Izquierda']]:
            self.rect.x -= self.velocidad
        if keys[self.teclas['Derecha']]:
            self.rect.x += self.velocidad
        if keys[self.teclas['Arriba']]:
            self.rect.y -= self.velocidad
        if keys[self.teclas['Abajo']]:
            self.rect.y += self.velocidad
    def recoger(self,estación):
        self.ingrediente = estación.ingrediente
    def soltar(self,estación):
        estación.ingrediente = self.ingrediente
        self.ingrediente = None
    def interactuar(self,estaciones):
        for estacion in estaciones:
            if self.rect.colliderect(estacion.rect):
                if self.ingrediente is None:
                    self.recoger(estacion)
                else:
                    self.soltar(estacion)
                break
    def update(self,keys):
        self.mover(keys)
    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)