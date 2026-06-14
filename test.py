import pygame
from entities.player import Player
from entities.ingredientes import Ingrediente
from entities.station import Station
from constants import CHEF1_TECLAS

pygame.init()

print("=== PRUEBA INGREDIENTE ===")
ingrediente = Ingrediente("papa", {"estado": "crudo", "estacion": "freidora"})
print(f"Nombre: {ingrediente.nombre}")        # → papa
print(f"Estado: {ingrediente.estado}")        # → crudo
print(f"Estacion: {ingrediente.estacion}")    # → freidora
print(f"Str: {str(ingrediente)}")             # → papa

print("\n=== PRUEBA STATION ===")
estacion = Station(100, 100, "freidora")
print(f"Tipo: {estacion.tipo}")               # → freidora
print(f"Activa: {estacion.activa}")           # → False
print(f"Ingrediente: {estacion.ingrediente}") # → None

print("\n-- Recibir ingrediente correcto --")
estacion.recibir(ingrediente)
print(f"Activa: {estacion.activa}")                        # → True
print(f"Ingrediente: {estacion.ingrediente.nombre}")       # → papa

print("\n-- Recibir ingrediente incorrecto --")
ingrediente_malo = Ingrediente("carne", {"estado": "crudo", "estacion": "sarten"})
estacion.recibir(ingrediente_malo)
print(f"Ingrediente sigue siendo: {estacion.ingrediente.nombre}")  # → papa (no cambió)

print("\n-- Update 6 segundos --")
estacion.update(6)
print(f"Estado: {ingrediente.estado}")        # → preparado

print("\n-- Update 10 segundos más --")
estacion.update(10)
print(f"Estado: {ingrediente.estado}")        # → quemado

print("\n-- Entregar --")
ing = estacion.entregar()
print(f"Entregado: {ing.nombre}")             # → papa
print(f"Activa: {estacion.activa}")           # → False
print(f"Timer: {estacion.timer}")             # → 0
print(f"Ingrediente: {estacion.ingrediente}") # → None

print("\n=== PRUEBA PLAYER ===")
chef = Player(100, 100, CHEF1_TECLAS)
print(f"Ingrediente inicial: {chef.ingrediente}")  # → None

print("\n-- Recoger de estacion vacía --")
estacion2 = Station(200, 100, "sarten")
chef.recoger(estacion2)
print(f"Chef ingrediente: {chef.ingrediente}")     # → None

print("\n-- Recoger de estacion con ingrediente --")
ingrediente2 = Ingrediente("carne", {"estado": "crudo", "estacion": "sarten"})
estacion2.recibir(ingrediente2)
chef.recoger(estacion2)
print(f"Chef cargando: {chef.ingrediente.nombre}") # → carne
print(f"Estacion vacia: {estacion2.ingrediente}")  # → None

print("\n-- Soltar en estacion --")
estacion3 = Station(300, 100, "sarten")
chef.soltar(estacion3)
print(f"Chef ingrediente: {chef.ingrediente}")          # → None
print(f"Estacion tiene: {estacion3.ingrediente.nombre}") # → carne

print("\nPruebas completadas")