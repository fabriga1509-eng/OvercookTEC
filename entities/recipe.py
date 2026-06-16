from constants import recetas #Importamos el diccionario

class Recipe: #Metodo para las recetas
    def __init__(self,cocina,platillo):
        self.nombre = platillo
        self.cocina = cocina
        self.ingredientes = recetas[cocina][platillo]
    def esta_completa(self, ingredientes_entregados):
        nombres = []
        for ingrediente in ingredientes_entregados:
            nombres.append(ingrediente.nombre)
        for requerido in self.ingredientes:
            if requerido not in nombres:
                return False
        return True