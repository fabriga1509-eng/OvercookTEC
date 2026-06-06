import pygame
import sys
from constants import ancho_ventana, alto_ventana, fps, titulo, white
from entities.player import Player
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ancho_ventana,alto_ventana))
        pygame.display.set_caption(titulo)
        self.clock = pygame.time.Clock()
        self.running = True
        self.chef = Player(100,100)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runing = False
    def update(self):
        keys = pygame.key.get_pressed()
        self.chef.update(keys)
    def draw(self):
        self.screen.fill(white)
        self.chef.draw(self.screen)
        pygame.display.flip()
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()