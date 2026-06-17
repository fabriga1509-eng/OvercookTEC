import pygame
import sys
import random
from constants import ancho_ventana, alto_ventana, fps, titulo, CHEF1_TECLAS, CHEF2_TECLAS,chef1_img,chef2_img,fuente_pixel,recetas
from entities.player import Player
from levels.level import Level
from entities.order import Order
from entities.dish import Dish
from entities.recipe import Recipe
from UI.menu import MainMenu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
        pygame.display.set_caption(titulo)
        self.clock = pygame.time.Clock()
        self.running = True

        # Menú
        self.menu = MainMenu()
        self.estado_actual = "MENU"
        
        # Entidades base
        self.chef1 = Player(100, 100, CHEF1_TECLAS, chef1_img)
        self.chef2 = Player(200, 100, CHEF2_TECLAS, chef2_img)
        
        # Variables de Nivel (Se configuran en cargar_nivel)
        self.nivel_actual = 1
        self.estaciones = []
        self.nivel = None
        self.ordenes = []
        self.puntuacion = 0 
        self.spawn_timer = 0
        self.spawn_interval = 30 #Eleji 30s entre ordenes
        self.tiempo_nivel = 150 #Segundos por nivel
        #Cargar el primer nivel
        self.cargar_nivel(self.nivel_actual)

    def cargar_nivel(self, numero_nivel):
        self.nivel = Level(numero_nivel)
        self.estaciones = self.nivel.estaciones
        self.ordenes = [] #Limpiar órdenes viejas
        self.spawn_timer = 0 #Resetear timer de spawn
        self.tiempo_inicio = pygame.time.get_ticks() #Reinicia el reloj
        
        # Resetear chefs a posición inicial
        self.chef1.rect.topleft = (100, 100)
        self.chef2.rect.topleft = (300, 100)
        self.chef1.ingrediente = None # Manos vacías
        self.chef2.ingrediente = None
        for est in self.estaciones:
            est.reset() # Llama al reset interno de la estación

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                return

        if self.estado_actual == "MENU":
            nuevo_estado = self.menu.handle_events(events)
            if nuevo_estado == "GAME":
                self.estado_actual = "GAME"
                # Reiniciamos el tiempo al empezar la partida
                self.tiempo_inicio = pygame.time.get_ticks()

        elif self.estado_actual == "GAME":
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n: #K para saltar nivel
                        print("Saltar nivel")
                        self.cambiar_nivel()
                    # Chef 1 Interactuar
                    if event.key == self.chef1.teclas["interactuar"]:
                        estacion_cerca = self.obtener_estacion_cercana(self.chef1)
                        if estacion_cerca and estacion_cerca.tipo == "entrega":
                            self.procesar_entrega(self.chef1)
                        else:
                            self.chef1.interactuar(self.estaciones)
                    elif event.key == self.chef1.teclas.get("desechar", pygame.K_t): #Intento de desechar ingrdiente pero se sigue viendo el sprite
                        if self.chef1.recoger is not None: 
                            self.chef1.recoger = None

                    # Chef 2 Interactuar
                    if event.key == self.chef2.teclas["interactuar"]:
                        estacion_cerca = self.obtener_estacion_cercana(self.chef2)
                        if estacion_cerca and estacion_cerca.tipo == "entrega":
                            self.procesar_entrega(self.chef2)
                        else:
                            self.chef2.interactuar(self.estaciones)
                    elif event.key == self.chef2.teclas.get("desechar", pygame.K_BACKSPACE):
                        if self.chef2.recoger is not None: 
                            self.chef2.recoger = None

    def update(self):
        dt_ms = self.clock.get_time()
        dt = dt_ms / 1000 #Tiempo para las barras

        if self.estado_actual == "MENU":
            self.menu.update()
            return #No hacer nada si esta en el menu

        if self.estado_actual == "GAME":
            #Temporizador
            tiempo_pasado_seg = (pygame.time.get_ticks() - self.tiempo_inicio) // 1000
            self.tiempo_restante = max(0, self.tiempo_nivel - tiempo_pasado_seg)

            if self.tiempo_restante <= 0:
                self.cambiar_nivel()
                return 

            #actualizar entities
            keys = pygame.key.get_pressed()
            self.chef1.update(keys)
            self.chef2.update(keys)
            self.nivel.update(dt)

            for estacion in self.estaciones:
                estacion.update(dt)

            #Spawn de Órdenes
            self.spawn_timer += dt
            # Genera orden si pasa el tiempo o si no hay ninguna
            if self.spawn_timer >= self.spawn_interval or len(self.ordenes) == 0:
                self.spawn_timer = 0

                if self.nivel_actual == 1:
                    cultura = "Japonesa"
                elif self.nivel_actual == 2:
                    cultura = "Tica"
                elif self.nivel_actual == 3:
                    cultura = "Gringa"
                
                #Selecciona un platillo al azar
                recetas_disponibles = list(recetas[cultura].keys())
                if recetas_disponibles:
                    platillo_aleatorio = random.choice(recetas_disponibles)
                    
                    #Crear la orden
                    nueva_receta = Recipe(cultura, platillo_aleatorio)
                    nueva_orden = Order(nueva_receta)
                    self.ordenes.append(nueva_orden)

            #Actualizar Órdenes Activas
            for orden in self.ordenes[:]:
                orden.update(dt, self) # Pasamos 'self' (Game) para restar puntos si expira
                if orden.eliminada or orden.completada:
                    self.ordenes.remove(orden)

    def cambiar_nivel(self):
        print(f"Nivel {self.nivel_actual} completado. Puntuación: {self.puntuacion}")
        
        #Aqui va pantalla de resultados
        
        self.nivel_actual += 1
        self.puntuacion = 0 
        
        #Cargar el mapa nuevo
        self.cargar_nivel(self.nivel_actual)

    def draw(self):
        self.screen.fill((0, 0, 0)) 

        if self.estado_actual == "MENU":
            self.menu.draw(self.screen)

        elif self.estado_actual == "GAME":
            #Fondo del nivel
            self.nivel.draw(self.screen)
            
            #Estaciones
            for estacion in self.estaciones:
                estacion.draw(self.screen)
                
            #Chefs (con sus ingredientes flotantes)
            self.chef1.draw(self.screen)
            self.chef2.draw(self.screen)
            
            #Tabla de ordenes
            ancho_p = self.screen.get_width()
            margen_derecho = 20
            pos_x_hud = ancho_p - margen_derecho
            
            fuente_hud = pygame.font.SysFont(fuente_pixel, 24, bold=True)
            
            txt_score = fuente_hud.render(f"Puntos: {self.puntuacion}", True, (255, 255, 0))
            rect_score = txt_score.get_rect()
            rect_score.topright = (pos_x_hud, 20)
            self.screen.blit(txt_score, rect_score)
            
            pos_y_inicial_ordenes = 60
            espaciado_ordenes = 90
            ancho_tarjeta_orden = 210 
            
            for i, orden in enumerate(self.ordenes):
                x_orden = ancho_p - ancho_tarjeta_orden - margen_derecho
                y_orden = pos_y_inicial_ordenes + (i * espaciado_ordenes)
                orden.draw(self.screen, x_orden, y_orden)
            
            #Tiempo en la otra esquna
            fuente_tiempo = pygame.font.SysFont(fuente_pixel, 36, bold=True)
            
            #Cambiar color a rojo si queda poco tiempo 
            color_tiempo = (255, 255, 255)
            if self.tiempo_restante < 15: color_tiempo = (231, 76, 60)
            
            img_tiempo = fuente_tiempo.render(f" {self.tiempo_restante}", True, color_tiempo)
            self.screen.blit(img_tiempo, (20, 20))

        pygame.display.flip()

    def obtener_estacion_cercana(self, chef):
        #Colicion con alguna estacion
        area_deteccion = chef.rect.inflate(10, 10)
        for estacion in self.estaciones:
            if area_deteccion.colliderect(estacion.rect):
                return estacion
        return None
    
    def procesar_entrega(self, chef):
        if isinstance(chef.ingrediente, Dish):
            plato_chef = chef.ingrediente
            
            #Ver si el plato esta vacio
            if len(plato_chef.ingredientes) == 0:
                 return

            for orden in self.ordenes:
                #Comparar la receta
                if orden.receta.esta_completa(plato_chef.ingredientes):
                    self.puntuacion += orden.puntuacion
                    orden.completar() 
                    chef.ingrediente = None 
                    #Sonido de completado
                    return
            
        else:
            print("Falta plato")

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(fps) 
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()