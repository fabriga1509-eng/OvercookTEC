#Importamos lo necesario
import pygame
import os
from constants import recetas, STATION_WIDTH,STATION_HEIGHT,TIEMPOS_ESTACION,STATION_COLOR

#from ingredientes import 

#Definimos la clase station
class Station:
    def __init__(self,x,y,tipo,tipo_ingrediente=None):
        self.rect = pygame.Rect(x, y, STATION_WIDTH, STATION_HEIGHT)
        self.tipo = tipo
        self.ingrediente = None
        self.timer = 0
        self.activa = False
        if tipo == "almacen":
            self.stock = 10000
            self.tipo_ingrediente = tipo_ingrediente
        elif tipo in ["mostrador","platos","entrega"]:
            self.tiempo_min = 0
            self.tiempo_max = 0
        else:
            self.tiempo_min = TIEMPOS_ESTACION[tipo]["min"]
            self.tiempo_max = TIEMPOS_ESTACION[tipo]["max"]

        imgs_estaciones={
        "freidora": "estacion_freidora.png",
        "sarten":   "estacion_sarten.png",
        "horno":    "estacion_horno.png",
        "olla":     "estacion_olla.png",
        "tabla de cortar": "estacion_picar.png",
        "cocina":  "estacion_picar.png",
        "mostrador": "estacion_pared.png"
        }

        # Lógica especial para los almacenes (cajas de ingredientes)
        if self.tipo == "almacen":
            #si es un almacén, intentamos buscar una imagen específica para ese ingrediente
            nombre_img = f"almacen_{self.tipo_ingrediente}.png"
        else:
            #Si no es almacén, buscamos en el diccionario. Si no existe, usa la mesa normal
            nombre_img = imgs_estaciones.get(self.tipo, "estacion_pared.png")
        ruta_img = os.path.join("assets", "imagenes", nombre_img)
        try:
            self.sprite = pygame.image.load(ruta_img).convert_alpha()
            factor_escala = 4 
            nuevo_ancho = 32 * factor_escala
            nuevo_alto = 32 * factor_escala
    
            #Escalamos la imagen al nuevo tamaño grande
            self.sprite = pygame.transform.scale(self.sprite, (nuevo_ancho, nuevo_alto))
            self.usar_sprite = True
        except pygame.error:
            print(f"No se pudo cargar {ruta_img}. Usando color sólido de respaldo.")
            self.usar_sprite = False
        # ========================================================
    def recibir(self, ingrediente):
        if ingrediente.estacion == self.tipo:
            self.ingrediente = ingrediente
            self.activa = True #Modifica si es necesario Abi

    def entregar(self):
        ingrediente = self.ingrediente
        self.ingrediente = None
        self.activa = False
        self.timer = 0
        return ingrediente #Modifica si es necesario Abi
    
    def update(self, dt):
        if self.activa and self.ingrediente is not None:
            self.timer += dt
            if self.timer >= self.tiempo_max:        # ← adentro del if self.activa
                self.ingrediente.estado = "quemado"
            elif self.timer >= self.tiempo_min:      # ← adentro del if self.activa
                self.ingrediente.estado = "preparado" #Modifica si es necesario Abi
    def draw(self, screen): #Modifica si es necesario Abi
        # Si la imagen se cargó con éxito, la dibujamos
        if self.usar_sprite:
            screen.blit(self.sprite, (self.rect.x, self.rect.y))
        else:
            # Si la imagen no existe, se dibuja el rectángulo original de tus compañeros
            pygame.draw.rect(screen, STATION_COLOR, self.rect)

