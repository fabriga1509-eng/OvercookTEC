import pygame
import sys
from constants import ancho_ventana, alto_ventana, fps, titulo, white, CHEF1_TECLAS, CHEF2_TECLAS,chef1_img,chef2_img,gray
from entities.player import Player
from levels.level import Level
from entities.order import Order
from UI.menu import MainMenu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
        pygame.display.set_caption(titulo)
        self.clock = pygame.time.Clock()
        self.running = True

        #Menu
        self.menu = MainMenu()
        self.estado_actual = "MENU"

        self.chef1 = Player(100, 100, CHEF1_TECLAS,chef1_img)
        self.chef2 = Player(200, 100, CHEF2_TECLAS,chef2_img)
        self.nivel = Level(1)
        self.estaciones = self.nivel.estaciones
        self.ordenes = []

    def handle_events(self):
        events=pygame.event.get()

        for event in events:
            if event.type==pygame.QUIT:
                self.running=False
                return

        if self.estado_actual=="MENU":
            nuevo_estado=self.menu.handle_events(events)
            if nuevo_estado=="GAME":
                self.estado_actual="GAME"

        elif self.estado_actual=="GAME":
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == self.chef1.teclas["interactuar"]:
                        self.chef1.interactuar(self.estaciones)
                    if event.key == self.chef2.teclas["interactuar"]:
                        self.chef2.interactuar(self.estaciones)

    def update(self):
        dt = self.clock.get_time() / 1000

        if self.estado_actual == "MENU":
            self.menu.update()

        if self.estado_actual=="GAME":
            keys = pygame.key.get_pressed()
            self.chef1.update(keys)
            self.chef2.update(keys)
            self.nivel.update(dt)
            for estacion in self.estaciones:
                estacion.update(dt)
            for orden in self.ordenes:
                orden.update(dt)
            if self.nivel.tiempo_agotado():
                self.running = False

    def draw(self):

        if self.estado_actual=="MENU":
            self.menu.draw(self.screen)

        elif self.estado_actual=="GAME":
            self.nivel.draw(self.screen)
            self.chef1.draw(self.screen)
            self.chef2.draw(self.screen)
            for estacion in self.estaciones:
                estacion.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()