import pygame
import os
ancho_ventana = 1024
alto_ventana = 640
fps = 60
titulo = "OvercookTEC"
white = (255, 255, 255)
gray= (30,30,30)
black = (0,0,0)
piso=(74,42,13)
fuente_pixel=os.path.join("assets","fuentes", "8bitOperatorPlusSC-Bold.ttf")

#Fondos
fondo_menu=os.path.join("assets","imagenes","fondo_menu.png")
fondo_japones=os.path.join("assets","imagenes","PisoJaponesOscuro.png")


boton_normal=os.path.join("assets","imagenes","FondoBotonInicio.png")
boton_presionado=os.path.join("assets","imagenes","FondoBotonInicioPresionado.png")

chef1_img=os.path.join("assets","imagenes","Chef1.png")
chef2_img=os.path.join("assets","imagenes","Chef2.png")

PLAYER_SPEED = 10
PLAYER_WIDTH = 85
PLAYER_HEIGHT = 120
PLAYER_COLOR = (255, 0, 0)
STATION_WIDTH = 128
STATION_HEIGHT = 128
CHEF1_TECLAS = { 
    "arriba": pygame.K_w,
    "abajo": pygame.K_s,
    "izquierda": pygame.K_a,
    "derecha": pygame.K_d,
    "interactuar": pygame.K_e
}
CHEF2_TECLAS = { 
    "arriba": pygame.K_UP,
    "abajo": pygame.K_DOWN,
    "izquierda": pygame.K_LEFT,
    "derecha": pygame.K_RIGHT,
    "interactuar": pygame.K_p
}
recetas = {"Japonesa":
    {"Sushi":
        {"arroz":{"estado":"crudo","estacion":"olla"},
        "pescado_sushi":{"estado":"crudo","estacion":"sarten"},
        "alga":{"estado":"crudo","estación":"sarten"}},
    "Shashimi":
        {"pescado":{"estado":"sin_cortar","estacion":"tabla de cortar"}}},

"Gringa":
    {"Pizza":
        {"masa":{"estado":"crudo","estacion":"horno"},
        "salsa":{"estado":"crudo","estacion":"sarten"},
        "queso":{"estado":"crudo","estacion":"horno"}},
    "Hamburguesa": 
        {"pan":{"estado":"suave","estacion":"horno"},
        "carne":{"estado":"crudo","estacion":"sarten"},
        "lechuga":{"estado":"sin_cortar","estacion":"tabla de cortar"},
        "tomate":{"estado":"sin_cortar","estacion":"tabla de cortar"}},
    "Smores":
        {"galleta":{"estado":"crudo","estacion":"horno"},
        "malvavisco":{"estado":"crudo","estacion":"horno"},
        "chocolate":{"estado":"crudo","estacion":"horno"}},},

"Tica":
    {"Pinto":
        {"arroz":{"estado":"crudo","estacion":"olla"},
        "frijoles":{"estado":"crudo","estacion":"olla"},
        "huevo":{"estado":"crudo","estacion":"sarten"}},
    "Arroz con pollo":
        {"arroz":{"estado":"crudo","estacion":"olla"},
        "verduras":{"estado":"sin_cortar","estacion":"sarten"},
        "pollo":{"estado":"crudo","estación":"sarten"}},
    "Olla de carne":
        {"verduras":{"estado":"crudo","estacion":"olla"},
        "carne":{"estado":"crudo","estacion":"olla"},}}}

STATION_COLOR = (150, 75, 0)

TIEMPOS_ESTACION = {
    "freidora": {"min": 8,  "max": 15},
    "sarten":   {"min": 6,  "max": 12},
    "horno":    {"min": 10, "max": 18},
    "olla":     {"min": 8,  "max": 14},
    "tabla de cortar": {"min": 4, "max": 8},
    "cocina":   {"min": 7,  "max": 13}
}
TIEMPO_NIVEL = 300

#Mapa de japones
#'.' = Suelo, 'M' = Mostrador, 'A' = Arroz, 'P' = Pescado Sushi, 'G' = Alga, 'F' = Pescado Normal
# 'O' = Olla, 'C' = Tabla de Cortar, 'D' = Platos, 'E' = Entrega

MAPA_JAPONES = [
    ["M", "M", "A", ".", ".", "P", ".", ".", "M", "M", "M", "M"],
    ["M", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "M"],
    ["M", ".", "M", "M", "O", ".", ".", ".", "M", "M", "C", "M"],
    [".", ".", ".", ".", ".", ".", "G", "F", ".", ".", ".", "."],
    ["M", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["D", ".", ".", ".", ".", ".", ".", ".", "E", ".", ".", "M"]
]