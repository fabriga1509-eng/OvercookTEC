from constants import recetas #Importamos el diccionario

class Recipe: #Metodo para las recetas
    def __init__(self,cocina,platillo):
        self.nombre = platillo
        self.cocina = cocina
        self.ingredientes = recetas[cocina][platillo]
    def esta_completa(self,ingredientes_entregados):
        for i in self.ingredientes:
            if i not in ingredientes_entregados or self.ingredientes[i]["estado"] != "preparado":
                return False  # si falta alguno, no está completa
        return True  # si pasó todos, está completa
    def _str_ (self):
        return self.nombre