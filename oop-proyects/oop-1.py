#!/usr/bin/python3
import time


class BankAccount:
    def __init__(self, account, name, money):
        self.account = account
        self.name = name
        self.money = money


    def log_account(self):
        return f"\n[*] The user with name {self.name} has logged in the account {self.account}"

    def add_money(self, amount):
        self.money += amount 
        time.sleep(2)
        return f"\n[+] Money added: {amount}€, the current balance now is: {self.money} €"

    def withdraw_money(self, amount):
        if amount > self.money:
            return "\n[!] Not enough money to withdraw."
        self.money -= amount
        time.sleep(2)
        return f"\n[+] Withdrawn: {amount}€. the current balance now is: {self.money} €"

    def show_balance(self):
          return (
        f"\n The ID account is: {self.account}"
        f"\n The username is: {self.name}"
        f"\n The new balance is: {self.money}€"
    )

# Crear cuentas
michael = BankAccount("00010", "Michael Loumis", 10000)
john = BankAccount("00500", "John Wish", 20000)

# Probar metodos
print(michael.log_account())
print(michael.add_money(100))
print(michael.withdraw_money(500))
print(michael.show_balance())
print("\n")
print(john.log_account())
print(john.add_money(100))
print(john.withdraw_money(500))
print(john.show_balance())
print("\n")
