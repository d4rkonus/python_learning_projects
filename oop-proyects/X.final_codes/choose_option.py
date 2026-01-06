#!/usr/bin/python3
import random
import time

# Clase Carta
class Card:
    def __init__(self, nombre, tecnica, poder):
        self.nombre = nombre
        self.tecnica = tecnica
        self.poder = poder

# Cartas ofensivas
tornado_fuego = Card("tornado de fuego", "ofensiva", 40)
ventisca_eterna = Card("ventisca eterna", "ofensiva", 35)
cañon_meteor = Card("cañón de meteoritos", "ofensiva", 60)
proyectil_letal = Card("proyectil letal", "ofensiva", 50)
xk4libur = Card("excalibur", "ofensiva", 95)
emperor = Card("pingüino emperador X", "ofensiva", 150)
x_shot = Card("cañón X", "ofensiva", 130)
cataclism = Card("golpe cataclismo", "ofensiva", 200)

# Cartas defensivas
escudo_fuerza = Card("escudo de fuerza", "defensiva", 50)
agujero_gusano = Card("agujero gusano", "defensiva", 80)
mano_celestial_v = Card("mano celestial v", "defensiva", 90)
portal = Card("portal", "defensiva", 120)

#----------------------------------------------------------------------

# Pregunta nombre
try:
    name = input("\n¿Cuál es tu nombre?: ")
    time.sleep(1)
    print(f"\n[!] Bueno {name}, que sepas que soy un reto de mal perder, y es poco probable que me derrotes.")
    time.sleep(1)
    print("[!] Pero al menos te dejaré intentarlo, escoge tu carta y veamos quién es el jefe aquí.\n")

# Elegir carta
    while True:
        print("\nCartas ofensivas disponibles:")
        print("1 - Tornado de Fuego")
        print("2 - Ventisca Eterna")
        choice = input("\nEscoge tu carta: ")

        if choice == "1":
            carta_elegida = tornado_fuego
            time.sleep(1)
            print(f"\nHas elegido {carta_elegida.nombre} como táctica {carta_elegida.tecnica}.")
            print(f"Esta técnica tiene un poder ofensivo de {carta_elegida.poder} puntos.\n")
            break
        elif choice == "2":
            carta_elegida = ventisca_eterna
            time.sleep(1)
            print(f"\nHas elegido {carta_elegida.nombre} como táctica {carta_elegida.tecnica}.")
            print(f"Esta técnica tiene un poder ofensivo de {carta_elegida.poder} puntos.\n")
            break
        else:
            print("Elige una de las opciones.")

    # Turno del rival
    print(f"[!] Ja! Eso es todo lo que tienes? Ahora me toca.")
    carta_rival = escudo_fuerza
    time.sleep(1)
    print(f"\nEl rival ha elegido {carta_rival.nombre} como táctica {carta_rival.tecnica}.")
    print(f"Esta técnica tiene un poder defensivo de {carta_rival.poder} puntos.\n")

    if carta_rival.poder >= carta_elegida.poder:
        print(f"No se pudo romper la defensa {carta_rival.nombre} por una diferencia de: {carta_rival.poder - carta_elegida.poder} puntos.\n")
        time.sleep(1)
        print(f"[!] Te lo dije, {name}. No puedes romper mi defensa.")
    # Turno del jugador
    print(f"\n[!] Sigue intentando romper mi defensa, {name}!. Aunque los facking panzas nunca lo consiguen.")
    time.sleep(1)
    print(f"Nuevas cartas ofensivas disponibles: ")
    print("1 - Cañón de Meteoritos")
    print("2 - Proyectil Letal")
    print("3 - Excalibur")

    choice = input("\nEscoge tu carta: ")

    if choice == "1":
        carta_ofensiva = cañon_meteor
        print(f"\nHas elegido {carta_ofensiva.nombre} como táctica {carta_ofensiva.tecnica}.")
        print(f"Esta técnica tiene un poder ofensivo de {carta_ofensiva.poder} puntos.\n")
    elif choice == "2":
        carta_ofensiva = proyectil_letal
        print(f"\nHas elegido {carta_ofensiva.nombre} como táctica {carta_ofensiva.tecnica}.")
        print(f"Esta técnica tiene un poder ofensivo de {carta_ofensiva.poder} puntos.\n")
    elif choice == "3":
        carta_ofensiva = xk4libur
        print(f"\nHas elegido {carta_ofensiva.nombre} como táctica {carta_ofensiva.tecnica}.")
        print(f"Esta técnica tiene un poder ofensivo de {carta_ofensiva.poder} puntos.\n")
    else:
        print("Elige una de las opciones.")

    time.sleep(1)
    print(f"\n[!] Vaya, eso es nuevo. Pero ni de coña podrás con esto.")
    carta_rival = mano_celestial_v
    time.sleep(1)
    print(f"\nEl rival ha elegido {carta_rival.nombre} como táctica {carta_rival.tecnica}.")
    print(f"Esta técnica tiene un poder defensivo de {carta_rival.poder} puntos.\n")

    if carta_rival.poder >= carta_elegida.poder:
        time.sleep(1)
        print(f"No se pudo romper la defensa {carta_rival.nombre} por una diferencia de: {carta_rival.poder - carta_elegida.poder} puntos.\n")
        print(f"[!] Maldito perro. Es imposible que puedas vencerme.")

    time.sleep(1)
    print(f"Nuevas cartas ofensivas disponibles: ")
    print("1 - Pingüino Emperador X")
    print("2 - Cañón X")
    print("3 - Golpe Cataclismo")
    choice = input("\nEscoge tu carta: ")
    if choice == "1":
        carta_ofensiva = emperor
        print(f"\nHas elegido {carta_ofensiva.nombre} como táctica {carta_ofensiva.tecnica}.")
        print(f"Esta técnica tiene un poder ofensivo de {carta_ofensiva.poder} puntos.\n")
    elif choice == "2":
        carta_ofensiva = x_shot
        print(f"\nHas elegido {carta_ofensiva.nombre} como táctica {carta_ofensiva.tecnica}.")
        print(f"Esta técnica tiene un poder ofensivo de {carta_ofensiva.poder} puntos.\n")
    elif choice == "3":
        carta_ofensiva = cataclism
        print(f"\nHas elegido {carta_ofensiva.nombre} como táctica {carta_ofensiva.tecnica}.")
        print(f"Esta técnica tiene un poder ofensivo de {carta_ofensiva.poder} puntos.\n")
    else:
        print("Elige una de las opciones.")

        time.sleep(1)   
        print(f"\n[!] Por mas que lo intentes, nunca podrás vencerme.")
        carta_rival = portal
        time.sleep(1)
        print(f"\nEl rival ha elegido {carta_rival.nombre} como táctica {carta_rival.tecnica}.")
        print(f"Esta técnica tiene un poder defensivo de {carta_rival.poder} puntos.\n")
        if carta_elegida.poder > carta_rival.poder:
            print(f"\n La técnica {carta_elegida.nombre} ha logrado romper la defensa {carta_rival.nombre} por una diferencia de: {carta_elegida.poder - carta_rival.poder} puntos.")

except KeyboardInterrupt:
    print("Saliendo ...")

