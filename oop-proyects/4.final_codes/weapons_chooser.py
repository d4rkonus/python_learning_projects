#!/usr/bin/python3
import random

# Base class - Soldier
class Soldier:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def attack(self):
        return f"\n· {self.name} attacks with {self.element} power!"

# Derived class - Letal Weapons
class Sword(Soldier):
    def attack(self):
        return f"\n· {self.name} swings the sword with {self.element} power!"
    
class Bow(Soldier):
    def attack(self):
        return f"\n· {self.name} shoots an arrow with {self.element} power!"
class Spear(Soldier):
    def attack(self):
        return f"\n· {self.name} thrusts the spear with {self.element} power!"
    

# Elements in the weapons
elements = ["Fire", "Ice", "Stone", "Air", "Lightning", "Energon"]

# Soldier names
names = ["Lancelot", "Percival", "Scourge", "Blaze", "Fallen"]
soldiers = {}

for name in names: 
    element = random.choice(elements)
    weapon_class = random.choice([Sword, Bow, Spear])
    soldier = weapon_class(name, element)
    soldiers[name] = soldier

# Each soldier attacks
for soldier in soldiers.values():
    print(soldier.attack())