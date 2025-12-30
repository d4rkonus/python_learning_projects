#!/usr/bin/python3

# Base class
class Animal:
    def sound(self):
        print("[!] New animal discovered makes a new sound")

# Derived class: Dog
class Dog(Animal):
    def sound(self):
        print("[+] Dog barks to a ghost.")

# Derived class: Wolf
class Wolf(Animal):
    def sound(self):
        print("[+] Wolf howls to the moon.")

# Creating objets of the each class
animals = [Animal(), Dog(), Wolf()]

# Calling all the animals
for animal in animals:
    animal.sound()
