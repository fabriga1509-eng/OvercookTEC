import pygame
import sys
from constants import ancho_ventana, alto_ventana, fps, titulo, white, CHEF1_TECLAS, CHEF2_TECLAS #Importamos las constantes necesarias para el juego
from entities.player import Player #Importamos la clase Player para crear a los chefs en el juego
class Game:
    def __init__(self): #Metodo constructor para inicializar el juego, crear la ventana, el reloj y los jugadores
        pygame.init()
        self.screen = pygame.display.set_mode((ancho_ventana,alto_ventana))
        pygame.display.set_caption(titulo)
        self.clock = pygame.time.Clock()
        self.running = True
        self.chef1 = Player(100,100,CHEF1_TECLAS)
        self.chef2 = Player(200,100,CHEF2_TECLAS)
    def handle_events(self): #Metodo para manejar los eventos del juego, como cerrar la ventana o interactuar con las estaciones
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == self.chef1.teclas["Interactuar"]:
                    self.chef1.interactuar(self.estaciones)
                    if event.key == self.chef2.teclas["Interactuar"]:
                        self.chef2.interactuar(self.estaciones)
    def update(self): #Metodo para actualizar el estado del juego, como la posición de los jugadores
        keys = pygame.key.get_pressed()
        self.chef1.update(keys)
        self.chef2.update(keys)
    def draw(self): #Metodo para dibujar los elementos del juego en la pantalla, como los jugadores y las estaciones
        self.screen.fill(white)
        self.chef1.draw(self.screen)
        self.chef2.draw(self.screen)
        pygame.display.flip()
    def run(self): #Metodo principal del juego
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()