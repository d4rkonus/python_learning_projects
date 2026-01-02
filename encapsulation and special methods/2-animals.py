#!/usr/bin/python3

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self._age = age
        self.__species = species

    def animal_info(self):
        print(f"\nAnimal Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Species: {self.__species}")

animal_1 = Animal("Leo", 3, "Lion")
animal_2 = Animal("Molly", 5, "Cat")

animal_1.animal_info()
animal_2.animal_info()
