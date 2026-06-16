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
        if estación.tipo == "almacen":
            self.ingrediente = estación.tipo_ingrediente  # Ej: "arroz", "pescado"
            print(f"🎒 Sacaste {self.ingrediente} del almacén.")
        
        # Si es cualquier otra estación (mesas, ollas) que tenga algo listo encima
        elif estación.ingrediente is not None:
            # Usamos el método que programó tu equipo para extraerlo de forma segura
            self.ingrediente = estación.entregar()
            print(f"✋ Recogiste {self.ingrediente} de la estación {estación.tipo}.")

    def soltar(self,estación): #El método soltar recibe una estación y suelta el ingrediente que el jugador tiene en esa estación
        # Evitamos que dejen basura o regresen comida al almacén de suministros
        if estación.tipo == "almacen":
            print("❌ No puedes devolver ingredientes al almacén.")
            return

        # Solo podemos soltar si la mesa o estación está completamente vacía
        if estación.ingrediente is None:
            estación.ingrediente = self.ingrediente
            print(f"🧺 Dejaste {self.ingrediente} en la estación {estación.tipo}.")
            
            # Vaciamos la mano del chef
            self.ingrediente = None
            
            # Activamos la estación por si requiere cocinar (olla) o picar (tabla)
            estación.activa = True
        else:
            print("❌ Esta estación ya está ocupada.")

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
        
        if self.ingrediente!=None:
            pos_x = self.rect.centerx - 10
            pos_y = self.rect.top - 22  # Flota 22 píxeles arriba de la cabeza del chef
            
            # Dibujamos un cuadrito naranja que representa temporalmente el ingrediente
            pygame.draw.rect(screen, (245, 130, 48), (pos_x, pos_y, 20, 20))