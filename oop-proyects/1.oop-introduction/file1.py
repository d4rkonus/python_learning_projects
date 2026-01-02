#!/usr/bin/python3

class cerberus:
    def __init__(self, name, year, head, power):
        self.name = name
        self.year = year
        self.head = head
        self.power = power

    def action(self):
        return f"\n [+] The hell guardian {self.name}, with {self.head} heads, has the {self.power} power!\n"
    
cerberus1 = cerberus("Cerberus", "Hell times", 3, "Dark fire")

print(cerberus1.action())