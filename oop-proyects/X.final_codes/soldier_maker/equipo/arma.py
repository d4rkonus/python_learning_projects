#!/usr/bin/python3

# define cuanto daño hace el arma al atacar

class Arma:
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio
    
    def atacar(self):
        return self.danio