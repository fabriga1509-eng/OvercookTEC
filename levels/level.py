import pygame
import os
from entities.recipe import Recipe
from entities.station import Station
from constants import (
    TIEMPO_NIVEL, STATION_WIDTH, STATION_HEIGHT, 
    ancho_ventana, alto_ventana, MAPA_JAPONES,fondo_japones,piso
)


class Level:
    def __init__(self, num):
        self.tiempo = TIEMPO_NIVEL #Modifica si es necesario Abi
        self.num = num
        self.puntos = 0 #Modifica si es necesario Abi
        self.timer = 0 #Modifica si es necesario Abi
        self.estaciones=[]
        
        self.usar_suelo = False

        try:
            self.img_suelo = pygame.image.load(fondo_japones).convert_alpha()
            self.img_suelo = pygame.transform.scale(self.img_suelo, (STATION_WIDTH, STATION_HEIGHT))
            self.usar_suelo = True  
        except pygame.error:
            print("No se encontró textura_suelo.png. Usando color de respaldo.")
            self.usar_suelo = False 

        if num == 1:
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
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "pescado_sushi"))

                    elif caracter == "G":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "alga"))

                    elif caracter == "F":
                        self.estaciones.append(Station(x_pos, y_pos, "almacen", "pescado"))

                    elif caracter == "O":
                        self.estaciones.append(Station(x_pos, y_pos, "olla"))

                    elif caracter == "C":
                        self.estaciones.append(Station(x_pos, y_pos, "tabla de cortar"))

                    elif caracter == "D":
                        estacion = Station(x_pos, y_pos, "platos")
                        estacion.recetas = self.rcts
                        self.estaciones.append(Station(x_pos, y_pos, "platos"))

                    elif caracter == "E":
                        self.estaciones.append(Station(x_pos, y_pos, "entrega"))

        elif num == 2:
            self.rcts = [Recipe("Gringa", "Pizza"), Recipe("Gringa", "Hamburguesa"), Recipe("Gringa", "Smores")]
            self.estaciones = [Station(100, 100, "cocina"),
                Station(200, 100, "horno"),
                Station(300, 100, "tabla de cortar"),
                Station(100, 200, "almacen", "masa"),
                Station(200, 200, "almacen", "salsa"),
                Station(300, 200, "almacen", "queso"),
                Station(400, 200, "almacen", "pan"),
                Station(500, 200, "almacen", "carne"),
                Station(600, 200, "almacen", "lechuga"),
                Station(700, 200, "almacen", "tomate"),
                Station(100, 300, "almacen", "galleta"),
                Station(200, 300, "almacen", "malvavisco"),
                Station(300, 300, "almacen", "chocolate"),]
        elif num == 3:
            self.rcts = [Recipe("Tica", "Pinto"), Recipe("Tica", "Arroz con pollo"), Recipe("Tica", "Olla de carne")]
            self.estaciones = [Station(100, 100, "olla"),
                Station(200, 100, "cocina"),
                Station(300, 100, "sarten"),
                Station(400, 100, "tabla de cortar"),
                Station(100, 200, "almacen", "arroz"),
                Station(200, 200, "almacen", "frijoles"),
                Station(300, 200, "almacen", "huevo"),
                Station(400, 200, "almacen", "verduras"),
                Station(500, 200, "almacen", "pollo"),
                Station(600, 200, "almacen", "carne"),]
    def tiempo_agotado(self):
        return self.timer >= self.tiempo
    def update(self, dt):
        self.timer += dt

    def draw(self, screen):
        ancho_real=screen.get_width()
        alto_real=screen.get_height()
        if self.usar_suelo and self.img_suelo:
            piso_acomodado=pygame.transform.scale(self.img_suelo,(STATION_WIDTH,STATION_HEIGHT))

            for x in range(0, ancho_real, STATION_WIDTH):
                for y in range(0, alto_real, STATION_HEIGHT):
                    screen.blit(piso_acomodado, (x, y))
        else:
            screen.fill(piso) 

        for estacion in self.estaciones:
            estacion.draw(screen)