def solicitar_y_transformar():
    texto = input("Ingrese un texto: ")
    opcion = int(input("Ingrese una opción (1, 2 o 3): "))

    if opcion == 1:
        print(texto.upper())
    elif opcion == 2:
        print(texto.lower())
    elif opcion == 3:
        print(texto.capitalize())
    else:
        print("Opción no válida")


solicitar_y_transformar()
