#!/usr/bin/python3

from parser import Parser


class Calculadora:
    def __init__(self):
        self.parser = Parser()

    def calcular(self, expresion):
        return self.parser.evaluar(expresion)