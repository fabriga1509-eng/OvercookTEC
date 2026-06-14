from entities.recipe import Recipe
from entities.station import Station
from constants import TIEMPO_NIVEL

class Level:
    def __init__(self, num):
        self.tiempo = TIEMPO_NIVEL #Modifica si es necesario Abi
        self.num = num
        self.puntos = 0 #Modifica si es necesario Abi
        self.timer = 0 #Modifica si es necesario Abi
        if num == 1:
            self.rcts = [Recipe("Japonesa", "Sushi"), Recipe("Japonesa", "Shashimi")]
            self.estaciones = [Station(100, 100, "olla"),
                Station(200, 100, "cocina"),
                Station(300, 100, "tabla de cortar"),
                Station(100, 200, "almacen", "arroz"),
                Station(200, 200, "almacen", "pescado_sushi"),
                Station(300, 200, "almacen", "alga"),
                Station(400, 200, "almacen", "pescado"),]
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