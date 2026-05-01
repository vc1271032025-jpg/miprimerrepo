import random


def jugar():
    continuar = "s"

    while continuar.lower() == "s":
        print("\n--- BIENVENIDO AL JUEGO DE ADIVINANZA ---")
        print("Seleccione un nivel de dificultad:")
        print("1. Fácil (1-10, 5 intentos)")
        print("2. Medio (1-50, 7 intentos)")
        print("3. Difícil (1-100, 10 intentos)")

        opcion = input("Elija una opción (1, 2 o 3): ")

        match opcion:
            case "1":
                rango, intentos_totales = 10, 5
            case "2":
                rango, intentos_totales = 50, 7
            case "3":
                rango, intentos_totales = 100, 10
            case _:
                print("Opción no válida, usando nivel fácil por defecto.")
                rango, intentos_totales = 10, 5

        numero_secreto = random.randint(1, rango)
        gano = False

        print(
            f"\nHe pensado un número entre 1 y {rango}. ¡Tienes {intentos_totales} intentos!"
        )

        for i in range(1, intentos_totales + 1):
            try:
                intento = int(input(f"Intento {i}: ¿Cuál es el número? "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if intento == numero_secreto:
                print(f"¡Felicidades! Adivinaste en el intento {i}.")
                gano = True
                break
            elif intento < numero_secreto:
                print("Pista: El número es mayor.")
            else:
                print("Pista: El número es menor.")

        if not gano:
            print(
                f"\nLo siento, se acabaron los intentos. El número era {numero_secreto}."
            )

        continuar = input("\n¿Deseas jugar de nuevo? (s/n): ")

    print("¡Gracias por jugar!")


if __name__ == "__main__":
    jugar()
