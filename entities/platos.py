import pygame

class EstacionPlatos:
    def __init__(self, x, y, ancho=48, alto=48):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.tipo = "plato_estacion"
        # Si tienes un sprite para la mesa de platos lo cargas aquí, si no, usamos un color de respaldo
        self.color = (149, 165, 166) # Gris piedra de mostrador

    def update(self, dt):
        pass # No necesita actualizar nada en el tiempo

    def draw(self, screen):
        # Dibuja la estación (Cambia esto por tu blit de sprite cuando lo tengas)
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2) # Borde
        
        # Mini indicador visual de que es de platos
        fuente = pygame.font.SysFont("Arial", 12, bold=True)
        txt = fuente.render("PLATOS", True, (255, 255, 255))
        screen.blit(txt, (self.rect.x + 2, self.rect.y + 18))