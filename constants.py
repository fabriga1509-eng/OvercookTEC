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
STATION_WIDTH = 50
STATION_HEIGHT = 40
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
    "Interactuar": pygame.K_p
}
recetas = {"Japonesa":
    {"Sushi":
        {"arroz":{"estado":"crudo","estacion":"olla"},
        "pescado_sushi":{"estado":"crudo","estacion":"cocina"},
        "alga":{"estado":"crudo","estación":"cocina"}},
    "Shashimi":
        {"pescado":{"estado":"sin_cortar","estacion":"tabla de cortar"}}},
"Gringa":
    {"Pizza":
        {"masa":{"estado":"crudo","estacion":"cocina"},
        "salsa":{"estado":"crudo","estacion":"cocina"},
        "queso":{"estado":"crudo","estacion":"cocina"}},
    "Hamburguesa": 
        {"pan":{"estado":"suave","estacion":"horno"},
        "carne":{"estado":"crudo","estacion":"cocina"},
        "lechuga":{"estado":"sin_cortar","estacion":"tabla de cortar"},
        "tomate":{"estado":"sin_cortar","estacion":"tabla de cortar"}},
    "Smores":
        {"galleta":{"estado":"crudo","estacion":"horno"},
        "malvavisco":{"estado":"crudo","estacion":"horno"},
        "chocolate":{"estado":"crudo","estacion":"horno"}},},
"Tica":
    {"Pinto":
        {"arroz":{"estado":"crudo","estacion":"olla"},
        "frijoles":{"estado":"crudo","estacion":"cocina"},
        "huevo":{"estado":"crudo","estacion":"sarten"}},
    "Arroz con pollo":
        {"arroz":{"estado":"crudo","estacion":"olla"},
        "verduras":{"estado":"sin_cortar","estacion":"cocina"},
        "pollo":{"estado":"crudo","estación":"cocina"}},
    "Olla de carne":
        {"verduras":{"estado":"crudo","estacion":"cocina"},
        "carne":{"estado":"crudo","estacion":"olla"},}}}
TIEMPOS_ESTACION = {
    "freidora": {"min": 5, "max": 10},
    "sarten":   {"min": 4, "max": 8},
    "horno":    {"min": 8, "max": 15},
    "olla":     {"min": 6, "max": 12}
}
STATION_COLOR = (150, 75, 0)
TIEMPOS_ESTACION = {
    "freidora": {"min": 8,  "max": 15},
    "sarten":   {"min": 6,  "max": 12},
    "horno":    {"min": 10, "max": 18},
    "olla":     {"min": 8,  "max": 14},
    "tabla de cortar": {"min": 4, "max": 8}
}
TIEMPO_NIVEL = 300