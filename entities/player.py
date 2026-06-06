import pygame 
from constants import PLAYER_SPEED, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR
class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocidad = PLAYER_SPEED
        self.ingrediente = None
    def mover(self,keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if keys[pygame.K_DOWN]:
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