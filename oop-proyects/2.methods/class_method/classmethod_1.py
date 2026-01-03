#!/usr/bin/python3

class Users:
    total_users = 0
    users_lists = []

    def __init__(self, name):
        self.name = name
        Users.total_users += 1
        Users.users_lists.append(name)

    @classmethod
    def show_total(cls):
        print(f"\n[+] New user has been created:\n")
        for name in cls.users_lists:
            print(f"-", name)

        print(f"\n[*] Users created", cls.total_users)

user_1 = Users("Ana")
user_2 = Users("Michael")
user_3 = Users("John")

Users.show_total()