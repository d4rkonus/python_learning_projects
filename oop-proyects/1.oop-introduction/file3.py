#!/usr/bin/python3

class greecianGods:
    def __init__(self, name, domain, powers):
        self.name = name
        self.domain = domain
        self.powers = powers

    def show_info(self):
        return f"\n[+] {self.name} is the {self.domain} and has the powers of {self.powers}.\n"

class Pantheon:
    def __init__(self):
        self.gods = {
            "Zeus": ["king of the gods", "Lightning"],
            "Poseidon": ["god of the sea", "Water control"],
            "Hades": ["god of the hell", "Death manipulation"],
            "Athena": ["god of wisdom", "Strategic warfare"],
            "Apollo": ["god of the sun", "Sunlight and music"],
            "Artemis": ["god of the moon", "Hunting and wilderness"],
            "Ares": ["god of war", "Battle and conflict"],
            "Aphrodite": ["Goddess of love", "Beauty and desire"]
        }

    def show_gods(self):
        for name, details in self.gods.items():
            god = greecianGods(name, details[0], details[1])
            print(god.show_info())

# Crear un objeto cualquiera y usar el método
pantheon = Pantheon()
pantheon.show_gods()
