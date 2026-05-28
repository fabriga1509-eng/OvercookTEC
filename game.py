import pygame
import sys
from constants import ancho_ventana, alto_ventana, fps, titulo, white
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ancho_ventana,alto_ventana)  )
        pygame.display.set_caption(titulo)
        self.clock = pygame.time.Clock()
        self.runing = True
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runing = False
    def update(self):
        pass
    def draw(self):
        self.screen.fill(white)
        pygame.display.flip()
    def run(self):
        while self.runing:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()