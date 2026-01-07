#!/usr/bin/python3

# este archivo gestionar la vida y el estado del personaje, si esta vivo o muerto.

class Cuerpo:
    def __init__(self, vida, energia, fuerza, inteligencia):
        self.vida_max = vida
        self.vida = vida 
        self.energia = energia
        self.fuerza = fuerza
        self.inteligencia = inteligencia

    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
        
    def esta_muerto(self):
        return self.vida <= 0


    def esta_vivo(self):
        return self.vida > 0