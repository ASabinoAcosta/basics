"""
    Juego de piedra, papel o tijeras
"""

import random
import json

def main():
    readme()

def readme():
    user = input("""
          ¿Lista para jugar? (y/n)
          """)
    
    if user.lower() == "y":
        return game()
    else:
        print("Bye, bye!")
        
    
def game():
    """
    Tomamos la función usuario donde se le pide al usuario que ingrese su jugada.
    Tomamos la función machine en donde la máquina elige una jugada aleatoria en base a cada partida.
    Luego comparamos las jugadas y se dice el ganador.
    Se almacena el dato y se continúa el juego si el usuario quiere seguir jugando.
    """
    pass

class User:
    def __init__(self, name):
        self.movimiento = None
        self.intentos = 3
        self.ganadas = 0
        self.perdidas = 0
        self.empates = 0
        self.name = name
        
    def movimiento(self):
        self.movimiento = input("Elige tu movimiento (piedra, papel o tijeras): ")
        
        with open("movimientos.json", "w") as file:
            json
    
    def perder(self):
        self.perdidas += 1
        
        if self.intentos == 0:
            return self.game_over()
        self.intentos -= 1
    
    def ganar(self):
        if self.ganadas == 3:
            print(f"¡Felicidades! ¡{self.name} has ganado!")
        
        self.ganadas += 1
    
    def empatar(self):
        self.empates += 1
    
    def game_over(self):
        self.intentos = 3
        self.ganadas = 0
        self.perdidas = 0
        self.empates = 0

    def __str__(self):
        return f"Jugador: {self.name}, Intentos: {self.intentos}, Ganadas: {self.ganadas}, Perdidas: {self.perdidas}, Empates: {self.empates}"
    
class Machine:
    def __init__(self):
        self.movimiento = None
        self.movimientos = ["piedra", "papel", "tijeras"]
        self.ganadas = 0
        self.intentos = 3
        self.perdidas = 0
        self.empates = 0
        
    def movimiento(self):
        pass