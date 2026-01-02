#!/usr/bin/python3

class PC:
    def __init__(self, os, ram, pc_id):
        self.os = os
        self._ram = ram  # en GB
        self.__id = pc_id 

    def info(self):
        print(f"\nEl PC tiene los siguientes componentes:")
        print(f"\nOS: {self.os}")
        print(f"RAM: {self._ram} GB")
        print(f"ID: {self.__id}")

pc = PC("Windows 10", 32, "PC-0001")

