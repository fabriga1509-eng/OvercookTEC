class Dish:
    def __init__(self, receta, ingredientes):
        self.receta = receta
        self.nombre = receta.nombre if receta is not None else "Plato Vacio"
        self.ingredientes = ingredientes
    def verificar_receta_actual(self):#Validacion de las recetas a mano (Lo intente de otra forma y me hostine, asi queda)
        ing_ordenados = sorted(self.ingredientes)

        if ing_ordenados == sorted(['arroz_cocido', 'pescadosushi_cortado', 'alga_cortado']):
            self.receta = "Sushi"  
            
        elif ing_ordenados == sorted(['pescado_cortado']):
            self.receta = "Shashimi" 
        
        elif ing_ordenados == sorted(['masa_cocido','salsa_cocido','queso_cocido']):
            self.receta = "Pizza" 

        elif ing_ordenados == sorted(['pan_cocido','carne_cocido','lechuga_cortado','tomate_cortado']):
            self.receta = "Hamburguesa" 
        
        elif ing_ordenados == sorted(['papas_cocido']):
            self.receta = "Papas" 
        
        elif ing_ordenados == sorted(['arroz_cocido','frijoles_cocido','huevo_cocido']):
            self.receta = "Pinto" 

        elif ing_ordenados == sorted(['verduras_cocido','pollo_cocido','arroz_cocido']):
            self.receta = "Arroz con pollo" 
        
        elif ing_ordenados == sorted(['verduras_cocido','carne_cocido']):
            self.receta = "Olla de carne"
        else:
            self.receta = None #Si no es ningura receta es un plato normal