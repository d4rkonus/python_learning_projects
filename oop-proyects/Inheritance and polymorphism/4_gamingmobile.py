#!/usr/bin/python3

# Base class
class Gaming_Phones:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# Derivered class #1 (ROG Phone)
class ROG_Phone(Gaming_Phones):
    def __init__(self, year):
        super().__init__("ROG Phone", year)
    
    def gaming_mode(self):
        return (
            f"\n· [+] You have the {self.brand}, released in {self.year}!"
            f"\n· [-] It has active gaming lights for a good night gaming!"
        )

# Derivered class #2 (Black Shark)
class Black_Shark(Gaming_Phones):
    def __init__(self,year):
        super().__init__("Black Shark", year)
    
    def gaming_mode(self):
        return (
            f"\n· [+] You have the {self.brand}, released in {self.year}!"
            f"\n· [-] It has physical gaming buttons, for quickly reaction on intenses gaming sessions!"
        )

# Derivered class #3 (Red Magic)
class RedMagic(Gaming_Phones):
    def __init__(self,year):
        super().__init__("Red Magic", year)
    
    def gaming_mode(self):
        return (
            f"\n· [+] You have the {self.brand}, released in {self.year}!"
            f"\n· [-] It has an active liquid cooling system to avoid overheating!"
        )

Gaming_Phones = [
    ROG_Phone(2019),
    Black_Shark(2018), 
    RedMagic(2021)
]

for phone in Gaming_Phones:
    print(phone.gaming_mode())