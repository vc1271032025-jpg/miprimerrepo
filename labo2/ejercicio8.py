def menu():
    texto = input("Ingrese el texto: ")
    print("Opciones: 1 (Mayus), 2 (Minus), 3 (Cap)")
    opcion = int(input("Elija opción: "))

    if opcion == 1:
        print(texto.upper())
    elif opcion == 2:
        print(texto.lower())
    elif opcion == 3:
        print(texto.capitalize())
    else:
        print("Opción inválida")


if __name__ == "__main__":
    menu()
