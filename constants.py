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
    "Interactuar": pygame.K_p
}
recetas = {"Japonesa":
    {"Sushi":
        {"arroz":{"estado":"crudo","estacion":"cocina"},
        "pescado":{"estado":"crudo","estacion":"cocina"},
        "alga":{"estado":"crudo","estación":"cocina"}},
    "Shashimi":
        {"pescado":{"estado":"sin_cortar","Estacion":"tabla de cortar"}}},
"Estadounidense":
    {"Pizza":
        {"masa":{"estado":"crudo","estacion":"cocina"},
        "salsa":{"estado":"crudo","estacion":"cocina"},
        "queso":{"estado":"crudo","estacion":"cocina"}},
    "Hamburguesa": 
        {"pan":{"Estado":"suave","estacion":"horno"},
        "carne":{"estado":"crudo","estacion":"cocina"},
        "lechuga":{"estado":"sin_cortar","estacion":"tabla de cortar"},
        "tomate":{"estado":"sin_cortar","estacion":"tabla de cortar"}},
    "Smores":
        {"galleta":{"estado":"crudo","estacion":"horno"},
        "malvavisco":{"estado":"crudo","estacion":"horno"},
        "chocolate":{"estado":"crudo","estacion":"horno"}},},
"Tica":
    {"Pinto":
        {"arroz viejo":{"estado":"crudo","estacion":"olla"},
        "frijoles":{"estado":"crudo","estacion":"cocina"},
        "huevo":{"estado":"crudo","estacion":"sarten"}},
    "Arroz con pollo":
        {"arroz_precocido":{"estado":"crudo","estacion":"olla"},
        "vergetales":{"estado":"sin_cortar","estacion":"tabla de cortar"},
        "pollo":{"estado":"crudo","estación":"cocina"}},
    "Olla de carne":
        {"verduras":{"estado":"crudo","estacion":"cocina"},
        "carne":{"estado":"crudo","estacion":"olla"},}}}