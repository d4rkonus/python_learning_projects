#!/usr/bin/python3

class Armadura:
    def __init__(self, nombre, defensa):
        self.nombre = nombre
        self.defensa = defensa

    def proteger(self, daño):
        daño_reducido = daño - self.defensa
        if daño_reducido < 0:
            daño_reducido = 0
        return daño_reducido