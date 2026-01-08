from calculadora import Calculadora


def main():
    calc = Calculadora()

    print("Calculadora sencilla")
    print("Escribe una operación con espacios")
    print("Ejemplo: 10 + 2 * 3 - 4 / 2")
    print("Escribe 'salir' para terminar")

    while True:
        expresion = input("> ")

        if expresion.lower() == "salir":
            print("Adiós 👋")
            break

        try:
            resultado = calc.calcular(expresion)
            print("=", resultado)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()