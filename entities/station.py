import pygame
import os
from constants import recetas, STATION_WIDTH,STATION_HEIGHT,TIEMPOS_ESTACION,SPRITES_INGREDIENTES,TRANSICIONES_ESTACIONES,imgs_estaciones,fuente_pixel
from entities.dish import Dish
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
        elif tipo in ["mostrador","platos","entrega","plato_station"]:
            self.tiempo_min = 0
            self.tiempo_max = 0
        else:
            self.tiempo_min = TIEMPOS_ESTACION[tipo]["min"]
            self.tiempo_max = TIEMPOS_ESTACION[tipo]["max"]

        

        #Almacenes
        if self.tipo == "almacen":
            #buscar la img si es almacen
            nombre_img = f"almacen_{self.tipo_ingrediente}.png"
        else:
            #buscar que estacion es, si no es ninguna es un mostrador
            nombre_img = imgs_estaciones.get(self.tipo, "estacion_pared.png")
        ruta_img = os.path.join("assets", "imagenes", nombre_img)

        #Trata de cargar la img si no puede pone un color solido para que no se caiga el programa
        try:
            self.sprite = pygame.image.load(ruta_img).convert_alpha()
            factor_escala = 4 
            nuevo_ancho = 32 * factor_escala
            nuevo_alto = 32 * factor_escala
    
            #escalar img
            self.sprite = pygame.transform.scale(self.sprite, (nuevo_ancho, nuevo_alto))
            self.usar_sprite = True
        except pygame.error:
            print(f"No se pudo cargar {ruta_img}. Usando color sólido de respaldo.")
            self.usar_sprite = False

    def recibir(self, ingrediente):
        if ingrediente.estacion == self.tipo:
            self.ingrediente = ingrediente
            self.activa = True 
    def reset(self):
        #Limpia todo
        self.ingrediente = None
        self.timer = 0.0
        self.procesando = False 

    def entregar(self):
        #Para sacar un ingrediente de un almacen
        item_retornado = self.ingrediente
        self.ingrediente = None
        self.timer = 0
        self.activa = False
        
        if hasattr(self, 'progreso'):
            self.progreso = 0
        if hasattr(self, 'tiempo_coccion'):
            self.tiempo_coccion = 0
        if hasattr(self, 'tiempo_corte'):
            self.tiempo_corte = 0
        if hasattr(self, 'cocinado'):
            self.cocinado = False
        if hasattr(self, 'listo'):
            self.listo = False
        if hasattr(self, 'barra_visible'):
            self.barra_visible = False
        if hasattr(self, 'color_barra'):
            self.color_barra = (255, 0, 0) 
            
        return item_retornado
    
    def update(self, dt):
        if self.tipo in ["mostrador", "almacen", "entrega", "platos", "plato_station"]:
            return
    
        if self.activa and self.ingrediente is not None: 
            
            from constants import TIEMPOS_ESTACION, TRANSICIONES_ESTACIONES
            
            #Verificar que la estación y el ingrediente existan
            if self.tipo in TIEMPOS_ESTACION and self.ingrediente in TRANSICIONES_ESTACIONES:
                t_min = TIEMPOS_ESTACION[self.tipo]["min"]
                t_max = TIEMPOS_ESTACION[self.tipo]["max"]
                config = TRANSICIONES_ESTACIONES[self.ingrediente]
                
                #Avanzart el relog solo si la barra esta activa
                self.timer += dt

                #Cocinar o picar
                if self.timer >= t_min and self.timer < t_max:
                    if self.ingrediente != config["listo"]:
                        self.ingrediente = config["listo"]
                    
                    #Si el ingrediente NO se quema, se apaga la estación
                    if config["quemado"] is None:
                        self.activa = False
                        self.timer = t_min # Bloqueamos la barra al máximo

                #Se quema
                elif self.timer >= t_max and config["quemado"] is not None:
                    self.ingrediente = config["quemado"]
                    self.activa = False # Se apaga al destruirse la comida

    def draw(self, screen): #Modifica si es necesario Abi
        #Si la imagen cargo bien 
        if hasattr(self, 'usar_sprite') and self.usar_sprite:
            screen.blit(self.sprite, (self.rect.x, self.rect.y))
        else:
            #Cuadro gris si no funciona la img para que no crashee el juego
            print("adios")
            pygame.draw.rect(screen, (100, 100, 100), self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
            
            fuente = pygame.font.SysFont(fuente_pixel, 10, bold=True)
            txt = fuente.render(self.tipo.upper(), True, (255, 255, 255))
            screen.blit(txt, (self.rect.x + 2, self.rect.y + 15))

        if self.ingrediente is not None:
            t_sprite = 128
            centro_x = self.rect.centerx - (t_sprite // 2)
            centro_y = self.rect.centery - (t_sprite // 2)

            if isinstance(self.ingrediente, Dish):
                #Si la receta esta completa se actualiza el sprite por la receta
                if self.ingrediente.receta is not None:
                    clave_buscar = self.ingrediente.receta
                else:
                    clave_buscar = "plato_limpio"
            else:
                clave_buscar = self.ingrediente

            if clave_buscar in SPRITES_INGREDIENTES:
                ruta_imagen = SPRITES_INGREDIENTES[clave_buscar]
                try:
                    imagen_item = pygame.image.load(ruta_imagen).convert_alpha()
                    imagen_item = pygame.transform.scale(imagen_item, (t_sprite, t_sprite))
                    screen.blit(imagen_item, (centro_x, centro_y))
                except pygame.error:
                    pygame.draw.rect(screen, (245, 130, 48), (centro_x, centro_y, 20, 20))
            else:
                pygame.draw.rect(screen, (245, 130, 48), (centro_x, centro_y, 20, 20))

        if self.tipo in ["olla", "sarten", "tabla de cortar","horno","freidora"]: #barra de progreso
            #posicion de la barra
            barra_ancho = 64
            barra_alto = 10
            barra_x = self.rect.centerx - (barra_ancho // 2)
            barra_y = self.rect.top +10  

            # Definición de Colores (RGB)
            COLOR_FONDO = (50, 50, 50)       
            COLOR_BORDE = (0, 0, 0)        
            
            if self.timer < self.tiempo_min:
                #Barra de progreso para prepararse
                color_barra = (160, 160, 160) 
                porcentaje = self.timer / self.tiempo_min if self.tiempo_min > 0 else 0
                
            elif self.timer >= self.tiempo_min and self.timer < self.tiempo_max:
                #Barra de listo
                color_barra = (46, 204, 113)  
                #Reinicio de la barra para quemarse
                rango_quemado = self.tiempo_max - self.tiempo_min
                tiempo_transcurrido_verde = self.timer - self.tiempo_min
                porcentaje = tiempo_transcurrido_verde / rango_quemado if rango_quemado > 0 else 0

            else: #Barra roja
                color_barra = (231, 76, 60)   
                porcentaje = 1.0              

            #Barra de progreso
            porcentaje = max(0.0, min(1.0, porcentaje))
            pygame.draw.rect(screen, COLOR_FONDO, (barra_x, barra_y, barra_ancho, barra_alto))
            ancho_dinamico = int(barra_ancho * porcentaje)
            if ancho_dinamico > 0:
                pygame.draw.rect(screen, color_barra, (barra_x, barra_y, ancho_dinamico, barra_alto))
            pygame.draw.rect(screen, COLOR_BORDE, (barra_x, barra_y, barra_ancho, barra_alto), 2)
                
