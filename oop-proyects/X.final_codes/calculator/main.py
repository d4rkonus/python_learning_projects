#!/usr/bin/python3

from operadores import add, subtract, multiply, divide


def obtener_numeros(cantidad):
    numeros = []
    for numero in range(cantidad):
        while True:
            try:
                numero = float(input(f"Ingresa el número {numero + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Error: Ingresa un número válido")
    return numeros


def mostrar_numeros_formateados(numeros):
    formateados = []
    for num in numeros:
        if num.is_integer():
            formateados.append(int(num))
        else:
            formateados.append(num)
    return formateados


def realizar_operacion(operador, numeros):
    resultado = numeros[0]

    for num in numeros[1:]:
        if operador == "+":
            resultado = add(resultado, num)
        elif operador == "-":
            resultado = subtract(resultado, num)
        elif operador == "*":
            resultado = multiply(resultado, num)
        elif operador == "/":
            resultado = divide(resultado, num)

    return resultado


def main():
    print("=" * 40)
    print("       TERMINAL CALCULATOR")
    print("=" * 40)

    operadores_validos = ["+", "-", "*", "/"]

    try:
        while True:
            print("\n¿Qué operación quieres realizar?")
            print("  + : Suma")
            print("  - : Resta")
            print("  * : Multiplicación")
            print("  / : División")
            print("  salir : Terminar programa")

            operador = input("\nSelecciona una opción: ").strip()

            if operador.lower() == "salir":
                print("\n[$] Saliendo del programa...")
                break

            if operador not in operadores_validos:
                print("Error: Operador no válido")
                continue

            while True:
                try:
                    cantidad = int(input("\n¿Cuántos números? (mínimo 2): "))
                    if cantidad < 2:
                        print("Necesitas al menos 2 números")
                    else:
                        break
                except ValueError:
                    print("Ingresa un número entero válido")

            numeros = obtener_numeros(cantidad)
            resultado = realizar_operacion(operador, numeros)
            numeros_formateados = mostrar_numeros_formateados(numeros)

            print("\nOperación:", end=" ")
            for i, num in enumerate(numeros_formateados):
                if i > 0:
                    print(f" {operador} ", end="")
                print(num, end="")
            print(f" = {resultado}")

    except KeyboardInterrupt:
        print("\n\n[!] Saliendo hacia zona segura...")


if __name__ == "__main__":
    main()
