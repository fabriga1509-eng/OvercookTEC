import pygame
import sys
from constants import ancho_ventana, alto_ventana, fps, titulo, white, CHEF1_TECLAS, CHEF2_TECLAS
from entities.player import Player
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ancho_ventana,alto_ventana))
        pygame.display.set_caption(titulo)
        self.clock = pygame.time.Clock()
        self.running = True
        self.chef1 = Player(100,100,CHEF1_TECLAS)
        self.chef2 = Player(200,100,CHEF2_TECLAS)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == self.chef1.teclas["Interactuar"]:
                    self.chef1.interactuar(self.estaciones)
                    if event.key == self.chef2.teclas["Interactuar"]:
                        self.chef2.interactuar(self.estaciones)
    def update(self):
        keys = pygame.key.get_pressed()
        self.chef1.update(keys)
        self.chef2.update(keys)
    def draw(self):
        self.screen.fill(white)
        self.chef1.draw(self.screen)
        self.chef2.draw(self.screen)
        pygame.display.flip()
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()