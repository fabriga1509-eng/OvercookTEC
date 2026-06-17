import pygame
from constants import fuente_pixel
class Order:
    def __init__(self, receta_objeto): 
        self.receta = receta_objeto
        self.nombre = receta_objeto.nombre
        self.ingredientes_requeridos = receta_objeto.ingredientes_esperados
        
        #Puntuacion de la receta (Mas complicada,mas puntos)
        num_ingredientes = len(self.ingredientes_requeridos)
        self.valor_original = num_ingredientes * 100
        self.puntuacion = self.valor_original
        self.tiempo_limite = num_ingredientes * 25.0 
        
        self.timer = 0
        self.completada = False
        self.eliminada = False

    #Vigila el tiempo y quitar la mitad de los puntos
    def update(self, dt, game_manager):
        if self.completada or self.eliminada:
            return

        self.timer += dt
        
        if self.timer >= self.tiempo_limite: #Se cumple el tiempo maximo de la receta
            self.puntuacion //= 2  # La puntuación se reduce a la mitad
            self.timer = 0        # Se reinicia el reloj
            
            if self.puntuacion <= 0: #si el jugador tiene puntos y se le acaba la posible puntiacion para la receta
                self.eliminada = True
                # Se le restan los puntos de su puntaje
                game_manager.puntaje = max(0, game_manager.puntaje - self.valor_original)

    def esta_expirada(self):
        return self.puntuacion <= 0

    def completar(self):
        self.completada = True

    def draw(self, screen, x, y): #Cuadro de recetas
        ancho, alto = 180, 75
        pygame.draw.rect(screen, (245, 240, 220), (x, y, ancho, alto))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, ancho, alto), 2)
        
        fuente_titulo = pygame.font.SysFont(fuente_pixel, 20, bold=True)
        fuente_detalles = pygame.font.SysFont(fuente_pixel, 16)

        # Nombre de la receta
        txt_nombre = fuente_titulo.render(f"{self.nombre}", True, (0, 0, 0))
        
        #Color del precio, verde si no perdio valor, rojo si ya se lo hizo
        color_precio = (46, 204, 113) if self.puntuacion == self.valor_original else (231, 76, 60)
        txt_puntos = fuente_titulo.render(f"${self.puntuacion}", True, color_precio)
        
        screen.blit(txt_nombre, (x + 10, y + 8))
        screen.blit(txt_puntos, (x + ancho - txt_puntos.get_width() - 10, y + 8))

        #Barra de tiempode la receta
        pct_tiempo = max(0.0, min(1.0, 1.0 - (self.timer / self.tiempo_limite)))
        color_barra = (241, 196, 15) if self.puntuacion == self.valor_original else (231, 76, 60)
        
        #Fondo gris oscuro de la barrita
        pygame.draw.rect(screen, (100, 100, 100), (x + 10, y + 32, ancho - 20, 6))
        #Relleno amarillo/rojo que se encoge
        pygame.draw.rect(screen, color_barra, (x + 10, y + 32, int((ancho - 20) * pct_tiempo), 6))

        nombres_limpios = [i.split('_')[0] for i in self.ingredientes_requeridos]
        txt_ingredientes = fuente_detalles.render(", ".join(nombres_limpios), True, (70, 70, 70))
        screen.blit(txt_ingredientes, (x + 10, y + 48))