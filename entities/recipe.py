from constants import recetas #Importamos el diccionario

class Recipe: #Metodo para las recetas
    def __init__(self,cocina,platillo):
        self.nombre = platillo
        self.cocina = cocina
        self.ingredientes_base = recetas[cocina][platillo]
        
        self.ingredientes_esperados = []
        for ing, info in self.ingredientes_base.items():
            if info["estacion"] in ["olla","sarten","horno","freidora"]:
                self.ingredientes_esperados.append(f"{ing}_cocido")
            elif info["estacion"] in ["tabla de cortar", "cocina"]:
                self.ingredientes_esperados.append(f"{ing}_cortado")
            
    def esta_completa(self,ingredientes_entregados):
        #Comprobacion pq en olla de carne hay que cortar y cocinar entonces se concatena
        esperados_limpios = []
        for e in self.ingredientes_esperados:
            nombre_limpio = e.replace("_cortado_cocido", "_cocido")
            esperados_limpios.append(nombre_limpio)
        
        esperados_ordenados = sorted(esperados_limpios)
        entregados_ordenados = sorted(ingredientes_entregados)
        
        return esperados_ordenados == entregados_ordenados
    def _str_ (self):
        return self.nombre