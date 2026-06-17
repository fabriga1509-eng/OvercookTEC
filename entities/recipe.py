from constants import recetas #Importamos el diccionario

class Recipe: #Metodo para las recetas
    def __init__(self,cocina,platillo):
        self.nombre = platillo
        self.cocina = cocina
        self.ingredientes_base = recetas[cocina][platillo]
        
        self.ingredientes_esperados = []
        for ing, info in self.ingredientes_base.items():
            if info["estacion"] == "olla":
                self.ingredientes_esperados.append(f"{ing}_cocido")
            elif info["estacion"] in ["tabla de cortar", "cocina"]:
                self.ingredientes_esperados.append(f"{ing}_cortado")
            elif info["estacion"] == "sarten":
                self.ingredientes_esperados.append(f"{ing}_cocido")
            elif info["estacion"] == "freido":
                self.ingredientes_esperados.append(f"{ing}_cocido")
            
    def esta_completa(self,ingredientes_entregados):
        if len(ingredientes_entregados) != len(self.ingredientes_esperados):
            return False
            
        #ver si el chef tiene en la mano una receta
        for esperado in self.ingredientes_esperados:
            if esperado not in ingredientes_entregados:
                return False
        return True  # si pasó todos, está completa
    def _str_ (self):
        return self.nombre