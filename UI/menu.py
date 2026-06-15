import pygame
import sys
import os
from constants import ancho_ventana, alto_ventana, gray, fuente_pixel, fondo_menu,boton_normal,boton_presionado

class MainMenu:
    def __init__(self):
        #fondo
        self.fondo=pygame.image.load(fondo_menu).convert()
        self.fondo=pygame.transform.scale(self.fondo, (ancho_ventana,alto_ventana))
        
        self.fuente_opciones = pygame.font.Font(fuente_pixel,30)
        self.boton_jugar = pygame.Rect(ancho_ventana // 2 - 140, 480, 280, 60)
        self.img_btn_normal = pygame.image.load(boton_normal).convert_alpha()
        self.img_btn_hover = pygame.image.load(boton_presionado).convert_alpha()

        #Transformar a la escala del boton
        self.img_btn_normal = pygame.transform.scale(self.img_btn_normal, (self.boton_jugar.width, self.boton_jugar.height))
        self.img_btn_hover = pygame.transform.scale(self.img_btn_hover, (self.boton_jugar.width, self.boton_jugar.height))
        self.usar_imagenes_boton = True

        
        

    def handle_events(self, events):
        #Cambio de ventana
        pos_mouse = pygame.mouse.get_pos()
        
        self.hover_jugar = self.boton_jugar.collidepoint(pos_mouse)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if self.hover_jugar:
                        return "GAME"  

                        
        return "MENU" 

    def update(self):
        """Aquí irían animaciones del menú si las hubiera."""
        pass

    def draw(self, surface):
        if self.fondo:
            surface.blit(self.fondo, (0, 0))
        else:
            surface.fill(gray) 

        # Seleccionamos la imagen dependiendo de si el mouse está encima o no
        imagen_actual = self.img_btn_hover if self.hover_jugar else self.img_btn_normal
        # Dibujamos la imagen usando la posición (x, y) de nuestro rectángulo
        surface.blit(imagen_actual, (self.boton_jugar.x, self.boton_jugar.y))
        


        texto_jugar = self.fuente_opciones.render("Jugar", True, (255, 255, 255))

        surface.blit(texto_jugar, (self.boton_jugar.centerx - texto_jugar.get_width() // 2, 
                                   self.boton_jugar.centery - texto_jugar.get_height() // 2))
        