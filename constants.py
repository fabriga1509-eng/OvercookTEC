import pygame
ancho_ventana = 800
alto_ventana = 500
fps = 60
titulo = "OvercookTEC"
white = (255, 255, 255)
black = (0,0,0)
PLAYER_SPEED = 5 
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
PLAYER_COLOR = (255, 0, 0)
CHEF1_TECLAS = { 
    "Arriba": pygame.K_w,
    "Abajo": pygame.K_s,
    "Izquierda": pygame.K_a,
    "Derecha": pygame.K_d,
    "Interactuar": pygame.K_e
}
CHEF2_TECLAS = { 
    "Arriba": pygame.K_UP,
    "Abajo": pygame.K_DOWN,
    "Izquierda": pygame.K_LEFT,
    "Derecha": pygame.K_RIGHT,
    "Interactuar": pygame.K_RETURN
}