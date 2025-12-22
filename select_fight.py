#/usr/bin/python3

helios_character = ("Helios", "Atomic flame", "Fire sword", "Fire hell")
drago_character = ("Drago", "Fire wings", "Fire ball", "Lava shield")
vulcan_character = ("Vulcan", "Force shield", "Land missile", "Earthquake")

character_number = int(input("Choose your fighter: "))


if character_number == 1:
    print(f"\nYou chose the character: {helios_character[0]}, and it has these powers:\n")
    print(f"[+] {helios_character[1]}")
    print(f"[+] {helios_character[2]}")
    print(f"[+] {helios_character[3]}\n")
elif character_number == 2:
    print(f"\nYou chose the character: {drago_character[0]}, and it has these powers:\n")
    print(f"[+] {drago_character[1]}")
    print(f"[+] {drago_character[2]}")
    print(f"[+] {drago_character[3]}\n")
elif character_number == 3:
    print(f"\nYou chose the character: {vulcan_character[0]}, and it has these powers:\n")
    print(f"[+] {vulcan_character[1]}")
    print(f"[+] {vulcan_character[2]}")
    print(f"[+] {vulcan_character[3]}\n")
else:
    print("Invalid choice")

