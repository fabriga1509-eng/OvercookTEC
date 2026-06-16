import pygame 
from constants import PLAYER_SPEED, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR, ancho_ventana, alto_ventana #Importamos las constantes necesarias para el jugador
class Player: #Creamos la clase Player para representar a los chefs en el juego
    
    def __init__(self,x,y,teclas,ruta_imagenPlayer): #El constructor recibe la posición inicial del jugador y las teclas asignadas para controlar al jugador
        self.rect = pygame.Rect(x,y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocidad = PLAYER_SPEED
        self.ingrediente = None
        self.teclas = teclas

        #Imagenes del chef
        self.sprite=pygame.image.load(ruta_imagenPlayer).convert_alpha()
        self.sprite=pygame.transform.scale(self.sprite, (self.rect.width, self.rect.height))
        self.usar_spite=True
        
    def mover(self,keys): #El método mover recibe las teclas presionadas y actualiza la posición del jugador en función de las teclas asignadas
        if keys[self.teclas['izquierda']]:
            self.rect.x -= self.velocidad
        if keys[self.teclas['derecha']]:
            self.rect.x += self.velocidad
        if keys[self.teclas['arriba']]:
            self.rect.y -= self.velocidad
        if keys[self.teclas['abajo']]:
            self.rect.y += self.velocidad
        #Limitar dentro de la ventana
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ancho_ventana:
            self.rect.right = ancho_ventana
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > alto_ventana:
            self.rect.bottom = alto_ventana

    def recoger(self,estación): #El método recoger recibe una estación y recoge el ingrediente de esa estación, asignándolo al jugador
        self.ingrediente = estación.entregar()

    def soltar(self,estación): #El método soltar recibe una estación y suelta el ingrediente que el jugador tiene en esa estación
        estación.recibir(self.ingrediente)
        self.ingrediente = None

    def interactuar(self,estaciones): #Metodo para interactuar con las estaciones
        for estacion in estaciones:
            if self.rect.colliderect(estacion.rect): #Verificamos si el jugador está colisionando con alguna estación
                if self.ingrediente is None:
                    self.recoger(estacion) #Si el jugador no tiene un ingrediente, lo recoge de la estación
                else:
                    self.soltar(estacion) #Si el jugador tiene un ingrediente, lo suelta en la estación
                break

    def update(self,keys): #El método update recibe las teclas presionadas y llama al método mover para actualizar la posición del jugador
        self.mover(keys)

    def draw(self, screen): #El método draw recibe la pantalla y dibuja al jugador
        if self.usar_spite:
            screen.blit(self.sprite,(self.rect.x,self.rect.y))
        else:
            pygame.draw.rect(screen, PLAYER_COLOR, self.rect) #Abi aquí puedes modificar el dibujo del jugador, cuando ya tengas el sprite cambia el rectángulo por el sprite del chef