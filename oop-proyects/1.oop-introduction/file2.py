#!/usr/bin/python3
import time

class Jaeger:
    def __init__(self, name, model, weapons, abilities):
        self.name = name
        self.model = model
        self.weapons = weapons
        self.abilities = abilities

    def new_project(self):
        time.sleep(1)
        return f"\n[+] New project on the way! Code name: {self.name}.\n"

    def action(self):
        steps = [
            f"· Assembling body parts for Jaeger {self.name}, model {self.model}.",
            f"· Installing and mounting weapons: {self.weapons}.",
            f"· Activating and mounting abilities: {self.abilities}.\n"
            f"\n [!] Jaeger {self.name} ready to road!\n"
        ]

        for step in steps:
            print(step)
            time.sleep(1)

# Crear objeto Jaeger
jaeger1 = Jaeger("Atom", "Mark-3", "Plasma Gun", "Adaptive Shield")

# Ejecutar proyecto
print(jaeger1.new_project())
jaeger1.action()
