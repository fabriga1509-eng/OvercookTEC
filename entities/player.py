import pygame 
from constants import recetas,PLAYER_SPEED, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR,SPRITES_INGREDIENTES, ancho_ventana, alto_ventana #Importamos las constantes necesarias para el jugador
from entities.dish import Dish
class Player: #Creamos la clase Player para representar a los chefs en el juego
    
    def __init__(self,x,y,teclas,ruta_imagenPlayer): #El constructor recibe la posición inicial del jugador y las teclas asignadas para controlar al jugador
        self.rect = pygame.Rect(x,y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocidad = PLAYER_SPEED
        self.ingrediente = None
        self.teclas = teclas

        #Imagenes del chef
        self.sprite=pygame.image.load(ruta_imagenPlayer).convert_alpha()
        self.sprite=pygame.transform.scale(self.sprite, (self.rect.width, self.rect.height))
        self.usar_sprite=True
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

    def recoger(self,estación): 
        #El método recoger recibe una estación y recoge el ingrediente de esa estación
        if estación.tipo == "almacen":
            self.ingrediente = estación.tipo_ingrediente
        
        # Si es cualquier otra estación que tenga algo listo encima
        elif estación.ingrediente is not None:
            self.ingrediente = estación.entregar()

    def soltar(self,estación): #recibe una estación y suelta el ingrediente que el jugador tiene en esa estación
        #para que no se pueda devolver al almacen
        if estación.tipo == "almacen":
            return

        # Solo podemos soltar si la mesa o estación está vacía
        if estación.ingrediente is None:
            es_plato = isinstance(self.ingrediente, Dish)
            estaciones_cocina = ["olla", "tabla de cortar", "sarten", "horno", "freido"]

            #Para que no se pueda poner  un ingrediente en una estacion que no
            if es_plato and hasattr(estación, 'tipo') and estación.tipo in estaciones_cocina:
                return

            #Se busque a que estacion pertenence ese ingrediente
            if hasattr(estación, 'tipo') and estación.tipo in estaciones_cocina:
                ingrediente_actual = self.ingrediente
                estaciones_validas = set()
                for cultura, platos in recetas.items():
                    for plato, ingredientes_receta in platos.items():
                        if ingrediente_actual in ingredientes_receta:
                            info_ing = ingredientes_receta[ingrediente_actual]
                            estacion_destino = info_ing.get("estacion") or info_ing.get("estación")
                            if estacion_destino:
                                estaciones_validas.add(estacion_destino)

                #Si no es la estacion correcta
                if len(estaciones_validas) > 0:
                    if estación.tipo not in estaciones_validas:
                        opciones = " o ".join(estaciones_validas)
                        return

                #Si ya se cocino no lo permite volver a cocinar
                elif "_" in str(ingrediente_actual):
                    return

            #Si es ingrediente normal se pone en el mostrador
            estación.ingrediente = self.ingrediente
            
            #Vaciar la mano del chef
            self.ingrediente = None
            
            #Activar la estacion
            estación.activa = True
        else:
            print("Esta estación ya está ocupada.")

    def interactuar(self,estaciones): #Metodo para interactuar con las estaciones
        for estacion in estaciones:
            #Ver si esta tocando la mesa
            if self.rect.colliderect(estacion.rect) or self.rect.inflate(10, 10).colliderect(estacion.rect):
                
                #Si son los platos
                if estacion.tipo == "plato_station":
                    if self.ingrediente is None:
                        self.ingrediente = Dish(receta=None, ingredientes=[])
                        return 
                    elif isinstance(self.ingrediente, Dish) and len(self.ingrediente.ingredientes) == 0:
                        self.ingrediente = None
                        return
                
                #Si tienes un plato y quieres recoger un ingrdiente listo
                if estacion.ingrediente is not None and "_" in str(estacion.ingrediente):
                    if isinstance(self.ingrediente, Dish):
                        if len(self.ingrediente.ingredientes) < 4:
                            self.ingrediente.ingredientes.append(estacion.ingrediente)
                            self.ingrediente.verificar_receta_actual()
                            estacion.ingrediente = None  
                            return
                        else:
                            print("El plato ya está lleno.")
                            return

                #Poner plato mostrador
                if estacion.ingrediente is None and isinstance(self.ingrediente, Dish):
                    if estacion.tipo not in ["entrega", "plato_station"]: 
                        estacion.ingrediente = self.ingrediente 
                        self.ingrediente = None
                        return

                #Ingrediente normal en el mostrador
                if self.ingrediente is None:
                    self.recoger(estacion)
                else:
                    self.soltar(estacion)
                
                return 

    def update(self,keys): 
        self.mover(keys)

    def draw(self, screen): 
        
        #Dibujar lo que lleva en las manos
        if self.ingrediente is not None:
            es_plato = isinstance(self.ingrediente, Dish)
            
            #Comprobacion de emergencia
            if es_plato:
                ing_ordenados = sorted(self.ingrediente.ingredientes)
                if ing_ordenados == sorted(['arroz_cocido', 'pescadosushi_cortado', 'alga_cortado']):
                    self.ingrediente.receta = "Sushi"
                elif ing_ordenados == sorted(['pescado_cortado']):
                    self.ingrediente.receta = "Shashimi"
                else:
                    self.ingrediente.receta = None

            #Ver si el plato ya tiene una receta armada
            receta_completada = es_plato and self.ingrediente.receta is not None
            
            #Si es un plato no terminado
            if isinstance(self.ingrediente, list) or (es_plato and not receta_completada and len(self.ingrediente.ingredientes) > 0):
                lista_items = self.ingrediente.ingredientes if es_plato else self.ingrediente
                num_actual = len(lista_items)
                
                #Cuadros fallidos
                slots_totales = min(4, num_actual + 1)
                
                t_cuadro = 40 
                espacio = 5
                ancho_total = (slots_totales * t_cuadro) + ((slots_totales - 1) * espacio)
                
                inicio_x = self.rect.centerx - (ancho_total // 2)
                inicio_y = self.rect.top - 55  
                
                for i in range(slots_totales):
                    x_slot = inicio_x + i * (t_cuadro + espacio)
                    y_slot = inicio_y

                    #cuadros fallidos :(
                    #pygame.draw.rect(screen, (220, 220, 220), (x_slot, y_slot, t_cuadro, t_cuadro))
                    #pygame.draw.rect(screen, (0, 0, 0), (x_slot, y_slot, t_cuadro, t_cuadro), 2)

                    #sprite del ingrediente del plato
                    if i < num_actual:
                        ing = lista_items[i]
                        if ing in SPRITES_INGREDIENTES:
                            try:
                                img = pygame.image.load(SPRITES_INGREDIENTES[ing]).convert_alpha()
                                img = pygame.transform.scale(img, (t_cuadro + 60, t_cuadro + 60))
                                screen.blit(img, (x_slot + 10, y_slot - 25))
                            except pygame.error:
                                pygame.draw.rect(screen, (245, 130, 48), (x_slot + 2, y_slot + 2, t_cuadro - 6, t_cuadro - 6))
            
            #Plato Completo
            else:
                t_sprite = 128  
                pos_x = self.rect.centerx - (t_sprite // 2)
                pos_y = self.rect.top - t_sprite + 50

                if es_plato:
                    if receta_completada:
                        clave_buscar = self.ingrediente.receta
                    else:
                        clave_buscar = "plato_limpio"
                else:
                    clave_buscar = self.ingrediente

                #Buscar el sprite del ingrediente
                if clave_buscar in SPRITES_INGREDIENTES:
                    ruta_imagen = SPRITES_INGREDIENTES[clave_buscar]
                    try:
                        imagen_item = pygame.image.load(ruta_imagen).convert_alpha()
                        imagen_item = pygame.transform.scale(imagen_item, (t_sprite, t_sprite))
                        screen.blit(imagen_item, (pos_x, pos_y))
                    except pygame.error:
                        pygame.draw.rect(screen, (245, 130, 48), (pos_x, pos_y, 25, 25))
                else:
                    pygame.draw.rect(screen, (245, 130, 48), (pos_x, pos_y, 25, 25))
        #Chef
        if self.usar_sprite:
            screen.blit(self.sprite, (self.rect.x, self.rect.y))
        else:
            pygame.draw.rect(screen, PLAYER_COLOR, self.rect)
        