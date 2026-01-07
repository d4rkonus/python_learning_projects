#!/usr/bin/python3

# define cuanto daño hace el arma al atacar

class Arma:
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño
    
    def atacar(self):
        return self.daño