#!/usr/bin/python3

from .cuerpo import Cuerpo

# combina el cuerpo y el arma, ademas de definir acciones al atacar

class Personaje:
    def __init__(self, nombre, cuerpo):
        self.nombre = nombre
        self.cuerpo = cuerpo
        self.arma = None # el personaje nace sin arma (de primeras)


    def agregar_arma(self, arma):
        self.arma = arma

    def atacar(self, target):
        if self.arma:
            danio = self.arma.atacar()
        else:
            danio = 5
        
        target.cuerpo.recibir_danio(danio)
        return danio