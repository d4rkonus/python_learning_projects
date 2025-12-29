import random

# Base class: Soldier
class Soldier:
    def __init__(self, name, weapon, element):
        self.name = name
        self.weapon = weapon
        self.element = element

    def attack(self):
        return f"\n ·{self.name} attacks with {self.weapon} and the power of {self.element}!"

# Derived classes: Lethal Weapons
class Sword(Soldier):
    def __init__(self, name, element):
        super().__init__(name, 'Sword', element)

class Bow(Soldier):
    def __init__(self, name, element):
        super().__init__(name, 'Bow', element)

class Spear(Soldier):
    def __init__(self, name, element):
        super().__init__(name, 'Spear', element)

class Hammer(Soldier):
    def __init__(self, name, element):
        super().__init__(name, 'Hammer', element)

class Axe(Soldier):
    def __init__(self, name, element):
        super().__init__(name, 'Axe', element)

# Unique elements for each soldier
elements = ["Fire", "Ice", "Stone", "Air", "Lightning", "Energon", "Darkness"]
weapons = [Sword, Bow, Spear, Hammer, Axe]
random.shuffle(elements)  
random.shuffle(weapons)

# Soldier names
names = ["Lancelot", "Percival", "Scourge", "Blaze", "Fallen"]
soldiers = []

# Create soldiers with unique weapon and element
for name, weapon_class, element in zip(names, weapons, elements):
    soldier = weapon_class(name, element)
    soldiers.append(soldier)

# Each soldier attacks
for soldier in soldiers:
    print(soldier.attack())
