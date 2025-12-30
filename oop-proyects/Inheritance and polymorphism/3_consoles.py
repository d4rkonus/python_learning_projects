#!/usr/bin/python3

# Base class
class Console:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def chill_gaming(self):
        if self.brand == "Play Station 5":
         return (
         f"\n· Having some chill gaming on the {self.brand}, released in {self.year}!"
         f"\n· You can play God of War on the {self.brand}!"
        )
        elif self.brand == "Xbox Series X":
         return (
         f"\n· Having some chill gaming on the {self.brand}, released in {self.year}!"
         f"\n· You can play Halo on the {self.brand}!"
        )
        elif self.brand == "Nintendo Switch 2":
            return (
            f"\n· Having some chill gaming on the {self.brand}, released in {self.year}!"
            f"\n· You can play Mario on the {self.brand}!"
            )

# Derived classes
class PlayStation(Console):
    def __init__(self, year):
        super().__init__("Play Station 5", year)

    
class Xbox(Console):
    def __init__(self, year):
        super().__init__("Xbox Series X", year)

class Nintendo(Console):
    def __init__(self, year):
        super().__init__("Nintendo Switch 2", year)

consoles = [PlayStation(2020), Xbox(2020), Nintendo(2025)]

for console in consoles:
    print(console.chill_gaming())