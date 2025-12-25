#!/usr/bin/python3


try:
    name = input("\n[+] Give me name: ").lower()

    table = {
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "s": "5",
    "t": "7"
    }

    new_name = ""

    for chat in name:
        if chat in table:
            new_name += table[chat]
        else:
            new_name += chat

    print("\nThe new name is: " + new_name)

except KeyboardInterrupt:
    print("\n\n[!] Some explotion happened, moving to safe zone :)\n")
    exit()