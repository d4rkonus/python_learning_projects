#!/usr/bin/python3

class Armadura:
    def __init__(self, nombre, defensa):
        self.nombre = nombre
        self.defensa = defensa

    def proteger(self, danio):
        danio_reducido = danio - self.defensa
        if danio_reducido < 0:
            danio_reducido = 0
        return danio_reducido