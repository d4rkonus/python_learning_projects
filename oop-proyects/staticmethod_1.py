#!/usr/bin/python3

class Calculator:

    @staticmethod
    def suma(num1, num2):
        return num1 + num2

    @staticmethod
    def resta(num4, num2):
        return num4 - num2

num1 = 1
num2 = 2
num3 = 3
num4 = 4 
print(f"\nLa suma de {num1} y {num2} es: {Calculator.suma(num1, num2)}")
print(f"\nLa resta de {num4} y {num2} es: {Calculator.resta(num4, num2)}\n")