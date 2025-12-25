#!/usr/bin/python3

real_user = "d4rkonus"
real_password = "123"
fails_tried = 0
fails_max = 2  

while fails_tried < fails_max:
    user = input("User: ")
    password = input("Password: ")

    if user == real_user and password == real_password:
        print(f"\n[+] Acceso permitido, ambas credenciales correctas :)\n")
        break
    elif user != real_user and password != real_password:
        fails_tried += 1
        print(f"\n - Acceso denegado, usuario y contraseña incorrectos.")
    elif user != real_user:
        fails_tried += 1
        print(f"\n - Acceso denegado, usuario incorrecto.")
    elif password != real_password:
        fails_tried += 1
        print(f"\n - Acceso denegado, contraseña incorrecta.")

    if fails_tried == fails_max:
        print(f"\n[-] Cuenta bloqueada, se usaron los {fails_max} intentos :(.")
        break
