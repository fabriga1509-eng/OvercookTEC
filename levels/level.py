import pygame
import os
from entities.recipe import Recipe
from entities.station import Station
from constants import STATION_WIDTH, STATION_HEIGHT, ancho_ventana, alto_ventana, MAPA_JAPONES,fondo_japones,MAPA_TICO,MAPA_GRINGO,fondo_tico,fondo_gringo


class Level:
    def __init__(self, num):
        self.num = num
        self.puntos = 0
        self.timer = 0 
        self.estaciones=[]
        fondo_actual=None
        self.usar_suelo = False
        fondos={
            1:fondo_japones,
            2:fondo_tico,
            3:fondo_gringo
        }
        #Cargamos los fondos
        if num in fondos:
            try:
                ruta = fondos[num]
                self.fondo_actual = pygame.image.load(ruta).convert()
                self.fondo_actual = pygame.transform.scale(self.fondo_actual, (ancho_ventana, alto_ventana))
                self.usar_suelo = True
            except pygame.error:
                print(f"No se encontró textura para el nivel {num}")
                self.usar_suelo = False
        
        if num == 1:#Nivel Japones
            #Se cargan las recetas y el mapa del nivel
            self.rcts = [Recipe("Japonesa", "Sushi"), Recipe("Japonesa", "Shashimi")]
            for fila_idx, fila in enumerate(MAPA_JAPONES):
                for col_idx, caracter in enumerate(fila):
                    x_pos = col_idx * STATION_WIDTH
                    y_pos = fila_idx * STATION_HEIGHT
                    
                    if caracter == "M":
                        self.estaciones.append(Station(x_pos, y_pos, "mostrador"))

                    elif caracter == "A":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "arroz"))

                    elif caracter == "P":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "pescadosushi"))

                    elif caracter == "G":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "alga"))

                    elif caracter == "F":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "pescado"))

                    elif caracter == "O":
                        self.estaciones.append(Station(x_pos, y_pos, "olla"))

                    elif caracter == "C":
                        self.estaciones.append(Station(x_pos, y_pos, "tabla de cortar"))

                    elif caracter == "D":
                        self.estaciones.append(Station(x_pos, y_pos, "platos"))

                    elif caracter == "E":
                        self.estaciones.append(Station(x_pos, y_pos, "entrega"))
                    elif caracter == "R":
                        self.estaciones.append(Station(x_pos, y_pos, "plato_station"))

        elif num == 2:#Fondo Tico
            self.rcts = [Recipe("Tica", "Pinto"), Recipe("Tica", "Arroz con pollo"), Recipe("Tica", "Olla de carne")]
            for fila_idx, fila in enumerate(MAPA_TICO):
                for col_idx, caracter in enumerate(fila):
                    x_pos = col_idx * STATION_WIDTH
                    y_pos = fila_idx * STATION_HEIGHT
                    
                    if caracter == "M":
                        self.estaciones.append(Station(x_pos, y_pos, "mostrador"))

                    elif caracter == "A":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "arroz"))

                    elif caracter == "J":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "frijoles"))
                    
                    elif caracter == "D":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "verduras"))
                    
                    elif caracter == "K":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "pollo"))
                    
                    elif caracter == "H":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "huevo"))
                    
                    elif caracter == "N":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "carne"))

                    elif caracter == "S":
                        self.estaciones.append(Station(x_pos, y_pos, "sarten"))

                    elif caracter == "F":
                        self.estaciones.append(Station(x_pos, y_pos, "freidora"))

                    elif caracter == "C":
                        self.estaciones.append(Station(x_pos, y_pos, "tabla de cortar"))

                    elif caracter == "O":
                        self.estaciones.append(Station(x_pos, y_pos, "olla"))

                    elif caracter == "E":
                        self.estaciones.append(Station(x_pos, y_pos, "entrega"))

                    elif caracter == "P":
                        self.estaciones.append(Station(x_pos, y_pos, "plato_station"))
            
        elif num == 3: #Fondo Gringo
            self.rcts = [Recipe("Gringa", "Pizza"), Recipe("Gringa", "Hamburguesa"), Recipe("Gringa", "Papas")]
            for fila_idx, fila in enumerate(MAPA_GRINGO):
                for col_idx, caracter in enumerate(fila):
                    x_pos = col_idx * STATION_WIDTH
                    y_pos = fila_idx * STATION_HEIGHT
                    
                    if caracter == "M":
                        self.estaciones.append(Station(x_pos, y_pos, "mostrador"))

                    elif caracter == "D":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "masa"))

                    elif caracter == "I":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "salsa"))

                    elif caracter == "P":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "pan"))

                    elif caracter == "N":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "carne"))
                    
                    elif caracter == "Q":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "queso"))

                    elif caracter == "L":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "lechuga"))

                    elif caracter == "T":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "tomate"))

                    elif caracter == "V":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "papas"))
                    
                    elif caracter == "O":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "pollo"))

                    elif caracter == "S":
                        self.estaciones.append(Station(x_pos, y_pos, "sarten"))

                    elif caracter == "F":
                        self.estaciones.append(Station(x_pos, y_pos, "freidora"))

                    elif caracter == "C":
                        self.estaciones.append(Station(x_pos, y_pos, "tabla de cortar"))

                    elif caracter == "H":
                        self.estaciones.append(Station(x_pos, y_pos, "horno"))

                    elif caracter == "E":
                        self.estaciones.append(Station(x_pos, y_pos, "entrega"))

                    elif caracter == "X":
                        self.estaciones.append(Station(x_pos, y_pos, "plato_station"))
        
    def tiempo_agotado(self):
        return self.timer >= self.tiempo
    def update(self, dt):
        self.timer += dt

    def draw(self, screen):
        if self.usar_suelo and self.fondo_actual:
            screen.blit(self.fondo_actual, (0, 0))
        else:
            screen.fill((30, 30, 30))

        for estacion in self.estaciones:
            estacion.draw(screen)