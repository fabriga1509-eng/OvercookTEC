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
fondo_tico=os.path.join("assets","imagenes","PisoTico.png")
fondo_gringo=os.path.join("assets","imagenes","PisoGringo.png")

#Efectos de sonido
RUTAreceta_perdida="assets/sonidos/receta_perdida.mp3"
RUTAreceta_completada="assets/sonidos/receta_completada.wav"
RUTAtiempo_reducido="assets/sonidos/tiempo_reducido.mp3"
RUTAsiguiente_nivel="assets/sonidos/siguiente_nivel.mp3"

#Boton menu
boton_normal=os.path.join("assets","imagenes","FondoBotonInicio.png")
boton_presionado=os.path.join("assets","imagenes","FondoBotonInicioPresionado.png")

#Sprites de los chefs
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
imgs_estaciones={
        "freidora": "estacion_freidora.png",
        "sarten":   "estacion_sarten.png",
        "horno":    "estacion_horno.png",
        "olla":     "estacion_olla.png",
        "tabla de cortar": "estacion_picar.png",
        "cocina":  "estacion_picar.png",
        "mostrador": "estacion_pared.png",
        "entrega": "estacion_entrega.png",
        "plato_station": "MesaConPlato.png"
        }
SPRITES_INGREDIENTES={
    "arroz": os.path.join("assets", "imagenes", "arroz_crudo.png"),
    "arroz_cocido": os.path.join("assets", "imagenes", "arroz_cocido.png"),
    "arroz_quemado": os.path.join("assets", "imagenes", "arroz_quemado.png"),

    "pescadosushi":os.path.join("assets", "imagenes", "pescadosushi_crudo.png"),
    "pescadosushi_cortado": os.path.join("assets", "imagenes", "pescadosushi_cortado.png"),

    "alga": os.path.join("assets", "imagenes", "alga_crudo.png"),
    "alga_cortado": os.path.join("assets", "imagenes", "alga_cortado.png"),

    "pescado": os.path.join("assets", "imagenes", "pescado_sincortar.png"),
    "pescado_cortado": os.path.join("assets", "imagenes", "pescado_preparado.png"),

    "masa": os.path.join("assets", "imagenes", "masa_crudo.png"),
    "masa_cocido": os.path.join("assets", "imagenes", "masa_preparado.png"),
    "masa_quemado": os.path.join("assets", "imagenes", "arroz_quemado.png"),

    "salsa": os.path.join("assets", "imagenes", "salsa_crudo.png"),
    "salsa_cocido": os.path.join("assets", "imagenes", "salsa_crudo.png"),
    "salsa_quemado": os.path.join("assets", "imagenes", "arroz_quemado.png"),
    
    "queso": os.path.join("assets", "imagenes", "queso_crudo.png"),
    "queso_cocido": os.path.join("assets", "imagenes", "queso_cocido.png"),
    "queso_quemado": os.path.join("assets", "imagenes", "arroz_quemado.png")
    ,
    "pan": os.path.join("assets", "imagenes", "pan_crudo.png"),
    "pan_cocido": os.path.join("assets", "imagenes", "pan_cocido.png"),
    "pan_quemado": os.path.join("assets", "imagenes", "arroz_quemado.png"),

    "carne": os.path.join("assets", "imagenes", "carne_cruda.png"),
    "carne_cocido": os.path.join("assets", "imagenes", "carne_cocinada.png"),
    "carne_quemado": os.path.join("assets", "imagenes", "carne_quemada.png"),

    "lechuga": os.path.join("assets", "imagenes", "lechuga_crudo.png"),
    "lechuga_cortado": os.path.join("assets", "imagenes", "lechuga_cortada.png"),

    "tomate": os.path.join("assets", "imagenes", "tomate_crudo.png"),
    "tomate_cortado": os.path.join("assets", "imagenes", "tomate_cortado.png"),

    "frijoles": os.path.join("assets", "imagenes", "frijoles_crudo.png"),
    "frijoles_cocido": os.path.join("assets", "imagenes", "frijoles_cocido.png"),
    "frijoles_quemado": os.path.join("assets", "imagenes", "frijoles_quemado.png"),

    "huevo": os.path.join("assets", "imagenes", "huevo_crudo.png"),
    "huevo_cocido": os.path.join("assets", "imagenes", "huevo_cocido.png"),
    "huevo_quemado": os.path.join("assets", "imagenes", "arroz_quemado.png"),

    "verduras": os.path.join("assets", "imagenes", "verduras_crudo.png"),
    "verduras_cortado": os.path.join("assets", "imagenes", "verduras_cortado.png"),
    "verduras_cocido": os.path.join("assets", "imagenes", "verduras_cocido.png"),
    "verduras_quemado": os.path.join("assets", "imagenes", "arroz_quemado.png"),

    "pollo": os.path.join("assets", "imagenes", "pollo_crudo.png"),
    "pollo_cocido": os.path.join("assets", "imagenes", "pollo_cocido.png"),
    "pollo_quemado": os.path.join("assets", "imagenes", "pollo_quemado.png"),

    "papas": os.path.join("assets", "imagenes", "papa_crudo.png"),
    "papas_cocido": os.path.join("assets", "imagenes", "papas_cocido.png"),
    "papas_quemado": os.path.join("assets", "imagenes", "papa_quemado.png"),

    "plato_limpio" : os.path.join("assets", "imagenes", "plato.png"),

    "Sushi" : os.path.join("assets", "imagenes", "receta_pescado.png"),
    "Shashimi": os.path.join("assets", "imagenes", "receta_sashimi.png"),

    "Papas": os.path.join("assets", "imagenes", "receta_papasfritas.png"),
    "Pizza": os.path.join("assets", "imagenes", "receta_pizza.png"),
    "Olla de carne": os.path.join("assets", "imagenes", "receta_olladecarne.png"),
    "Pinto": os.path.join("assets", "imagenes", "receta_pinto.png"),
    "Arroz con pollo": os.path.join("assets", "imagenes", "receta_arrozconpollo.png"),
    "Hamburguesa": os.path.join("assets", "imagenes", "receta_hamburguesa.png"),
}
recetas = {"Japonesa":
    {"Sushi":
        {"arroz":{"estado":"crudo","estacion":"olla"},
        "pescadosushi":{"estado":"sin_cortar","estacion":"tabla de cortar"},
        "alga":{"estado":"sin_cortar","estacion":"tabla de cortar"}},
    "Shashimi":
        {"pescado":{"estado":"sin_cortar","estacion":"tabla de cortar"}}},

"Gringa":
    {"Pizza":
        {"masa":{"estado":"crudo","estacion":"horno"},
        "salsa":{"estado":"crudo","estacion":"sarten"},
        "queso":{"estado":"crudo","estacion":"horno"}},
    "Hamburguesa": 
        {"pan":{"estado":"crudo","estacion":"horno"},
        "carne":{"estado":"crudo","estacion":"sarten"},
        "lechuga":{"estado":"sin_cortar","estacion":"tabla de cortar"},
        "tomate":{"estado":"sin_cortar","estacion":"tabla de cortar"}},
    "Papas":
        {"papas":{"estado":"crudo","estacion":"freidora"},},},

"Tica":
    {"Pinto":
        {"arroz":{"estado":"crudo","estacion":"olla"},
        "frijoles":{"estado":"crudo","estacion":"olla"},
        "huevo":{"estado":"crudo","estacion":"sarten"}},

    "Arroz con pollo":
        {"arroz":{"estado":"crudo","estacion":"olla"},
        "verduras":{"estado":"sin_cortar","estacion":"tabla de cortar"},
        "pollo":{"estado":"crudo","estacion":"sarten"}},

    "Olla de carne":
        {"verduras_cortado":{"estado":"crudo","estacion":"olla"},
        "carne":{"estado":"crudo","estacion":"olla"},}}}

TRANSICIONES_ESTACIONES={
    "arroz":         {"listo": "arroz_cocido",   "quemado": "arroz_quemado"},
    "arroz_cocido":  {"listo": "arroz_cocido",   "quemado": "arroz_quemado"},
    "pescadosushi": {"listo": "pescadosushi_cortado", "quemado": None},
    "alga":          {"listo": "alga_cortado",     "quemado": None},
    "pescado":       {"listo": "pescado_cortado",   "quemado": None},

    "masa":          {"listo": "masa_cocido",   "quemado": "masa_quemado"},
    "masa_cocido":  {"listo": "masa_cocido",   "quemado": "masa_quemado"},
    "salsa":         {"listo": "salsa_cocido", "quemado": "salsa_quemado"},
    "salsa_cocido":  {"listo": "salsa_cocido", "quemado": "salsa_quemado"},
    "queso":         {"listo": "queso_cocido", "quemado": "queso_quemado"},
    "queso_cocido":  {"listo": "queso_cocido", "quemado": "queso_quemado"},

    "pan":         {"listo": "pan_cocido",   "quemado": "pan_quemado"},
    "pan_cocido":    {"listo": "pan_cocido",   "quemado": "pan_quemado"},
    "carne":        {"listo": "carne_cocido",   "quemado": "carne_quemado"},
    "carne_cocido":  {"listo": "carne_cocido",   "quemado": "carne_quemado"},
    "lechuga":      {"listo": "lechuga_cortado", "quemado": None},
    "tomate":          {"listo": "tomate_cortado","quemado": None},

    "frijoles":         {"listo": "frijoles_cocido",   "quemado": "frijoles_quemado"},
    "frijoles_cocido":         {"listo": "frijoles_cocido",   "quemado": "frijoles_quemado"},
    "huevo":        {"listo": "huevo_cocido",   "quemado": "huevo_quemado"},
    "huevo_cocido":  {"listo": "huevo_cocido",   "quemado": "huevo_quemado"},

    "verduras":        {"listo": "verduras_cortado",   "quemado": None},
    "verduras_cortado": {"listo": "verduras_cocido", "quemado": "verduras_quemado"},
    "verduras_cocido":        {"listo": "verduras_cocido",   "quemado": "verduras_quemado"},

    "pollo":        {"listo": "pollo_cocido",   "quemado": "pollo_quemado"},
    "pollo_cocido":        {"listo": "pollo_cocido",   "quemado": "pollo_quemado"},

    "papas":        {"listo": "papas_cocido",   "quemado": "papas_quemado"},
    "papas_cocido":        {"listo": "papas_cocido",   "quemado": "papas_quemado"},
}
STATION_COLOR = (150, 75, 0)

TIEMPOS_ESTACION = {
    "freidora": {"min": 8,  "max": 15},
    "sarten":   {"min": 6,  "max": 12},
    "horno":    {"min": 10, "max": 18},
    "olla":     {"min": 8,  "max": 14},
    "tabla de cortar": {"min": 4, "max": 8},
    "cocina":   {"min": 7,  "max": 13},
    "plato_station":{"min":0, "max":0}
}

#Mapa de japones
#'.' = Suelo, 'M' = Mostrador, 'A' = Arroz, 'P' = Pescado Sushi, 'G' = Alga, 'F' = Pescado Normal
# 'O' = Olla, 'C' = Tabla de Cortar, 'E' = Entrega, 'R' = platos

MAPA_JAPONES = [
    ["M", "M", "A", "R", ".", "P", ".", ".", ],
    ["M", ".", ".", ".", ".", ".", ".", ".", ],
    ["M", ".", "M", "M", "O", ".", ".", ".", ],
    ["C", ".", ".", ".", ".", ".", "G", "F", ],
    ["M", ".", "M", ".", ".", "E", ".", ".", ],
]
#Mapa tico

MAPA_TICO = [
    ["A", "J", "M", "M", "P", "O", ".", ".",],
    ["M", ".", ".", ".", ".", ".", ".", "M",],
    ["C", ".", "M", "M", "M", "H", ".", "K",],
    ["M", ".", ".", ".", ".", ".", ".", "M",],
    ["M", "D", "S", "M", "F", "N", "E", ".",],
]
#Mapa gringo
#'.' = Suelo, 'M' = Mostrador, 'D' = Masa, 'I' = Salsa, 'P' = Pan, 
# 'N' = Carne. 'Q'= Queso, 'L' = Lechuga, 'T'= Tomate, 
# 'V'= Papas, 'S'= Sarten ,'H' = Horno, 'C' = Tabla de Cortar, 'E' = Entrega, 'R' = platos
MAPA_GRINGO = [
    ["L", "M", "M", ".", ".", "N", ".", ".",],
    ["P", ".", ".", "T", "R", ".", ".", ".",],
    ["V", ".", ".", "M", "I", "X", ".", "H",],
    ["D", ".", "F", "C", "S", "M", ".", "Q",],
    ["E", ".", "M", "M", "S", "M", "H", "M",],
]